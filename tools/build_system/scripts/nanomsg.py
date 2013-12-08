import os
import config
from base import *

class Nanomsg(Base):
    
    def __init__(self):
        self.name = "nanomsg"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG, config.COMPILER_WIN_MSVC2010, config.COMPILER_UNIX_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        if rb_is_unix():
            self.dependencies = ["automake", "autoconf", "libtool"];
        else:
            self.dependencies = []

    def download(self):
        rb_git_clone(self, "https://github.com/nanomsg/nanomsg.git", self.version)

    def build(self):
        if rb_is_unix():
            if not rb_download_file_exists(self, "configure"):
                cmd = [
                    "cd " +rb_get_download_dir(self),
                    "./autogen.sh"
                    ]
                rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())

            rb_build_with_autotools(self)
        elif rb_is_win():
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

        if rb_is_mac():
            rb_deploy_lib(rb_install_get_lib_file("libnanomsg.0.dylib"))
            rb_deploy_lib(rb_install_get_lib_file("libnanomsg.dylib"))

        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libnanomsg.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"nanomsg") 
            
        if rb_is_win():
            rb_deploy_headers(dir = rb_install_get_include_dir() +"nanomsg", subdir = "nanomsg")
            rb_deploy_lib(rb_install_get_lib_file("nanomsg.lib"))
            rb_deploy_dll(rb_install_get_bin_file("nanomsg.dll"))





                
            



