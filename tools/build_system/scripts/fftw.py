import os
import config
from base import *
import subprocess

class FFTW(Base):
    def __init__(self):
        self.name = "fftw"
        self.version = "3.3.3"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "only compiled on mac"

    def download(self): 
        rb_download_and_extract(self,
                                "http://www.fftw.org/fftw-" +self.version +".tar.gz",
                                "fftw-" +self.version +".tar.gz",
                                "fftw-" +self.version)
        
        return True

    def build(self):
        if rb_is_mac():
            rb_build_with_autotools(self);
        return False

    def is_build(self):
        if rb_is_mac():
            return rb_install_lib_file_exists("libfftw3.a")
        return False

    def deploy(self):
        if rb_is_mac():
            rb_deploy_lib(rb_install_get_lib_file("libfftw3.a"))
            rb_deploy_header(rb_install_get_include_file("fftw3.h"))

        return True
        
