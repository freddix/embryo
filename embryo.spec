Summary:	Enlightenment Foundation Library
Name:		embryo
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	33703f2161f0be2fcb843e1b6ed58f09
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	eina-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Embryo is a tiny library designed to interpret limited Small programs
compiled by the included compiler, embryo_cc. It is mostly a cleaned
up and smaller version of the original Small abstract machine.

%package devel
Summary:	Header files for eet library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for eet library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %ghost %{_libdir}/libembryo.so.1
%attr(755,root,root) %{_libdir}/libembryo.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libembryo.so
%{_includedir}/embryo-1
%{_pkgconfigdir}/embryo.pc

