%define libardour	%mklibname ardour 3
%define libardouralsa	%mklibname ardouralsautil 0
%define libaudiographer	%mklibname audiographer 0
%define libcanvas	%mklibname canvas 0
%define libevoral	%mklibname evoral 0
%define libgtkmm2ext	%mklibname gtkmm2ext 0
%define libmidipp	%mklibname midipp 4
%define libpbd		%mklibname pbd 4
%define libptformat	%mklibname ptformat 0
%define libqmdsp	%mklibname qmdsp 0
%define libardourvampplugins	%mklibname ardourvampplugins 0

%define devname	%mklibname -d ardour


%define oname	Ardour
%define maj	%{expand:%(echo "%{version}" | cut -d. -f1)}
Name:		ardour
Version:	5.0.0
Release:	1
Epoch:		1
Summary:	Professional multi-track audio recording application
Group:		Sound
License:	GPLv2+
URL:		http://ardour.org/

# NB to receive a free (as beer) source tarball you need to give your e-mail address here:
# "http://community.ardour.org/download_process_selection_and_amount" to get a download link
Source0:	srctar

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
BuildRequires:	pkgconfig(cppunit) >= 1.12.0
BuildRequires:	pkgconfig(cwiid)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(flac) >= 1.2.1
BuildRequires:	pkgconfig(glib-2.0) >= 2.2
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libcurl) >= 7.0.0
BuildRequires:	pkgconfig(libgnomecanvas-2.0) >= 2.30
BuildRequires:	pkgconfig(libgnomecanvasmm-2.6) >= 2.16
BuildRequires:	pkgconfig(liblo) >= 0.24
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(lilv-0) >= 0.14
BuildRequires:	pkgconfig(lrdf) >= 0.4.0
BuildRequires:	pkgconfig(ltc) >= 1.1.0
BuildRequires:	pkgconfig(lv2)
BuildRequires:	pkgconfig(ogg) >= 1.1.2
BuildRequires:	pkgconfig(raptor2)
BuildRequires:	pkgconfig(redland)
BuildRequires:	pkgconfig(rubberband)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(serd-0) >= 0.14.0
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

Obsoletes:	%{name}3 < 4.0
Conflicts:	%{name}3 < 4.0
Provides:	%{name}3 = %{version}-%{release}

%description
Ardour is a digital audio workstation. You can use it to record, edit and mix
multi-track audio. You can produce your own CDs, mix video sound tracks, or
just experiment with new ideas about music and sound.

Ardour capabilities include: multi channel recording, non-destructive editing
with unlimited undo/redo, full automation support, a powerful mixer, unlimited
tracks/buses/plugins, time-code synchronization, and hardware control from
surfaces like the Mackie Control Universal.

%package -n	%{libardour}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libardour}
%{summary}

%package -n	%{libardouralsa}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libardouralsa}
%{summary}

%package -n	%{libaudiographer}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libaudiographer}
%{summary}

%package -n	%{libcanvas}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libcanvas}

%package -n	%{libardourvampplugins}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libardourvampplugins}

%package -n	%{libevoral}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libevoral}
%{summary}

%package -n	%{libgtkmm2ext}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libgtkmm2ext}
%{summary}

%package -n	%{libmidipp}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libmidipp}
%{summary}


%package -n	%{libpbd}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libpbd}
%{summary}

%package -n	%{libptformat}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libptformat}
%{summary}

%package -n	%{libqmdsp}
Summary:	Ardour5 lib
Group:		System/Libraries

%description -n	%{libqmdsp}
%{summary}

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libqmdsp} = %{version}-%{release}
Requires:	%{libptformat} = %{version}-%{release}
Requires:	%{libpbd} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}%{maj}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

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
    --cxx11

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
ln -s %{_datadir}/%{name}%{maj}/icons/%{name}_icon_${i}px.png \
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

%find_lang %{name}%{maj}

%files -f %{name}%{maj}.lang
%doc README README.urpmi README.omv
%{_sysconfdir}/%{name}5/%{name}.keys
%{_bindir}/%{name}%{maj}
%{_datadir}/%{name}%{maj}/export/
%{_datadir}/%{name}%{maj}/icons/
%{_datadir}/%{name}%{maj}/mcp/
%{_datadir}/%{name}%{maj}/midi_maps/
%{_datadir}/%{name}%{maj}/patchfiles/
%{_datadir}/%{name}%{maj}/resources/
%{_datadir}/%{name}%{maj}/scripts/
%{_datadir}/%{name}%{maj}/themes/
%{_datadir}/%{name}%{maj}/ArdourMono.ttf
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}%{maj}/LV2/
%{_libdir}/%{name}%{maj}/panners/*.so
%{_libdir}/%{name}%{maj}/surfaces/*.so
%{_libdir}/%{name}%{maj}/engines/*.so
%{_libdir}/%{name}%{maj}/backends/*.so
%{_libdir}/%{name}%{maj}/sanityCheck
%{_libdir}/%{name}%{maj}/ardour*
%{_libdir}/%{name}%{maj}/h*ardour*
%dir %{_sysconfdir}/%{name}%{maj}
%{_iconsdir}/hicolor/*
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/%{name}.menus
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/clearlooks.rc
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/default_ui_config
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/system_config
%config(noreplace) %{_sysconfdir}/%{name}%{maj}/trx.menus

%files -n	%{libardour}
%{_libdir}/%{name}%{maj}/libardour.so.3*

%files -n	%{libaudiographer}
%{_libdir}/%{name}%{maj}/libaudiographer.so.0*

%files -n	%{libcanvas}
%{_libdir}/%{name}%{maj}/libcanvas.so.0*

%files -n	%{libevoral}
%{_libdir}/%{name}%{maj}/libevoral.so.0*

%files -n	%{libgtkmm2ext}
%{_libdir}/%{name}%{maj}/libgtkmm2ext.so.0*

%files -n	%{libmidipp}
%{_libdir}/%{name}%{maj}/libmidipp.so.*

%files -n	%{libpbd}
%{_libdir}/%{name}%{maj}/libpbd.so.*

%files -n	%{libptformat}
%{_libdir}/%{name}%{maj}/libptformat.so.*

%files -n	%{libqmdsp}
%{_libdir}/%{name}%{maj}/libqmdsp.so.*

%files -n	%{libardouralsa}
%{_libdir}/%{name}%{maj}/libardouralsautil.so.0*

%files -n %{libardourvampplugins}
%{_libdir}/%{name}%{maj}/vamp/libardourvampplugins.so.*

%files -n %{devname}
%{_libdir}/%{name}%{maj}/*.so
%{_libdir}/%{name}%{maj}/vamp/*.so

