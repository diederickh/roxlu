import os
import config
from base import *

class LibUSB(Base):
    
    def __init__(self):
        self.name = "libusb"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["libtool"]
        self.info = "NOT FINISHED YET"

    def download(self):
        rb_git_clone(self, "git://git.libusb.org/libusb.git")

    def build(self):
        if rb_is_mac():
            dd = rb_get_download_dir(self)
            cmd = (
                "cd "+dd,
                "./autogen.sh",
                )
            rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())
            rb_build_with_autotools(self)
        else:
            rb_red_ln("@todo build !mac")
        return True

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libusb-1.0.a")
        else:
            rb_red_ln("@todo libusb")

        return True

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libusb-1.0.a"))
            rb_deploy_headers(dir = rb_install_get_dir() +"include/libusb-1.0/", subdir = "libusb-1.0")

        return True



                
            



