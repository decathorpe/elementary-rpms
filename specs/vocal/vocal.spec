%global appname com.github.needle-and-thread.vocal

Name:           vocal
Summary:        Powerful, beautiful, and simple podcast client
Version:        2.0.20+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/needle-and-thread/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26.2

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(unity)
BuildRequires:  pkgconfig(webkit2gtk-4.0)


%description
Vocal is a powerful, fast, and intuitive application that helps users
find new podcasts, manage their libraries, and enjoy the best that
independent audio and video publishing has to offer. Vocal features full
support for both episode downloading and streaming, native system
integration, iTunes store search and top 100 charts (with international
results support), iTunes link parsing, OPML importing and exporting, and
so much more. Plus, it has great smart features like automatically
keeping your library clean from old files, and the ability to set custom
skip intervals.


%prep
%autosetup


%build
# mark sources files and docs as NOT executable
for i in $(find -name "*.vala"); do chmod a-x $i; done
chmod a-x AUTHORS README.md COPYING

mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang vocal


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f vocal.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/vocal

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/vocal/


%changelog
* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171230.165435.e4d64f27-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171230.152508.678fee74-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171212.210526.647f1fc3-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171212.024458.d9c1df3d-1
- Update to latest snapshot.

* Mon Dec 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171211.142348.dc83ad7e-1
- Update to latest snapshot.

* Tue Nov 21 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171121.131311.897241a7-1
- Update to latest snapshot.

* Wed Nov 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20+git171022.233729.93af560d-1
- Initial snapshot build.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20-4
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.20-1
- Update to version 2.0.20.

* Sun May 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.19-1
- Initial package.


