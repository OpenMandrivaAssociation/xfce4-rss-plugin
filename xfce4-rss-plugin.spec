Summary: 	A RSS Plugin for the Xfce panel
Name: 		xfce4-rss-plugin
Version: 	0.1.0
Release: 	%mkrel 9
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-rss-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-rss-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	python-xfce
BuildRequires:	python-exo
BuildRequires:	pygtk2.0
BuildRequires:	python-feedparser
Requires:	xfce4-panel >= 4.4.2
Requires:	python-feedparser
Requires:	python-exo
Requires:	python-xfce
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
An RSS Xfce panel plugin.

%prep
%setup -q -n trunk

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS README
%{_libdir}/xfce4/panel-plugins/*
%{py_puresitedir}/xfce4/rssplugin/*
%{_datadir}/xfce4/panel-plugins/rss.desktop
