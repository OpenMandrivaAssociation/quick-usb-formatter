%define binname quickusbformatter

Name:		quick-usb-formatter
Version:	0.4.1
Release:	1
Summary:	A small KDE4 application to format usb sticks and devices
Group:		Graphical desktop/KDE
License:	LGPLv2+
URL:		http://kde-apps.org/content/show.php?content=137493
Source0:	http://sourceforge.net/projects/chakra/files/Tools/Quick-Usb-Formatter/quick-usb-formatter-%{version}.tar.gz
Patch0:		quick-usb-formatter-0.4.1-desktop.patch
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	gettext

%description
Quick Usb Formatter is a tiny app designed for enhance the usability of the
device notifier, an additional option for quick format usb sticks.

%prep
%setup -q -n chakra-quick-usb-formatter
%patch0 -p1 -b .desktop

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{binname}

%files -f %{binname}.lang
%doc README.txt
%{_kde_bindir}/%{binname}
%{_kde_appsdir}/solid/actions/%{binname}.desktop

