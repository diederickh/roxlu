import os
import config
from base import *

class MPG123(Base):
    
    def __init__(self):
        self.name = "mpg123"
        self.version = "1.17.0"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = ""

    def download(self):
        rb_download_and_extract(self, 
                                "https://sourceforge.net/projects/mpg123/files/mpg123/" +self.version +"/mpg123-" +self.version +".tar.bz2/download",
                                "mpg123-" +self.version +".tar.bz2", 
                                "mpg123-" +self.version)


    def build(self):
        if rb_is_unix():
            opts = ( "--enable-static=yes" )
            rb_build_with_autotools(self, opts)
        else:
            rb_red_ln("@todo build mpg123 on !unix")
        return True

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libmpg123.a")
        else:
            rb_red_ln("@todo mpg123 check if file exists on windows")
        return True

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libmpg123.a"))
            rb_deploy_header(rb_install_get_dir() +"include/mpg123.h")
        else:
            rb_red_ln("@todo deploy mpg123 on non-unix")
        return True


                
            



