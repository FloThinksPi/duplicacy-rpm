Name:    duplicacy
Version: 2.1.2
Release: 1%{?dist}
Summary: Backup software written in golang
URL:     https://github.com/gilbertchen/duplicacy
License: Custom License

BuildRequires: golang
Source0: https://github.com/gilbertchen/%{name}/archive/v%{version}.tar.gz

%define debug_package %{nil}

%description
Duplicacy is a new generation cross-platform cloud backup tool based on the idea of Lock-Free Deduplication.

%prep
%autosetup

%build
#go get ./...
go run duplicacy/duplicacy_main.go

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}/%{_bindir}

%files
%{_bindir}/%{name}

%license LICENSE

%changelog

* Sun Dec 30 2018 Florian Braun - 2.1.2
- Fixed a bug in calculating the padding size during chunk encryption: https://github.com/gilbertchen/duplicacy/commit/21b3d9e57f087d0d7913b0bd444557d4a5208929
- Print the number of files if available in the snapshot file before downloading the file list: https://github.com/gilbertchen/duplicacy/commit/244b797a1c9c1e8ae2d48dd7bb464fe76ba613fc
- Don't list snapshots whose tags don't match the given one when the `-tag` is provided: https://github.com/gilbertchen/duplicacy/commit/073292018cf42361d05e43d9499fa0c3b387d3b8
- Show more statistics in the check command (for the new web-based GUI): https://github.com/gilbertchen/duplicacy/commit/15f15aa2ca5b035a9e5b15331548d2c997b12d04
- In some backends the benchmark command may incorrectly list the chunks directory when looking for previous temporary files: https://github.com/gilbertchen/duplicacy/commit/d8e13d8d85936e88481f9ced6ca2e6e6e3f6d1d0 
- Optimizing restore to avoid reading newly created sparse file: https://github.com/gilbertchen/duplicacy/commit/bfb4b44c0ab9afbbd33cd641c2dab49c3518b751
- Align snapshot times to the beginning of days when calculating the time differences so that prune operations running on the same day will prune the same set of old snapshots: https://github.com/gilbertchen/duplicacy/commit/22a0b222db56c8bbbe0b250e1f2b5fa751b5aaee
- Make B2 backend work with application keys (based on https://github.com/gilbertchen/duplicacy/pull/475 by @bekriebel): https://github.com/gilbertchen/duplicacy/commit/674d35e5cae603b641a048609ff48335a36ebb36
- Restore UID and GID of symlinks: https://github.com/gilbertchen/duplicacy/commit/a7d2a941bec536b54f89c8c1656598e3edf16fa8
- Fixed a divide by zero bug when the repository has only zero-byte files: https://github.com/gilbertchen/duplicacy/commit/39d71a325606698abcf060630622f3ec31590faa
- Do not update the Windows keyring file if the password remains unchanged: https://github.com/gilbertchen/duplicacy/commit/9d10cc77fcacb16d0910999ddaa39c94cd5faf72
- Continue to check other snapshots when one snapshot has missing chunks: https://github.com/gilbertchen/duplicacy/commit/e8b8922754056f74b605c8deef0b834ab1c9d391
- Record deleted snapshots in the fossil collection and if any deleted snapshot still exists then nuke the fossil collection: https://github.com/gilbertchen/duplicacy/commit/93cc632021a9281ae8dec6225c66e7c43f6607fa
- Add Git commit numbers to version info: https://github.com/gilbertchen/duplicacy/commit/48cc5eaedb400dffb888e4eae797aeb70b62a44a
- Removed a redundant call to manager.chunkOperator.Resurrect (which can cause a crash): https://github.com/gilbertchen/duplicacy/commit/f304b64b3f607a61bdda9e3ece74fe6b022fb6ec
- Remove extra newline in the PRUNE_NEWSNAPSHOT log message: https://github.com/gilbertchen/duplicacy/commit/8ae7d2a97d4bf44359f806d8cb21546cba806275
- Fix crashes on 32 bit machines caused by misaligned 64 bit integers: https://github.com/gilbertchen/duplicacy/commit/fce42348617039134300101a54af4990aa7d6c3c
- Fix "Failed to fossilize chunk" errors in wasabi backend: https://github.com/gilbertchen/duplicacy/pull/459 (by @jtackaberry)
- Add a -storage option to the benchmark comman: https://github.com/gilbertchen/duplicacy/commit/89769f39067370f0b3500ec462df9341953737e3

* Sun Dec 30 2018 Florian Braun - 2.1.1
- Initial Version
