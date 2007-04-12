%define name spec-helper
%define version 0.24
%define release %mkrel 2

Summary: Tools to ease the creation of rpm packages
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
URL: http://www.mandriva.com
License: GPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: perl /sbin/ldconfig findutils /usr/bin/python gettext

%description
Tools to ease the creation of rpm packages for the Mandriva Linux distribution.
Compress man pages using bzip2, strip executables, convert links...

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT bindir=%{_bindir} rpmmacrosdir=%_sys_macros_dir 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS Howto-spec-helper ChangeLog
%{_bindir}/macroszification
%{_datadir}/spec-helper
%_sys_macros_dir/%{name}.macros


