%global package_speccommit 075f4fedc8d0f4d5ed4d820746e9856a98428951
%global package_srccommit v1.0.1
%define private_config_path /opt/xensource/rpmconfig/
%define replace_spaces() %(echo -n "%1" | sed 's/ /_/g')
%global my_rpmdir /usr/lib/rpm

Name:           xenserver-config
Version: 1.0.1
Release: 3%{?xsrel}%{?dist}
Summary:        XenServer configuration
License:        GPL+
BuildArch:      noarch
## Break this link and allow xenserver-release-config to pull in
## the "packages" sub-package so that it is only included in real installs
## and not buildroots. Leave it here and commented out so that people know
## why. When the time comes to retire xenserver-release-config, we will need
## another subpackage here which will have it as a virtual Provides and this
## Requires: will then move to there and be uncommented.
# Requires:       %%{name}-packages
Provides:       system-config = %{version}

BuildRequires:  systemd
Source0: xenserver-config-1.0.1.tar.gz

%description
Additional utilities and configuration for XenServer.

%package        presets
Summary:        XenServer presets file
Provides:       xs-presets = 1.4
Requires(posttrans): systemd

%description    presets
XenServer preset file.

%package        packages
Summary:        Xenserver package importer
Requires:       xenserver-telemetry >= 1.0.1
Requires:       xenserver-nagios-plugins >= 1.0.4
Requires:       nagios-plugins-nrpe >= 4.1.0-4
Requires:       nagios-plugins-disk >= 2.4.3-2
Requires:       nagios-plugins-load >= 2.4.3-2
Requires:       nagios-plugins-swap >= 2.4.3-2
Requires:       xenserver-snmp-agent >= 1.0.8-1

%description    packages
A means of requiring extra packages into an installation when the install groups cannot be updated.

%package        rpm
Summary:        Xenserver RPM config
Provides:       system-rpm-config = %{version}-%{release}

%description    rpm
Xenserver RPM Configuration. Most of this is taken originally from
distributions such as CentOS and/or Fedora, and are preserved here to
ensure that changes are synchronised to Xenserver's release schedules, but
some are Xenserver-specific and may diverge over time as needs require.

%package        macros
Summary:        Xenserver RPM macros
Requires:       %{name}-rpm = %{version}-%{release}

%description    macros
Xenserver RPM Macros.

%prep
%autosetup

%build

