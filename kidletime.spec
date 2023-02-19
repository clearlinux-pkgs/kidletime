#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kidletime
Version  : 5.103.0
Release  : 65
URL      : https://download.kde.org/stable/frameworks/5.103/kidletime-5.103.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.103/kidletime-5.103.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.103/kidletime-5.103.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: kidletime-data = %{version}-%{release}
Requires: kidletime-lib = %{version}-%{release}
Requires: kidletime-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(x11-xcb)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KIdleTime
Reporting of idle time of user and system
## Introduction
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package data
Summary: data components for the kidletime package.
Group: Data

%description data
data components for the kidletime package.


%package dev
Summary: dev components for the kidletime package.
Group: Development
Requires: kidletime-lib = %{version}-%{release}
Requires: kidletime-data = %{version}-%{release}
Provides: kidletime-devel = %{version}-%{release}
Requires: kidletime = %{version}-%{release}

%description dev
dev components for the kidletime package.


%package lib
Summary: lib components for the kidletime package.
Group: Libraries
Requires: kidletime-data = %{version}-%{release}
Requires: kidletime-license = %{version}-%{release}

%description lib
lib components for the kidletime package.


%package license
Summary: license components for the kidletime package.
Group: Default

%description license
license components for the kidletime package.


%prep
%setup -q -n kidletime-5.103.0
cd %{_builddir}/kidletime-5.103.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676844936
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676844936
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kidletime
cp %{_builddir}/kidletime-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kidletime/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kidletime-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kidletime/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kidletime-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kidletime/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kidletime-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kidletime/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kidletime.categories
/usr/share/qlogging-categories5/kidletime.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KIdleTime/KIdleTime
/usr/include/KF5/KIdleTime/kidletime.h
/usr/include/KF5/KIdleTime/kidletime_export.h
/usr/include/KF5/KIdleTime/kidletime_version.h
/usr/include/KF5/KIdleTime/private/abstractsystempoller.h
/usr/lib64/cmake/KF5IdleTime/KF5IdleTimeConfig.cmake
/usr/lib64/cmake/KF5IdleTime/KF5IdleTimeConfigVersion.cmake
/usr/lib64/cmake/KF5IdleTime/KF5IdleTimeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5IdleTime/KF5IdleTimeTargets.cmake
/usr/lib64/libKF5IdleTime.so
/usr/lib64/qt5/mkspecs/modules/qt_KIdleTime.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5IdleTime.so.5
/usr/lib64/libKF5IdleTime.so.5.103.0
/usr/lib64/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeWaylandPlugin.so
/usr/lib64/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin0.so
/usr/lib64/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin1.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kidletime/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kidletime/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kidletime/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/kidletime/fa05e58320cb7c64786b26396f4b992579a628bc
