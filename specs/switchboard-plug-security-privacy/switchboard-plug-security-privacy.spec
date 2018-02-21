%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-security-privacy
Summary:        Switchboard Privacy and Security Plug
Version:        0.1.2.99+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       light-locker
Requires:       ufw


%description
The security & privacy plug is a section in Switchboard, the elementary
System Settings app, where users can configure the security and the
level of privacy according to his needs.


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

%find_lang pantheon-security-privacy-plug


%files -f pantheon-security-privacy-plug.lang
%doc AUTHORS README.md
%license COPYING

%{_libdir}/switchboard/personal/pantheon-security-privacy/

%{_datadir}/glib-2.0/schemas/org.pantheon.security-privacy.gschema.xml
%{_datadir}/polkit-1/actions/org.pantheon.security-privacy.policy


%changelog
* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git180221.000835.bf684ea5-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git180218.110903.9e72e8dd-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git180213.094930.f49c046b-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git180211.000911.e541fb45-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git180205.001203.eda63662-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git180109.001825.23143ac7-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git171119.000900.ec7d8c7e-2
- Merge .spec file from elementary-stable.

* Thu Nov 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.99+git171119.000900.ec7d8c7e-1
- Switch to git snapshots.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev421-1
- Update to latest snapshot.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev417-1
- Update to latest snapshot.

* Mon Sep 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev416-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev415-1
- Update to latest snapshot.

* Sun Aug 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev411-2
- Remove dependency on e-dpms-helper.

* Sun Jul 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev411-1
- Update to latest snapshot.

* Sun Jul 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev408-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev383-1
- Update to latest snapshot.

* Mon May 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev375-1
- Update to latest snapshot.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2+rev354-1
- Update to version 0.1.2.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev354-1
- Update to latest snapshot.

* Thu May 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev353-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev330-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev329-2
- Adapt to upstream changes.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev329-1
- Update to latest snapshot.

* Sat Apr 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev328-1
- Update to latest snapshot.

* Thu Apr 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev323-1
- Update to latest snapshot.

* Wed Apr 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev322-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev321-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev320-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev319-1
- Update to latest snapshot.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev318-1
- Update to latest snapshot.

* Sun Mar 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev317-1
- Update to latest snapshot.

* Fri Mar 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev315-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev314-1
- Update to latest snapshot.

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev311-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev309-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev306-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev298-1
- Update to latest snapshot.

* Sun Feb 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev296-1
- Update to latest snapshot.

* Sun Feb 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev295-1
- Update to latest snapshot.

* Sun Feb 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev294-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev292-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev291-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev290-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev289-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev288-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev287-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev286-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev285-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev284-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev283-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev282-1
- Update to version 0.1.1.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev281-1
- Update to version 0.1.1.1.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev280-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev279-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev278-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev277-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev276-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev275-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev274-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev273-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev272-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev271-1
- Update to latest snapshot.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1+rev270-1
- Update to version 0.1.1.1.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev270-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev269-1
- Update to latest snapshot.

* Thu Dec 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev268-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev267-1
- Update to latest snapshot.

* Mon Nov 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev266-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev265-1
- Update to version 0.1.1.


