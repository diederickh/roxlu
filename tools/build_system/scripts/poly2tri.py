import os
import config
from base import *

class Poly2Tri(Base):
    
    def __init__(self):
        self.name = "poly2tri"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = ""

    def download(self):
        rb_hg_clone(self, "https://code.google.com/p/poly2tri/")

    def build(self):

        if rb_is_unix():
            cmd = ("cd " +rb_get_download_dir(self),
                   "./waf configure",
                   "./waf build"
                )
            env = rb_get_autotools_environment_vars()
            rb_execute_shell_commands(self, cmd, env)
        else:
            rb_red_ln("@todo poly2tri")
        return True

    def is_build(self):
        rb_red_ln("@todo poly2tri")
        return True

    def deploy(self):
        rb_red_ln("@todo deploy poly2tri")
        return True


                
            



