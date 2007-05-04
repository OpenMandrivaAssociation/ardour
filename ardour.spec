%define oname ardour2

Summary:   	Professional multitrack audio recording application
Name:		ardour
Version:	2.0
Release:	%mkrel 1
Source0:	http://ardour.org/releases/%{name}-%{version}.tar.bz2
Source5:	%{name}16.png
Source6:	%{name}32.png
Source7:	%{name}48.png
URL:		http://%{name}.sourceforge.net/
Group:		Sound
License:	GPL
BuildRequires:	scons
BuildRequires: 	libalsa-devel
BuildRequires:	jackit-devel		>= 0.80.0
BuildRequires:	libsndfile-devel	>= 1.0.18
BuildRequires:	libsamplerate-devel
BuildRequires:	liblrdf-devel
Buildrequires:	liblo-devel
BuildRequires:	libglib2.0-devel
BuildRequires:	libgnomecanvas2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libboost1-devel
Requires:	jackit			>= 0.80.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Ardour is a digital audio workstation.You can use it to record,
edit and mix multi-track audio. You can produce your own CDs,
mix video soundtracks, or just experiment with new ideas about
music and sound.

Ardour capabilities include: multichannel recording, non-destructive 
editing with unlimited undo/redo, full automation support, a powerful 
mixer, unlimited tracks/busses/plugins, timecode synchronization, 
and hardware control from surfaces like the Mackie Control Universal.
If you've been looking for a tool similar to ProTools, Nuendo, Pyramix,
or Sequoia, you might have found it. 

You MUST have jackd running and an ALSA sound driver to use ardour.

%prep
%setup -q

%build
scons PREFIX=%{_prefix}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
scons DESTDIR=%{buildroot} install 

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Ardour
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;AudioVideo;Audio;AudioVideoEditing;X-MandrivaLinux-Multimedia-Sound;
Encoding=UTF-8
EOF

# icons
mkdir -p %{buildroot}%{_miconsdir} %{buildroot}%{_liconsdir} %{buildroot}%{_iconsdir}
cat %{SOURCE5} > %{buildroot}%{_miconsdir}/%{name}.png
cat %{SOURCE6} > %{buildroot}%{_iconsdir}/%{name}.png
cat %{SOURCE7} > %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name} --all-name

%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc DOCUMENTATION/{AUTHORS*,CONTRIBUTORS*,FAQ*,README*,TRANSLATORS*}
%dir %{_sysconfdir}/%{oname}
%dir %{_libdir}/%{oname}
%dir %{_datadir}/%{oname}
%dir %{_datadir}/%{oname}/icons
%dir %{_datadir}/%{oname}/pixmaps
%dir %{_datadir}/%{oname}/templates
%config(noreplace) %{_sysconfdir}/%{oname}/%{name}.rc
%config(noreplace) %{_sysconfdir}/%{oname}/%{name}_system.rc
%config(noreplace) %{_sysconfdir}/%{oname}/%{oname}_ui.rc
%config(noreplace) %{_sysconfdir}/%{oname}/%{name}.bindings
%config(noreplace) %{_sysconfdir}/%{oname}/%{name}.colors
%config(noreplace) %{_sysconfdir}/%{oname}/%{name}.menus
%{_bindir}/%{oname}
%{_libdir}/%{oname}/*.so
%{_libdir}/%{oname}/ardour-2.0
%{_libdir}/%{oname}/surfaces/*.so
%{_libdir}/%{oname}/engines/*.so
%{_datadir}/applications/mandriva-ardour.desktop
%{_datadir}/%{oname}/icons/*.png
%{_datadir}/%{oname}/pixmaps/*.xpm
%{_datadir}/%{oname}/*.png
%{_datadir}/%{oname}/templates/*.template
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
