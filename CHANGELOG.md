<!-- markdownlint-disable MD012 MD013 -->

# Changelog

## [2.0.0](https://github.com/tiborsimko/cernopendata-client/compare/v1.0.0...2.0.0) (2025-11-05)


### ⚠ BREAKING CHANGES

* **python:** Drops support for Python 3.6 and 3.7.

### Build

* **docker:** upgrade to Ubuntu 24.04 and Python 3.12 ([#143](https://github.com/tiborsimko/cernopendata-client/issues/143)) ([bac8200](https://github.com/tiborsimko/cernopendata-client/commit/bac82006d8ab701c45c4a80df6cec1abfec5963a))
* **python:** add support for Python 3.13 ([#146](https://github.com/tiborsimko/cernopendata-client/issues/146)) ([1714dbf](https://github.com/tiborsimko/cernopendata-client/commit/1714dbf62fef7a9267629c2baef77d33427c15d0))
* **python:** add support for Python 3.14 ([#158](https://github.com/tiborsimko/cernopendata-client/issues/158)) ([0083d29](https://github.com/tiborsimko/cernopendata-client/commit/0083d290687bc462f97c060b45e3d0a4c6eee131))
* **python:** drop support for Python 3.6 and 3.7 ([#143](https://github.com/tiborsimko/cernopendata-client/issues/143)) ([cb633e0](https://github.com/tiborsimko/cernopendata-client/commit/cb633e0f3a49484a852033bdf053207b0233670d))


### Bug fixes

* **searcher:** adapt to the new metadata schema with file indices ([#147](https://github.com/tiborsimko/cernopendata-client/issues/147)) ([bab9401](https://github.com/tiborsimko/cernopendata-client/commit/bab94012690bdd7a71ad2542920a8a82b670ddf3)), closes [#148](https://github.com/tiborsimko/cernopendata-client/issues/148)
* **searcher:** respect `get-file-locations --protocol` parameter ([#154](https://github.com/tiborsimko/cernopendata-client/issues/154)) ([625eb9d](https://github.com/tiborsimko/cernopendata-client/commit/625eb9d301a4a8d3c5fef25efdeb505fe45b846c)), closes [#152](https://github.com/tiborsimko/cernopendata-client/issues/152)
* **searcher:** respect `get-file-locations --server` parameter ([#155](https://github.com/tiborsimko/cernopendata-client/issues/155)) ([16af0d0](https://github.com/tiborsimko/cernopendata-client/commit/16af0d0b90a75c38551b4c152bfad33b4886ed45)), closes [#153](https://github.com/tiborsimko/cernopendata-client/issues/153)


### Code refactoring

* **docs:** move from reST to Markdown ([#145](https://github.com/tiborsimko/cernopendata-client/issues/145)) ([845b1bc](https://github.com/tiborsimko/cernopendata-client/commit/845b1bc09d6b022d744bec87e79208d4ce2d0691))


### Test suite

* **metadater:** adapt filtering test after CCID removal ([#147](https://github.com/tiborsimko/cernopendata-client/issues/147)) ([4ff86a9](https://github.com/tiborsimko/cernopendata-client/commit/4ff86a91d87b57da15b48dfd491ae8913a156567))
* **verifier:** replace `sed` calls with native Python code ([#157](https://github.com/tiborsimko/cernopendata-client/issues/157)) ([20588e8](https://github.com/tiborsimko/cernopendata-client/commit/20588e8a5dc919476db6d447ec6daed331b18130))


### Continuous integration

* **actions:** update GitHub actions due to Node 16 deprecation ([#143](https://github.com/tiborsimko/cernopendata-client/issues/143)) ([a3a898e](https://github.com/tiborsimko/cernopendata-client/commit/a3a898ed9bd50b30b439b60e90cd166b74615524))
* **actions:** upgrade to Ubuntu 24.04 and Python 3.12 ([#143](https://github.com/tiborsimko/cernopendata-client/issues/143)) ([925c0b5](https://github.com/tiborsimko/cernopendata-client/commit/925c0b5ddc471bc6937b718f4178934bd818602a))
* Add Github Actions ([92404ce](https://github.com/tiborsimko/cernopendata-client/commit/92404ce228beea86f16796a756a423728f0d8cc6))
* add shellcheck and improve run-tests script ([f16b5f7](https://github.com/tiborsimko/cernopendata-client/commit/f16b5f7a174c757d7f3a916bac71f9c81358c245)), closes [#64](https://github.com/tiborsimko/cernopendata-client/issues/64) [#66](https://github.com/tiborsimko/cernopendata-client/issues/66)
* **commitlint:** addition of commit message linter ([#143](https://github.com/tiborsimko/cernopendata-client/issues/143)) ([e01fff8](https://github.com/tiborsimko/cernopendata-client/commit/e01fff80623da66299794dec3f94ec9c1946fbb3))
* **jsonlint:** add JSON linting ([#150](https://github.com/tiborsimko/cernopendata-client/issues/150)) ([cab5fcb](https://github.com/tiborsimko/cernopendata-client/commit/cab5fcba919557af09b39df7cf99c7390f4b8679))
* **markdownlint:** add Markdown linting ([#150](https://github.com/tiborsimko/cernopendata-client/issues/150)) ([45a2a5f](https://github.com/tiborsimko/cernopendata-client/commit/45a2a5f6aa5f3f9d64dfcda45e1eec9e67d3515d))
* **prettier:** add Prettier code formatting checks ([#150](https://github.com/tiborsimko/cernopendata-client/issues/150)) ([1020c7c](https://github.com/tiborsimko/cernopendata-client/commit/1020c7cf5dde9c3397e3073eda73ba0537081351))
* **release-please:** increment version number in Dockerfile ([#151](https://github.com/tiborsimko/cernopendata-client/issues/151)) ([1bbfcd5](https://github.com/tiborsimko/cernopendata-client/commit/1bbfcd5d1a6fa0f32014e2ad50f3a255b0ca1f55))
* **release-please:** initial Release Please configuration ([#143](https://github.com/tiborsimko/cernopendata-client/issues/143)) ([5724844](https://github.com/tiborsimko/cernopendata-client/commit/5724844659369e7888a76bf58abf5e556c9f286e))
* **run-tests:** add usage help and refactor options ([#150](https://github.com/tiborsimko/cernopendata-client/issues/150)) ([b9368d8](https://github.com/tiborsimko/cernopendata-client/commit/b9368d83577bdc1e0a2305dde56c2fc22ff97eb9))
* **run-tests:** stop properly after running all tests ([#145](https://github.com/tiborsimko/cernopendata-client/issues/145)) ([357a719](https://github.com/tiborsimko/cernopendata-client/commit/357a719b25aa65ce8569989a3abd2c92f0a5e7e9))
* **shfmt:** add shfmt code formatting checks ([#150](https://github.com/tiborsimko/cernopendata-client/issues/150)) ([e70291e](https://github.com/tiborsimko/cernopendata-client/commit/e70291e62e9331e46977741f847383de32c7f08c))
* **yamllint:** add YAML linting ([#150](https://github.com/tiborsimko/cernopendata-client/issues/150)) ([0d70783](https://github.com/tiborsimko/cernopendata-client/commit/0d707832ef1835092d043d15e44b01f5dda0730c))


### Documentation

* add Development section ([65da439](https://github.com/tiborsimko/cernopendata-client/commit/65da439d53aa67e661988b6d34f9554c9a12db50))
* Add GH actions and Codecov CI badge ([b30daa0](https://github.com/tiborsimko/cernopendata-client/commit/b30daa019c40e608cd3044a5782afe33a1c8fbbd))
* addition of badges ([d6fde62](https://github.com/tiborsimko/cernopendata-client/commit/d6fde62a06e2156c0a4263270ac23370531f2142))
* autodoc_mock_imports for pycurl ([5765a02](https://github.com/tiborsimko/cernopendata-client/commit/5765a02dcd2dfb522881d1ea7aa2cda453188730))
* download-files and verify-files log formatting ([b20cd72](https://github.com/tiborsimko/cernopendata-client/commit/b20cd72d67b6c330732b554c8d6b9b224a5ea35e))
* enrich CLI API page ([470143c](https://github.com/tiborsimko/cernopendata-client/commit/470143cc01e88abff6f08aa194e3deb4ad3451ee)), closes [#55](https://github.com/tiborsimko/cernopendata-client/issues/55)
* fix command-line typo ([7c8532f](https://github.com/tiborsimko/cernopendata-client/commit/7c8532ff5d0977b85526beb789ba65346ca12ffd))
* fix Sphinx-related exception ([b5723b3](https://github.com/tiborsimko/cernopendata-client/commit/b5723b3047f757889a99e6fe861d82a81c93a4b9))
* flatter CLI API hierarchy ([d3c9c15](https://github.com/tiborsimko/cernopendata-client/commit/d3c9c151b064f897a5bff282b48823c08030fff7))
* formatting improvements ([e3ce8fb](https://github.com/tiborsimko/cernopendata-client/commit/e3ce8fb05091b9ec79773d439c086dbd45f08f9c))
* initialize sphinx documentation ([0b2d584](https://github.com/tiborsimko/cernopendata-client/commit/0b2d5847d9a7ec9d132ac32719c9ebcf73fd5387))
* introduce pydocstyle ([252b3fb](https://github.com/tiborsimko/cernopendata-client/commit/252b3fbaa59256a89b05a3103a45e27aea372216)), closes [#53](https://github.com/tiborsimko/cernopendata-client/issues/53)
* mention xrootd and pycurl installation options ([91dcd9b](https://github.com/tiborsimko/cernopendata-client/commit/91dcd9b81c1cfb0f0c5c91ba167668113f06882d)), closes [#80](https://github.com/tiborsimko/cernopendata-client/issues/80)
* migration to ReadTheDocs v2 ([eead01e](https://github.com/tiborsimko/cernopendata-client/commit/eead01e75f8ab5f7a8e3867e87eca8db1da9c7a0))
* minor improvements to the Development section ([8f81811](https://github.com/tiborsimko/cernopendata-client/commit/8f818117182318491fe9daf8f97a87e0b5979222))
* new author ([514823e](https://github.com/tiborsimko/cernopendata-client/commit/514823eec237976d1394744e704d5fab3a72d71b))
* new documentation structure ([c993ea3](https://github.com/tiborsimko/cernopendata-client/commit/c993ea39f3518533d5054a81f1e0f0caa8d02680))
* ReadTheDocs configuration file ([2a4e4b9](https://github.com/tiborsimko/cernopendata-client/commit/2a4e4b9a1aa0a052dadbf72886a87e1e2268897b))
* richer user guide ([c04eeb4](https://github.com/tiborsimko/cernopendata-client/commit/c04eeb4227fbfe57242e9ae1f0e2fbeef4056401))
* shows complete `--help` output ([9cc277d](https://github.com/tiborsimko/cernopendata-client/commit/9cc277d12f9c977cf6ca60aae93c99df2bca52a7))
* **usage:** add an example on how to retrieve container images ([#141](https://github.com/tiborsimko/cernopendata-client/issues/141)) ([fef3295](https://github.com/tiborsimko/cernopendata-client/commit/fef329555565c2d6a4b0841da57b7fe7665c49c5))

## [1.0.0](https://github.com/cernopendata/cernopendata-client/compare/0.4.0...1.0.0) (2025-02-25)


### ⚠ BREAKING CHANGES

* **python:** Drops support for Python 3.6 and 3.7.

### Build

* **docker:** upgrade to Ubuntu 24.04 and Python 3.12 ([#143](https://github.com/cernopendata/cernopendata-client/issues/143)) ([bac8200](https://github.com/cernopendata/cernopendata-client/commit/bac82006d8ab701c45c4a80df6cec1abfec5963a))
* **python:** add support for Python 3.13 ([#146](https://github.com/cernopendata/cernopendata-client/issues/146)) ([1714dbf](https://github.com/cernopendata/cernopendata-client/commit/1714dbf62fef7a9267629c2baef77d33427c15d0))
* **python:** drop support for Python 3.6 and 3.7 ([#143](https://github.com/cernopendata/cernopendata-client/issues/143)) ([cb633e0](https://github.com/cernopendata/cernopendata-client/commit/cb633e0f3a49484a852033bdf053207b0233670d))


### Bug fixes

* **searcher:** adapt to the new metadata schema with file indices ([#147](https://github.com/cernopendata/cernopendata-client/issues/147)) ([bab9401](https://github.com/cernopendata/cernopendata-client/commit/bab94012690bdd7a71ad2542920a8a82b670ddf3)), closes [#148](https://github.com/cernopendata/cernopendata-client/issues/148)


### Code refactoring

* **docs:** move from reST to Markdown ([#145](https://github.com/cernopendata/cernopendata-client/issues/145)) ([845b1bc](https://github.com/cernopendata/cernopendata-client/commit/845b1bc09d6b022d744bec87e79208d4ce2d0691))


### Test suite

* **metadater:** adapt filtering test after CCID removal ([#147](https://github.com/cernopendata/cernopendata-client/issues/147)) ([4ff86a9](https://github.com/cernopendata/cernopendata-client/commit/4ff86a91d87b57da15b48dfd491ae8913a156567))


### Continuous integration

* **actions:** update GitHub actions due to Node 16 deprecation ([#143](https://github.com/cernopendata/cernopendata-client/issues/143)) ([a3a898e](https://github.com/cernopendata/cernopendata-client/commit/a3a898ed9bd50b30b439b60e90cd166b74615524))
* **actions:** upgrade to Ubuntu 24.04 and Python 3.12 ([#143](https://github.com/cernopendata/cernopendata-client/issues/143)) ([925c0b5](https://github.com/cernopendata/cernopendata-client/commit/925c0b5ddc471bc6937b718f4178934bd818602a))
* **commitlint:** addition of commit message linter ([#143](https://github.com/cernopendata/cernopendata-client/issues/143)) ([e01fff8](https://github.com/cernopendata/cernopendata-client/commit/e01fff80623da66299794dec3f94ec9c1946fbb3))
* **jsonlint:** add JSON linting ([#150](https://github.com/cernopendata/cernopendata-client/issues/150)) ([cab5fcb](https://github.com/cernopendata/cernopendata-client/commit/cab5fcba919557af09b39df7cf99c7390f4b8679))
* **markdownlint:** add Markdown linting ([#150](https://github.com/cernopendata/cernopendata-client/issues/150)) ([45a2a5f](https://github.com/cernopendata/cernopendata-client/commit/45a2a5f6aa5f3f9d64dfcda45e1eec9e67d3515d))
* **prettier:** add Prettier code formatting checks ([#150](https://github.com/cernopendata/cernopendata-client/issues/150)) ([1020c7c](https://github.com/cernopendata/cernopendata-client/commit/1020c7cf5dde9c3397e3073eda73ba0537081351))
* **release-please:** increment version number in Dockerfile ([#151](https://github.com/cernopendata/cernopendata-client/issues/151)) ([1bbfcd5](https://github.com/cernopendata/cernopendata-client/commit/1bbfcd5d1a6fa0f32014e2ad50f3a255b0ca1f55))
* **release-please:** initial Release Please configuration ([#143](https://github.com/cernopendata/cernopendata-client/issues/143)) ([5724844](https://github.com/cernopendata/cernopendata-client/commit/5724844659369e7888a76bf58abf5e556c9f286e))
* **run-tests:** add usage help and refactor options ([#150](https://github.com/cernopendata/cernopendata-client/issues/150)) ([b9368d8](https://github.com/cernopendata/cernopendata-client/commit/b9368d83577bdc1e0a2305dde56c2fc22ff97eb9))
* **run-tests:** stop properly after running all tests ([#145](https://github.com/cernopendata/cernopendata-client/issues/145)) ([357a719](https://github.com/cernopendata/cernopendata-client/commit/357a719b25aa65ce8569989a3abd2c92f0a5e7e9))
* **shfmt:** add shfmt code formatting checks ([#150](https://github.com/cernopendata/cernopendata-client/issues/150)) ([e70291e](https://github.com/cernopendata/cernopendata-client/commit/e70291e62e9331e46977741f847383de32c7f08c))
* **yamllint:** add YAML linting ([#150](https://github.com/cernopendata/cernopendata-client/issues/150)) ([0d70783](https://github.com/cernopendata/cernopendata-client/commit/0d707832ef1835092d043d15e44b01f5dda0730c))


### Documentation

* **usage:** add an example on how to retrieve container images ([#141](https://github.com/cernopendata/cernopendata-client/issues/141)) ([fef3295](https://github.com/cernopendata/cernopendata-client/commit/fef329555565c2d6a4b0841da57b7fe7665c49c5))

## 0.4.0 (2024-08-22)

* Adds support for Python 3.11 and 3.12.
* Improves `get-metadata --output-field` command by adding a new `--filter`
  option allowing to output only selected field values matching desired
  criteria.
* Changes container image base to Fedora 38 and slightly optimises image size.
* Drops support for Python 2.7.

## 0.3.0 (2022-03-16)

* Adds support for Python 3.10.
* Improves `download-files` command to resume interrupted downloads when using
  HTTP downloads with `pycurl` engine.
* Improves XRootD downloader by using vanilla XRootD package. Changes
  `xrootdpyfs` to `xrootd` download engine.
* Improves `download-files` command with a new option `--download-engine` to
  select `pycurl` or `requests` engines when downloading files over HTTP.
* Fixes minor issues with file index unwinding and output directory handling.

## 0.2.0 (2020-11-19)

* Adds new `list-directory` command to list content of EOS directories holding
  open data files.
* Adds support for Python 3.9.
* Improves `download-files` command to allow using XRootD protocol.
* Improves `download-files` command to allow using HTTPS protocol.
* Improves `download-files` command to optionally verify file integrity as soon
  as files are being downloaded.
* Improves `get-file-locations` command to optionally output file sizes and
  checksums.
* Improves output format colouring to better indicate notes and errors.
* Fixes minor issues and improves code coverage.

## 0.1.0 (2020-09-24)

* Enriches `download-files` command to optionally download only files matching
  certain name, regexp, or range count.
* Adds new `verify-files` command to verify number, size, and checksum of
  downloaded files.
* Improves `get-metadata` command with respect to outputting only certain
  desired metadata field values.
* Enriches user documentation.

## 0.0.1 (2020-09-09)

* Initial public release.
