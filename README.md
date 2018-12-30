This repository holds the spec file and associated Makefiles used for the [flothinkspi/duplicacy](https://copr.fedorainfracloud.org/coprs/flothinkspi/duplicacy/) COPR.

This Project only packages https://github.com/gilbertchen/duplicacy for Fedora/Centos Distributions.

Manually Updating to the newest version
--------------------
* Edit Version, Changelog and Revision in Specfile
* Run `make update-sources`
* Commit the result
* Push to upstream
* Start a new copr build (or set up a webhook to build on push)


Autoupdating on new Release
--------------------

* Run triggerBuild.sh via CRON every X Minutes
* The Script will look for a newer Version on Github Releases than defined in the Specfile
* If a newer Version is Found it will edit the Specfile, trigger `make update-sources` and automatically commit and push the Changes which triggers the COPR webhook.
