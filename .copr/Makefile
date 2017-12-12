outdir = .
VERSION := $(shell rpm -q --queryformat='%{version}' --specfile restic.spec)
RELEASE := $(shell rpm -q --queryformat='%{release}' --specfile restic.spec)
ARCH := $(shell rpm -q --queryformat='%{arch}' --specfile restic.spec)
SRPM := restic-$(VERSION)-$(RELEASE).src.rpm
SOURCE := restic-$(VERSION).tar.gz
SHA512 := $(shell grep $(SOURCE) sources | sed s'/^[^=]*= *//')

srpm:
	[ -e $(SOURCE) ] || curl -L -o $(SOURCE) https://github.com/restic/restic/releases/download/v$(VERSION)/restic-$(VERSION).tar.gz
	sha512sum --check sources
	rpmbuild -bs restic.spec --define "_sourcedir ." --define "_srcrpmdir $(outdir)"

rpm: srpm
	rm mock/*.rpm
	mock --rebuild --resultdir=mock $(SRPM)
	mv mock/*.$(ARCH).rpm .

.PHONY:
	rpm srpm
