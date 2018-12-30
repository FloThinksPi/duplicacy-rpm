Name:    duplicacy
Version: 2.1.1
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
* Sun Dec 30 2018 Florian Braun - 2.1.1
- Initial Version