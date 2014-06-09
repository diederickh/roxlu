import os
import config
from base import *

class LibNice(Base):
    def __init__(self):
        self.name = "libnice"
        self.version = "0.1.5"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["glib"]
        self.info = "libnice"

    def download(self): 
        rb_download_and_extract(self, 
                               "http://nice.freedesktop.org/releases/libnice-" +self.version +".tar.gz",
                                "libnice-" +self.version +".tar.gz", 
                                "libnice-" +self.version)
        return True

    def build(self):
        if rb_is_mac():
            rb_build_with_autotools(self);
        return False

    def is_build(self):
        if rb_is_mac():
            return rb_deploy_lib_file_exists("libre.a")
        return False

    def deploy(self):
        return True
        if rb_is_mac():
            rb_deploy_lib(rb_get_download_file(self, "libre.a"))
        rb_deploy_headers(dir = rb_get_download_dir(self) +"include/")
        return True
        
