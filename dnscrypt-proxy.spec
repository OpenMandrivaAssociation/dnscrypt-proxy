%global debug_package %{nil}

Name:		dnscrypt-proxy
Version:	2.1.14
Release:	1
Source0:	https://github.com/DNSCrypt/dnscrypt-proxy/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.gz
Summary:	dnscrypt-proxy 2 - A flexible DNS proxy, with support for encrypted DNS protocols.
URL:		https://github.com/DNSCrypt/dnscrypt-proxy
License:	ISC
Group:		Network/WWW
BuildRequires:	go

%description
A flexible DNS proxy, with support for modern encrypted DNS protocols such as DNSCrypt v2, DNS-over-HTTPS, Anonymized DNSCrypt and ODoH (Oblivious DoH).

%prep
%autosetup -p1
tar zxf %{S:1}
%build
cd %{name}
export GOFLAGS="-buildmode=pie"
go build -v -o %{name}

%install
install -Dpm755 %{name}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
