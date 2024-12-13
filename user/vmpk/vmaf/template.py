pkgname = "vmaf"
pkgver = "2.3.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["nasm", "xxd"]
pkgdesc = "Perceptual video quality assessment tool developed by Netflix"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause-Patent"
url = "https://github.com/Netflix/vmaf"
source = f"https://github.com/Netflix/vmaf/archive/refs/tags/v${pkgver}.tar.gz"
sha256 = "8d60b1ddab043ada25ff11ced821da6e0c37fd7730dd81c24f1fc12be7293ef2"


@subpackage("libb2-devel")
def _(self):
    return self.default_devel()
