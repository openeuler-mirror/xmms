Name:           xmms
Epoch:          1
Version:        1.2.11
Release:        38.20071117cvs
License:        GPLv2+
Summary:        XMMS is a legacy GTK+1 music player modeled after Winamp
URL:            https://git.conf.top/public/rpmbuild/src/master/xmms
Source0:        xmms-%{version}-20071117cvs.patched.tar.bz2
Source1:        xmms.sh
Source2:        xmms.xpm
Source3:        xmms-1.2.11-mpg123.tar.bz2
Source4:        xmms.desktop
Provides:       xmms-esd = 1:%{version}-%{release} xmms-gui bundled(libmpg123) xmms-mp3 = %{version}-%{release} xmms-libs = 1:%{version}-%{release}
Obsoletes:      xmms-esd < 1:18.20071117cvs xmms-mp3 < 1.2.11-8 xmms-libs < 1:%{version}-%{release}
BuildRequires:  gtk+-devel alsa-lib-devel libogg-devel libvorbis-devel mikmod-devel gettext-devel
BuildRequires:  zlib-devel libGL-devel libXt-devel libSM-devel libXxf86vm-devel desktop-file-utils
Requires:       unzip libcanberra-gtk2 gtk2
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Patch0001:      xmms-1.2.6-audio.patch
Patch0002:      xmms-1.2.6-lazy.patch
Patch0003:      xmms-1.2.8-default-skin.patch
Patch0004:      xmms-1.2.11-alsalib.patch
Patch0005:      xmms-cd-mountpoint.patch
Patch0006:      xmms-1.2.11-multilib.patch
Patch0007:      xmms-1.2.11-is_quitting.patch
Patch0008:      xmms-1.2.10-configfile-safe-write.patch
Patch0009:      xmms-1.2.10-reposition.patch
Patch0010:      xmms-play.patch
Patch0011:      xmms-1.2.11-dso.patch
Patch0012:      xmms-1.2.10-ubuntu-CVE-2007-0653.patch
Patch0013:      xmms-alsa-fix-loop.patch
Patch0014:      xmms-1.2.11-mikmod-fix.patch
Patch0015:      xmms-1.2.11-a-b.patch

%description
XMMS is a legacy GTK+1 music player similar to Winamp's. XMMS supports
playlists and streaming content and has a configurable interface.

%package        devel
Summary:        Files required for XMMS plug-in development
Requires:       gtk+-devel pkgconfig
Requires:       xmms

%description    devel
Files needed for building plug-ins for XMMS.

%package        help
Summary:        Help document for XMMS
Buildarch:      noarch

%description    help
Help document for XMMS.

%prep
%autosetup -n xmms-%{version}-20071117cvs -a3 -p1
sed -i -e 's|"/lib /usr/lib"|"/%{_lib} %{_libdir}"|' configure
%build
%configure --disable-dependency-tracking --enable-kanji --enable-texthack --enable-ipv6 --with-pic --disable-esd
%make_build
%install
%make_install
install -dm 755 %{buildroot}%{_datadir}/xmms/Skins
%delete_la_and_a
mv %{buildroot}/%{_datadir}/locale/sr@Latn %{buildroot}/%{_datadir}/locale/sr@latin
for bin in xmms wmxmms ; do
    install -Dpm 755 %{buildroot}%{_bindir}/$bin %{buildroot}%{_libexecdir}/$bin
    sed -e "s|/usr/libexec/xmms|%{_libexecdir}/$bin|" %{SOURCE1} > %{buildroot}%{_bindir}/$bin
    chmod 755 %{buildroot}%{_bindir}/$bin
done
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}
install -Dpm 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/xmms.xpm
install -Dpm 644 xmms.pc %{buildroot}%{_libdir}/pkgconfig/xmms.pc
%find_lang xmms
%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files -f xmms.lang
%doc COPYING AUTHORS ChangeLog FAQ NEWS TODO README README.ab
%{_bindir}/{xmms,wmxmms}
%{_libexecdir}/{xmms,wmxmms}
%{_datadir}/applications/xmms.desktop
%{_datadir}/icons/hicolor/*x*/apps/xmms.xpm
%{_datadir}/xmms
%{_libdir}/libxmms.so.*
%{_libdir}/xmms/{Effect,General,Input,Output,Visualization}

%files devel
%{_bindir}/xmms-config
%{_includedir}/xmms/
%{_libdir}/libxmms.so
%{_datadir}/aclocal/xmms.m4
%{_libdir}/pkgconfig/xmms.pc

%files help
%{_mandir}/man1/*xmms.1*

%changelog
* Mon Jan 20 2020 wangzhishun <wangzhishun1@huawei.com> - 1:1.2.11-38.20071117cvs
- modify url

* Wed Jan 15 2020 openEuler Buildteam <buildteam@openeuler.org> - 1:1.2.11-37.20071117cvs
- Fix build dependence

* Fri Nov 29 2019 Ling Yang <lingyang2@huawei.com> - 1:1.2.11-36.20071117cvs
- Package init
