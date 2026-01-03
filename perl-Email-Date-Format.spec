#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Email
%define	pnam	Date-Format
Summary:	Email::Date::Format - format Date headers
Summary(pl.UTF-8):	Email::Date::Format - formatowanie nagłówków Date
Name:		perl-Email-Date-Format
Version:	1.008
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e79e57e1fd33e564aecdc7fa5e973901
URL:		https://search.cpan.org/dist/Email-Date-Format/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC 2822 defines the Date: header. It declares the header a required
part of an email message. The syntax for date headers is clearly laid
out. Still, even a perfectly planned world has storms. The truth is,
many programs get it wrong. Very wrong. Or, they don't include a Date:
header at all. This often forces you to look elsewhere for the date,
and hoping to find something.

For this reason, the tedious process of looking for a valid date has
been encapsulated in this software. Further, the process of creating
RFC compliant date strings is also found in this software.

%description -l pl.UTF-8
RFC 2822 definiuje nagłówek Date: (zawierający datę). Określa ten
nagłówek jako obowiązkową część listu. Składnia nagłówków daty jest
jasno opisana. Mimo to wiele programów źle tworzy ten nagłówek. Bardzo
źle. Albo nie dołącza go w ogóle. Zwykle zmusza to do szukania daty
gdzieś indziej z nadzieją znalezienia czegoś.

Z tego powodu nudny proces poszukiwania poprawnej daty został
opakowany w ten pakiet. Co więcej, proces tworzenia łańcuchów daty
zgodnych z RFC także można tu znaleźć.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Email/Date
%{perl_vendorlib}/Email/Date/*.pm
%{_mandir}/man3/*
