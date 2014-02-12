import os
import config
from base import *
import subprocess

class GMP(Base):
    def __init__(self):
        self.name = "gmp"
        self.version = "5.1.3"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "Arbitrary precision arithmic"

    def download(self): 
        rb_download_and_extract(self, 
                                "https://gmplib.org/download/gmp/gmp-" +self.version +".tar.bz2",
                                "gmp-" +self.version +".tar.bz2", 
                                "gmp-" +self.version)
        return True

    def build(self):
        if rb_is_unix():
            rb_build_with_autotools(self)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libgmp.a")
        else:
            return False

    def deploy(self):
        if rb_is_mac(): 
            rb_deploy_lib(rb_install_get_lib_file("libgmp.a"))
            rb_deploy_header(rb_install_get_include_file("gmp.h"))
        return True
        
