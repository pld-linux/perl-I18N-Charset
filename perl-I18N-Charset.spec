#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	I18N
%define	pnam	Charset
Summary:	I18N::Charset - IANA Character Set Registry names and Unicode::MapUTF8 conversion scheme names
Summary(pl):	I18N::Charset - nazwy zestaw�w znak�w wg IANA oraz nazwy tabel konwersji Unicode::MapUTF8
Name:		perl-I18N-Charset
Version:	1.371
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ae515dea452c64f2820bcead466265f
BuildRequires:	perl-devel >= 5.6
%if %{with tests}
BuildRequires:	perl-File-Which
BuildRequires:	perl-IO-String
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Unicode-MapUTF8 >= 1.09
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The I18N::Charset module provides access to the IANA Character Set
Registry names for identifying character encoding schemes.  It also
provides a mapping to the character set names used by the Unicode::Map8
and Unicode::Map modules.

So, for example, if you get an HTML document with a META CHARSET="..."
tag, you can fairly quickly determine what Unicode::MapXXX module can
be used to convert it to Unicode.

%description -l pl
Modu� I18N::Charset daje dost�p do nazw z IANA Character Set Registry
(rejestru zestaw�w znak�w IANA) s�u��cych do identyfikowania schemat�w
kodowania znak�w. Udost�pnia tak�e mapowanie dla nazw zestaw�w znak�w
u�ywanych w modu�ach Unicode::Map8 i Unicode::Map.

W ten spos�b mo�na np. maj�c dokument HTML ze znacznikiem META
CHARSET="..." szybko okre�li�, jakiego modu�u Unicode::MapXXX u�y� do
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
