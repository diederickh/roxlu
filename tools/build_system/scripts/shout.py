import os
import config
from base import *

class Shout(Base):

    def __init__(self):
        self.name = "shout"
        self.version = "2.3.1"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "libshout"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://downloads.xiph.org/releases/libshout/libshout-" +self.version +".tar.gz",
                                "libshout-" +self.version +".tar.gz",
                                "libshout-" +self.version)
        return True

    def build(self):
        rb_build_with_autotools(self)
        return False

    def is_build(self):
        if rb_is_unix():
            return rb_deploy_lib_file_exists("libshout.a")
        return False

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libshout.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"shout")
        return True
        
