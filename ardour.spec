%define oname	Ardour
%define maj	%{expand:%(echo "%{version}" | cut -d. -f1)}
Name:		ardour
Version:	5.12.0
Release:	1
Epoch:		1
Summary:	Professional multi-track audio recording application
Group:		Sound
License:	GPLv2+
URL:		http://ardour.org/

# NB to receive a free (as beer) source tarball you need to give your e-mail address here:
# "http://community.ardour.org/download_process_selection_and_amount" to get a download link
Source0:	%{oname}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc

BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gettext
BuildRequires:	graphviz
BuildRequires:	gtkmm2.4-devel >= 2.8
BuildRequires:	jackit-devel
BuildRequires:	shared-mime-info
BuildRequires:	xdg-utils
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(aubio) >= 0.3.2
BuildRequires:	pkgconfig(cairomm-1.0)
BuildRequires:	pkgconfig(cppunit) >= 1.12.0
BuildRequires:	pkgconfig(cwiid)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(flac) >= 1.2.1
BuildRequires:	pkgconfig(glib-2.0) >= 2.2
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libcurl) >= 7.0.0
BuildRequires:	pkgconfig(libgnomecanvas-2.0) >= 2.30
BuildRequires:	pkgconfig(libgnomecanvasmm-2.6) >= 2.16
BuildRequires:	pkgconfig(liblo) >= 0.24
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(lilv-0) >= 0.14
BuildRequires:	pkgconfig(lrdf) >= 0.4.0
BuildRequires:	pkgconfig(ltc) >= 1.1.0
BuildRequires:	pkgconfig(lv2)
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
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(sratom-0) >= 0.4.0
BuildRequires:	pkgconfig(suil-0) >= 0.6.0
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vamp-sdk)
BuildRequires:	desktop-file-utils

Requires:	jackit
Requires:	gtk-engines2

Obsoletes:	%{name}4
Obsoletes:	%{name}3 < 4.0
Conflicts:	%{name}3 < 4.0
Provides:	%{name}3 = %{EVRD}

%description
Ardour is a digital audio workstation. You can use it to record, edit and mix
multi-track audio. You can produce your own CDs, mix video sound tracks, or
just experiment with new ideas about music and sound.

Ardour capabilities include: multi channel recording, non-destructive editing
with unlimited undo/redo, full automation support, a powerful mixer, unlimited
tracks/buses/plugins, time-code synchronization, and hardware control from
surfaces like the Mackie Control Universal.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's!os << obj;!!g' libs/pbd/pbd/compose.h

%build
%{__python2} ./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --configdir=%{_sysconfdir} \
    --program-name=Ardour \
    --nls \
    --docs \
    --freedesktop \
    --cxx11 \
    --optimize

%{__python2} ./waf build \
    --nls \
    --docs

%{__python2} ./waf i18n_mo

%install
%{__python2} ./waf install --destdir=%{buildroot}

# Symlink icons and mimetypes into the right folders
install -d -m 0755 %{buildroot}%{_iconsdir}

for i in 16 22 32 48; do
install -d -m 0755 %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps
install -d -m 0755 %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/mimetypes
ln -s %{_datadir}/%{name}%{maj}/icons/application-x-%{name}_${i}px.png \
%{buildroot}%{_iconsdir}/hicolor/${i}x${i}/mimetypes/application-x-%{name}%{maj}.png
ln -s %{_datadir}/%{name}%{maj}/resources/%{oname}-icon_${i}px.png \
%{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}%{maj}.png
done


cat>%{name}.desktop<<EOF
[Desktop Entry]
Comment=Digital Audio Workstation
Comment[en_GB]=Digital Audio Workstation
Exec=ardour%{maj}
GenericName=%{oname}
GenericName[en_GB]=%{oname}
Icon=%{name}%{maj}
MimeType=application/x-%{name};
Name=%{oname}
Name[en_GB]=%{oname}
StartupNotify=true
Terminal=false
Type=Application
Categories=AudioVideo;Audio;X-Recorders;X-Multitrack;X-Jack;X-OpenMandriva-CrossDesktop;

EOF

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{name}.desktop

cat > README.urpmi <<EOF
You will need to add yourself to the 'audio' and 'realtime' groups before using Ardour.
This may be done in a terminal by using the following commands:

su

gpasswd -a <yourusername> audio

gpasswd -a <yourusername> realtime

exit

You can alternatively do this by using the OpenMandriva Control Center GUI:
System -> Manage Users on System -> Right click on your user, twice -> Edit -> Groups tab -> 
Check boxes for audio and realtime groups -> Click on OK

You will need to log out and log back in before using Ardour for the first time.

EOF

cp -a README.urpmi README.omv

%files
%doc README README.urpmi README.omv
%{_sysconfdir}/%{name}5/%{name}.keys
%{_bindir}/%{name}%{maj}
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
%{_datadir}/%{name}%{maj}/ArdourMono.ttf
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}%{maj}
%dir %{_sysconfdir}/%{name}%{maj}
%{_iconsdir}/hicolor/*
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/%{name}.menus
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/clearlooks.rc
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/default_ui_config
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/system_config
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/trx.menus
