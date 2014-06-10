import os
import config
from base import *

class Websockets(Base):
    
    def __init__(self):
        self.name = "websockets"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["openssl"]
        self.info = ""

    def download(self):
        #rb_git_clone(self, "git://git.libwebsockets.org/libwebsockets"); # doesn't work; cannot find, looks like wrong dns configuratio
        rb_git_clone(self, "https://github.com/warmcat/libwebsockets")

    def build(self):
        if rb_is_win():
            # SSL build gives unresolved symbols
            debug_flag = "d" if rb_is_debug() else ""
            opts = [ "-DWITH_SSL=0",
                     "-DZLIB_LIBRARY=" +rb_deploy_get_lib_file("zlibstatic" +debug_flag +".lib"),
                     "-DZLIB_INCLUDE_DIR=" +rb_deploy_get_include_dir(),
                     "-DWITHOUT_TESTAPPS=1",
                     "-DUSE_EXTERNAL_ZLIB=1"
                 ]
            
        rb_cmake_configure(self, opts)
        rb_cmake_build(self)
        return True

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libwebsockets.a")
        else:
            rb_red_ln("@todo websockets check if file exists on windows")
        return True

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libwebsockets.a"))
            rb_deploy_header(rb_install_get_include_file("libwebsockets.h"))
        elif rb_is_win():
            rb_deploy_dll(rb_install_get_bin_file("websockets.dll"))
            rb_deploy_header(rb_install_get_include_file("libwebsockets.h"))
            rb_deploy_header(rb_install_get_include_file("websock-w32.h"))
            rb_deploy_header(rb_install_get_include_file("gettimeofday.h"))
            rb_deploy_lib(rb_install_get_lib_file("websockets.lib"))
            rb_deploy_lib(rb_install_get_lib_file("websockets_static.lib"))
        else:
            rb_red_ln("@todo deploy websockets on non-unix")
        return True


                
            



