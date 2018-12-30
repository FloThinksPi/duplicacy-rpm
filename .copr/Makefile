outdir = .
VERSION := $(shell rpm -q --queryformat='%{version}' --specfile duplicacy.spec)
RELEASE := $(shell rpm -q --queryformat='%{release}' --specfile duplicacy.spec)
ARCH := $(shell rpm -q --queryformat='%{arch}' --specfile duplicacy.spec)
SRPM := duplicacy-$(VERSION)-$(RELEASE).src.rpm
SOURCE := duplicacy-$(VERSION).tar.gz
SHA512 := $(shell grep $(SOURCE) sources | sed s'/^[^=]*= *//')

download:
	[ -e $(SOURCE) ] || curl -L -o $(SOURCE) https://github.com/gilbertchen/duplicacy/releases/download/v$(VERSION)/duplicacy-$(VERSION).tar.gz

update-sources: download
	if ( echo SHA512 "($(SOURCE))" = $$(sha512sum $(SOURCE) | cut -f 1 -d ' ') ; grep -v '(duplicacy-.*.tar.gz)' sources || true ) > sources.new ; then \
	    mv sources.new sources ; \
	else \
	    rm sources.new ; \
	fi

srpm: download
	sha512sum --check sources
	rpmbuild -bs duplicacy.spec --define "_sourcedir ." --define "_srcrpmdir $(outdir)"

rpm: srpm
	rm mock/*.rpm
	mock --rebuild --resultdir=mock $(SRPM)
	mv mock/*.$(ARCH).rpm .

.PHONY:
	rpm srpm download update-source
