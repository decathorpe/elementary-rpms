%define rev 24

Summary: Captive Portal Assistant
Name: capnet-assist
Version: 0.1.1~rev%{rev}
Release: 2%{?dist}
License: GPLv2
URL: http://launchpad.net/capnet-assist

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(webkitgtk-3.0)


%description
Assists users in connective to Captive Portals such as those found on public access points in train stations, coffee shops, universities, etc.

Upon detection, the assistant appears showing the captive portal. Once a connection is known to have been established, it dismisses itself.

Written in Vala and using WebkitGtk+.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files
%doc AUTHORS README
%license COPYING

%config %{_sysconfdir}/NetworkManager/dispatcher.d/90captive_portal_test
%{_bindir}/captive-login


%changelog
* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev24-2
- Update to fix rpm build.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev24-1
- Update to new upstream snapshot.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev23-2
- Cleanup .spec file.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev23-1
- Initial package.
