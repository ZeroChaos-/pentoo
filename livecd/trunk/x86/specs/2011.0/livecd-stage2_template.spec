subarch: i686
version_stamp: 2011.0
target: livecd-stage2
rel_type: default
profile: hardened/linux/x86
snapshot: 2011.0
source_subpath: default/livecd-stage1-i686-2011.0
portage_confdir: /var/svn/pentoo/livecd/trunk/portage
portage_overlay: /usr/local/portage /var/lib/layman/enlightenment

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
# pkgcache_path:

# This allows the optional directory containing the output packages for kernel
# builds.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# kerncache_path: /tmp/kernel
#kerncache_path:

livecd/fstype: squashfs
livecd/fsops:  -comp xz -Xbcj x86 -b 1048576 -Xdict-size 1048576 -no-recovery
#livecd/fsops: -b 1048576 -comp lzma -sort sort_file.txt -no-recovery -processors 8
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/grub-memtest86+-cdtar.tar.bz2
livecd/iso: /tmp/pentoo-i686-2011.0_beta.iso

# A fsscript is simply a shell script that is copied into the chroot of the CD
# after the kernel(s) and any external modules have been compiled and is 
# executed within the chroot.  It can contain any commands that are available
# via the packages installed by our stages or by the packages installed during
# the livecd-stage1 build.  We do not use one for the official release media, so
# there will not be one listed below.  The syntax is simply the full path and
# filename to the shell script that you wish to execute.  The script is copied
# into the chroot by catalyst automatically.
# example:
# livecd/fsscript:
livecd/fsscript: /var/svn/pentoo/livecd/trunk/scripts/2010.0/fsscript.sh

# The splash type determines the automatic arguments for the bootloader on
# supported architectures.  The possible options are gensplash and bootsplash.
# example:
# livecd/splash_type: gensplash
# livecd/splash_type: gensplash

# This is where you set the splash theme.  This theme must be present in either
# /etc/splash or /etc/bootsplash, depending on your livecd/splash_type, before
# the kernel has completed building during the livecd-stage2 target.
# example:
# livecd/splash_theme: livecd-2005.0
# livecd/splash_theme: gentoo

# This is a set of arguments that get passed to the bootloader for your CD.  It
# is used on the x86/amd64 release media to enable keymap selection.
# example:
# livecd/bootargs: dokeymap
livecd/bootargs: aufs max_loop=256 dokeymap

# This is a set of arguments that will be passed to genkernel for all kernels
# defined in this target.  It is useful for passing arguments to genkernel that
# are not otherwise available via the livecd-stage2 spec file.
# example:
# livecd/gk_mainargs: --lvm2 --dmraid
#livecd/gk_mainargs: --no-clean --no-mrproper --unionfs --makeopts=-j5
livecd/gk_mainargs: --makeopts=-j8 --dmraid --gpg --luks --lvm

# This option allows you to specify your own linuxrc script for genkernel to use
# when building your CD.  This is not checked for functionality, so it is up to
# you to debug your own script.  We do not use one for the official release
# media, so there will not be one listed below.
# example:
# livecd/linuxrc:
# livecd/linuxrc:

# This option controls quite a bit of catalyst internals and sets up several
# defaults.  Each type behaves slightly differently and is explained below.
# gentoo-release-minimal - This creates an official minimal InstallCD.
# gentoo-release-universal - This creates an official universal InstallCD.
# gentoo-release-livecd - This creates an official LiveCD environment.
# gentoo-gamecd - This creates an official Gentoo GameCD.
# generic-livecd - This should be used for all non-official media.
# example:
# livecd/type: gentoo-release-minimal
livecd/type: generic-livecd

# This is for the README.txt on the root of the CD.  For Gentoo releases, we
# use a default README.txt, and this will be used on your CD if you do not
# provide one yourself.  Since we do not use this for the official releases, it
# is left blank below.
# example:
# livecd/readme:
# livecd/readme:

