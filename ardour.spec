%define oname ardour2

Summary:   	Professional multitrack audio recording application
Name:		ardour
Version:	2.1
Release:	%mkrel 1
Epoch:		1
Group:		Sound
License:	GPLv2+
URL:		http://%{name}.sourceforge.net/
Source0:	http://ardour.org/releases/%{name}-%{version}.tar.bz2
Patch1:		ardour-2.0.5-fix_compile.patch
BuildRequires:	curl-devel
BuildRequires:	fftw3-devel
BuildRequires:	gettext >= 0.11.5
BuildRequires:	gtk2-devel >= 2.8
BuildRequires:	gtkmm2.4-devel >= 2.10.8
BuildRequires:	jackit-devel >= 0.100
BuildRequires: 	libalsa-devel
BuildRequires:	libart_lgpl-devel >= 2.3.16
BuildRequires:	libboost-devel
BuildRequires:	libflac-devel
BuildRequires:	libglib2.0-devel >= 2.10
BuildRequires:	libgnomecanvas2-devel
BuildRequires:	libgnomecanvasmm2.6-devel
BuildRequires:	liblo-devel
BuildRequires:	liblrdf-devel >= 0.3.1
BuildRequires:	libsamplerate-devel >= 0.0.13
BuildRequires:	libsndfile-devel >= 1.0.16
BuildRequires:	libtool
BuildRequires: 	libusb-devel
BuildRequires:	libxml2-devel >= 2.5.0
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	raptor-devel
BuildRequires:	scons >= 0.96
BuildRequires:	soundtouch-devel >= 1.3.1
BuildRequires:	sqlite3-devel
Requires:	jackit >= 0.100

%description
Ardour is a digital audio workstation.You can use it to record, edit and mix
multi-track audio. You can produce your own CDs, mix video soundtracks, or just
experiment with new ideas about music and sound.

Ardour capabilities include: multichannel recording, non-destructive editing
with unlimited undo/redo, full automation support, a powerful mixer, unlimited
tracks/busses/plugins, timecode synchronization, and hardware control from
surfaces like the Mackie Control Universal. If you've been looking for a tool
similar to ProTools, Nuendo, Pyramix, or Sequoia, you might have found it.

You must have jackd running and an ALSA sound driver to use ardour. If you are
new to jackd, try qjackctl.

See the online user manual at http://ardour.org/files/manual/index.html

Important notice: This package is built against the system libraries in
Mandriva, and in the SConstruct file there is a text that seems to invalidate
support from upstream authors "USE AT YOUR OWN RISK: CANCELS ALL SUPPORT FROM
ARDOUR AUTHORS".

%prep

%setup -q
%patch1 -p1

%build
scons %{_smp_mflags} PREFIX="%{_prefix}" FFT_ANALYSIS="1" LIBDIR="%{_libdir}" SYSLIBS="1" SURFACES="1" LIBLO="1" TRANZPORT="1" NLS="1"
#scons %{_smp_mflags} PREFIX="%{_prefix}" FFT_ANALYSIS="1" LIBDIR="%{_libdir}" SYSLIBS="0" DEBUG=1

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}

scons DESTDIR=%{buildroot} install 

mv %{buildroot}/%{_bindir}/ardour2 %{buildroot}/%{_bindir}/ardour

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Ardour
Comment=Professional multitrack audio recording application
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;AudioVideo;Audio;AudioVideoEditing;
EOF

# icons
mkdir -p %{buildroot}/%{_liconsdir} %{buildroot}/%{_miconsdir}
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,22x22,32x32,48x48}/apps
cp gtk2_ardour/icons/ardour_icon_16px.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
cp gtk2_ardour/icons/ardour_icon_22px.png %{buildroot}/%{_iconsdir}/hicolor/22x22/apps/%{name}.png
cp gtk2_ardour/icons/ardour_icon_32px.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
cp gtk2_ardour/icons/ardour_icon_48px.png %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name} --all-name

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc DOCUMENTATION/{AUTHORS*,CONTRIBUTORS*,FAQ*,README*,TRANSLATORS*}
%dir %{_sysconfdir}/%{oname}
%dir %{_libdir}/%{oname}
%dir %{_datadir}/%{oname}
%dir %{_datadir}/%{oname}/icons
%dir %{_datadir}/%{oname}/pixmaps
%dir %{_datadir}/%{oname}/templates
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_dark.rc
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_default.conf
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_light.rc
%config(noreplace) %{_sysconfdir}/%{oname}/ardour.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/ardour.menus
%config(noreplace) %{_sysconfdir}/%{oname}/ardour_system.rc
%{_bindir}/%{name}
%{_libdir}/%{oname}/*.so
%{_libdir}/%{oname}/ardour-*
%{_libdir}/%{oname}/surfaces/*.so
%{_libdir}/%{oname}/engines/*.so
%{_datadir}/applications/mandriva-ardour.desktop
%{_datadir}/%{oname}/icons/*.png
%{_datadir}/%{oname}/pixmaps/*.xpm
%{_datadir}/%{oname}/*.png
%{_datadir}/%{oname}/templates/*.template
%{_iconsdir}/hicolor/*/apps/%{name}.png
