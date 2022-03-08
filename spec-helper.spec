Summary:	Tools to ease the creation of rpm packages
Name:		spec-helper
Version:	0.31.52
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		https://github.com/OpenMandrivaSoftware/spec-helper
Source0:	https://github.com/OpenMandrivaSoftware/spec-helper/archive/refs/tags/v%{version}.tar.gz
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
Compress man pages using zstd, convert links and perform some sanitizing on
packages built...

%prep
%autosetup -p1

%build

%install
%make_install bindir=%{_bindir} rpmmacrodir=%{_rpmmacrodir}
rm -f %{buildroot}%{_bindir}/spec-cleaner

%check
make test

%files
%doc README NEWS
%{_bindir}/*
%{_datadir}/spec-helper
%{_rpmmacrodir}/macros.%{name}
