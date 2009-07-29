%define upstream_name    String-Koremutake
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Convert to/from Koremutake Memorable Random Strings
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildRequires:	perl-Test-Exception
BuildRequires:  perl-Error
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The String::Koremutake module converts to and from Koremutake Memorable Random
Strings.

The term "Memorable Random String" was thought up by Sean B. Palmer as a name
for those strings like dopynl, glargen, glonknic, spoopwiddle, and kebble etc.
that don't have any conventional sense, but can be used as random identifiers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/String/*
%{_mandir}/*/*
