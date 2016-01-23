%define date 160123
%define rev 57c4e54b

Summary:        Vocal Podcatcher
Name:           vocal
Version: 2.0~git%{date}~%{rev}
Release: 0%{?dist}
License:        GPLv3
URL:            http://launchpad.net/vocal

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

Patch0:         00-webkitdeps.patch

BuildRequires:  cmake pkgconfig
BuildRequires:  vala gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme


%description
Vocal is a podcatcher designed for elementaryOS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install

mv %{buildroot}/%{_datadir}/locale-langpack %{buildroot}/%{_datadir}/locale

%find_lang vocal


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/vocal.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f vocal.lang
%{_bindir}/vocal

%{_datadir}/appdata/*
%{_datadir}/applications/vocal.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.vocal.gschema.xml
%{_datadir}/icons/hicolor/*/apps/vocal.svg
%{_datadir}/vocal


%changelog
* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0-1
- Unretire vocal package. Downgrade to version 1.0. Git snapshots coming soon.

