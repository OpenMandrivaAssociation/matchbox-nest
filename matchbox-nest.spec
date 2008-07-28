%define name 	matchbox-nest
%define version 0.3
%define release %mkrel 4

Summary: 	X nesting for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://matchbox-project.org/sources/matchbox-nest/0.3/%{name}-%{version}.tar.bz2

BuildRequires:	libmatchbox-devel libxtst-devel expat-devel

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
