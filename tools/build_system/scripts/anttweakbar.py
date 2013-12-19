# NOT FINISHED YET!
import os
import config
from base import *

class AntTweakbar(Base):
    
    def __init__(self):
        self.name = "anttweakbar"
        self.version = "116"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "NOT FINISHED YET"

    def download(self):
        #                                 "https://sourceforge.net/projects/anttweakbar/files/anttweakbar/116/AntTweakBar_" +self.version +".zip/download",
        rb_download_and_extract(self, 
                                "http://sourceforge.net/projects/anttweakbar/files/AntTweakBar_116.zip/download",
                                "AntTweakBar_" +self.version +".zip", 
                                "AntTweakBar")



    def build(self):
        if rb_is_mac():
            dd = rb_get_download_dir(self)
            cmd = (
                "cd "+dd,
                "cd src",
                "make -f Makefile.osx"
                )
            rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())
            #rb_build_with_autotools(self)

        return True

    def is_build(self):
        return True
        if rb_is_unix():
            return rb_install_lib_file_exists("libwebsockets.a")
        else:
            rb_red_ln("@todo websockets check if file exists on windows")
        return True

    def deploy(self):
        return True
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libwebsockets.a"))
            rb_deploy_header(rb_install_get_include_file("libwebsockets.h"))
        else:
            rb_red_ln("@todo deploy websockets on non-unix")
        return True


                
            



