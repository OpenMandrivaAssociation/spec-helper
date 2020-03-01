Name:		spec-helper
Version:	0.31.48
Release:	2
Summary:	Tools to ease the creation of rpm packages
License:	GPLv2+
Group:		Development/Other
URL:		https://github.com/OpenMandrivaSoftware/spec-helper
Source0:	https://github.com/OpenMandrivaSoftware/spec-helper/archive/v%{version}.tar.gz
Requires:	findutils
Requires:	gettext
Requires:	chrpath
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(List::MoreUtils)
# For "make test"
BuildRequires:	perl(ExtUtils::Command)
BuildRequires:	perl(ExtUtils::Command::MM)
BuildRequires:	perl(Test::More)
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
%makeinstall_std bindir=%{_bindir} rpmmacrosdir=%{_rpmmacrodir}
rm -f %{buildroot}%{_bindir}/spec-cleaner

%check
make test

%files
%doc README NEWS
%{_bindir}/*
%{_datadir}/spec-helper
%{_rpmmacrodir}/%{name}.macros
