import os
import config
from base import *

class Tpl(Base):
    
    def __init__(self):
        self.name = "tpl"
        self.version = "git"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG, config.COMPILER_WIN_MSVC2010, config.COMPILER_UNIX_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.info = "C based serialization"

    def download(self):
        rb_git_clone(self, "https://github.com/troydhanson/tpl.git", self.version)

    def build(self):
        rb_copy_to_download_dir(self, "CMakeLists.txt")
        rb_cmake_configure(self)
        rb_cmake_build(self)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libnanomsg.a")
        elif rb_is_win():
            return rb_deploy_lib_file_exists("nanomsg.lib")
        else:
            rb_red_ln("@todo nanomsg")

    def deploy(self):
        rb_deploy_lib(rb_install_get_lib_file("libtpl.a"))
        rb_deploy_header(rb_install_get_include_file("tpl.h"))




                
            