# This is for the CD's message of the day.  It is not required for official
# release media, as catalyst builds a default motd when the livecd/type is set
# to one of the gentoo-* options.  This setting overrides the default motd even
# on official media.  Since we do not use this for the official releases, it is
# left blank below.
# example:
# livecd/motd:
# livecd/motd:

# This is for blacklisting modules from being hotplugged that are known to cause
# problems.  Putting a module name here will keep it from being auto-loaded,
# even if ti is detected by hotplug.
# example:
# livecd/modblacklist: 8139cp
livecd/modblacklist: arusb_lnx rt2870sta rt3070sta prism54 ipv6 r8187 pcspkr nouveau ieee1394

# This is for adding init scripts to runlevels.  The syntax for the init script
# is the script name, followed by a pipe, followed by the runlevel in which you
# want the script to run.  It looks like spind|default and is space delimited.
# We do not use this on the official media, as catalyst sets up the runlevels
# correctly for us.  Since we do not use this, it is left blank below.
# This option will automatically create missing runlevels
# example:
# livecd/rcadd:
livecd/rcadd: autoconfig|default gpm|default dbus|default microcode_ctl|boot

# This is for removing init script from runlevels.  It is executed after the
# defaults shipped with catalyst, so it is possible to remove the defaults using
# this option.  It can follow the same syntax as livcd/rcadd, or you can leave
# the runlevel off to remove the script from any runlevels detected.  We do not
# use this on the official media, so it is left blank.
# example:
# livecd/rcdel:
livecd/rcdel: keymaps|boot spind|default

# This overlay is dropped onto the CD filesystem and is outside any loop which
# has been configured.  This is typically used for adding the documentation,
# distfiles, snapshots, and stages to the official media.  These files will not 
# be available if docache is enabled, as they are outside the loop.
# example:
# livecd/overlay: /tmp/overlay-minimal
livecd/overlay: /var/svn/pentoo/livecd/trunk/isoroot

# This overlay is dropped onto the filesystem within the loop.  This can be used
# for such things as updating configuration files or adding anything else you
# would want within your CD filesystem.  Files added here are available when
# docache is used.  We do not use this on the official media, so we will leave
# it blank below.
# example:
# livecd/root_overlay:
livecd/root_overlay: /var/svn/pentoo/livecd/trunk/root_overlay

# This is here to enable udev support in both catalyst and genkernel.  This
# option requires genkernel >= 3.1.0, and is not needed with genkernel >=3.2.0,
# as udev is the default.
# example:
# livecd/devmanager: udev
# livecd/devmanager:

# This is used by catalyst to copy the specified file to /etc/X11/xinit/xinitrc
# and is used by the livecd/type gentoo-gamecd and generic-livecd.  While the
# file will still be copied for any livecd/type, catalyst will only create the
# necessary /etc/startx for those types, so X will not be automatically started.
# This is useful also for setting up X on a CD where you do not wish X to start
# automatically.  We do not use this on the release media, so it is left blank.
# example:
# livecd/xinitrc:
# livecd/xinitrc:

# This is used by catalyst to determine which display manager you wish to
# become the default.  This is used on the official Gentoo LiveCD and is valid
# for any livecd/type.
# example:
# livecd/xdm: gdm
# livecd/xdm:

# This is used by catalyst to determine which X session should be started by
# default by the display manager.  This is used on the official Gentoo LiveCD
# and is valid for any livecd/type.
# example:
# livecd/xsession: gnome
# livecd/xsession:

# This option is used to create non-root users on your CD.  It takes a space
# separated list of user names.  These users will be added to the following
# groups: users,wheel,audio,games,cdrom,usb
# If this is specified in your spec file, then the first user is also the user
# used to start X. Since this is not used on the release media, it is blank.
# example:
# livecd/users:
# livecd/users:

# This option sets the volume ID of the CD created.
# example:
# livecd/volid: Gentoo Linux 2005.0 X86
livecd/volid: 2011.0

