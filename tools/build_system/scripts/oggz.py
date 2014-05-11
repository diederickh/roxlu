import os
import config
from base import *

class Oggz(Base):
    def __init__(self):
        self.name = "oggz"
        self.version = "git"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "Testing with oggz"

    def download(self): 
        rb_git_clone(self, "https://git.xiph.org/liboggz.git")
        cmd = (
            "cd " +rb_get_download_dir(self),
            "./autogen.sh"
        )

        rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())

        return True

    def build(self):
        rb_build_with_autotools(self)
        
        return True
        env = { "SDL_CFLAGS" : "-I" +rb_install_get_dir() +"/include/SDL2/" }         
        rb_build_with_autotools(self, environmentVars = env)
        return False

    def is_build(self):
        return True
        if rb_is_unix():
            return rb_deploy_lib_file_exists("libSDL2.a")
        return False

    def deploy(self):
        """
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libSDL2.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"SDL2")
        """
        return True
        
