%define realname String-Koremutake
%define name perl-%{realname}
%define version 0.30
%define release %mkrel 6

Summary:	Convert to/from Koremutake Memorable Random Strings
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildRequires:	perl-Test-Exception
BuildRequires:  perl-Error
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
The String::Koremutake module converts to and from Koremutake Memorable Random
Strings.

The term "Memorable Random String" was thought up by Sean B. Palmer as a name
for those strings like dopynl, glargen, glonknic, spoopwiddle, and kebble etc.
that don't have any conventional sense, but can be used as random identifiers.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/String/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

