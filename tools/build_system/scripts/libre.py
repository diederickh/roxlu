import os
import config
from base import *

class LibRE(Base):
    def __init__(self):
        self.name = "libre"
        self.version = "0.4.7"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "only compiled on mac - rtp/rtsp/stun/ice lib"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://www.creytiv.com/pub/re-" +self.version +".tar.gz",
                                "re-" +self.version +".tar.gz", 
                                "re-" +self.version)
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
        if rb_is_mac():
            rb_deploy_lib(rb_get_download_file(self, "libre.a"))
        rb_deploy_headers(dir = rb_get_download_dir(self) +"include/")
        return True
        
