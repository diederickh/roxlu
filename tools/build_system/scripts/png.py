import os
import config
from base import *

class PNG(Base):
    def __init__(self):
        self.name = "png"
        self.version = "1.6.3"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_WIN_MSVC2010, config.COMPILER_WIN_MSVC2012]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["zlib"]
        self.info = "The mac build is not using our own custom zlib! "

    def download(self): 
        rb_download_and_extract(self, 
                                "http://prdownloads.sourceforge.net/libpng/libpng-" +self.version +".tar.gz?download",
                                "libpng-" +self.version +".tar.gz", 
                                "libpng-" +self.version)
    def build(self):
        if rb_is_unix():
      
            ef = ("--with-zlib-prefix=" +rb_install_get_dir(),
                  "--with-sysroot=" +rb_install_get_dir())

            dd = rb_get_download_dir(self)

            cmd = (
                "cd " +dd,
                "./configure "+ rb_get_configure_prefix_flag(),
                "make clean && make && make install"
                )

            rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())

            # something goes wrong with zlib version; the detected version is old/wrong
            #rb_build_with_autotools(self, " ".join(ef))

        elif rb_is_msvc():
            debug_flag = "d" if rb_is_debug() else ""
            opts = [ 
                "-DZLIB_LIBRARY=" +rb_deploy_get_lib_file("zlib" +debug_flag +".lib"),
                "-DZLIB_INCLUDE_DIR=" +rb_deploy_get_include_dir()
                ]
            rb_cmake_configure(self, opts)
            rb_cmake_build(self)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libpng.a")
        elif rb_is_win():
            rb_red_ln("WE NEED TO ADD THE IS_BUILD FOR PNG ON WINDOWS!")
        return False

    def deploy(self):
        if rb_is_msvc():
            # the dll debug lib crashes on windows, use the static ones
            debug_flag = "d" if rb_is_debug() else ""
            rb_deploy_lib(rb_install_get_lib_file("libpng16" +debug_flag +".lib"))
            rb_deploy_lib(rb_install_get_lib_file("libpng16_static" +debug_flag +".lib"))
            rb_deploy_dll(rb_install_get_bin_file("libpng16" +debug_flag +".dll"))
            rb_deploy_header(rb_install_get_include_file("png.h"))
            rb_deploy_header(rb_install_get_include_file("pngconf.h"))
            rb_deploy_header(rb_install_get_include_file("pnglibconf.h"))
        elif rb_is_mac():
            id = rb_install_get_dir()
            rb_deploy_lib(rb_install_get_lib_file("libpng16.a"))
            rb_deploy_lib(rb_install_get_lib_file("libpng16.16.dylib"))
            rb_deploy_lib(rb_install_get_lib_file("libpng.dylib"))
            rb_deploy_lib(rb_install_get_lib_file("libpng.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libpng16")
            rb_deploy_headers(rb_install_get_include_dir(), ["png.h", "pngconf.h", "pnglibconf.h"])
        elif rb_is_unix():
            id = rb_install_get_dir()
            rb_deploy_lib(rb_install_get_lib_file("libpng16.a"))
            rb_deploy_lib(rb_install_get_lib_file("libpng.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libpng16")
            rb_deploy_headers(rb_install_get_include_dir(), ["png.h", "pngconf.h", "pnglibconf.h"])


            
            
            
        
