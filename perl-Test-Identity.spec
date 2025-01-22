#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Test-Identity
Version  : 0.01
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Identity-0.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Identity-0.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-async-perl/libio-async-perl_0.72-1.debian.tar.xz
Summary  : 'assert the referential identity of a reference'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Identity-license = %{version}-%{release}
Requires: perl-Test-Identity-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
"Test::Identity" - assert the referential identity of a reference
SYNOPSIS
use Test::More tests => 2;
use Test::Identity;

%package dev
Summary: dev components for the perl-Test-Identity package.
Group: Development
Provides: perl-Test-Identity-devel = %{version}-%{release}
Requires: perl-Test-Identity = %{version}-%{release}

%description dev
dev components for the perl-Test-Identity package.


%package license
Summary: license components for the perl-Test-Identity package.
Group: Default

%description license
license components for the perl-Test-Identity package.


%package perl
Summary: perl components for the perl-Test-Identity package.
Group: Default
Requires: perl-Test-Identity = %{version}-%{release}

%description perl
perl components for the perl-Test-Identity package.


%prep
%setup -q -n Test-Identity-0.01
cd %{_builddir}
tar xf %{_sourcedir}/libio-async-perl_0.72-1.debian.tar.xz
cd %{_builddir}/Test-Identity-0.01
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Test-Identity-0.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Identity
cp %{_builddir}/Test-Identity-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Identity/801d36a8372e2c1f7a2bf0599fda0eab01e1ce18 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Test-Identity/127f6e9fcb6e6f60b441ea9af1efde0780d0f249 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Identity.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Identity/127f6e9fcb6e6f60b441ea9af1efde0780d0f249
/usr/share/package-licenses/perl-Test-Identity/801d36a8372e2c1f7a2bf0599fda0eab01e1ce18

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
