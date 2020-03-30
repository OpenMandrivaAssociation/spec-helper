Name:		spec-helper
Version:	0.31.49
Release:	2
Summary:	Tools to ease the creation of rpm packages
License:	GPLv2+
Group:		Development/Other
URL:		https://github.com/OpenMandrivaSoftware/spec-helper
Source0:	https://github.com/OpenMandrivaSoftware/spec-helper/archive/v%{version}.tar.gz
# The python shebangs check is Fedora policy, and shouldn't break the build
# for anyone else.
# In the Fedora world: "Force python 2 or python 3"
# In the rest of the world: "You can force python 2 or 3, or you can call
# /usr/bin/python to get the system's default version that has all the
# libraries available, and you'll automatically be updated to python 4
# when it becomes available".
# Calling python2 or python3 directly will break removing legacy cruft and
# is just a workaround for code that needs to be updated...
Patch0:		spec-helper-0.31.49-no-python-shebangs-check.patch
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
%makeinstall_std bindir=%{_bindir} rpmmacrosdir=%{_rpmmacrodir}
mv %{buildroot}/%{_rpmmacrodir}/%{name}.macros %{buildroot}/%{_rpmmacrodir}/macros.%{name}
rm -f %{buildroot}%{_bindir}/spec-cleaner

%check
make test

%files
%doc README NEWS
%{_bindir}/*
%{_datadir}/spec-helper
%{_rpmmacrodir}/macros.%{name}
