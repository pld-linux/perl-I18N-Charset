#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	I18N
%define	pnam	Charset
Summary:	IANA Character Set Registry names and Unicode::MapUTF8 conversion scheme names
#Summary(pl):	
Name:		perl-I18N-Charset
Version:	1.21
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-IO-String
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Unicode-Map8 >= 1.09
%endif
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

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
