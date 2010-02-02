%define name	neercs
%define version	0.0
%define svn	4079
%define release	%mkrel 0.r%svn.1

Summary:	Caca screen manager
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	WTFPL
Group:		System/
URL:		http://caca.zoy.org/wiki/neercs
Source0:	%{name}-%{version}.tar.bz2
Source1:	neercs.pam
BuildRequires:	pam-devel libcaca-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Like GNU screen, it allows you to detach a session from a terminal, but provides unique features:

 * Grabbing a process that you forgot to start inside neercs
 * Great screensaver
 * 3D rotating cube to switch between full screen terms
 * Real time thumbnails of your shells
 * Special effects when closing a window
 * Various window layouts... 

%prep
%setup -q

%build
./bootstrap
%configure2_5x 
%make

%install
rm -rf % {buildroot}

%makeinstall

mkdir -p %{buildroot}/etc/pam.d
cp -a %{SOURCE1} %{buildroot}/etc/pam.d/%name

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*
/etc/pam.d/%name
