%global debug_package %{nil}

Summary:        Application configuration management
Name:           switchboard-plug-applications
Version:        0.1.1+rev%{rev}
Release:        1%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/switchboard-plug-applications

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)


%description
The applications plug is a section in the Switchboard (System Settings)
that allows the user to manage application settings.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang applications-plug


%clean
rm -rf %{buildroot}


%files -f applications-plug.lang
%{_libdir}/switchboard/personal/pantheon-applications-plug/


%changelog
* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev227-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev226-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev220-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev219-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev218-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev217-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev216-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev215-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev214-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev213-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev212-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev211-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev210-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev209-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev208-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev207-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev206-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev205-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev204-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev203-1
- Update to version 0.1.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev202-1
- Update to version 0.1.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev201-1
- Update to version 0.1.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev200-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev199-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev198-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev197-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev196-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev195-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev194-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev193-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev192-1
- Update to latest snapshot.

* Wed Dec 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev191-1
- Update to latest snapshot.

* Tue Dec 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev190-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev189-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev188-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev187-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev186-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev185-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev184-1
- Update to latest snapshot.

* Sat Nov 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev183-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev181-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev179-1
- Update to latest snapshot.

* Tue Nov 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev177-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev176-1
- Update to latest snapshot.

* Tue Nov 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev175-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev174-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev173-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev172-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev171-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev170-1
- Update to latest snapshot.

* Fri Oct 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev169-1
- Update to latest snapshot.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev168-1
- Update to latest snapshot.

* Tue Oct 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev165-1
- Update to latest snapshot.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev164-1
- Update to latest snapshot.

* Mon Oct 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev161-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev160-1
- Update to latest snapshot.

* Fri Sep 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev159-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev158-1
- Update to version 0.1.1.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev158-2
- Spec file cosmetics.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev158-1
- Update to latest snapshot.

* Sat Sep 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev157-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev156-1
- Update to latest snapshot.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev155-1
- Update to version 0.1.1.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev154-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev153-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev152-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev151-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev151-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev150-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev149-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev148-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev147-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev146-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev145-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev144-1
- Update to latest snapshot.

* Thu Jul 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev143-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev142-2
- Update for packaging changes.

* Tue Jul 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev142-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev141-1
- Update to latest snapshot.

* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev140-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev139-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev138-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-2
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev137-1
- Update to version 0.1.0.2.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev137-1
- Initial package.


