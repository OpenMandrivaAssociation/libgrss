%define	api	1.0
%define major	0
%define libname	%mklibname grss %{major}
%define	devname	%mklibname grss	-d
%define _disable_rebuild_configure 1

Summary:	Library for easy management of RSS/Atom/Pie feeds
Name:		libgrss
Version:	0.7.0
Release:	2
License:	LGPLv3+
Group:          System/Libraries
Url:		http://live.gnome.org/Libgrss
Source0:	https://download.gnome.org/sources/libgrss/0.7/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.36.1
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8

%description
LibGRSS is a library for easy management of RSS/Atom/Pie feeds.

%package -n %{libname}
Summary:        Library for easy management of RSS/Atom/Pie feeds
Group:          System/Libraries

%description -n %{libname}
LibGRSS is a library for easy management of RSS/Atom/Pie feeds.

%package -n %{devname}
Summary:        Library for easy management of RSS/Atom/Pie feeds -- Development Files
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
LibGRSS is a library for easy management of RSS/Atom/Pie feeds.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgrss.so.%{major}*

%files -n %{devname}
%doc COPYING NEWS README
%doc %{_datadir}/gtk-doc/html/libgrss/
%{_includedir}/libgrss/
%{_libdir}/libgrss.so
%{_libdir}/pkgconfig/libgrss.pc

