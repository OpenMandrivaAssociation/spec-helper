Name:		spec-helper
Version:	0.31.11
Release:	1
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
BuildRequires:	rpm >= 1:5.4.4-21
BuildArch:	noarch

%description
Tools to ease the creation of rpm packages for the Mandriva Linux distribution.
Compress man pages using xz, convert links and perform some sanitizing on
packages built...

%prep
%setup -q

%install
%makeinstall_std bindir=%{_bindir} rpmmacrosdir=%{_sys_macros_dir}

%check
make test

%files
%doc README NEWS
%{_bindir}/macroszification
%{_datadir}/spec-helper
%{_sys_macros_dir}/%{name}.macros
