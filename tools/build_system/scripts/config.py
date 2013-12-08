import os
from sys import platform as _platform
from os.path import expanduser

COMPILER_WIN_MSVC2010 = 1
COMPILER_WIN_MSVC2012 = 2 
COMPILER_MAC_GCC  = 3
COMPILER_MAC_CLANG = 4
COMPILER_UNIX_GCC = 5
COMPILER_UNIX_CLANG = 6

BUILD_TYPE_DEBUG = 1
BUILD_TYPE_RELEASE = 2

ARCH_M32 = 1
ARCH_M64 = 2

base_dir = os.path.dirname(os.path.realpath(__file__)) +"/../"
download_dir = "./downloads"
script_dir = "./scripts"
tools_dir = "./tools"
compiler = COMPILER_MAC_CLANG
arch = ARCH_M32
install_prefix = base_dir +"build"
deploy_prefix = base_dir +"../../extern/"
build_type = BUILD_TYPE_RELEASE
