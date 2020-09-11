# -*- coding: utf-8 -*-
#
# This file is part of cernopendata-client.
#
# Copyright (C) 2020 CERN.
#
# cernopendata-client is free software; you can redistribute it and/or modify
# it under the terms of the GPLv3 license; see LICENSE file for more details.

"""cernopendata-client cli command get-metadata test."""

from click.testing import CliRunner
from cernopendata_client.cli import get_metadata


def test_get_metadata_from_recid():
    """Test `get-metadata --recid` command."""
    test_get_metadata = CliRunner()
    test_result = test_get_metadata.invoke(get_metadata, ["--recid", 3005])
    assert test_result.exit_code == 0
    assert (
        '"title": "Configuration file for LHE step HIG-Summer11pLHE-00114_1_cfg.py"'
        in test_result.output
    )


def test_get_metadata_from_recid_wrong():
    """Test `get-metadata --recid` command for wrong values."""
    test_get_metadata = CliRunner()
    test_result = test_get_metadata.invoke(get_metadata, ["--recid", 0])
    assert test_result.exit_code == 2


def test_get_metadata_from_doi():
    """Test `get-metadata --doi` command."""
    test_get_metadata = CliRunner()
    test_result = test_get_metadata.invoke(
        get_metadata, ["--doi", "10.7483/OPENDATA.CMS.A342.9982"]
    )
    assert test_result.exit_code == 0
    assert '"title": "/BTau/Run2010B-Apr21ReReco-v1/AOD"' in test_result.output


def test_get_metadata_from_doi_wrong():
    """Test `get-metadata --doi` command for wrong values."""
    test_get_metadata = CliRunner()
    test_result = test_get_metadata.invoke(get_metadata, ["--doi", "NONEXISTING"])
    assert test_result.exit_code == 2
