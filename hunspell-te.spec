%define lang te
%define langrelease 2
%define langversion 0.01

Name: hunspell-te
Summary: Telugu hunspell dictionaries
%define upstreamid 20050929
Version: 0.%{upstreamid}
Release: 5%{?dist}
Group:          Applications/Text
##Upstream is unresponsive so unable to verify license version
License:        GPL+
URL:            http://aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{langversion}-%{langrelease}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  aspell >= 12:0.60
BuildRequires:  hunspell-devel
Requires:       hunspell

%description
Telugu hunspell dictionaries. This package
contains the efforts of aspell-te that converted by
wordlist2hunspell.

%prep
%setup -q -n aspell6-%{lang}-%{langversion}-%{langrelease}
prezip-bin -d < te.cwl > te.txt

%build
export LANG=te_IN.utf8
wordlist2hunspell te.txt te_IN

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING Copyright
%{_datadir}/myspell/*

%changelog
* Thu Feb 25 2010 Parag <pnemade AT redhat.com> - 0.20050929-5
- Resolves:rh#568224 - Fix %%description and license tag 

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20050929-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Parag <pnemade@redhat.com> - 0.20050929-3
- Use aspell source instead to pull source as BR:aspell-te
- Resolves:rh#511262 buildrequires aspell-te

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050929-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Caolan McNamara <caolanm@redhat.com> - 0.20050929-1
- initial version


