import os
import config
from base import *

class AO(Base):
    
    def __init__(self):
        self.name = "libao"
        self.version = "1.1.0"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "Cross Platform Audio Playback"

    def download(self):
        rb_download_and_extract(self, 
                                "http://downloads.xiph.org/releases/ao/libao-" +self.version +".tar.gz",
                                "libao-" +self.version +".tar.gz", 
                                "libao-" +self.version)

    def build(self):
        if rb_is_unix():
            opts = ( "--enable-static=yes" )
            rb_build_with_autotools(self, opts)
        else:
            rb_red_ln("@todo build libao on !unix")
            return True

    def is_build(self):
         if rb_is_unix():
             return rb_install_lib_file_exists("libao.a")
         else:
             rb_red_ln("@todo libao check if file exists on windows")
             return True

    def deploy(self):
         if rb_is_unix():
             rb_deploy_lib(rb_install_get_lib_file("libao.a"))
             rb_deploy_headers(dir = rb_install_get_dir() +"include/ao/", subdir = "ao")
         else:
             rb_red_ln("@todo deploy libao on non-unix")
             return True


                
            



