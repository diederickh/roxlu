import os
import config
from base import *

class SDL(Base):
    def __init__(self):
        self.name = "sdl"
        self.version = "1.2.15"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "SDL - just a test on mac"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://www.libsdl.org/release/SDL-" +self.version +".tar.gz",
                                "SDL-" +self.version +".tar.gz",
                                "SDL-" +self.version)

        return True

    def build(self):
        rb_build_with_autotools(self)
        return False

    def is_build(self):
        if rb_is_unix():
            return rb_deploy_lib_file_exists("libSDL.a")
        return False

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libSDL.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"SDL")
        return True
        
