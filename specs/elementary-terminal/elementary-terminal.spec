%global srcname terminal
%global appname io.elementary.terminal

Name:           elementary-terminal
Summary:        The terminal of the 21st century
Version:        0.4.3+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(vte-2.91)

Obsoletes:      pantheon-terminal
Provides:       pantheon-terminal


%description
A super lightweight, beautiful, and simple terminal. It's designed to be
setup with sane defaults and little to no configuration. It's just a
terminal, nothing more, nothing less.


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
    %{buildroot}/%{_datadir}/applications/open-pantheon-terminal-here.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/%{appname}.appdata.xml || :


%files -f %{appname}.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180214.022835.176bd1a7-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180213.201510.d0d55529-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180211.000933.6107e806-1
- Update to latest snapshot.

* Thu Feb 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180201.162050.9e248fab-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180129.000256.4a45e09f-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180128.000905.806d3405-1
- Update to latest snapshot.

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180126.000933.5f8c2254-1
- Update to latest snapshot.

* Thu Jan 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180125.173350.1f3903cc-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.220929.04c0e4ff-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.153501.655d7c98-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.140456.e4a415ff-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180120.132931.8c2a36d0-1
- Update to latest snapshot.

* Fri Jan 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180119.223652.2620de17-1
- Update to latest snapshot.

* Thu Jan 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180118.161816.e77ad0fb-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180113.171426.3c3448e4-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180110.111640.ce8e3d02-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180110.000212.fd0e5f92-2
- Adapt to upstream file changes.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180110.000212.fd0e5f92-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180109.210401.2a1f43ae-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.3+git180103.094831.1a42c0a7-1
- Initial package.


