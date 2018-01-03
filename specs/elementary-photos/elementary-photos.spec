%global __provides_exclude_from ^%{_libdir}/pantheon-photos/.*\\.so$

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
    %{buildroot}/%{_datadir}/applications/%{oldname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{oldname}-viewer.desktop

# Validation currently fails due to a bug (?) in appstream-glib
# https://bugzilla.redhat.com/show_bug.cgi?id=1492566
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/appdata/%{appname}.appdata.xml || :


%files -f io.elementary.photos.lang
%doc AUTHORS README.md THANKS
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_libexecdir}/%{appname}/

%{_datadir}/applications/%{oldname}.desktop
%{_datadir}/applications/%{oldname}-viewer.desktop
%{_datadir}/glib-2.0/schemas/%{oldname}.gschema.xml
%{_datadir}/glib-2.0/schemas/%{oldname}-extras.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/%{appname}/


%changelog
* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git171229.222002.65512d02-1
- Initial package.


