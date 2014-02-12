import os
import config
from base import *
import subprocess

class MPFR(Base):
    def __init__(self):
        self.name = "mpfr"
        self.version = "3.1.2"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "Multiple Precision Floating Point"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://www.mpfr.org/mpfr-current/mpfr-" +self.version +".tar.gz",
                                "mpfr-" +self.version +".tar.gz", 
                                "mpfr-" +self.version)
        return True

    def build(self):
        if rb_is_unix():
            rb_build_with_autotools(self)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libmpfr.a")
        return False

    def deploy(self):
        if rb_is_mac(): 
            rb_deploy_lib(rb_install_get_lib_file("libmpfr.a"))
            rb_deploy_header(rb_install_get_include_file("mpfr.h"))
            rb_deploy_header(rb_install_get_include_file("mpf2mpfr.h"))
        return True
        
