import os
import config
from base import *

class Webm(Base):

    def __init__(self):
        self.name = "libwebm"
        self.version = "git"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "libwebm"

    def download(self): 
        rb_git_clone(self, "https://chromium.googlesource.com/webm/libwebm")
        return True

    def build(self):
        rb_build_with_autotools(self)
        return False

    def is_build(self):
        if rb_is_unix():
            return rb_deploy_lib_file_exists("libshout.a")
        return False

    def deploy(self):
        #rb_deploy_header(rb_install_get_include_file("zconf.h"))    
        rb_deploy_header(rb_download_get_file(self, "mkvmuxer.hpp"))
        rb_deploy_header(rb_download_get_file(self, "mkvmuxertypes.hpp"))
        rb_deploy_header(rb_download_get_file(self, "mkvmuxerutil.hpp"))
        rb_deploy_header(rb_download_get_file(self, "mkvparser.hpp"))
        rb_deploy_header(rb_download_get_file(self, "mkvreader.hpp"))
        rb_deploy_header(rb_download_get_file(self, "mkvwriter.hpp"))
        rb_deploy_header(rb_download_get_file(self, "webmids.hpp"))

        if rb_is_unix():
            rb_deploy_lib(rb_download_get_file(self, "libwebm.a"))


            
        return True
        
