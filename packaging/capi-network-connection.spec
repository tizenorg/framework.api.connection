Name:       capi-network-connection
Summary:    Network Connection library in TIZEN C API
Version:    0.1.3_19
Release:    1
Group:      System/Network
License:    Apache License Version 2.0
Source0:    %{name}-%{version}.tar.gz

%if %{_repository} == "wearable"
BuildRequires:  cmake
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(vconf)
BuildRequires:  pkgconfig(capi-base-common)
BuildRequires:  pkgconfig(network)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%else
BuildRequires:  cmake
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(vconf)
BuildRequires:  pkgconfig(capi-base-common)
BuildRequires:  pkgconfig(network)
%endif

%description
Network Connection library in Tizen C API

%package devel
Summary:  Network Connection library in Tizen C API (Development)
Group:    System/Network
Requires: %{name} = %{version}-%{release}

%description devel
Network Connection library in Tizen C API (Development)

%prep
%setup -q

%build
%if %{_repository} == "wearable"
cd wearable
export CFLAGS+=' -Wno-unused-local-typedefs '
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DFULLVER=%{version} -DMAJORVER=${MAJORVER}

make %{?_smp_mflags}
%else
cd mobile
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
%cmake . -DFULLVER=%{version} -DMAJORVER=${MAJORVER}

make %{?_smp_mflags}
%endif

%install
%if %{_repository} == "wearable"
cd wearable
%make_install

#License
mkdir -p %{buildroot}%{_datadir}/license
cp LICENSE.APLv2 %{buildroot}%{_datadir}/license/capi-network-connection
%else
cd mobile
%make_install

#License
mkdir -p %{buildroot}%{_datadir}/license
cp LICENSE.APLv2 %{buildroot}%{_datadir}/license/capi-network-connection
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%if %{_repository} == "wearable"
%manifest wearable/capi-network-connection.manifest
%else
%manifest mobile/capi-network-connection.manifest
%endif
%attr(644,-,-) %{_libdir}/libcapi-network-connection.so.*
%{_datadir}/license/capi-network-connection

%files devel
%{_includedir}/network/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libcapi-network-connection.so
