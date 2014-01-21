import os
import config
from base import *

class OpenCV(Base):
    
    def __init__(self):
        self.name = "opencv"
        self.version = ""
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_MAC_CLANG]
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = []
        self.info = "NOT FINISHED YET"

    def download(self):
        rb_git_clone(self, "git@github.com:Itseez/opencv.git")

    def build(self):

        shared_libs = "0"
        if rb_is_win():
            shared_libs = "1"

        opts = ["-DBUILD_SHARED_LIBS=" +shared_libs,
                "-DBUILD_PACKAGE=0",
                "-DBUILD_PERF_TESTS=0",
                "-DBUILD_PNG=0",
                "-DBUILD_TBB=0",
                "-DBUILD_TESTS=0",
                "-DBUILD_TIFF=0",
                "-DBUILD_WITH_DEBUG_INFO=0",
                "-DBUILD_ZLIB=0",
                "-DBUILD_EXAMPLES=1",
                "-DBUILD_opencv_apps=0",
                "-DBUILD_opencv_bioinspired=0",
                "-DBUILD_opencv_calib3d=0",
                "-DBUILD_opencv_contrib=0",
                "-DBUILD_opencv_core=1",
                "-DBUILD_opencv_cuda=0",
                "-DBUILD_opencv_features2d=1",
                "-DBUILD_opencv_flann=0",
                "-DBUILD_opencv_highgui=0",
                "-DBUILD_opencv_imgproc=1",
                "-DBUILD_opencv_legacy=0",
                "-DBUILD_opencv_ml=0",
                "-DBUILD_opencv_nonfree=0",
                "-DBUILD_opencv_objdetect=1",
                "-DBUILD_opencv_ocl=1",
                "-DBUILD_opencv_optim=1",
                "-DBUILD_opencv_photo=0",
                "-DBUILD_opencv_python=0",
                "-DBUILD_opencv_shape=0",
                "-DBUILD_opencv_softcascade=0",
                "-DBUILD_opencv_stitching=0",
                "-DBUILD_opencv_video=1",
                "-DBUILD_opencv_videostab=0",
                "-DBUILD_opencv_world=0",
                "-DWITH_CUDA=0",
                "-DWITH_CUFFT=0",
                "-DWITH_EIGEN=0",
                "-DWITH_JPEG=0",
                "-DWITH_JASPER=0",
                "-DWITH_LIBV4L=0",
                "-DWITH_OPENCL=1",
                "-DWITH_OPENEXR=0",
                "-DWITH_PNG=0",
                "-DWITH_TIFF=0",
                "-DWITH_V4L=0",
                "-DWITH_WEBP=0"
        ]
        rb_cmake_configure(self, opts)
        rb_cmake_build(self)
        return True

    def is_build(self):
        if rb_is_unix():
            return False
        else:
            rb_red_ln("@todo opencv check if file exists on windows")
        return True


    def deploy(self):
        if rb_is_unix():
            rb_deploy_lib(rb_install_get_lib_file("libopencv_core.a"))
            #rb_deploy_lib(rb_install_get_lib_file("libopencv_ts.a"))
            rb_deploy_lib(rb_install_get_lib_file("libopencv_imgproc.a"))
            rb_deploy_lib(rb_install_get_lib_file("libopencv_video.a"))
            rb_deploy_headers(dir = rb_install_get_dir() +"include/opencv/", subdir = "opencv")
            rb_deploy_headers(dir = rb_install_get_dir() +"include/opencv2/", subdir = "opencv2")
        return True



                
            



