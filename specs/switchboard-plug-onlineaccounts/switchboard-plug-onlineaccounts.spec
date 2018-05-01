%global __provides_exclude_from ^%{_libdir}/(pantheon-online-accounts)|(switchboard)/.*\\.so$

Name:           switchboard-plug-onlineaccounts
Summary:        Switchboard Online Accounts plug
Version:        0.3.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Supplements:    switchboard%{?_isa}

Requires:       hicolor-icon-theme
Requires:       pantheon-online-accounts%{?_isa} = %{version}-%{release}


%description
%{summary}.


%package     -n pantheon-online-accounts
Summary:        Pantheon Online Accounts system (plugins)
Requires:       pantheon-online-accounts-libs%{?_isa} = %{version}-%{release}
%description -n pantheon-online-accounts
This package contains plugins for POA (Pantheon Online Accounts).


%package     -n pantheon-online-accounts-libs
Summary:        Pantheon Online Accounts system
%description -n pantheon-online-accounts-libs
This package contains the libraries making up POA (Pantheon Online
Accounts).


%package     -n pantheon-online-accounts-devel
Summary:        Pantheon Online Accounts system (development headers)
Requires:       pantheon-online-accounts-libs%{?_isa} = %{version}-%{release}
%description -n pantheon-online-accounts-devel
This package contains the development files for POA (Pantheon Online
Accounts).


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-online-accounts


%post   -n pantheon-online-accounts-libs -p /sbin/ldconfig
%postun -n pantheon-online-accounts-libs -p /sbin/ldconfig


%files -f pantheon-online-accounts.lang
%{_libdir}/switchboard/network/pantheon-online-accounts/


%files -n pantheon-online-accounts
%{_libdir}/pantheon-online-accounts/*

%{_datadir}/accounts/providers/*.provider
%{_datadir}/accounts/services/*.service
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service
%{_datadir}/icons/hicolor/*/apps/*.svg


%files -n pantheon-online-accounts-libs
%license COPYING

%{_libdir}/libpantheon-online-accounts.so.0
%{_libdir}/libpantheon-online-accounts.so.0.1

%dir %{_libdir}/pantheon-online-accounts


%files -n pantheon-online-accounts-devel
%{_includedir}/pantheon-online-accounts/

%{_libdir}/libpantheon-online-accounts.so
%{_libdir}/pkgconfig/pantheon-online-accounts.pc

%{_datadir}/vala/vapi/pantheon-online-accounts.deps
%{_datadir}/vala/vapi/pantheon-online-accounts.vapi


%changelog
* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180429.140459.d27880a1-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180426.000400.bbae39f4-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180425.000355.fa2cf116-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180420.001229.076f8540-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180414.122720.0a67281a-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180413.224003.53ed4500-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180413.174634.57314690-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180328.000418.dd88920e-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180326.000923.e0e81d25-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180325.000944.f1062df8-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180322.000551.e076b4f0-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180318.000834.4ba1ddb0-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180314.000246.dd7645af-1
- Update to latest snapshot.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180312.001018.6449fd0d-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180310.000445.baf33cb0-1
- Update to latest snapshot.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180308.175706.fe9c5855-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180224.000451.858c3a83-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180211.000918.86f9a2b3-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180205.001214.43e2b5ec-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git180119.124731.fe7d6b39-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-3
- Remove icon cache scriptlets.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-2
- Merge .spec file from fedora.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git171104.071431.369e4703-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170818.231615.62729c89-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170703.172833.b673f979-1
- Update to latest snapshot.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170628.152738.cde8dcd5-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170617.150143.919b2c92-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170417.235528.5a0270aa-1
- Initial package.


