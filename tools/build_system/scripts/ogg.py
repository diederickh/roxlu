import os
import config
from base import *

class Ogg(Base):

    def __init__(self):
        self.name = "ogg"
        self.version = "1.3.1"
        self.compilers = [config.COMPILER_WIN_MSVC2010, config.COMPILER_WIN_MSVC2012, config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "see how we use the helper functions for vs2010/vs2012 in vorbis.py"
        
    def download(self): 
        rb_download_and_extract(self, 
                                "http://downloads.xiph.org/releases/ogg/libogg-" +self.version +".tar.gz",
                                "libogg-" +self.version +".tar.gz", 
                                "libogg-" +self.version)
    def build(self):
        if rb_is_unix():
            rb_build_with_autotools(self);
        elif rb_is_win():
            rb_copy_to_download_dir(self, "CMakeLists.txt")
            rb_cmake_configure(self)
            rb_cmake_build(self)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libogg.a")
        elif rb_is_win():
            return rb_deploy_lib_file_exists("libogg_static.lib")

    def deploy(self):
        """
        if rb_is_msvc():
            sd = "VS2010" if rb_is_vs2010() else "VS2012"
            dd = rb_get_download_dir(self) +"win32/" +sd +"/Win32/" +rb_msvc_get_build_type_string() +"/"
            rb_deploy_dll(dd +"libogg.dll")
            rb_deploy_lib(dd +"libogg.lib")
            rb_deploy_headers(dir = rb_get_download_dir(self) +"/include/ogg", subdir =  "ogg")
        """
        if rb_is_win():
            rb_deploy_lib(rb_install_get_lib_file("libogg_static.lib"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"ogg", subdir = "ogg")
        elif rb_is_mac():
            rb_deploy_lib(rb_install_get_lib_file("libogg.a"))
            rb_deploy_lib(rb_install_get_lib_file("libogg.0.dylib"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"ogg", subdir = "ogg")
        elif rb_is_linux():
            rb_deploy_lib(rb_install_get_lib_file("libogg.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"ogg", subdir = "ogg")

                
        
