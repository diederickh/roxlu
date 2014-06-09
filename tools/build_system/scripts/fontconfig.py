import os
import config
from base import *

class FontConfig(Base):
    
    def __init__(self):
        self.name = "fontconfig"
        self.version = "2.11.0"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []

    def download(self):
       
        rb_download_and_extract(self, 
                                "http://www.freedesktop.org/software/fontconfig/release/fontconfig-" +self.version +".tar.gz",
                                "fontconfig-" +self.version +".tar.gz", 
                                "fontconfig-" +self.version)


    def build(self):
        rb_build_with_autotools(self)
        return True

    def is_build(self):
        return True

    def deploy(self):
        """
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libcairo.a"))
            rb_deploy_lib(rb_install_get_lib_file("libcairo.dylib"))
            rb_deploy_lib(rb_install_get_lib_file("libcairo.2.dylib"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"cairo", subdir = "cairo")
        """



                
            



