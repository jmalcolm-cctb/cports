pkgname = "vmaf"
pkgver = "3.0.0"
pkgrel = 0
build_style = "meson"
meson_dir = "libvmaf"
hostmakedepends = ["pkgconf", "meson", "nasm", "doxygen"]
checkdepends = ["xxd"]
pkgdesc = "Perceptual video quality assessment tool developed by Netflix"
maintainer = "LeFantome <malcolm.justin@gmail.com>"
license = "BSD-2-Clause-Patent"
url = "https://github.com/Netflix/vmaf"
source = f"https://github.com/Netflix/vmaf/archive/v{pkgver}/libvmaf-{pkgver}.tar.gz"
sha256 = "7178c4833639e6b989ecae73131d02f70735fdb3fc2c7d84bc36c9c3461d93b1"
options = ["splitstatic"]

def post_install(self):
    self.install_license("LICENSE")
