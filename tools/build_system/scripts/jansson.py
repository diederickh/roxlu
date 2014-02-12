import os
import config
from base import *
import subprocess

class Jansson(Base):
    def __init__(self):
        self.name = "jansson"
        self.version = "(latest git)"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_WIN_MSVC2012, config.COMPILER_WIN_MSVC2010]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []

    def download(self): 
        rb_git_clone(self, "https://github.com/akheron/jansson.git")

    def build(self):
        if rb_is_win():
            rb_cmake_configure(self)
            rb_cmake_build(self)
        else:
            rb_build_with_autotools(self)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libjansson.a")
        else:
            return rb_deploy_lib_file_exists("jansson.lib")

    def deploy(self):
        if rb_is_win():
            debug_flag = "_d" if rb_is_debug() else ""
            rb_deploy_lib(rb_install_get_lib_file("jansson" +debug_flag +".lib"))
            rb_deploy_header(rb_install_get_include_file("jansson.h"))
            rb_deploy_header(rb_install_get_include_file("jansson_config.h"))
        else:
            rb_deploy_lib(rb_install_get_lib_file("libjansson.a"))
            rb_deploy_lib(rb_install_get_lib_file("libjansson.4.dylib"))
            rb_deploy_lib(rb_install_get_lib_file("libjansson.dylib"))
            rb_deploy_header(rb_install_get_include_file("jansson.h"))
            rb_deploy_header(rb_install_get_include_file("jansson_config.h"))
        
