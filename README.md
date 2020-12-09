<div><a href="https://copr.fedorainfracloud.org/coprs/flothinkspi/duplicacy/package/duplicacy/"><img src="https://copr.fedorainfracloud.org/coprs/flothinkspi/duplicacy/package/duplicacy/status_image/last_build.png" /></a><br><br></div>

# Duplicacy-RPM

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

* Run autoUpdate.sh scheduled
* The Script will look for a newer Version on Github Releases than defined in the Specfile
* If a newer Version is Found it will edit the files `dulpicacy.spec` and `sources` and make a commit
* You then have to automatically push them into the repo.
* When a webhook is defined Copr will see the changed specfile and sources file and trigger a new build.

This procedure is done in a [Github Action File](https://github.com/FloThinksPi/duplicacy-rpm/blob/master/.github/workflows/autoupdate_version.yml).

The Logs for the update job can be found [here](https://github.com/FloThinksPi/duplicacy-rpm/actions).

The Logs for the bould of rpm packages can be found [here](https://copr.fedorainfracloud.org/coprs/flothinkspi/duplicacy/builds/).

