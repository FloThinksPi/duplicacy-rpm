all:
	@echo Usage: make [srpm/rpm/clean]

srpm:
	make -f .copr/Makefile srpm

rpm:
	make -f .copr/Makefile rpm

update-sources:
	make -f .copr/Makefile update-sources

clean:
	rm -rf *.tar.gz *.rpm mock

.PHONY:
	rpm srpm update-source clean

