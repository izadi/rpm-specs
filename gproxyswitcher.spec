Name:		gproxyswitcher
Version:	0.3.0
Release:	1%{?dist}
Summary:	A simple applet to switch between locations defined in GNOME's Network Proxy

Group:		User Interface/Desktops
License:	GPLv2+
URL:		N/A
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gettext
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	gtk2-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	GConf2-devel
BuildRequires:	libgnomeui-devel
Requires:	gtk2
Requires:	gnome-panel-libs
Requires:	GConf2
Requires:	libgnomeui

%description
A simple applet to switch between locations defined in GNOME's Network Proxy


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :


%postun
if [ $1 -eq 0 ]; then
	touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
	gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :


%files
%defattr(-,root,root,-)
%doc ChangeLog README COPYING AUTHORS INSTALL NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/status/%{name}-direct.png
%{_datadir}/icons/hicolor/*/status/%{name}-proxy.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/status/%{name}-direct.svg
%{_datadir}/icons/hicolor/scalable/status/%{name}-proxy.svg



%changelog

