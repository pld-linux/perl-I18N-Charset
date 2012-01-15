#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	I18N
%define		pnam	Charset
Summary:	I18N::Charset - IANA Character Set Registry names and Unicode::MapUTF8 conversion scheme names
Summary(pl.UTF-8):	I18N::Charset - nazwy zestawów znaków wg IANA oraz nazwy tabel konwersji Unicode::MapUTF8
Name:		perl-I18N-Charset
Version:	1.401
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/I18N/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3587c451956705e3b26e41f4b6e9a0d7
URL:		http://search.cpan.org/dist/I18N-Charset/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-File-Which
BuildRequires:	perl-IO-Capture
BuildRequires:	perl-IO-String
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Unicode-MapUTF8 >= 1.09
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The I18N::Charset module provides access to the IANA Character Set
Registry names for identifying character encoding schemes. It also
provides a mapping to the character set names used by the
Unicode::Map8 and Unicode::Map modules.

So, for example, if you get an HTML document with a META CHARSET="..."
tag, you can fairly quickly determine what Unicode::MapXXX module can
be used to convert it to Unicode.

%description -l pl.UTF-8
Moduł I18N::Charset daje dostęp do nazw z IANA Character Set Registry
(rejestru zestawów znaków IANA) służących do identyfikowania schematów
kodowania znaków. Udostępnia także mapowanie dla nazw zestawów znaków
używanych w modułach Unicode::Map8 i Unicode::Map.

W ten sposób można np. mając dokument HTML ze znacznikiem META
CHARSET="..." szybko określić, jakiego modułu Unicode::MapXXX użyć do
konwersji dokumentu do Unikodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/I18N/*.pm
%{_mandir}/man3/*
