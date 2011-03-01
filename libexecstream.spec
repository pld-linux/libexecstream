Summary:	C++ library to run a child process with standard C++ streams
Summary(pl.UTF-8):	Biblioteka C++ do uruchamiania procesów potomnych ze strumieniami C++
Name:		libexecstream
Version:	0.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libexecstream/%{name}-%{version}.tar.gz
# Source0-md5:	5b1b9d653723ba78e221a28a8b98e973
URL:		http://libexecstream.sourceforge.net/
BuildRequires:	libstdc++-devel >= 5:3.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libexecstream is a C++ library that allows you to run a child process
and have its input, output and error available as standard C++
streams.

%description -l pl.UTF-8
libexecstream to bibliotekaC++ pozwalająca na uruchamianie procesów
potomnych z ich wejściem, wyjściem i wyjściem diagnostycznym dostępnym
jako standardowe strumienie C++.

%package devel
Summary:	Header files for libexecstream library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libexecstream
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 5:3.0

%description devel
Header files for libexecstream library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libexecstream.

%package static
Summary:	Static libexecstream library
Summary(pl.UTF-8):	Statyczna biblioteka libexecstream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libexecstream library.

%description static -l pl.UTF-8
Statyczna biblioteka libexecstream.

%prep
%setup -q -n %{name}

%build
libtool --mode=compile --tag=CXX %{__cxx} %{rpmcxxflags} -c exec-stream.cpp
libtool --mode=link --tag=CXX %{__cxx} %{rpmldflags} %{rpmcxxflags} \
	-o libexecstream.la exec-stream.lo -lpthread -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

libtool --mode=install install libexecstream.la $RPM_BUILD_ROOT%{_libdir}
install exec-stream.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_libdir}/libexecstream.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexecstream.so
%{_libdir}/libexecstream.la
%{_includedir}/exec-stream.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libexecstream.a
