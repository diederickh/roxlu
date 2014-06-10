# NOT FINISHED YET!
import os
import config
from base import *

class AntTweakbar(Base):
    
    def __init__(self):
        self.name = "anttweakbar"
        self.version = "b716e5cdaff0fadf62feac46104c6b1459e44133"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "AntTweakbar does not work on 10.9, we supply a patch"

    def download(self):
        downloaded = rb_download_dir_exists(self)
        rb_git_clone(self, "git://git.code.sf.net/p/anttweakbar/code", self.version)

        # Apply patch on mac (dlopen doesn't seem to work)
        if not downloaded and rb_is_mac():
            rb_copy_to_download_dir(self, "anttweakbar_macos_ldopen.patch")
            dd = rb_get_download_dir(self)
            cmd = (
                "cd "+dd,
                "git checkout -b fix",
                "git am -3 --ignore-whitespace anttweakbar_macos_ldopen.patch"
            )
            rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())


    def build(self):
        if rb_is_mac():
            dd = rb_get_download_dir(self)
            cmd = (
                "cd "+dd,
                "cd src",
                "make -f Makefile.osx"
                )
            rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())
        elif rb_is_linux():
            dd = rb_get_download_dir(self)
            cmd = (
                "cd "+dd,
                "cd src",
                "make"
                )
            rb_execute_shell_commands(self, cmd, rb_get_autotools_environment_vars())
        else: 
            rb_red_ln("@todo build anttweakbar on non-unix")

        return True

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libAntTweakBar.a")
        else:
            rb_red_ln("@todo anttweakbar check if file exists on windows")
        return True

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_get_download_dir(self) +"lib/libAntTweakBar.a")
            rb_deploy_header(rb_get_download_dir(self) +"include/AntTweakBar.h")
        else:
            rb_red_ln("@todo deploy anttweakbar on non-unix")
        return True


                
            



