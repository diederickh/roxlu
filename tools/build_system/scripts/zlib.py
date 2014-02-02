import os
import config
from base import *

class ZLib(Base):
    def __init__(self):
        self.name = "zlib"
        self.version = "1.2.8"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_WIN_MSVC2010, config.COMPILER_WIN_MSVC2012, config.COMPILER_UNIX_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "Check if vs2010 and vs2012 is used for the correct builds"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://zlib.net/zlib-" +self.version +".tar.gz",
                                "zlib-" +self.version +".tar.gz", 
                                "zlib-" +self.version)
    def build(self):
        if rb_is_mac():
            if rb_is_32bit():
                cmd = ("cd " +rb_get_download_dir(self),
                       "./configure --prefix='" +rb_install_get_dir() +"' --archs='-arch i386'",
                       "make clean && make V=1 && make install")
                os.system(" && ".join(cmd))
            elif rb_is_64bit():
                cmd = ("cd " +rb_get_download_dir(self),
                       "./configure --prefix='" +rb_install_get_dir() +"' --archs='-arch x86_64'",
                       "make clean && make V=1 && make install")
                os.system(" && ".join(cmd))
        elif rb_is_linux():
            cmd = (
                "cd " +rb_get_download_dir(self),
                "./configure -prefix=\"" +rb_install_get_dir() +"\"",
                "make clean",
                "make V=1",
                "make install"
                )
            rb_execute_shell_commands(self, cmd)
        elif rb_is_msvc():
            rb_cmake_configure(self)
            rb_cmake_build(self)

    def is_build(slef):
        if rb_is_unix():
            return rb_install_lib_file_exists("libz.a")
        elif rb_is_win():
            return rb_deploy_lib_file_exists("zdll.lib")
        else:
            rb_red_ln("Cannot check if the lib is build on this platform")

    def deploy(self):

        if rb_is_msvc():
            debug_flag = "d" if rb_is_debug() else ""
            rb_deploy_lib(rb_install_get_lib_file("zlib" +debug_flag +".lib"))
            rb_deploy_dll(rb_install_get_bin_file("zlib" +debug_flag +".dll"))
            rb_deploy_header(rb_install_get_include_file("zconf.h"))
            rb_deploy_header(rb_install_get_include_file("zlib.h"))
        else:
            rb_deploy_lib(rb_install_get_lib_file("libz.a"))
            rb_deploy_header(rb_install_get_include_file("zlib.h"))
            rb_deploy_header(rb_install_get_include_file("zconf.h"))

        

    

        
