%global __provides_exclude_from ^%{_libdir}/io.elementary.photos/.*\\.so$
%undefine _strict_symbol_defs_build

%global srcname photos
%global appname io.elementary.photos
%global oldname org.pantheon.photos

Name:           elementary-photos
Summary:        elementary photo manager and viewer
Version:        0.2.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:  pkgconfig(libwebp) >= 0.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(rest-0.7) >= 0.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(unity) >= 4.0.0
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.0.0

Requires:       hicolor-icon-theme

Provides:       pantheon-photos
Obsoletes:      pantheon-photos


%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.


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

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}-viewer.desktop

# Validation currently fails due to a bug (?) in appstream-glib
# https://bugzilla.redhat.com/show_bug.cgi?id=1492566
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/%{appname}.appdata.xml || :


%files -f %{appname}.lang
%doc AUTHORS README.md THANKS
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_libexecdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}-viewer.desktop
%{_datadir}/glib-2.0/schemas/%{oldname}.gschema.xml
%{_datadir}/glib-2.0/schemas/%{oldname}-extras.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180528.000248.8ed76f41-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180527.000522.3778e7e0-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180526.113321.2e3c0432-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180526.102238.8f28afd9-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180526.093004.91c183ec-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180525.223208.dd0282d6-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180524.001024.4021795b-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180516.132053.74e3b238-1
- Update to latest snapshot.

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180513.001124.516244d6-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180512.120806.13693b65-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180512.001130.8cd0d6a0-1
- Update to latest snapshot.

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180508.001055.9b328659-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.155608.4c35372b-1
- Update to latest snapshot.

* Mon May 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180507.000248.b023889e-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180506.000954.92bebca1-1
- Update to latest snapshot.

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180503.080210.2c709da1-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180427.000259.307fffb6-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180426.000328.a28e8ed8-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180425.000326.0ab89d26-1
- Update to latest snapshot.

* Tue Apr 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180424.204113.34bd84f8-1
- Update to latest snapshot.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180422.000415.a44776c6-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180420.001153.d8adf62b-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180415.001005.23008bd3-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180414.001125.e8229e98-1
- Update to latest snapshot.

* Fri Apr 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180413.000625.6173ccc7-1
- Update to latest snapshot.

* Tue Apr 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180410.000648.318d48e8-1
- Update to latest snapshot.

* Mon Apr 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180409.140831.37e01d91-1
- Update to latest snapshot.

* Sun Apr 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180408.184134.6c9db543-1
- Update to latest snapshot.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180405.101732.b7f31f32-2
- Adapt to upstream file changes.

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180405.101732.b7f31f32-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180330.173315.7ce3bfc7-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180327.175340.5fa0c8d2-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180327.000214.3fafedeb-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180324.001137.1582cbf3-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180322.175440.bbc20a13-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180320.001140.f884ae9e-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180316.000402.98fbe885-1
- Update to latest snapshot.

* Sun Mar 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180311.000612.a5730199-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180309.000551.6e1a6548-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180307.000958.11124944-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180225.215521.d2230cc1-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.192126.4ec9a01a-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.151118.f6e83337-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180224.000408.90ed1c54-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180223.172740.7697078c-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180223.164140.7d0f8841-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180222.235332.04f2e91d-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180222.020851.1baa9791-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180219.074729.6d50d687-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180215.234249.5ddd938f-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180213.094320.66e9b6ff-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180211.000838.06a140ea-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180209.000952.16d1e7c2-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180207.173134.81465c26-1
- Update to latest snapshot.

* Sun Feb 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.211411.607bd847-3
- Update for packaging changes.

* Sun Feb 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.211411.607bd847-2
- Adapt to upstream file changes.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.211411.607bd847-1
- Update to latest snapshot.

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180202.204802.cd46b71b-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180131.000935.26bb0331-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180125.164951.1ef2492e-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180125.164948.cdce74af-2
- Be lazy about undefined symbols in plugins.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180125.164948.cdce74af-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180122.145746.8d765102-1
- Update to latest snapshot.

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180121.013249.e7fdc59c-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git180119.190020.c20a59cb-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171229.222002.65512d02-1
- Initial package.


