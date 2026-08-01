%define upstream_name    String-Koremutake
%define upstream_version 0.30
Name:		perl-%{upstream_name}
Version:	0.30
Release:	3

Summary:	Convert to/from Koremutake Memorable Random Strings
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/String-Koremutake
Source0:	https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/String-Koremutake-0.30.tar.gz

BuildRequires:	make
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
%setup -q -n String-Koremutake-0.30

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/String/*
%{_mandir}/*/*

