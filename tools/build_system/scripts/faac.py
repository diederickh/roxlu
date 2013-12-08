import os
import config
from base import *

class Faac(Base):
    
    def __init__(self):
        self.name = "faac"
        self.version = "1.28"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = ""

    def download(self):
        rb_download_and_extract(self, 
                                "http://downloads.sourceforge.net/faac/faac-" +self.version +".tar.gz",
                                "faac-" +self.version +".tar.gz",
                                "faac-" +self.version)


    def build(self):
        if rb_is_mac():
            rb_build_with_autotools(self)
        elif rb_is_linux():
            # on linux we got an error when we use the autotools, the below command seems to work
            cmd = (
                "cd " +rb_get_download_dir(self),
                "./configure " +rb_get_configure_prefix_flag() +" CC=gcc CFLAGS=-O2 ",
                "make ",
                "make install"
            )
            rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())
        else:
            rb_yellow_ln("@todo build faac on !unix")

    def is_build(self):
        return True

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libfaac.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"/faac.h");
            rb_deploy_headers(dir = rb_install_get_include_dir() +"/faaccfg.h");
        else:
            rb_yellow_ln("@todo deploy faac on !unix")
        return True


                
            



