import os
import config
from base import *

class LibHaru(Base):
    
    def __init__(self):
        self.name = "libharu"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = [];
        self.info = ""

    def download(self):
        rb_git_clone(self, "https://github.com/libharu/libharu.git");

    def build(self):
        rb_cmake_configure(self)
        rb_cmake_build(self)
        return True

    def is_build(self):
        return True

    def deploy(self):
        return True
        """
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libwebsockets.a"))
            rb_deploy_header(rb_install_get_include_file("libwebsockets.h"))
        else:
            rb_red_ln("@todo deploy websockets on non-unix")
        return True
        """


                
            



