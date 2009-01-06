subarch: i686
version_stamp: 2009.0
target: livecd-stage1
rel_type: default
profile: default/linux/x86/2008.0
snapshot: 2009.0
source_subpath: default/stage3-i686-2009.0
portage_confdir: /root/pentoo/x86/portage
portage_overlay: /usr/local/portage /usr/portage/local/layman/enlightenment

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
# pkgcache_path:

livecd/use: X livecd -gnome -nls gtk -kde -eds gtk2 cairo -pam firefox gpm dvdr oss
mmx sse sse2 mpi
wifi injection
-quicktime -qt -qt3 -qt4 -cups -spell lua
png jpeg gif dri svg aac 
alsa esd gstreamer jack mp3 vorbis wavpack wma
dvd mpeg ogg rtsp x264 xvid wxwindows sqlite
opengl dbus

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
livecd/packages:
sys-kernel/pentoo-sources
sys-kernel/linux-headers
app-admin/gamin
=app-admin/genmenu-9999
app-admin/localepurge
app-admin/syslog-ng
app-arch/gzip
app-crypt/chntpw
app-crypt/johntheripper
app-crypt/md5bf
app-crypt/plaintoo
app-crypt/SIPcrack
app-editors/hexedit
app-editors/nano
app-editors/ghex
app-editors/scite
#app-text/epdf
app-text/epdfview
app-forensics/cmospwd
app-fuzz/Peach
app-fuzz/bed
app-fuzz/bss
app-fuzz/fuzzer-server
app-fuzz/fusil
app-fuzz/http-fuzz
app-fuzz/protos
#app-fuzz/scapy
app-fuzz/smtp-fuzz
app-fuzz/smudge
#app-fuzz/snmp-fuzzer
app-fuzz/ohrwurm
app-fuzz/taof
app-misc/livecd-tools
app-mobilephone/obexftp
app-portage/gentoolkit
app-text/dos2unix
dev-db/absinthe
dev-db/mssqlscan
dev-db/oat
dev-db/sqid
dev-db/sqlat
dev-db/sqlbf
#dev-db/sqlinject
dev-db/sqlix
dev-db/sqlmap
dev-db/sqlninja
dev-java/jad-bin
dev-libs/libxslt
dev-libs/openobex
dev-libs/libxml2
dev-python/pysqlite
dev-python/pygtk
=dev-python/lxml-1.3.6
dev-util/dialog
dev-util/subversion
dev-util/insight
gnome-base/gnome-menus
media-gfx/scrot
media-sound/audacious
media-sound/alsa-utils
media-sound/sox
media-video/vlc
net-analyzer/aimsniff
net-analyzer/amap
net-analyzer/angst
net-analyzer/arpwatch
net-analyzer/authforce
net-analyzer/autoscan-network
net-analyzer/dnsa
net-analyzer/dnsenum
#net-analyzer/driftnet
net-analyzer/dsniff
net-analyzer/ettercap
net-analyzer/fierce
net-analyzer/firewalk
net-analyzer/fragroute
net-analyzer/ftester
net-analyzer/geoedge
net-analyzer/gspoof
net-analyzer/honeyd
net-analyzer/hping
net-analyzer/hunt
#net-analyzer/hydra
net-analyzer/inguma
net-analyzer/ike-scan
net-analyzer/isic
net-analyzer/macchanger
net-analyzer/mbrowse
net-analyzer/medusa
net-analyzer/metacoretex-ng
net-analyzer/metagoofil
net-analyzer/metasploit
net-analyzer/mosref
net-analyzer/nbtscan
net-analyzer/nessus
net-analyzer/nessus-plugins
net-analyzer/netcat
net-analyzer/netdiscover
#net-analyzer/netdude
#net-analyzer/net-snmp+++Replaced-by-onesixtyone
net-analyzer/netwag
net-analyzer/netwox
net-analyzer/ngrep
net-analyzer/nikto
net-analyzer/nmap
net-analyzer/nmbscan
net-analyzer/ntop
net-analyzer/ntp-fingerprint
net-analyzer/onesixtyone
net-analyzer/p0f
net-analyzer/packit
net-analyzer/paketto
net-analyzer/rain
net-analyzer/sara
net-analyzer/scanssh
net-analyzer/siphon
net-analyzer/sipvicious
net-analyzer/smtpmap
net-analyzer/sniffit
net-analyzer/snmpenum
net-analyzer/snort
net-analyzer/subdomainer
net-analyzer/tcpdump
net-analyzer/tcptraceroute
net-analyzer/thcrut
net-analyzer/theHarvester
net-analyzer/traceroute
net-analyzer/upnpscan
net-analyzer/voiphopper
net-analyzer/w3af
net-analyzer/wfuzz
net-analyzer/wireshark
net-analyzer/xprobe
net-analyzer/yersinia
net-dialup/linux-atm
net-dialup/lrzsz
net-dialup/minicom
net-dns/bind-tools
net-dns/c-ares
#net-firewall/fwbuilder
net-fs/nfs-utils
net-fs/samba
net-ftp/ftp
net-ftp/netkit-ftpd
net-ftp/oftpd
net-im/pidgin
#net-im/skype
#net-im/ekiga
net-irc/irssi
net-irc/xchat
net-mail/mailbase
net-misc/bridge-utils
net-misc/curl
net-misc/dhcp
net-misc/dhcpcd
#net-misc/ipsorcery
net-misc/iputils
net-misc/karma
net-misc/nemesis
net-misc/neon
net-misc/netkit-fingerd
net-misc/netkit-rsh
net-misc/netsed
net-misc/ntp
net-misc/openssh
net-misc/partysip
net-misc/proxychains
net-misc/raccess
net-misc/rdesktop
net-misc/grdesktop
net-misc/rsync
#net-misc/sipbomber
net-misc/sipp
#net-misc/siproxd
net-misc/sipsak
net-misc/socat
net-misc/stunnel
net-misc/telnet-bsd
net-misc/tightvnc
net-misc/tor
net-misc/voipong
net-misc/wget
net-misc/whois
net-p2p/bittorrent
net-proxy/3proxy
net-proxy/httpush
net-proxy/paros
net-proxy/privoxy
net-proxy/tsocks
net-proxy/webscarab
net-wireless/afrag
net-wireless/aircrack-ng
net-wireless/airsnort
net-wireless/airtraf
net-wireless/bluez-libs
net-wireless/bluez-utils
net-wireless/btscanner
net-wireless/kismet
net-wireless/mdk
net-wireless/ska
#net-wireless/waveselect
net-wireless/wepattack
net-wireless/wepdecrypt
net-wireless/wifi-radar
net-wireless/wifiscanner
net-wireless/wifitap
net-wireless/wireless-tools
net-wireless/wpa_supplicant
net-www/netscape-flash
sys-apps/baselayout
sys-apps/eject
sys-apps/hwdata-redhat
sys-apps/hwsetup
sys-apps/iproute2
sys-apps/less
sys-apps/pciutils
sys-apps/portage
sys-apps/slocate
sys-block/disktype
sys-block/gparted
sys-boot/grub
sys-boot/syslinux
sys-devel/gettext
sys-devel/crossdev
sys-devel/gdb
sys-fs/device-mapper
sys-fs/jfsutils
sys-fs/reiserfsprogs
sys-fs/reiser4progs
sys-fs/squashfs-tools
sys-fs/udev
sys-libs/gpm
sys-libs/libkudzu
sys-power/acpid
www-client/mozilla-firefox-bin
mail-client/mozilla-thunderbird-bin
x11-base/xorg-server
x11-base/xorg-x11
x11-libs/ecore
x11-libs/esmart
x11-libs/evas
x11-libs/gtk+
x11-plugins/firecat
#x11-plugins/e_modules
x11-plugins/e_modules-bling
x11-plugins/e_modules-calendar
x11-plugins/e_modules-cpu
x11-plugins/e_modules-language
x11-plugins/e_modules-mem
x11-plugins/e_modules-net
#x11-plugins/e_modules-notification
#x11-plugins/e_modules-screenshot
x11-plugins/e_modules-weather
x11-plugins/e_modules-wlan
x11-plugins/itask-ng
x11-plugins/winlist_ng
x11-terms/rxvt-unicode
x11-libs/e_dbus
x11-wm/enlightenment
