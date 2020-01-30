%define binname quickusbformatter

%define beta preview

Name:		quick-usb-formatter
Version:	0.6
Release:	1.%{beta}.4
Summary:	A small KF5 application to format usb sticks and devices
Group:		Graphical desktop/KDE
License:	LGPLv2+
URL:		https://gitorious.org/chakra/quick-usb-formatter
# (tpg) taken from https://code.chakralinux.org/chakra/quick-usb-formatter/tree/qt5
Source0:	quick-usb-formatter-qt5.tar.bz2
Patch0:		quick-usb-formatter-0.6-alt-kf5.patch
Patch1:		quick-usb-formatter-0.6-mga-path.patch
Patch2:		quick-usb-formatter-desktopfile.patch
BuildRequires:	cmake(ECM)
BuildRequires:	gettext
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)

Requires:	ntfs-3g
Requires:	f2fs-tools
Requires:	dosfstools
Requires:	e2fsprogs
Requires:	exfat-utils

%description
Quick Usb Formatter is a tiny app designed for enhance the usability of the
device notifier, an additional option for quick format usb sticks.

%prep
%autosetup -n quick-usb-formatter-qt5 -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{binname}

%files -f %{binname}.lang
%doc README.txt
%{_kde5_bindir}/%{binname}
%{_datadir}/solid/actions/%{binname}_solid.desktop
%{_datadir}/applications/%{binname}.desktop
%{_kde5_libdir}/libexec/kauth/qufhelper
%{_datadir}/dbus-1/system-services/org.kde.auth.quf.service
%{_datadir}/polkit-1/actions/org.kde.auth.quf.policy
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.kde.auth.quf.conf