# This option is only used when creating a GameCD.  This specifies the file that
# contains the definitions for GAME_NAME and GAME_EXECUTABLE, which are used by
# the GameCD scripts to set some specific options for the game.  This is not
# used on the release media, and is therefore blank.
# example:
# gamecd/conf:
gamecd/conf:

# This option is used to specify the number of kernels to build and also the
# labels that will be used by the CD bootloader to refer to each kernel image.
# example:
# boot/kernel: gentoo
boot/kernel: pentoo

boot/kernel/pentoo/sources: ~pentoo-sources-2.6.38

# This option is the full path and filename to a kernel .config file that is
# used by genkernel to compile the kernel this label applies to.
# example:
# boot/kernel/gentoo/config: /tmp/2.6.11-smp.config
boot/kernel/pentoo/config:  /var/svn/pentoo/livecd/trunk/x86/kernel/config-2.6.38

# This option sets genkernel parameters on a per-kernel basis and applies only
# to this kernel label.  This can be used for building options into only a
# single kernel, where compatibility may be an issue.  Since we do not use this
# on the official release media, it is left blank, but it follows the same
# syntax as livecd/gk_mainargs.
# example:
# boot/kernel/gentoo/gk_kernargs:
boot/kernel/pentoo/gk_kernargs: 

# This option sets the USE flags used to build the kernel and also any packages
# which are defined under this kernel label.  These USE flags are additive from
# the default USE for the specified profile.
# example:
# boot/kernel/gentoo/use: pcmcia usb -X
boot/kernel/pentoo/use: X livecd -nls gtk -kde -eds gtk2 cairo pam firefox gpm dvdr oss
mmx sse sse2 mpi wps offensive dwm -64bit -doc -examples
wifi injection lzma speed gnuplot pyx test-programs fwcutter qemu
-quicktime -qt -qt3 qt3support qt4 -webkit -cups -spell lua curl -dso
png jpeg gif dri svg aac nsplugin xrandr consolekit -ffmpeg fontconfig
alsa esd gstreamer jack mp3 vorbis wavpack wma
dvd mpeg ogg rtsp x264 xvid sqlite truetype nss
opengl dbus binary-drivers hal acpi usb subversion libkms
analyzer bluetooth cracking databse enlightenment exploit forensics mitm proxies
scanner rce footprint forging fuzzers voip wireless -openfile_log pentoo
grsec aufs -stage2

# This option appends an extension to the name of your kernel, as viewed by a
# uname -r/  This also affects any modules built under this kernel label.  This
# is useful for having two kernels using the same sources to keep the modules
# from overwriting each other.  We do not use this on the official media, so it
# is left blank.
# example:
# boot/kernel/gentoo/extraversion:
# boot/kernel/gentoo/extraversion:

# This option is for merging kernel-dependent packages and external modules that
# are configured against this kernel label.
# example:
# boot/kernel/gentoo/packages: pcmcia-cs speedtouch slmodem globespan-adsl hostap-driver hostap-utils ipw2100 ipw2200 fritzcapi fcdsl cryptsetup
#pentoo/pentoo
boot/kernel/pentoo/packages: 
x11-misc/mkxf86config
app-emulation/open-vm-tools
sys-apps/pcmciautils
net-misc/iodine
net-wireless/atmel-firmware
net-wireless/bcm43xx-fwcutter
net-wireless/compat-wireless
sys-kernel/linux-firmware
net-wireless/ipw2100-firmware
net-wireless/ipw2200-firmware
#net-wireless/iwl3945-ucode
#net-wireless/iwl4965-ucode
#net-wireless/iwl5000-ucode
#net-wireless/ralink-firmware
#net-wireless/madwifi-hal
net-wireless/orinoco-fwutils
#net-wireless/prism54-firmware
net-wireless/wpa_supplicant
net-wireless/zd1201-firmware
net-wireless/zd1211-firmware
sys-fs/fuse
sys-fs/ntfs3g
net-firewall/firehol
x11-drivers/ati-drivers
x11-drivers/nvidia-drivers
x11-drivers/xf86-input-synaptics
x11-drivers/xf86-video-virtualbox
#pentoo/pentoo-cracking
#=app-crypt/pyrit-9999
#app-crypt/oclhashcat-bin
#app-crypt/cuda-multiforcer
#app-crypt/cuda-rarcrypt

