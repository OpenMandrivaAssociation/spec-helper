Name:		spec-helper
Version:	0.31.36
Release:	1
Summary:	Tools to ease the creation of rpm packages
License:	GPLv2+
Group:		Development/Other
URL:		https://abf.io/omv_software/spec-helper
Source0:	%{name}-%{version}.tar.xz
Requires:	findutils
Requires:	gettext
Requires:	chrpath
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Slurp)
BuildArch:	noarch

%description
Tools to ease the creation of rpm packages for the
%{distribution} distribution.
Compress man pages using xz, convert links and perform some sanitizing on
packages built...

%prep
%setup -q

%build

%install
%makeinstall_std bindir=%{_bindir} rpmmacrosdir=%{_sys_macros_dir}

%check
make test

%files
%doc README NEWS
%{_bindir}/*
%{_datadir}/spec-helper
%{_sys_macros_dir}/%{name}.macros
