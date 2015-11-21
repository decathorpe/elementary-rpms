%define rev 1854

Summary: Noise audio player
Name: noise
Version: 0.3.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/noise

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: pkgconfig(libgda-5.0)
BuildRequires: pkgconfig(libgpod-1.0)
BuildRequires: pkgconfig(libgsignon-glib)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(taglib_c)
BuildRequires: pkgconfig(zeitgeist-2.0)

Requires: libgda-sqlite
Requires: hicolor-icon-theme


%description
The official elementary music player.


%package devel
Summary: noise development headers
%description devel
The official elementary music player. This package contains the development headers.


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang noise


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/noise.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig



%files -f noise.lang
%{_bindir}/noise

%{_libdir}/libnoise-core.so.0
%{_libdir}/libnoise-core.so.0.1

%{_libdir}/noise/

%{_datadir}/accounts/applications/noise-lastfm.application

%{_datadir}/applications/noise.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.noise.gschema.xml
%{_datadir}/noise/

%{_datadir}/icons/hicolor/16x16/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/22x22/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/24x24/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/32x32/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/48x48/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/64x64/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/128x128/apps/multimedia-audio-player.svg
%{_datadir}/icons/hicolor/scalable/apps/multimedia-audio-player.svg


%files devel
%{_libdir}/libnoise-core.so
%{_libdir}/pkgconfig/noise-core.pc

%{_includedir}/noise-core/

%{_datadir}/vala/vapi/noise-core.deps
%{_datadir}/vala/vapi/noise-core.vapi


%changelog
* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1854-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1853-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1852-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1851-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1849-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1848-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1847-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1846-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1845-1
- Update to new upstream snapshot.

* Thu Oct 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1844-1
- Update to new upstream snapshot.

* Wed Sep 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1843-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1842-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1841-1
- Update to new upstream snapshot.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1840-1
- Update to new upstream snapshot.

* Thu Sep 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1839-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1838-1
- Update to new upstream snapshot.

* Fri Sep 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1837-1
- Update to new upstream snapshot.

* Thu Sep 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1836-1
- Update to new upstream snapshot.

* Wed Sep 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1834-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1833-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1831-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1830-3
- Remove BR on libindicate.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1830-2
- Update spec and add Req: libgda-sqlite for new DB backend.

* Tue Sep 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1830-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1829-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1828-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1828-1
- Update to new upstream snapshot.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1827-1
- Update spec to reflect BR changes and use make_build and make_install macros.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1827-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1826-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1825-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.3.1~rev1823-1
- Update to new upstream snapshot.

* Mon Jul 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1822-1
- Update to bzr snapshot revno 1822.

* Sat Jul 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev1821-1
- Initial package.


