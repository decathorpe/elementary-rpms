Name:           pantheon-agent-geoclue2
Summary:        Pantheon Geoclue2 Agent
Version:        0+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/pantheon-agent-geoclue2
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)


%description
Provides a dialog asking for the user's permission when an application
requests access to location services.


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

%find_lang pantheon-agent-geoclue2


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files -f pantheon-agent-geoclue2.lang
%{_prefix}/lib/geoclue2-1-pantheon/

%{_datadir}/applications/org.pantheon.agent-geoclue2.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.agent-geoclue2.gschema.xml


%changelog
* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170430.102728.b77d163f-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0+git170424.172841.1b407d1b-1
- Initial package.


