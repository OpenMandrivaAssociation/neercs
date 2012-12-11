%define name	neercs
%define version	0.0
%define svn	4342
%define release	%mkrel 0.r%svn.3

Summary:	Caca screen manager
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	WTFPL
Group:		Terminals
URL:		http://caca.zoy.org/wiki/neercs
Source0:	%{name}-%{version}.tar.bz2
Source1:	neercs.pam
BuildRequires:	pam-devel python-devel
BuildRequires:	libcaca-devel >= 0.99-0.beta17

%description
Like GNU screen, it allows you to detach a session from a terminal,
but provides unique features:

 * Grabbing a process that you forgot to start inside neercs
 * Great screensaver
 * 3D rotating cube to switch between full screen terms
 * Real time thumbnails of your shells
 * Special effects when closing a window
 * Various window layouts... 

%prep
%setup -q

%build
export LDFLAGS="-lm"
./bootstrap
%configure2_5x 
%make

%install
%makeinstall

mkdir -p %{buildroot}/etc/pam.d
cp -a %{SOURCE1} %{buildroot}/etc/pam.d/%name

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/man1/neercs.1.*
/etc/pam.d/%name



%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.0-0.r4342.2mdv2011.0
+ Revision: 592415
- rebuild for python 2.7

* Mon Feb 08 2010 Pascal Terjan <pterjan@mandriva.org> 0.0-0.r4342.1mdv2010.1
+ Revision: 502280
- import neercs


* Tue Jan 02 2010 Pascal Terjan <pterjan@mandriva.org> 0.0-0.r4079.1mdv2010.1
- Initial package

