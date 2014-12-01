%global cartridgedir %{_libexecdir}/openshift/cartridges/memcached

Summary:       Provides Memcached support to OpenShift
Name:          openshift-cartridge-memcached
Version:       1.0
Release:       0%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://memcached.org
Source0:       %{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-cartridge-memcached = 1.0
Provides:      openshift-cartridge-memcached-1.0 = 1.0
BuildArch:     noarch

%description
Provides Memcached cartridge support to OpenShift.

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__rm -rf %{buildroot}%{cartridgedir}/rel-eng

%post
%{_sbindir}/oo-admin-cartridge --action install --source %{cartridgedir}

%files
%{cartridgedir}
%attr(0755,-,-) %{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Mon Dec 01 2014 Builder <getup@getupcloud.com>
- rebuild

* Mon Dec 01 2014 Builder <getup@getupcloud.com> 1.0-0
- new package built with tito