# This option is only for ppc64 machines.  If used it will create the /etc/yaboot.conf
# entry used for booting a ibm powerpc machine.
# example:
# boot/kernel/gentoo/machine_type: ibm
# boot/kernel/gentoo/machine_type:

# This is only supported on ppc64 currently.  This entry sets up the console=
# boot parameters required for sending the output to the appropriate console.
# example:
# boot/kernel/gentoo/console: hvsi0 
# boot/kernel/gentoo/console: hvc0
# boot/kernel/gentoo/console: tty0 ttyS0
# boot/kernel/gentoo/console:

# This is a list of packages that will be unmerged after all the kernels have
# been built.  There are no checks on these packages, so be careful what you
# add here.  They can potentially break your CD.
# example:
# livecd/unmerge: acl attr autoconf automake bin86 binutils libtool m4 bison ld.so make perl patch linux-headers man-pages sash bison flex gettext texinfo ccache distcc addpatches man groff lib-compat miscfiles rsync sysklogd bc lcms libmng genkernel diffutils libperl gnuconfig gcc-config gcc bin86 cpio cronbase ed expat grub lilo help2man libtool gentoo-sources
livecd/unmerge: sys-apps/zerosmagic dev-java/ant-core dev-java/libreadline-java dev-java/javacup dev-java/jakarta-oro dev-java/ant-nodeps dev-java/xml-commons-external dev-java/xml-commons-resolver dev-java/bcel dev-java/sun-jaf dev-java/commons-logging dev-java/ant-swing dev-java/jzlib dev-java/junit dev-java/ant-antlr dev-java/log4j dev-java/jakarta-regexp dev-java/xjavac dev-java/jdepend dev-java/ant-junit dev-java/xalan-serializer dev-java/commons-net dev-java/ant-apache-resolver dev-java/jsch dev-java/ant-apache-bcel dev-java/sun-javamail dev-java/ant-apache-oro dev-java/ant-apache-log4j dev-java/ant-apache-regexp dev-java/jython dev-java/ant-commons-logging dev-java/ant-jdepend dev-java/ant-commons-net dev-java/ant-jsch dev-java/ant-javamail dev-java/xerces dev-java/xalan dev-java/bsf dev-java/ant-trax dev-java/ant-apache-bsf dev-java/ant-tasks dev-java/ant dev-libs/klibc x11-libs/qt-webkit x11-libs/qt-assistant dev-texlive/texlive-latex dev-texlive/texlive-basic dev-texlive/texlive-latexrecommended app-text/texlive-core gentoo-sources dev-java/icedtea6-bin

# This option is used to empty the directories listed.  It is useful for getting
# rid of files that don't belong to a particular package, or removing files from
# a package that you wish to keep, but won't need the full functionality.
# example:
livecd/empty: /var/empty /var/lock /var/tmp /var/spool /var/state /tmp /usr/local/portage

# This option tells catalyst to clean specific files from the filesystem and is
# very usefu in cleaning up stray files in /etc left over after livecd/unmerge.
# example:
livecd/rm: /etc/resolv.conf /usr/share/gtk-doc /usr/share/doc/lib* /usr/share/doc/g* /usr/share/doc/tiff* /usr/share/doc/twisted* /usr/share/doc/ruby* /usr/share/doc/paramiko* /usr/share/doc/perl* /usr/share/doc/pcre* /usr/share/doc/binutils* /usr/share/doc/ntp* /usr/share/doc/readline* /usr/share/doc/cmake* /usr/share/doc/freetds* /usr/share/doc/flac* /usr/share/doc/postfix* 
# /usr/src/linux* we keep the sources
