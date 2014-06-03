import os
import config
from base import *

class LibVPX(Base):
    def __init__(self):
        self.name = "libvpx"
        self.version = "git"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["yasm"]
        self.info = "libvpx (vp8 and vp9)"

    def download(self): 
        rb_git_clone(self, "https://chromium.googlesource.com/webm/libvpx")
        return True

    def build(self):
        if rb_is_unix():
            # vp9 doesn't compile
            dd = rb_get_download_dir(self)
            cmd = (
                "export PATH=" +rb_install_get_dir() +"bin/:$PATH",
                "yasm --version",
                "cd " +dd,
                "./configure " +rb_get_configure_flags() +" --as=yasm --disable-shared --enable-static --disable-vp9", 
                "make",
                "make install"
            )
            rb_execute_shell_commands(self, cmd);
        return False

    def is_build(self):
        if rb_is_mac():
            return rb_deploy_lib_file_exists("libvpx.a")
        return False

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libvpx.a"))
        rb_deploy_headers(dir = rb_install_get_dir() +"include/vpx/", subdir = "vpx")
        return True
        
