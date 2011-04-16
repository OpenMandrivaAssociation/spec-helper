Name:		spec-helper
Version:	0.31.6
Release:	%mkrel 1
Summary:	Tools to ease the creation of rpm packages
License:	GPLv2+
Group:		Development/Other
URL:		http://svn.mandriva.com/svn/soft/rpm/spec-helper
Source0:	%{name}-%{version}.tar.xz
Requires:	findutils
Requires:	gettext
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(List::MoreUtils)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Tools to ease the creation of rpm packages for the Mandriva Linux distribution.
Compress man pages using xz, convert links and perform some sanitizing on
packages built...

%prep
%setup -q

%install
rm -rf %{buildroot}
%makeinstall_std bindir=%{_bindir} rpmmacrosdir=%{_sys_macros_dir}

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS
%{_bindir}/macroszification
%{_datadir}/spec-helper
%{_sys_macros_dir}/%{name}.macros