%install
# Fileattrs
mkdir -p %{buildroot}/%{my_rpmdir}/fileattrs
# install -D -m 644 rpmconfig/fileattrs/libsymlink.attr %%{buildroot}/%%{my_rpmdir}/fileattrs/libsymlink.attr
# lua
install -D -m 644 rpmconfig/lua/xenserver/common.lua %{buildroot}/%{my_rpmdir}/lua/xenserver/common.lua
install -D -m 644 rpmconfig/lua/xenserver/srpm/forge.lua %{buildroot}/%{my_rpmdir}/lua/xenserver/srpm/forge.lua
# macros.d
# install -D -m 644 rpmconfig/macros.d/macros.build-constraints %%{buildroot}/%%{my_rpmdir}/macros.d/macros.build-constraints
install -D -m 644 rpmconfig/macros.d/macros.dwz %{buildroot}/%{my_rpmdir}/macros.d/macros.dwz
install -D -m 644 rpmconfig/macros.d/macros.forge %{buildroot}/%{my_rpmdir}/macros.d/macros.forge
install -D -m 644 rpmconfig/macros.d/macros.ldc-srpm %{buildroot}/%{my_rpmdir}/macros.d/macros.ldc-srpm
install -D -m 644 rpmconfig/macros.d/macros.ldconfig %{buildroot}/%{my_rpmdir}/macros.d/macros.ldconfig
install -D -m 644 rpmconfig/macros.d/macros.misc %{buildroot}/%{my_rpmdir}/macros.d/macros.misc
install -D -m 644 rpmconfig/macros.d/macros.misc-srpm %{buildroot}/%{my_rpmdir}/macros.d/macros.misc-srpm
install -D -m 644 rpmconfig/macros.d/macros.shell-completions %{buildroot}/%{my_rpmdir}/macros.d/macros.shell-completions
install -D -m 644 rpmconfig/macros.d/macros.valgrind-srpm %{buildroot}/%{my_rpmdir}/macros.d/macros.valgrind-srpm
install -D -m 644 rpmconfig/macros.d/macros.vpath %{buildroot}/%{my_rpmdir}/macros.d/macros.vpath
install -D -m 644 rpmconfig/macros.d/macros.xenserver %{buildroot}/%{my_rpmdir}/macros.d/macros.xenserver
# RPM scripts
install -D -m 755 rpmconfig/xenserver/brp-ldconfig %{buildroot}/%{my_rpmdir}/xenserver/brp-ldconfig
install -D -m 755 rpmconfig/xenserver/brp-llvm-compile-lto-elf %{buildroot}/%{my_rpmdir}/xenserver/brp-llvm-compile-lto-elf
install -D -m 755 rpmconfig/xenserver/brp-mangle-shebangs %{buildroot}/%{my_rpmdir}/xenserver/brp-mangle-shebangs
install -D -m 755 rpmconfig/xenserver/brp-strip-lto %{buildroot}/%{my_rpmdir}/xenserver/brp-strip-lto
install -D -m 755 rpmconfig/xenserver/config.guess %{buildroot}/%{my_rpmdir}/xenserver/config.guess
install -D -m 755 rpmconfig/xenserver/config.sub %{buildroot}/%{my_rpmdir}/xenserver/config.sub
install -D -m 755 rpmconfig/xenserver/dist.sh %{buildroot}/%{my_rpmdir}/xenserver/dist.sh
install -D -m 755 rpmconfig/xenserver/find-provides %{buildroot}/%{my_rpmdir}/xenserver/find-provides
install -D -m 755 rpmconfig/xenserver/find-requires %{buildroot}/%{my_rpmdir}/xenserver/find-requires
install -D -m 755 rpmconfig/xenserver/gpgverify %{buildroot}/%{my_rpmdir}/xenserver/gpgverify
install -D -m 644 rpmconfig/xenserver/macros %{buildroot}/%{my_rpmdir}/xenserver/macros
install -D -m 644 rpmconfig/xenserver/rpmrc %{buildroot}/%{my_rpmdir}/xenserver/rpmrc
install -D -m 644 rpmconfig/xenserver/xenserver-hardened-cc1 %{buildroot}/%{my_rpmdir}/xenserver/xenserver-hardened-cc1
install -D -m 644 rpmconfig/xenserver/xenserver-hardened-clang.cfg %{buildroot}/%{my_rpmdir}/xenserver/xenserver-hardened-clang.cfg
install -D -m 644 rpmconfig/xenserver/xenserver-hardened-ld %{buildroot}/%{my_rpmdir}/xenserver/xenserver-hardened-ld
# doc
install -D -m 644 rpmconfig/doc/%{name}/buildflags.md %{buildroot}/%{_pkgdocdir}/buildflags.md

# An empty files section is necessary to get RPM to create output
%files

# An empty files section is necessary to get RPM to create output
%files packages

%files rpm
%dir %{my_rpmdir}/fileattrs
%{my_rpmdir}/lua
%dir %{my_rpmdir}/macros.d
# %%{my_rpmdir}/macros.d/macros.build-constraints
%{my_rpmdir}/macros.d/macros.dwz
%{my_rpmdir}/macros.d/macros.misc
%{my_rpmdir}/macros.d/macros.misc-srpm
%{my_rpmdir}/macros.d/macros.forge
%{my_rpmdir}/macros.d/macros.ldc-srpm
%{my_rpmdir}/macros.d/macros.ldconfig
%{my_rpmdir}/macros.d/macros.shell-completions
%{my_rpmdir}/macros.d/macros.valgrind-srpm
%{my_rpmdir}/macros.d/macros.vpath
%{my_rpmdir}/xenserver
%{_pkgdocdir}

%files macros
%{my_rpmdir}/macros.d/macros.xenserver

%changelog
* Wed Oct 25 2023 Deli Zhang <deli.zhang@cloud.com> - 1.0.1-3
- CP-44169: Add xenserver-snmp-agent package requires

* Thu May 18 2023 Deli Zhang <dzhang@tibco.com> - 1.0.1-2
- CP-42775: Add NRPE packages requires

* Mon May 15 2023 Tim Smith <tim.smith@citrix.com> - 1.0.1-1
- Convert to non-patchqueue package with internal sources

* Thu May 04 2023 Tim Smith <tim.smith@citrix.com> - 1.0.0-4
- CA-377018 Do not Require xenserver-config-packages from xenserver-config

* Wed Apr 26 2023 Ming Lu <ming.lu@cloud.com> - 1.0.0-3
- Requires xenserver-telemetry

* Fri Apr 14 2023 Tim Smith <tim.smith@citrix.com> - 1.0.0-2
- Config package should be noarch
- Add macros package

* Tue Apr 04 2023 Tim Smith <tim.smith@citrix.com> - 1.0.0-1
- Initial package
