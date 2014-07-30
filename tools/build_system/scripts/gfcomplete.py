import os
import config
from base import *

class GFComplete(Base):
    
    def __init__(self):
        self.name = "gfcomplete"
        self.version = "git"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG, config.COMPILER_WIN_MSVC2010, config.COMPILER_UNIX_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = ""

    def download(self):
        rb_git_clone(self, "https://bitbucket.org/jimplank/gf-complete.git")

    def build(self):
        cmd = [
            "cd " +rb_get_download_dir(self),
            "./autogen.sh"
            ]

        env = rb_get_autotools_environment_vars()
        rb_execute_shell_commands(self, cmd, env)
        rb_build_with_autotools(self, "--disable-sse") # sadly this fails on Mac :( 

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libgf_complete.a")
        else:
            rb_red_line("@todo libgfcomplete is_build()")


    def deploy(self):
        #rb_deploy_lib(rb_download_get_file(self, "libopenh264.a"))
        
        rb_deploy_lib(rb_install_get_lib_file("libgf_complete.a"))
        rb_deploy_header(rb_install_get_include_file("gf_complete.h"))
        rb_deploy_header(rb_install_get_include_file("gf_general.h"))
        rb_deploy_header(rb_install_get_include_file("gf_method.h"))
        rb_deploy_header(rb_install_get_include_file("gf_rand.h"))




                
            



