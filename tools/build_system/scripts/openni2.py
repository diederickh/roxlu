import os
import config
from base import *
import subprocess

class OpenNI2(Base):
    def __init__(self):
        self.name = "openni2"
        self.version = "2.2.0.33"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ['']
        self.info = "Experimental openni2"

    def download(self): 
        rb_git_clone(self, "https://github.com/OpenNI/OpenNI2.git")
        return True

    def build(self):
        if rb_is_unix():
            dd = rb_get_download_dir(self)
            lib_dirs = "LIB_DIRS=\"" +rb_install_get_lib_dir() +" " +dd +"ThirdParty/PSCommon/XnLib/Bin/X64-Release/\""
            """
            inc_dirs = "INC_DIRS=\"" +rb_install_get_include_dir() +" " \
                                     +dd +"ThirdParty/PSCommon/XnLib/Include/" \
                                     +dd +"Include/" \
                                     +"\""
            """
            inc_dirs = ""
            cmd = (
                "cd " +dd,
                #"make clean",
                "make ALLOW_WARNINGS=1 " +lib_dirs +" " +inc_dirs
                )
            rb_execute_shell_commands(self, cmd)
            #rb_build_with_autotools(self,"ALLOW_WARNINGS=1")

    def is_build(self):
        return True
        """
        if rb_is_unix():
            return rb_install_lib_file_exists("libmpfr.a")
        return False
        """

    def deploy(self):
        """
        if rb_is_mac(): 
            rb_deploy_lib(rb_install_get_lib_file("libmpfr.a"))
            rb_deploy_header(rb_install_get_include_file("mpfr.h"))
            rb_deploy_header(rb_install_get_include_file("mpf2mpfr.h"))
        """
        return True
        
