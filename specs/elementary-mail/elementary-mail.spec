%global srcname mail
%global appname io.elementary.mail

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-mail
Summary:        Mail app designed for elementary
Version:        1.0.8+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0)

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang pantheon-mail


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f pantheon-mail.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.124158.8eb41e0f-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.110412.592caf46-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.105514.69c5cd69-1
- Update to latest snapshot.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181218.060518.ca170dba-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181217.061041.3cd60697-1
- Update to latest snapshot.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181204.143528.2a633841-1
- Update to latest snapshot.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181126.174308.b9aef3c3-1
- Update to latest snapshot.

* Mon Nov 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181112.165250.8f86b5c5-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181107.173401.bc61b816-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181105.204856.004a725f-2
- Require granite >= 5.2.0.

* Mon Nov 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181105.204856.004a725f-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181102.083559.20eab2ea-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181102.083559.20eab2ea-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181029.185443.ace22983-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181029.174833.1d9b3900-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181029.093843.0d10f351-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181026.164252.a25b7d55-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181025.091500.deb577b3-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181023.213556.9da633a8-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181023.204710.598df5e0-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181023.125008.a8b8b354-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181022.203003.902f87a4-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181022.161029.46fbd0f1-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181017.174742.a00c9d66-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8+git181017.170608.7086c825-1
- Initial package.

