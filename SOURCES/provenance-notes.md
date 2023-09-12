# Comparison of xenserver-config-rpm + xenserver-config-macros with Fedora/CentOS.

Date: 2023-09-12

## Pure upstream Fedora/CentOS

```
.
└── usr
    └── lib
        └── rpm
            ├── fileattrs: empty dir. Normally provided by rpm-build.
            ├── lua
            │   └── xenserver
            │       ├── common.lua: from redhat-rpm-config, matches latest CentOS 9
            │       └── srpm
            │           └── forge.lua: from redhat-rpm-config, matches latest CentOS 9
            ├── macros.d
            │   ├── macros.dwz: from redhat-rpm-config, matches latest CentOS 9
            │   ├── macros.forge: from redhat-rpm-config, matches latest CentOS 9
            │   ├── macros.ldconfig: from redhat-rpm-config, matches latest CentOS 9
            │   ├── macros.ldc-srpm: from redhat-rpm-config, matches latest CentOS 9
            │   ├── macros.shell-completions: from redhat-rpm-config, matches latest CentOS 9
            │   ├── macros.valgrind-srpm: from redhat-rpm-config, matches latest CentOS 9
            │   └── macros.vpath: from redhat-rpm-config, matches latest CentOS 9
            └── xenserver
                ├── brp-ldconfig: from redhat-rpm-config, matches latest CentOS 9
                ├── brp-llvm-compile-lto-elf: from redhat-rpm-config, matches end of 2022 Fedora
                ├── brp-mangle-shebangs: from redhat-rpm-config, matches latest CentOS 9
                ├── brp-strip-lto: from redhat-rpm-config, matches latest CentOS 9
                ├── config.guess: from redhat-rpm-config, matches end of 2022 Fedora (date in file)
                ├── config.sub: from redhat-rpm-config, matches end of 2022 Fedora (date in file)
                ├── gpgverify: from redhat-rpm-config, matches latest CentOS 9
                └── rpmrc: from redhat-rpm-config, almost matches latest CentOS 9, with just one different line coming from Fedora 3 years ago (no impact, is for aarch64)
```

When we write "matches latest CentOS 9", this only means this is what we compared with first.
It likely also matches latest (or recent enough) Fedora. Some files have been found to be rarely changed over time.

Most of these file likely come from a CentOS or Fedora RPM I haven't found the exact version for,
that I would place somewhere around mid-2022, or the end of it.

## Modified by XenServer

```
.
└── usr
    ├── lib
    │   └── rpm
    │       ├── macros.d
    │       │   ├── macros.misc: is actually macros.fedora-misc from redhat-rpm-config, with one changed line ("redhat" replaced by "xenserver")
    │       │   ├── macros.misc-srpm: is actually macros.fedora-misc-srpm, simply renamed
    │       │   └── macros.xenserver: looks a lot like macros.epel-rpm-macros from the epel-rpm-macros RPM from EPEL 7,
    │       │           but I haven't found a version that matches exactly. Most changes look benign.
    │       │           Main change: macro %xenserver defined instead of %epel.
    │       └── xenserver
    │           ├── dist.sh: from redhat-rpm-config. Changed: RELEASEFILE=/etc/xenserver-release (instead of /etc/redhat-release)
    │                   This path doesn't exist on a XenServer host AFAIK.
    │           ├── find-provides: from redhat-rpm-config. "redhat" becomes "xenserver", which makes it look
    │           │       for /usr/lib/rpm/xenserver/find-provides.ksyms if exists, but I don't think it does.
    │           ├── find-requires: from redhat-rpm-config. "redhat" becomes "xenserver", which makes it look
    │           │       for /usr/lib/rpm/xenserver/find-requires.ksyms if exists, but I don't think it does.
    │           │       Latest Fedora disabled this part anyway because "the Fedora kernel doesn't produce kABI deps".
    │           ├── macros: from redhat-rpm-config. "redhat" replaced by "xenserver" and "redhat-rpm-config" by "xenserver-config-rpm"
    │           ├── xenserver-hardened-cc1: from redhat-rpm-config. Was just renamed from redhat-hardened-cc1.
    │           ├── xenserver-hardened-clang.cfg. Was just renamed from redhat-hardened-cc1.
    │           └── xenserver-hardened-ld. Was just renamed from redhat-hardened-cc1.
    └── share
        └── doc
            └── xenserver-config-1.0.1
                └── buildflags.md: doc from redhat-rpm-config, but "redhat" replaced by "xenserver"
```

In the end, the hard part is to find what version of the upstream file to compare with,
because there exists many revisions in CentOS and Fedora. We haven't found the exact origin version
for each file, but we have a rough idea.

The main changes made by XenServer were branding-related, where "redhat" and "epel" become "xenserver".

There may also be files removed (or not backported) by XenServer from the upstream packages. Not analyzed.
