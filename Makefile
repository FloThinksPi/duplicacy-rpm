srpm:
	make -f .copr/Makefile srpm

rpm:
	make -f .copr/Makefile rpm

download:
	make -f .copr/Makefile download

update-sources:
	make -f .copr/Makefile update-sources

clean:
	rm -rf *.tar.gz *.rpm mock

.PHONY:
	rpm srpm update-source clean

