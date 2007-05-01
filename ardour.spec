%define name 	ardour 
%define version	2.0
%define release	%mkrel 1

%define major	0
%define libname %mklibname %name %major

Summary:   	Professional multitrack audio recording application
Name: 	   	%{name}
Version:   	%{version}
Release:   	%{release}
Epoch:		1
Source0:   	http://ardour.org/releases/%{name}-%{version}.tar.bz2
Source3:   	manual.pdf.bz2
# extra documentation from the Ardour Documentation Project
Source4:   	%{name}-documentation.tar.bz2
Source5:   	%{name}16.png
Source6:   	%{name}32.png
Source7:   	%{name}48.png
Source8:	ardour-launch.sh.bz2
URL:       	http://%{name}.sourceforge.net/
Group:     	Sound
License:   	GPL
BuildRoot: 	%{_tmppath}/%{name}-buildroot

BuildRequires:	scons
BuildRequires: 	libalsa-devel gdbm-devel gtk+-devel
BuildRequires:	jackit-devel >= 0.80.0
BuildRequires:	libsndfile-devel libsamplerate-devel ladspa-devel
BuildRequires: 	autoconf2.5 flex bison
BuildRequires: 	gettext-devel pkgconfig
# will need when manual returns
#BuildRequires: tetex-latex tetex-dvips
BuildRequires:	ncurses-devel curl-devel
BuildRequires:	liblrdf-devel raptor-devel
BuildRequires:  libart_lgpl-devel
Requires:	jackit >= 0.80.0
Requires:	qjackctl

%description
Ardour is a multichannel hard disk recorder. It is capable of recording 24
or more channels of 32 bit audio at 48kHz. Ardour is intended to function
as a "professional" HDR system, replacing dedicated hardware solutions such
as the Mackie HDR, the Tascan 2424 and more traditional tape systems like
the Alesis ADAT series. It supports MIDI Machine Control, and so can be
controlled from any MMC controller, such as the Mackie Digital 8 Bus mixer
and many other modern digital mixers.

Ardour-KSI is a curses-based interface to Ardour.

You MUST have jackd running and an ALSA sound driver to use ardour.

%prep
%setup -q -n %{name}-%{version} -a 4
bzcat %SOURCE3 > manual.pdf

%build
scons PREFIX=%{_prefix} KSI=1 DIST_TARGET=none

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
scons DESTDIR=$RPM_BUILD_ROOT install 

#rm $RPM_BUILD_ROOT/%_bindir/ksi
#mv $RPM_BUILD_ROOT/%_libdir/ardour/ksix $RPM_BUILD_ROOT/%_bindir/ardour-ksi
#rm -f $RPM_BUILD_ROOT/%_datadir/ardour/libardour.*
mv $RPM_BUILD_ROOT/%_bindir/%{name} $RPM_BUILD_ROOT/%_bindir/%{name}x
bzcat %SOURCE8 > $RPM_BUILD_ROOT/%_bindir/%{name}
chmod 755 $RPM_BUILD_ROOT/%_bindir/%{name}
rm -f $RPM_BUILD_ROOT/%_datadir/locale/*/*/libgtkmmext.mo

# Mandrake Menu entry
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
section="Multimedia/Sound" \
title="Ardour" \
longtitle="Digital Audio Workstation" \
command="/usr/bin/%{name}" \
icon="%{name}.png" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir} $RPM_BUILD_ROOT%{_iconsdir}
cat %{SOURCE5} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
cat %{SOURCE6} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cat %{SOURCE7} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

# locales
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{name}
%{update_menus}

%postun -n %{name}
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc DOCUMENTATION/{AUTHORS*,CONTRIBUTORS*,FAQ*,README*,TRANSLATORS*}
%doc manual.pdf
%doc %{name}-documentation
%{_bindir}/%{name}
%{_bindir}/%{name}x
%dir %_sysconfdir/%{name}
%config(noreplace) %_sysconfdir/%{name}/%{name}.rc
%config(noreplace) %_sysconfdir/%{name}/%{name}_system.rc
%config(noreplace) %_sysconfdir/%{name}/%{name}_ui.rc
%_datadir/%{name}
%_datadir/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/*


