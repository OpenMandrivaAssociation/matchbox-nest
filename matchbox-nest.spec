%define name 	matchbox-nest
%define version 0.3
%define release 1mdk

Summary: 	X nesting for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	libmatchbox-devel

%description
X nesting for the panel from Matchbox.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/%name

