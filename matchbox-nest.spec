Summary: 	X nesting for the Matchbox Desktop
Name: 		matchbox-nest
Version: 	0.3
Release: 	7
Url: 		https://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://matchbox-project.org/sources/matchbox-nest/0.3/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libmb)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(expat)

%description
X nesting for the panel from Matchbox.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/%name
