%define upstream_name    String-Koremutake
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Convert to/from Koremutake Memorable Random Strings
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)
BuildRequires:  perl(Error)
BuildArch:	noarch

%description
The String::Koremutake module converts to and from Koremutake Memorable Random
Strings.

The term "Memorable Random String" was thought up by Sean B. Palmer as a name
for those strings like dopynl, glargen, glonknic, spoopwiddle, and kebble etc.
that don't have any conventional sense, but can be used as random identifiers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/String/*
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 404417
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.30-6mdv2009.0
+ Revision: 241908
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.30-4mdv2008.0
+ Revision: 23890
- rebuild


* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.30-3mdk
- BuildRequires

* Wed May 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.30-2mdk
- BuildRequires

* Wed May 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.30-1mdk
- First Mandriva release

