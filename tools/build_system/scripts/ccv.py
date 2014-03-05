import os
import config
from base import *

class CCV(Base):
    def __init__(self):
        self.name = "ccv"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "only tested on mac - makefile seems buggy; had to add the -I/to/build/path in the make file"

    def download(self): 
        rb_git_clone(self, "https://github.com/liuliu/ccv.git");
        """
        rb_download_and_extract(self,
                                "http://www.music.mcgill.ca/~gary/rtaudio/release/rtaudio-" +self.version +".tar.gz",
                                "rtaudio-" +self.version +".tar.gz",
                                "rtaudio-" +self.version)
        """
        
        return True

    def build(self):
        dd = rb_get_download_dir(self)
        cmd = (
            "cd " +dd +"lib",
            "./configure " +rb_get_configure_prefix_flag() +rb_get_configure_options(),
            "make",
            "make install"
            )
        rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())
        """
        if rb_is_mac():
            rb_build_with_autotools(self);
        """
        return False

    def is_build(self):
        """
        if rb_is_mac():
            return rb_install_lib_file_exists("libfftw3.a")
        """
        return False

    def deploy(self):
        """
        if rb_is_mac():
            rb_deploy_lib(rb_install_get_lib_file("libfftw3.a"))
            rb_deploy_header(rb_install_get_include_file("fftw3.h"))
        """

        return True
        
