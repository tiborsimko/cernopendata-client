# -*- coding: utf-8 -*-
# This file is part of cernopendata-client.
#
# Copyright (C) 2020 CERN.
#
# cernopendata-client is free software; you can redistribute it and/or modify
# it under the terms of the GPLv3 license; see LICENSE file for more details.

"""cernopendata-client record search related utilities."""

from __future__ import print_function

import argparse
import os
import sys
import datetime
import requests

from .config import SERVER_HTTP_URI, SERVER_ROOT_URI, SERVER_HTTPS_URI
from .printer import display_message

try:
    from urllib.parse import quote
except ImportError:
    # fallback for Python 2
    from urllib import quote

try:
    from xrootdpyfs import XRootDPyFS

    xrootd_available = True
except ImportError:
    xrootd_available = False


def verify_recid(server=None, recid=None):
    """Verify that recid corresponds to a valid Open Data record webpage.

    :param server: CERN Open Data server to query
    :param recid: Record ID
    :type server: str
    :type recid: int

    :return: Boolean after verifying the record id
    :rtype: bool
    """
    input_record_url = server + "/record/" + str(recid)
    input_record_url_check = requests.get(input_record_url)

    if input_record_url_check.status_code == 200:
        base_record_id = str(recid)
        return base_record_id
    else:
        try:
            input_record_url_check.raise_for_status()
        except requests.HTTPError:
            display_message(
                msg_type="error",
                msg="The record id number you supplied is not valid.",
            )
            sys.exit(1)
        return False


def get_recid_api(server=None, base_record_id=None):
    """Return api for the record with given recid.

    :param server: CERN Open Data server to query
    :param base_record_id: Record ID
    :type server: str
    :type base_record_id: int

    :return: String of record api
    :rtype: str
    """
    record_api_url = server + "/api/records/" + base_record_id
    record_api = requests.get(record_api_url)
    record_api.raise_for_status()
    return record_api


def get_recid(server=None, title=None, doi=None):
    """Return record id by either title or doi.

    :param server: CERN Open Data server to query
    :param title: Record title
    :param doi: Digital Object Identifier of record
    :type server: str
    :type title: str
    :type doi: str

    :return: record id
    :rtype: int
    """
    if title:
        name, value = "title", title
    elif doi:
        name, value = "doi", doi
    url = (
        server
        + "/api/records"
        + "?page=1&size=1&q={}:".format(name)
        + quote('"{}"'.format(value), safe="")
    )
    response = requests.get(url)
    response_json = response.json()
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        display_message(
            msg_type="error",
            msg="Connection to server failed: \n reason: {}.".format(e),
        )
    if "hits" in response_json:
        hits_total = response_json["hits"]["total"]
        if hits_total < 1:
            display_message(
                msg_type="error",
                msg="Record with given {} does not exist.".format(name),
            )
            sys.exit(2)
        elif hits_total > 1:
            display_message(
                msg_type="error",
                msg="More than one record fit this {}."
                "This should not happen.".format(name),
            )
            sys.exit(3)
        elif hits_total == 1:
            return response_json["hits"]["hits"][0]["id"]


def get_record_as_json(server=None, recid=None, doi=None, title=None):
    """Return record content in json by its recid, doi or title.

    :param server: CERN Open Data server to query
    :param recid: Record ID
    :param title: Record title
    :param doi: Digital Object Identifier of record
    :type server: str
    :type recid: int
    :type title: str
    :type doi: str

    :return: record content in JSON
    :rtype: json(dict)
    """
    if recid:
        record_id = recid
    elif title:
        record_id = get_recid(server=server, title=title)
    elif doi:
        record_id = get_recid(server=server, doi=doi)
    else:
        display_message(
            msg_type="error",
            msg="Please provide at least one of following arguments: "
            "(recid, doi, title)",
        )
        sys.exit(1)

    record_id = verify_recid(server=server, recid=record_id)
    record_api = get_recid_api(server=server, base_record_id=record_id)
    record_json = record_api.json()
    if "_files" in record_json["metadata"]:
        del record_json["metadata"]["_files"]
    if record_json["metadata"]["files"]:
        for field in record_json["metadata"]["files"]:
            if "bucket" in field:
                del field["bucket"]
            if "version_id" in field:
                del field["version_id"]
    return record_json


