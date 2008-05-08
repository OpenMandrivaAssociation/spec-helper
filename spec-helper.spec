%define name spec-helper
%define version 0.29.1
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Tools to ease the creation of rpm packages
License:    GPL
Group:      Development/Other
URL:        http://svn.mandriva.com/svn/soft/rpm/spec-helper
Source:     %{name}-%{version}.tar.bz2
Requires:   python-base
Requires:   findutils
Requires:   gettext
BuildArch:  noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Tools to ease the creation of rpm packages for the Mandriva Linux distribution.
Compress man pages using bzip2, strip executables, convert links...

%prep
%setup -q

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} bindir=%{_bindir} rpmmacrosdir=%_sys_macros_dir 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{_bindir}/macroszification
%{_datadir}/spec-helper
%_sys_macros_dir/%{name}.macros
