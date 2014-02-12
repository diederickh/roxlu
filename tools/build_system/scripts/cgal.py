import os
import config
from base import *
import subprocess

class CGal(Base):
    def __init__(self):
        self.name = "cgal"
        self.version = "(tested with 4.3)"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_WIN_MSVC2012, config.COMPILER_WIN_MSVC2010]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["boost"]
        self.info = "You need to download the package yourself and extract it in downloads/cgal/"

    def download(self): 
        # Download manually from https://gforge.inria.fr/frs/?group_id=52&release_id=8307
        return True

    def build(self):
        opts = [ "-DBUILD_SHARED_LIBS=0" ] 
        rb_cmake_configure(self, opts)
        rb_cmake_build(self)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libCGAL_Core.a")
        else:
            return rb_deploy_lib_file_exists("jansson.lib")

    def deploy(self):
        if rb_is_mac(): 
            rb_deploy_lib(rb_install_get_lib_file("libCGAL_Core.a"))
            rb_deploy_lib(rb_install_get_lib_file("libCGAL_ImageIO.a"))
            rb_deploy_lib(rb_install_get_lib_file("libCGAL.a"))
            rb_deploy_headers(dir = rb_install_get_dir() +"include/CGAL/", subdir = "CGAL")
        return True
        
