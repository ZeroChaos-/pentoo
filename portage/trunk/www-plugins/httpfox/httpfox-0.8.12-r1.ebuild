# Copyright 1999-2014 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=5

FFP_TARGETS="firefox"
inherit mozilla-addon

MOZ_FILEID="217452"
DESCRIPTION="A HTTP analyzer addon for Firefox"
HOMEPAGE="http://code.google.com/p/httpfox"
SRC_URI="http://addons.mozilla.org/firefox/downloads/file/${MOZ_FILEID} -> ${FFP_XPI_FILE}.xpi"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="amd64 x86"