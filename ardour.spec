%define oname ardour2

Summary:	Professional multitrack audio recording application
Name:		ardour
Version:	2.8.16
Release:	1
Epoch:		1
Group:		Sound
License:	GPLv2+
URL:		http://ardour.org/
# since 2.8.2 there is no direct link :(
Source0:	http://releases.ardour.org/%{name}-%{version}.tar.bz2
#Source1:	wiimote.tar.gz
Patch1:		ardour-2.8.11-flags.patch
Patch2:		ardour-2.8.12-syslibs.patch
Patch3:		ardour-2.8.11-soundtouch.patch
Patch4:		ardour-2.8.2-disable-fdo-actions.patch
Patch5:		ardour-SConscript.patch
Patch6:		ardour-2.8.12-unistd.patch
Patch7:		ardour-2.8.12-SConstruct2.patch
BuildRequires:	scons >= 0.96
BuildRequires:	gettext >= 0.11.5
BuildRequires:	libtool
BuildRequires:	raptor2 >= 2.0.4
BuildRequires:	boost-devel
BuildRequires:	cwiid-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires:	pkgconfig(libgnomecanvasmm-2.6)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(lrdf)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(raptor)
BuildRequires:	pkgconfig(slv2)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(lv2core)
BuildRequires:	pkgconfig(vamp-sdk)
BuildRequires:	pkgconfig(rubberband)
BuildRequires:	pkgconfig(aubio)
BuildRequires:	pkgconfig(redland)
BuildRequires:	desktop-file-utils
BuildRequires:	suil-devel
BuildRequires:	lilv-devel
#BuildRequires:	gtk+2.0
BuildRequires:	xdg-utils
BuildRequires:	shared-mime-info
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
#% patch2 -p0
#% atch3 -p1
%patch4 -p0
%patch5 -p1
%patch7 -p0

%build
#(tpg) disable strange optimisations, like SSE
%ifarch %{ix86}
TARGETCPU="i686"
ARCHFLAGS="-DARCH_X86"
%endif
%ifarch x86_64
TARGETCPU="x86_64"
ARCHFLAGS="-DARCH_X86 -DBUILD_SSE_OPTIMIZATIONS -DUSE_X86_64_ASM"
%endif

# ardour want to link against old library
# sed -i -e 's/soundtouch-1.0/soundtouch-1.4/g' SConstruct

%scons \
	PREFIX=%{_prefix} \
	DIST_TARGET="${TARGETCPU}" \
	LINKFLAGS="%{ldflags} --Wl, --as-needed" \
	CCFLAGS="%{optflags} -ffast-math" \
	ARCH="%{optflags} -ffast-math ${ARCHFLAGS}" \
	FFT_ANALYSIS="1" \
	LIBDIR="%{_libdir}" \
	SYSLIBS="1" \
	SURFACES="1" \
	LIBLO="1" \
	LV2="1" \
	TRANZPORT="1" \
	NLS="1" \
	FREEDESKTOP="1" \
	AUBIO="1" \
	FPU_OPTIMIZATION="1" \
	WIIMOTE="1" \
	FREESOUND="1" \
	AUSTATE="1"

%install
mkdir -p %{buildroot}
scons DESTDIR=%{buildroot} install

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README PACKAGER_README
%dir %{_sysconfdir}/%{oname}
%dir %{_libdir}/%{oname}
%dir %{_libdir}/%{oname}/vamp
%dir %{_libdir}/%{oname}/surfaces
%dir %{_datadir}/%{oname}
%dir %{_datadir}/%{oname}/icons
%dir %{_datadir}/%{oname}/pixmaps
%dir %{_datadir}/%{oname}/templates
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_dark.rc
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_default.conf
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_light.rc
%config(noreplace) %{_sysconfdir}/%{oname}/ardour.menus
%config(noreplace) %{_sysconfdir}/%{oname}/ardour_system.rc
%config(noreplace) %{_sysconfdir}/%{oname}/ergonomic-us.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/mnemonic-us.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/ardour-sae.menus
%config(noreplace) %{_sysconfdir}/%{oname}/SAE-de-keypad.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/SAE-de-nokeypad.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/SAE-us-keypad.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/SAE-us-nokeypad.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_dark_sae.rc
%config(noreplace) %{_sysconfdir}/%{oname}/ardour2_ui_light_sae.rc
%{_bindir}/%{oname}
%{_libdir}/%{oname}/*.so
%{_libdir}/%{oname}/ardour-*
%{_libdir}/%{oname}/surfaces/*.so
%{_libdir}/%{oname}/vamp/*.so
%{_libdir}/%{oname}/engines/libclearlooks.so
%{_datadir}/applications/*.desktop
%{_datadir}/%{oname}/icons/*.png
%{_datadir}/%{oname}/pixmaps/*.xpm
%{_datadir}/%{oname}/*.png
%{_datadir}/%{oname}/templates/*.template
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/mime/packages/*.xml


