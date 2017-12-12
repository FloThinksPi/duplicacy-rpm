all:
	@echo Usage: make [srpm/rpm/clean]

srpm:
	make -f .copr/Makefile srpm

rpm:
	make -f .copr/Makefile rpm

clean:
	rm -rf *.tar.gz *.rpm mock

.PHONY:
	rpm srpm

