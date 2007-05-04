%define major	0
%define libname %mklibname %{name} %{major}

Summary:   	Professional multitrack audio recording application
Name:		ardour
Version:	2.0
Release:	%mkrel 1
Source0:	http://ardour.org/releases/%{name}-%{version}.tar.bz2
Source3:	manual.pdf.bz2
# extra documentation from the Ardour Documentation Project
Source4:	%{name}-documentation.tar.bz2
Source5:	%{name}16.png
Source6:	%{name}32.png
Source7:	%{name}48.png
Source8:	ardour-launch.sh.bz2
URL:		http://%{name}.sourceforge.net/
Group:		Sound
License:	GPL
BuildRequires:	scons
BuildRequires: 	libalsa-devel
BuildRequires:	jackit-devel			>= 0.80.0
BuildRequires:	libsndfile-devel		>= 1.0.18
BuildRequires:	libsamplerate-devel
BuildRequires:	liblrdf-devel
Buildrequires:	liblo-devel
BuildRequires:	libglib2.0-devel
BuildRequires:	libgnomecanvas2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libboost1-devel
#Requires:	jackit >= 0.80.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Ardour is a multichannel hard disk recorder. It is capable of recording 24
or more channels of 32 bit audio at 48kHz. Ardour is intended to function
as a "professional" HDR system, replacing dedicated hardware solutions such
as the Mackie HDR, the Tascan 2424 and more traditional tape systems like
the Alesis ADAT series. It supports MIDI Machine Control, and so can be
controlled from any MMC controller, such as the Mackie Digital 8 Bus mixer
and many other modern digital mixers.

#Ardour-KSI is a curses-based interface to Ardour.

You MUST have jackd running and an ALSA sound driver to use ardour.

%prep
%setup -q -n %{name}-%{version} -a 4
bzcat %SOURCE3 > manual.pdf

%build
scons PREFIX=%{_prefix}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
scons DESTDIR=%{buildroot} install 

#rm %{buildroot}/%_bindir/ksi
#mv %{buildroot}/%_libdir/ardour/ksix %{buildroot}/%_bindir/ardour-ksi
#rm -f %{buildroot}/%_datadir/ardour/libardour.*
#mv %{buildroot}/%_bindir/%{name} %{buildroot}/%_bindir/%{name}x
#bcat %SOURCE8 > %{buildroot}/%_bindir/%{name}
#chmod 755 %{buildroot}/%_bindir/%{name}
#rm -f %{buildroot}/%_datadir/locale/*/*/libgtkmmext.mo

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
#mkdir -p %{buildroot}%{_miconsdir} %{buildroot}%{_liconsdir} %{buildroot}%{_iconsdir}
#cat %{SOURCE5} > %{buildroot}%{_miconsdir}/%{name}.png
#cat %{SOURCE6} > %{buildroot}%{_iconsdir}/%{name}.png
#cat %{SOURCE7} > %{buildroot}%{_liconsdir}/%{name}.png

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
#%doc manual.pdf
#%doc %{name}-documentation
%dir %_sysconfdir/%{name}
%dir %{_libdir}/ardour2
%dir %{_libdir}/ardour2/ardour-2.0
%dir %{_datadir}/ardour2
%dir %{_datadir}/ardour2/icons
%dir %{_datadir}/ardour2/pixmaps
%dir %{_datadir}/ardour2/templates
%config(noreplace) %_sysconfdir/%{name}/%{name}.rc
%config(noreplace) %_sysconfdir/%{name}/%{name}_system.rc
%config(noreplace) %_sysconfdir/%{name}/%{name}_ui.rc
%config(noreplace) %_sysconfdir/%{name}/%{name}.bindings
%config(noreplace) %_sysconfdir/%{name}/%{name}.colors
%{_bindir}/%{name}
%{_libdir}/ardour2/ardour-2.0/*.so
%{_libdir}/ardour2/surfaces/*.so
%{_datadir}/applications/mandriva-ardour.desktop
%{_datadir}/ardour2/icons/*.png
%{_datadir}/ardour2/pixmaps/*.xpm
%{_datadir}/ardour2/*.png
%{_datadir}/ardour2/templates/*.template
#%{_iconsdir}/%{name}.png
#%{_miconsdir}/%{name}.png
#%{_liconsdir}/%{name}.png