def get_files_list(
    server=None, record_json=None, protocol=None, expand=None, verbose=None
):
    """Return file list of a dataset by its recid, doi, or title.

    :param server: CERN Open Data server to query
    :param record_json: Record content in JSON
    :protocol: Protocol to be used in links [http,xrootd]
    :expand: Flag for expanding file indexes
    :verbose: Flag for showing size and checksum of file
    :type server: str
    :type record_json: json(dict)
    :type protocol: str
    :type expand: bool
    :type verbose: bool

    :return: List of files list
    :rtype: list
    """
    if verbose:
        files_list = [
            (file["uri"], file["size"], file["checksum"])
            for file in record_json["metadata"]["files"]
        ]
        if protocol == "http":
            files_list = [
                (file_[0].replace(SERVER_ROOT_URI, server), file_[1], file_[2])
                for file_ in files_list
            ]
    else:
        files_list = [file["uri"] for file in record_json["metadata"]["files"]]
        if expand:
            # let's unwind file indexes
            files_list_expanded = []
            for file_ in files_list:
                if file_.endswith("_file_index.txt"):
                    url_file = file_.replace(SERVER_ROOT_URI, server)
                    req = requests.get(url_file)
                    for url_individual_file in req.text.split("\n"):
                        if url_individual_file:
                            files_list_expanded.append(url_individual_file)
                elif file_.endswith("_file_index.json"):
                    pass
                else:
                    files_list_expanded.append(file_)
            files_list = files_list_expanded
        if protocol == "http":
            files_list = [
                file_.replace(SERVER_ROOT_URI, server) for file_ in files_list
            ]
        elif protocol == "https":
            files_list = [
                file_.replace(SERVER_ROOT_URI, SERVER_HTTPS_URI) for file_ in files_list
            ]
    return files_list


def get_file_info_remote(server, recid, protocol=None, filtered_files=None):
    """Return remote file information list for given record.

    :param server: CERN Open Data server to query
    :param recid: Record ID
    :param filtered_files: list of file locations after applying filters(if any)
    :type server: str
    :type recid: int
    :type filtered_files: list

    :return: Returns a list of dictionaries containing (checksum, name, size,
    uri) for each file in the record.  Note that 'name' property is
    not stored remotely, but is calculated in this function for
    convenience.
    :rtype: list
    """
    file_info_remote = []
    record_json = get_record_as_json(server=server, recid=recid)
    for file_info in record_json["metadata"]["files"]:
        file_checksum = file_info["checksum"]
        file_size = file_info["size"]
        file_uri = file_info["uri"]
        file_name = file_info["uri"].rsplit("/", 1)[1]
        if protocol == "http":
            file_uri = file_info["uri"].replace(SERVER_ROOT_URI, server)
        elif protocol == "https":
            file_uri = file_info["uri"].replace(SERVER_ROOT_URI, SERVER_HTTPS_URI)
        if not filtered_files or file_uri in filtered_files:
            file_info_remote.append(
                {
                    "checksum": file_checksum,
                    "name": file_name,
                    "size": file_size,
                    "uri": file_uri,
                }
            )
    return file_info_remote


def get_list_directory_recursive(path, timeout):
    """Return list of contents of a EOSPUBLIC Open Data directory recursively.

    :param path: EOSPUBLIC path
    :type path: str

    :return: List of files
    :rtype: list
    """
    files_list = []
    timeout_flag = False
    start_time = datetime.datetime.now()
    fs = XRootDPyFS("root://eospublic.cern.ch//")
    try:
        for dirs, files in fs.walk(path):
            current_time = datetime.datetime.now()
            elapsed_time = current_time - start_time
            if elapsed_time.seconds > timeout:
                timeout_flag = True
                break
            else:
                for _file in files:
                    files_list.append(_file)
        return files_list, timeout_flag
    except Exception:
        display_message(
            msg_type="error",
            msg="Directory {} does not exist.".format(path),
        )
        sys.exit(1)


def get_list_directory(path, recursive, timeout):
    """Return list of contents of a EOSPUBLIC Open Data directory.

    :param path: EOSPUBLIC path
    :param recursive: Iterate recurcively in the given directory path.
    :param timeout: Timeout for list-directory command.
    :type path: str
    :type recursive: bool
    :type timeout: int

    :return: List of files
    :rtype: list
    """
    if not xrootd_available:
        display_message(
            msg_type="error",
            msg="xrootd is required for this operation but it is not installed on your system.",
        )
        sys.exit(1)
    if not recursive:
        directory = SERVER_ROOT_URI + path
        fs = XRootDPyFS(directory)
        try:
            files_list = fs.listdir()
            return files_list
        except Exception:
            display_message(
                msg_type="error",
                msg="Directory {} does not exist.".format(path),
            )
            sys.exit(1)
    else:
        files_list, timeout_flag = get_list_directory_recursive(path, timeout)
        if timeout_flag:
            display_message(
                msg_type="error",
                msg="Command timed out. Please provide more specific path.",
            )
            sys.exit(2)
        return files_list
