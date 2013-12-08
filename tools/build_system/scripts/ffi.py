import os
import config
from base import *

class FFI(Base):
    
    def __init__(self):
        self.name = "ffi"
        self.version = "3.0.13"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]  # , config.COMPILER_WIN_MSVC2010, config.COMPILER_WIN_MSVC2012]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "When version changes, update the build() function of Glib too. It uses a hardcoded version"

    def download(self):
        return 
        rb_download_and_extract(self, 
                                "ftp://sourceware.org/pub/libffi/libffi-" +self.version +".tar.gzip",
                                "libffi-" +self.version +".tar.gzip", 
                                "libffi-" +self.version)


    def build(self):
        if rb_is_mac():
            rb_build_with_autotools(self)
        else:
            rb_red_ln("@todo pkgconfig")


    def deploy(self):
        if rb_is_mac():
            rb_red_ln("@todo pkgconfig ")
        else:
            rb_red_ln("@todo pkgconfig ")



                
            



