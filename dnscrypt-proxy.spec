%global debug_package %{nil}

Name:		dnscrypt-proxy
Version:	2.1.14
Release:	1
Source0:	https://github.com/DNSCrypt/dnscrypt-proxy/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.gz
Source2:	%{name}.service
Source3:	%{name}.socket
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
install -vDm 644 %{name}/example-%{name}.toml %{buildroot}/etc/%{name}/%{name}.toml
  for _config in {{allowed,blocked}-{ips,names},{cloaking,forwarding}-rules,captive-portals}.txt; do
    install -vDm 644 %{name}/example-$_config %{buildroot}/etc/%{name}/$_config
  done

install -vDm 644 utils/generate-domains-blocklist/*.{conf,txt} -t %{buildroot}%{_datadir}/%{name}/utils/generate-domains-blocklist
install -vDm 755 utils/generate-domains-blocklist/generate-domains-blocklist.py %{buildroot}%{_bindir}/generate-domains-blocklist
install -vDm 644 %{S:2} -t %{buildroot}%{_unitdir}
install -vDm 644 %{S:3} -t %{buildroot}%{_unitdir}



%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/generate-domains-blocklist
%{_sysconfdir}/%{name}
%{_unitdir}/dnscrypt-proxy.service
%{_unitdir}/dnscrypt-proxy.socket
%{_datadir}/dnscrypt-proxy/
