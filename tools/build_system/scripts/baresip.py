import os
import config
from base import *

class Baresip(Base):
    def __init__(self):
        self.name = "baresip"
        self.version = "0.4.10"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["libre"]
        self.info = "only compiled on mac - baresip lib"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://www.creytiv.com/pub/baresip-" +self.version +".tar.gz",
                                "baresip-" +self.version +".tar.gz", 
                                "baresip-" +self.version)
        return True

    def build(self):
        if rb_is_mac():
            vars = rb_get_autotools_environment_vars()            
            dd = rb_get_download_dir() 
            dpd = rb_deploy_get_dir()
            cmd = (
                "export LIBRE_MK=\"" +dd +"libre/mk/re.mk" +"\"",
                "export CFLAGS=-I\"" +rb_deploy_get_include_dir() +"\"",
                "cd " +rb_get_download_dir(self),
                "make"
            )
            rb_execute_shell_commands(self, cmd, vars)

            """
            vars = { 
                "LIBRE_MK" : "\"" +dd +"libre/mk/re.mk" +"\"",
                "LIBRE_INC" : "\"
            } 
            vars["LIBRE_MK"] = "\"" +dd +"libre/mk/re.mk" +"\""
            vars["LIBRE_INC"] = "\"" +rb_deploy_get_include_dir() +"\""
            #rb_build_with_autotools(self, None, True, vars);
            """
        return False

    def is_build(self):
        return True
        if rb_is_mac():
            return rb_install_lib_file_exists("libre.a")
        return False

    def deploy(self):
        return True
        if rb_is_mac():
            rb_deploy_lib(rb_get_download_file(self, "libre.a"))
        rb_deploy_headers(dir = rb_get_download_dir(self) +"include/")
        return True
        
