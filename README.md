This repository holds the spec file and associated Makefiles used for the [otaylor/restic](https://copr.fedorainfracloud.org/coprs/otaylor/restic/) COPR.

Updating the version
--------------------

* Update version in spec file, add a changelog entry
* Run `make update-sources`
* Commit the result
* Push to upstream
* Start a new copr build (or set up a webhook to build on push)
