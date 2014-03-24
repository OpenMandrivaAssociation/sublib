%define debug_package %{nil}

Summary: A library that eases the development of subtitling applications
Name:    sublib
Version: 0.9
Release: 5
License: GPLv2+
Group:   System/Libraries
URL:     http://sublib.sourceforge.net/
Source0: http://downloads.sourceforge.net/sublib/%{name}-%{version}.zip
BuildRequires: mono-devel

%description
SubLib is a library that eases the development of subtitling applications.
It supports the most common text-based subtitle formats and allows for
subtitle editing, conversion and synchronization.

%package devel
Summary: SubLib devel files
Group: Development/Other
Requires: %{name} = %{version}

%description devel
This package contains all files that are needed to build against %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README CREDITS NEWS ChangeLog
%{_libdir}/sublib/sublib.dll

%files devel
%{_libdir}/pkgconfig/sublib.pc
