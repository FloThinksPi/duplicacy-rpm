outdir = .
VERSION := $(shell rpm -q --queryformat='%{version}' --specfile restic.spec)
RELEASE := $(shell rpm -q --queryformat='%{release}' --specfile restic.spec)
ARCH := $(shell rpm -q --queryformat='%{arch}' --specfile restic.spec)
SRPM := restic-$(VERSION)-$(RELEASE).src.rpm
SOURCE := restic-$(VERSION).tar.gz
SHA512 := $(shell grep $(SOURCE) sources | sed s'/^[^=]*= *//')

download:
	[ -e $(SOURCE) ] || curl -L -o $(SOURCE) https://github.com/restic/restic/releases/download/v$(VERSION)/restic-$(VERSION).tar.gz

update-sources: download
	if ( echo SHA512 "($(SOURCE))" = $$(sha512sum $(SOURCE) | cut -f 1 -d ' ') ; grep -v '(restic-.*.tar.gz)' sources || true ) > sources.new ; then \
	    mv sources.new sources ; \
	else \
	    rm sources.new ; \
	fi

srpm: download
	sha512sum --check sources
	rpmbuild -bs restic.spec --define "_sourcedir ." --define "_srcrpmdir $(outdir)"

rpm: srpm
	rm mock/*.rpm
	mock --rebuild --resultdir=mock $(SRPM)
	mv mock/*.$(ARCH).rpm .

.PHONY:
	rpm srpm download update-source
