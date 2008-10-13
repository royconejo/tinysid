%define name SIDPlayer
%define version 4.4
%define release 1

Summary: SID tune replayer
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Multimedia
Source: %{name}-%{version}.tar.gz
URL: http://www.uni-mainz.de/~bauec002/SPMain.html
BuildRoot: %{_tmppath}/%{name}-root
Prefix: %{_prefix}

Requires: SDL >= 1.1.4

%description
SIDPlayer is a replayer program for C64 music ("SID tunes"). You can think
of it as being a stripped-down C64 emulator that only emulates the CPU and
the sound chip of the C64. SIDPlayer can replay SID tunes in the "PSID" file
format, but it cannot run any C64 programs.

%prep
%setup -q

%build
CFLAGS=${RPM_OPT_FLAGS} CXXFLAGS=${RPM_OPT_FLAGS} ./configure --prefix=%{_prefix} --mandir=%{_mandir}
if [ -x /usr/bin/getconf ] ; then
  NCPU=$(/usr/bin/getconf _NPROCESSORS_ONLN)
  if [ $NCPU -eq 0 ] ; then
    NCPU=1
  fi
else  
  NCPU=1
fi
PARL=$[ $NCPU + 1 ]
make -j $PARL

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install-strip

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/*
