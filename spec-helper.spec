%define name spec-helper
%define version 0.31.0
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Tools to ease the creation of rpm packages
License:    GPL
Group:      Development/Other
URL:        http://svn.mandriva.com/svn/soft/rpm/spec-helper
Source:     %{name}-%{version}.tar.bz2
Requires:   findutils
Requires:   gettext
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Slurp)
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

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS
%{_bindir}/macroszification
%{_datadir}/spec-helper
%_sys_macros_dir/%{name}.macros
