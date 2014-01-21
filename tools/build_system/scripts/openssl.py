import os
import sys
import config
from base import *

class OpenSSL(Base):

    def __init__(self):
        self.name = "openssl"
        self.version = "1.0.0l"
        self.compilers = [config.COMPILER_MAC_GCC, config.COMPILER_WIN_MSVC2010, config.COMPILER_WIN_MSVC2012, config.COMPILER_UNIX_GCC]        
        self.arch = [config.ARCH_M32, config.ARCH_M64]
        self.dependencies = ["zlib"]
        self.info = "Win 64bit is 'initial' and not implemented, release and debug builds are the same"

    def download(self): 
        rb_download_and_extract(self, 
                                "http://www.openssl.org/source/openssl-" +self.version +".tar.gz",
                                "openssl-" +self.version +".tar.gz", 
                                "openssl-" +self.version)
    def build(self):
        if rb_is_mac():
            # 32 / 64 bit
            platform = ""
            if rb_is_32bit():
                platform = "darwin-i386-cc"
            elif rb_is_64bit():
                platform = "darwin64-x86_64-cc"

            cmd = ( 
                "set -x && cd "+rb_get_download_dir(self),
                "./Configure --prefix=" +rb_install_get_dir() +" " +platform,
                "make clean",
                "make install",
            )

            os.system(" && ".join(cmd))

        elif rb_is_msvc():
            
            # @todo - try to use rb_msvc_setup_build_environment() which sets nasm + include (not the download dir include though)

            perl_version = subprocess.check_output(["perl", "--version"])
            if "activestate" not in perl_version.lower():
                rb_red_ln("You must install the ActiveState perl version")
                sys.exit()

            # perl / nasm
            rb_set_environment_vars()

            # includes
            dd = rb_get_download_dir(self)
            os.environ["INCLUDE"] += ";" +rb_deploy_get_include_dir() +";" +dd

            # compile commands
            cmd = (
                "cd " +dd,
                "call " +rb_msvc_get_setvars(),
                "perl Configure VC-WIN32 enable-camellia zlib-dynamic --openssldir=./ --prefix=" +rb_install_get_dir(),
                "nmake -f ms\\ntdll.mak",
                "ms\\do_nasm",
                "nmake -f ms\\ntdll.mak install"
            )
            
            rb_execute_shell_commands(self, cmd)
            rb_execute_shell_commands(self, cmd) # yes, we really need to execute these commands twice (something with env. variables I think)

        elif rb_is_linux():
            cmd = (
                "cd " +rb_get_download_dir(self), 
                "./Configure --prefix=" +rb_install_get_dir() +" linux-x86_64 ",
                "make clean",
                "make" #  update 2014.01.20, this time the install failed on the manual.. it did create a library file though.  we need install_sw because the manual install fail on arch linux
            )
            #env = {"CFLAGS":"-fPIC"}
            rb_execute_shell_commands(self, cmd)

    def is_build(self):
        if rb_is_unix():
            return rb_install_lib_file_exists("libssl.a")
        elif rb_is_win():
            return rb_deploy_lib_file_exists("libeay32.lib")
        else:
            rb_red_ln("Cannot check if the lib is build on this platform")

    def deploy(self):
        if rb_is_msvc():
            bd = rb_get_download_dir(self)
            bde = bd +"/out32dll/"
            rb_deploy_dll(bde +"ssleay32.dll")
            rb_deploy_dll(bde +"libeay32.dll")
            rb_deploy_lib(bde +"libeay32.lib")
            rb_deploy_lib(bde +"ssleay32.lib")
            rb_deploy_headers(dir = bd +"inc32/openssl/", subdir =  "openssl")
        elif rb_is_mac(): 
            rb_deploy_lib(rb_install_get_lib_file("libssl.a"))
            rb_deploy_lib(rb_install_get_lib_file("libcrypto.a"))
            rb_deploy_headers(dir = rb_install_get_include_dir() +"openssl")
        elif rb_is_linux():
            # The install script is buggy on linux
            dd = rb_get_download_dir(self)
            rb_deploy_lib(rb_download_get_file(self, "libssl.a"))
            rb_deploy_lib(rb_download_get_file(self, "libcrypto.a"))
            rb_deploy_headers(dir = dd +"/include/openssl")

        
