%global debug_package %{nil}
%global	_empty_manifest_terminate_build 0

%define oname	Ardour
%define maj	%{expand:%(echo "%{version}" | cut -d. -f1)}

Summary:		Professional multi-track audio recording application
Name:		ardour
Version:		9.0.0
Release:		1
License:		GPLv2+
Group:	Sound
Url:		https://ardour.org/
Source0:	https://community.ardour.org/srctar/%{oname}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	gettext
BuildRequires:	graphviz
BuildRequires:	itstool
BuildRequires:	python
BuildRequires:	shared-mime-info
BuildRequires:	xdg-utils
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(aubio) >= 0.4.0
BuildRequires:	pkgconfig(cairo) >= 1.12.0
BuildRequires:	pkgconfig(cairomm-1.0)
BuildRequires:	pkgconfig(cppunit) >= 1.12.0
BuildRequires:	pkgconfig(cwiid)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(fftw3) >= 3.3.5
BuildRequires:	pkgconfig(flac) >= 1.2.1
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28
BuildRequires:	pkgconfig(jack) >= 1.9.10
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libcurl) >= 7.55.0
BuildRequires:	pkgconfig(libgnomecanvas-2.0) >= 2.30
BuildRequires:	pkgconfig(libgnomecanvasmm-2.6) >= 2.16
BuildRequires:	pkgconfig(liblo) >= 0.26
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libusb-1.0) >= 1.0.16
# Not provided yet
#BuildRequires:	pkgconfig(libwebsockets)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(lilv-0) >= 0.14
BuildRequires:	pkgconfig(lrdf) >= 0.4.0
BuildRequires:	pkgconfig(ltc) >= 1.1.0
BuildRequires:	pkgconfig(lv2) >= 1.18.6
BuildRequires:	pkgconfig(ogg) >= 1.1.2
BuildRequires:	pkgconfig(pangomm-1.4)
BuildRequires:	pkgconfig(raptor2)
BuildRequires:	pkgconfig(redland)
BuildRequires:	pkgconfig(rubberband)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(serd-0) >= 0.14.0
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(sndfile) >= 1.0.18
BuildRequires:	pkgconfig(sord-0) >= 0.8.0
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(sratom-0) >= 0.4.0
BuildRequires:	pkgconfig(suil-0) >= 0.6.0
BuildRequires:	pkgconfig(taglib) >= 1.9
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vamp-sdk) >= 2.1
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi) >= 1.7.10
BuildRequires:	pkgconfig(xrandr) >= 1.5.0
Requires:	jackit
Requires:	gtk-engines2
# Still needed all the below?
%rename %{name}4
%rename %{name}3
#Conflicts:	%%{name}3 < 4.0

%description
Ardour is a digital audio workstation. You can use it to record, edit and mix
multi-track audio. You can produce your own CDs, mix video sound tracks, or
just experiment with new ideas about music and sound.
Its capabilities include: multi channel recording, non-destructive editing
with unlimited undo/redo, full automation support, a powerful mixer, unlimited
tracks/buses/plugins, time-code synchronization, and hardware control from
surfaces like the Mackie Control Universal.

%files
%doc README README.omv
%{_sysconfdir}/%{name}%{maj}/
%{_bindir}/%{name}%{maj}*
%{_libdir}/%{name}%{maj}
%dir %{_datadir}/%{name}%{maj}/
%{_datadir}/%{name}%{maj}/export/
%{_datadir}/%{name}%{maj}/icons/
%{_datadir}/%{name}%{maj}/mcp/
%{_datadir}/%{name}%{maj}/midi_maps/
%{_datadir}/%{name}%{maj}/osc
%{_datadir}/%{name}%{maj}/patchfiles/
%{_datadir}/%{name}%{maj}/resources/
%{_datadir}/%{name}%{maj}/scripts/
%{_datadir}/%{name}%{maj}/themes/
%{_datadir}/%{name}%{maj}/locale
%{_datadir}/%{name}%{maj}/web_surfaces/
%{_datadir}/applications/%{name}%{maj}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/appdata/%{name}%{maj}.appdata.xml
%{_datadir}/%{name}%{maj}/%{oname}Mono.ttf
%{_datadir}/%{name}%{maj}/%{oname}Sans.ttf
%{_datadir}/%{name}%{maj}/plugin_metadata/plugin_statuses
%{_datadir}/%{name}%{maj}/plugin_metadata/plugin_tags
%{_datadir}/%{name}%{maj}/templates/.stub
%{_datadir}/%{name}%{maj}/media/
%{_iconsdir}/hicolor/*/apps/%{name}%{maj}.png

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}


%build
#set_build_flags
#global ldflags %%{ldflags} -fuse-ld=bfd
# This is needed because otherwise the build will use gcc/g++ if installed
export CC=clang
export CXX=clang++
%{__python3} ./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --configdir=%{_sysconfdir} \
    --program-name=Ardour \
    --docs \
    --freedesktop \
    --cxx17 \
    --use-lld \
    --optimize \
    --keepflags \
    --no-phone-home

%{__python3} ./waf build \
    --docs

%{__python3} ./waf i18n_mo


%install
%{__python3} ./waf install --destdir=%{buildroot}

# Tell the user about the need to join some system groups
# FIXME: OMV does not seem to have "realtime" group
cat > README.omv <<EOF
You will need to add yourself to the 'audio' and 'realtime' groups before using Ardour.
This may be done in a terminal by using the following commands:
su
gpasswd -a <yourusername> audio
gpasswd -a <yourusername> realtime.

You can alternatively do the same by using the OpenMandriva Control Center GUI:
System -> Manage Users on System -> Right click on your user, twice -> Edit -> Groups tab -> 
Check boxes for audio and realtime groups -> Click on OK

Next You will need to log out and log back in before using Ardour for the first time.

EOF
