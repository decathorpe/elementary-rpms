Name:           pantheon-mail
Summary:        E-Mail client for Pantheon
Version:        1.0.6+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/mail
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.22.1

BuildRequires:  pkgconfig(gcr-3) >= 3.10.1
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.17
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libsecret-1) >= 0.11
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(sqlite3) >= 3.7.4
BuildRequires:  pkgconfig(unity) >= 5.12.0
BuildRequires:  pkgconfig(webkitgtk-3.0)


%description
Pantheon Mail is the E-Mail client for the Pantheon desktop.


%package        contract
Summary:        E-Mail client for Pantheon (contractor support)

Requires:       contractor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    contract
Pantheon Mail is the E-Mail client for the Pantheon desktop.
This package contains the contractor support.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake .. \
    -DICON_UPDATE:BOOL=OFF \
    -DDESKTOP_UPDATE:BOOL=OFF
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-mail


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/org.pantheon.mail.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/pantheon-mail-autostart.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/org.pantheon.mail.appdata.xml


%files -f pantheon-mail.lang
%doc README.md
%license COPYING

%{_bindir}/pantheon-mail

%{_datadir}/accounts/applications/pantheon-mail.application
%{_datadir}/applications/org.pantheon.mail.desktop
%{_datadir}/applications/pantheon-mail-autostart.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.mail.gschema.xml
%{_datadir}/metainfo/org.pantheon.mail.appdata.xml


%files contract
%{_bindir}/mail-attach
%{_datadir}/contractor/mail-attach.contract


%changelog
* Thu Aug 24 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git170824.063322.9e5a3156-1
- Update to version 1.0.6.

* Thu Aug 24 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170824.063322.9e5a3156-1
- Update to latest snapshot.

* Thu Jul 20 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170720.180807.5ff1e19b-1
- Update to latest snapshot.

* Sat Jul 08 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170708.055003.6d5da182-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170701.172125.becd8fa7-1
- Update to latest snapshot.

* Sat Jul 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170630.014106.62b9c645-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170617.161241.d9d06237-1
- Update to latest snapshot.

* Wed Jun 14 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170614.153814.facd70f9-1
- Update to latest snapshot.

* Sun May 28 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170527.211033.c25cf6f2-1
- Update to latest snapshot.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170527.140806.df4fccf1-1
- Update to latest snapshot.

* Thu May 25 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170524.230052.b898462b-1
- Update to latest snapshot.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170514.144333.1963d273-1
- Update to latest snapshot.

* Wed May 10 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170510.112743.14b3f508-1
- Update to latest snapshot.

* Tue May 09 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170509.102029.88ea896c-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170508.153122.5a537d7e-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170428.101350.e1bb88dc-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5+git170410.105449.585ae7b1-1
- Update to latest snapshot.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Initial package.

