Name:    duplicacy
Version: 2.7.2
Release: 2%{?dist}
Summary: Backup software written in golang
URL:     https://github.com/gilbertchen/duplicacy
License: Custom License

%if 0%{?el7}
# Work around a git-go conflict in el7
BuildRequires: golang yum
%else
BuildRequires: golang git
%endif
Source0: %{name}-%{version}.tar.gz

%define debug_package %{nil}

%description
Duplicacy is a new generation cross-platform cloud backup tool based on the idea of Lock-Free Deduplication.

%prep
%setup -q -n %{name}-%{version}
rm -rf vendor

%if 0%{?el7}
    # Work around a git-go conflict in el7
    yum -y remove git*
    yum -y install  https://centos7.iuscommunity.org/ius-release.rpm
    yum -y install  git2u-all
%endif

exit

%build
mkdir -p ./_build/src/github.com/gilbertchen
export GOPATH=$(pwd)/_build:%{gopath}
GO111MODULE=on go mod init github.com/gilbertchen/duplicacy || true
GO111MODULE=on go get -d ./...
rm -rf ./_build/src/github.com/gilbertchen/duplicacy
ln -s $(pwd) ./_build/src/github.com/gilbertchen/duplicacy
cd ./_build/src/github.com/gilbertchen/duplicacy
version="FloThinksPi-Copr[$(uname -m)-rpm-package"
GO111MODULE=on go build -o duplicacy/%{name} -ldflags "-X main.GitCommit=$version]" duplicacy/duplicacy_main.go

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./duplicacy/%{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc README.md LICENSE.md GUIDE.md DESIGN.md ACKNOWLEDGEMENTS.md
%license LICENSE.md

%changelog

* Wed Dec 09 2020 Florian Braun - 2.7.2
- Make -vss work with Big Sur: https://github.com/gilbertchen/duplicacy/commit/7c36311aa973c4189a68c4eae4191fa8bf9417e9
- Skip chunks already verified in previous runs when running `check -chunks`: https://github.com/gilbertchen/duplicacy/commit/d7c1903d5a5b06716265a3ea24bd135764a0813d
- Fixed reading/writing extended attributes on Linux by switching to github.com/pkg/xattr: https://github.com/gilbertchen/duplicacy/commit/b392302c0680ca4de569630031c43bab21f51d82
- Fixed a bug that caused a fresh restore of large files to fail without the -overwrite option: https://github.com/gilbertchen/duplicacy/commit/bec3a0edcd6329ed57d287eec996858a3621f567
- Validate that a repository id can only contain letters, numbers, dashes, and underscores: https://github.com/gilbertchen/duplicacy/commit/5eed6c65f688aa5dda1c45143837f4f0f886fff4
- Fixed a crash in the Dropbox backend caused by a nil Seeker: https://github.com/gilbertchen/go-dropbox/commit/2233fa1dd846b3a3e8060b6c1ea12883deb9d288


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
