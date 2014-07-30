import os
import config
from base import *

class Jerasure(Base):
    
    def __init__(self):
        self.name = "jerasure"
        self.version = "git"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG, config.COMPILER_WIN_MSVC2010, config.COMPILER_UNIX_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["gfcomplete"]
        self.info = ""

    def download(self):
        rb_git_clone(self, "https://bitbucket.org/jimplank/jerasure.git")

    def build(self):
        cmd = [
            "cd " +rb_get_download_dir(self),
            "autoreconf --force --install"
            ]
        env = rb_get_autotools_environment_vars()
        rb_execute_shell_commands(self, cmd, env)
        rb_build_with_autotools(self, "--enable-static") 

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("liJerasure.a")
        else:
            rb_red_line("@todo jerasure is_build()")

    def deploy(self):
        rb_deploy_lib(rb_install_get_lib_file("libJerasure.a"))
        rb_deploy_header(rb_install_get_include_file("jerasure.h"))
        rb_deploy_headers(dir = rb_install_get_include_dir() +"jerasure")





                
            



