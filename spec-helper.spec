Name:		spec-helper
Version:	0.31.23
Release:	1
Summary:	Tools to ease the creation of rpm packages
License:	GPLv2+
Group:		Development/Other
URL:		https://abf.rosalinux.ru/proyvind/spec-helper
Source0:	%{name}-%{version}.tar.xz
Requires:	findutils
Requires:	gettext
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Slurp)
BuildRequires:	rpm >= 1:5.4.4-21
BuildArch:	noarch

%description
Tools to ease the creation of rpm packages for the %{distribution} distribution.
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
%{_bindir}/macroszification
%{_datadir}/spec-helper
%{_sys_macros_dir}/%{name}.macros

%changelog
* Sat Jan 12 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.23-1
- new version:
	o fix_file_permissions should fix library file permissions to be 755


* Sun Jan  6 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.22-1
- new version:
	o don't run fix_eol together with other helpers after %%install,
	  as it'll be run after %%doc in stead

* Wed Dec 26 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.21-1
- drop compress-files in favour of upstream brp-compress

* Tue Dec 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.20-1
- new version:
	o add missing trailing semicolons to XDG *.desktop files
	  (from Denis Silakov)

* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.19-1
- new version:
	o rewrite check_elf_files in shell script
	o skip symlinks for fix_eol

* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.18-1
- make sure fix_eol doesn't exit with error code

* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.17-1
- update url
- use %%{distribution} macro
- new version:
	o rewrite fix_eol in shell script
	o rewrite clean_files script in shell script
	o free gprintify from dependency on perl(List::MoreUtils)

* Wed Dec 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.16-2
- rebuild on ABF

* Fri Sep 28 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.16-1
+ Revision: 817883
- new version:
	o get rid of .la symlinks as well
	o don't relativize symlinks to /dev, /proc & /sys (inspired by similar
	  change by colin in Mageia)
	o drop dead 'translate_menu' script
	o rewrite 'relink_symlinks' perl script in shell

* Wed Jun 06 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.15-1
+ Revision: 802910
- handle both /sbin/install-info & /usr/sbin/install-info

* Mon Jun 04 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.14-1
+ Revision: 802490
- /sbin/install-info has been moved to /usr/sbin/install-info

* Tue Mar 20 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.13-1
+ Revision: 785842
- add empty build section to satisfy rpmlint
- don't remove /usr/share/info/dir if /sbin/install-info is found in buildroot

* Fri Mar 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.12-1
+ Revision: 785374
- remove all .la files

* Sat Mar 10 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.11-1
+ Revision: 783939
- make sure that shared libraries & mono libraries/executables have executable
  permissions set

* Fri Dec 23 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.10-1
+ Revision: 744686
- support multiple libtool files with multiple pkgconfig files

* Thu Dec 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.9-1
+ Revision: 744311
- don't remove libtool .la files which has 'shouldnotlink=yes' set (thx Buchan!)

* Thu Dec 08 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.8-1
+ Revision: 738973
- fix error message printed when there's no pkgconfig dir

* Tue Dec 06 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.7-1
+ Revision: 738086
- remove legacy rpm stuff
- new version:
	o remove libtool .la files

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 0.31.6-3
+ Revision: 669799
- rebuild

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.31.6-2
+ Revision: 653365
- add back runtime dep, do not know why it was removed

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.31.6-1
+ Revision: 653354
- * 0.31.6:
  remove empty dirs for perl modules, as its only use is to push unneeded
  arch dependent dirs into noarch packages

* Wed Dec 15 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.5-1mdv2011.0
+ Revision: 621858
- update description...
- re-enable --text option for xz

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 0.31.4-1mdv2011.0
+ Revision: 599603
- xz 5.0 do not support '--text' option now

* Tue Mar 09 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.3-1mdv2010.1
+ Revision: 516813
- new release: 0.31.3

* Fri Mar 05 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.2-1mdv2010.1
+ Revision: 514714
- hasty new release 0.31.2 as previous one was DOA :(

* Fri Mar 05 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.31.1-1mdv2010.1
+ Revision: 514575
- don't duplicate stripping functionality (partly responsible for #57754)

* Sat Jan 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.31.0-1mdv2010.1
+ Revision: 484954
- new version

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.6-1mdv2010.1
+ Revision: 468582
- new version

