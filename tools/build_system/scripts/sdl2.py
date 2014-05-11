import os
import config
from base import *

class SDL2(Base):
    def __init__(self):
        self.name = "sdl2"
        self.version = "2.0.3"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "SDL2 - just a test on mac"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://www.libsdl.org/release/SDL2-" +self.version +".tar.gz",
                                "SDL2-" +self.version +".tar.gz",
                                "SDL2-" +self.version)

        return True

    def build(self):
        rb_build_with_autotools(self)
        return False

    def is_build(self):
        if rb_is_unix():
            return rb_deploy_lib_file_exists("libSDL2.a")
        return False

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libSDL2.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"SDL2")
        return True
        
