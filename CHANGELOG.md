# Changelog

## 0.4.0 (2024-08-22)

- Adds support for Python 3.11 and 3.12.
- Improves ``get-metadata --output-field`` command by adding a new ``--filter`` option allowing to output only selected field values matching desired criteria.
- Changes container image base to Fedora 38 and slightly optimises image size.
- Drops support for Python 2.7.

## 0.3.0 (2022-03-16)

- Adds support for Python 3.10.
- Improves ``download-files`` command to resume interrupted downloads when
  using HTTP downloads with ``pycurl`` engine.
- Improves XRootD downloader by using vanilla XRootD package. Changes
  ``xrootdpyfs`` to ``xrootd`` download engine.
- Improves ``download-files`` command with a new option ``--download-engine``
  to select ``pycurl`` or ``requests`` engines when downloading files over
  HTTP.
- Fixes minor issues with file index unwinding and output directory handling.

## 0.2.0 (2020-11-19)

- Adds new ``list-directory`` command to list content of EOS directories
  holding open data files.
- Adds support for Python 3.9.
- Improves ``download-files`` command to allow using XRootD protocol.
- Improves ``download-files`` command to allow using HTTPS protocol.
- Improves ``download-files`` command to optionally verify file integrity as
  soon as files are being downloaded.
- Improves ``get-file-locations`` command to optionally output file sizes and
  checksums.
- Improves output format colouring to better indicate notes and errors.
- Fixes minor issues and improves code coverage.

## 0.1.0 (2020-09-24)

- Enriches ``download-files`` command to optionally download only files
  matching certain name, regexp, or range count.
- Adds new ``verify-files`` command to verify number, size, and checksum of
  downloaded files.
- Improves ``get-metadata`` command with respect to outputting only
  certain desired metadata field values.
- Enriches user documentation.

## 0.0.1 (2020-09-09)

- Initial public release.
