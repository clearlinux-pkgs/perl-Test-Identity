#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Identity
Version  : 0.01
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Identity-0.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Identity-0.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-async-perl/libio-async-perl_0.72-1.debian.tar.xz
Summary  : Perl module to test the referential identity of a reference
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
BuildRequires : buildreq-cpan

%description
NAME
"Test::Identity" - assert the referential identity of a reference
SYNOPSIS
use Test::More tests => 2;
use Test::Identity;

%prep
%setup -q -n Test-Identity-0.01
cd ..
%setup -q -T -D -n Test-Identity-0.01 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-Identity-0.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Identity
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Identity/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Test-Identity/deblicense_copyright
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
