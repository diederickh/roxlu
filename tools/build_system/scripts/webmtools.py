import os
import config
from base import *

class WebmTools(Base):

    def __init__(self):
        self.name = "webmtools"
        self.version = "git"
        self.compilers = [config.COMPILER_MAC_GCC]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "webmtools"

    def download(self): 
        rb_git_clone(self, "http://git.chromium.org/webm/webm-tools.git")
        return True

    def build(self):
        rb_copy_to_download_dir(self, "CMakeLists.txt")
        rb_cmake_configure(self)
        rb_cmake_build(self)
        return False

    def is_build(self):
        if rb_is_unix():
            return rb_deploy_lib_file_exists("libwebmtools.a")
        return False

    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libwebmtools.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"webmtools")
            
        return True
        
