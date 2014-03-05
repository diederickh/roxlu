import os
import config
from base import *

class LibAV(Base):
    
    def __init__(self):
        self.name = "libav"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["yasm"]
        self.info = ""

    def download(self):
        rb_git_clone(self, "git://git.libav.org/libav.git")

    def build(self):
        if rb_is_mac():
            dd = rb_get_download_dir(self)
            env = rb_get_autotools_environment_vars()
            
            cmd = (
                "cd " +dd,
                "./configure --enable-static \
                             --enable-gpl \
                             --enable-libx264 \
                             --enable-nonfree" \
                +rb_get_configure_flags(), 
                "make clean",
                "make",
                "make install"
            )
        
            rb_execute_shell_commands(self, cmd, env)
        else:
            rb_yellow_ln("@todo need to implement libav building on !mac")
        return True

    def is_build(self):
        return True

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libavcodec.a"))
            rb_deploy_lib(rb_install_get_lib_file("libavfilter.a"))
            rb_deploy_lib(rb_install_get_lib_file("libavformat.a"))
            rb_deploy_lib(rb_install_get_lib_file("libavdevice.a"))
            rb_deploy_lib(rb_install_get_lib_file("libavformat.a"))
            rb_deploy_lib(rb_install_get_lib_file("libavutil.a"))
            rb_deploy_lib(rb_install_get_lib_file("libswscale.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libavcodec")
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libavdevice")
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libavformat")
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libavresample")
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libavutil")
            rb_deploy_headers(dir = rb_install_get_include_dir() +"libswscale")
        else:
            rb_yellow_ln("@todo deploy faac on !unix")
        return True


                
            



