%define binname quickusbformatter

%define beta altlinux

Name:		quick-usb-formatter
Version:	0.6
Release:	0.%{beta}.1
Summary:	A small KF5 application to format usb sticks and devices
Group:		Graphical desktop/KDE
License:	LGPLv2+
URL:		https://gitorious.org/chakra/quick-usb-formatter
# taken from altlinux: quick-usb-formatter-0.6-alt4.S1.src.rpm
Source0:	quick-usb-formatter-%{version}-%{beta}.tar.xz
Patch1:		alt-kf5.patch
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	gettext
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDELibs4Support)

%description
Quick Usb Formatter is a tiny app designed for enhance the usability of the
device notifier, an additional option for quick format usb sticks.

%prep
%setup -q -n quick-usb-formatter-%{version}
%apply_patches

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
%{_sysconfdir}/dbus-1/system.d/org.kde.auth.quf.conf
