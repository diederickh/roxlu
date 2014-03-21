# Build example: python rbs.py -c clang -b release -a 64 -t build -s ssl
import os
import sys, getopt
sys.path.append("./libs/")
sys.path.append("./scripts/")

import config

from scripts.base import *
from scripts.glfw import GLFW
from scripts.jansson import Jansson
from scripts.jpeg import JPEG
from scripts.tiff import Tiff
from scripts.png import PNG
from scripts.zlib import ZLib
from scripts.openssl import OpenSSL
from scripts.lamemp3 import LameMP3
from scripts.yasm import Yasm
from scripts.uv import UV
from scripts.curl import Curl
from scripts.pcre import PCRE
from scripts.ogg import Ogg
from scripts.vorbis import Vorbis
from scripts.theora import Theora
from scripts.speex import Speex
from scripts.mysql_c_connector import MySQLCConnector
from scripts.freetype import FreeType
from scripts.autoconf import AutoConf
from scripts.automake import AutoMake
from scripts.libtool import LibTool
from scripts.x264 import x264
from scripts.glew import Glew
from scripts.portaudio import PortAudio
from scripts.sndfile import SndFile
from scripts.pkgconfig import PkgConfig
from scripts.glib import Glib
from scripts.ffi import FFI
from scripts.gettext import GetText
from scripts.iconv import Iconv
from scripts.flac import Flac
from scripts.boost import Boost
from scripts.torrent import Torrent
from scripts.rtmp import Rtmp
from scripts.flvmeta import FLVMeta 
from scripts.h264bitstream import H264BitStream
from scripts.pixman import Pixman
from scripts.cairo import Cairo
from scripts.pango import Pango
from scripts.plplot import PLplot
from scripts.gnuplot import GnuPlot
from scripts.samplerate import Samplerate
from scripts.nanomsg import Nanomsg
from scripts.rapidxml import RapidXML
from scripts.libyuv import LibYUV
from scripts.glxw import GLXW
from scripts.faac import Faac
from scripts.libav import LibAV
from scripts.websockets import Websockets
from scripts.libharu import LibHaru
from scripts.anttweakbar import AntTweakbar # not finished yet
from scripts.libusb import LibUSB
from scripts.freenect import Freenect
from scripts.opencv import OpenCV
from scripts.mpg123 import MPG123
from scripts.ao import AO
from scripts.poly2tri import Poly2Tri
from scripts.cgal import CGal
from scripts.gmp import GMP
from scripts.mpfr import MPFR
from scripts.openni2 import OpenNI2
from scripts.poppler import Poppler
from scripts.fontconfig import FontConfig
from scripts.fftw import FFTW
from scripts.rtaudio import RTAudio
from scripts.ccv import CCV
from scripts.cubeb import Cubeb
from scripts.libre import LibRE
from scripts.roxlu import Roxlu 

from colorama import init, Fore, Back, Style
init()

TASK_LIST = 1
TASK_BUILD = 2
TASK_DOWNLOAD = 3

config.base_dir = os.path.dirname(os.path.realpath(__file__)) +"/"
config.download_dir = "./downloads"
config.script_dir = "./scripts"
config.tools_dir = "./tools"
config.compiler = config.COMPILER_MAC_CLANG
config.arch = config.ARCH_M32
config.install_prefix = config.base_dir +"build"
config.deploy_prefix = config.base_dir +"../../extern/"
config.build_type  = config.BUILD_TYPE_RELEASE

ins_glfw = GLFW()
ins_jansson = Jansson()
ins_jpeg = JPEG()
ins_tiff = Tiff()
ins_png = PNG()
ins_zlib = ZLib()
ins_openssl = OpenSSL()
ins_lamemp3 = LameMP3()
ins_yasm = Yasm()
ins_uv = UV()
ins_curl = Curl()
ins_pcre = PCRE()
ins_ogg = Ogg()
ins_vorbis = Vorbis()
ins_theora = Theora()
ins_speex = Speex()
ins_mysqlc = MySQLCConnector()
ins_freetype = FreeType()
ins_autoconf = AutoConf()
ins_automake = AutoMake()
ins_libtool = LibTool()
ins_x264 = x264()
ins_glew = Glew()
ins_portaudio = PortAudio()
ins_sndfile = SndFile()
ins_pkgconfig = PkgConfig()
ins_glib = Glib()
ins_ffi = FFI()
ins_gettext = GetText()
ins_iconv = Iconv()
ins_flac = Flac()
ins_boost = Boost()
ins_torrent = Torrent()
ins_rtmp = Rtmp()
ins_flvmeta = FLVMeta()
ins_h264bitstream = H264BitStream()
ins_pixman = Pixman()
ins_cairo = Cairo()
ins_plplot = PLplot()
ins_gnuplot = GnuPlot()
ins_pango = Pango()
ins_samplerate = Samplerate()
ins_nanomsg = Nanomsg()
ins_rapidxml = RapidXML()
ins_libyuv = LibYUV()
ins_glxw = GLXW()
ins_faac = Faac()
ins_libav = LibAV()
ins_websockets = Websockets()
ins_libharu = LibHaru()
ins_anttweakbar = AntTweakbar()
ins_libusb = LibUSB()
ins_freenect = Freenect()
ins_opencv = OpenCV()
ins_mpg123 = MPG123()
ins_ao = AO()
ins_poly2tri = Poly2Tri()
ins_cgal = CGal()
ins_gmp = GMP()
ins_mpfr = MPFR()
ins_openni2 = OpenNI2()
ins_poppler = Poppler()
ins_fontconfig = FontConfig()
ins_fftw = FFTW()
ins_rtaudio = RTAudio()
ins_ccv = CCV()
ins_cubeb = Cubeb()
ins_libre = LibRE()
ins_roxlu = Roxlu()

installers = [ins_glfw, ins_jansson, ins_jpeg, ins_tiff, ins_png, ins_zlib, 
              ins_openssl, ins_lamemp3, ins_yasm, ins_uv, ins_curl, ins_pcre,
              ins_ogg, ins_vorbis, ins_theora, ins_speex, ins_mysqlc,
              ins_freetype, ins_autoconf, ins_automake, ins_libtool, ins_x264,
              ins_glew, ins_portaudio, ins_sndfile, ins_pkgconfig, ins_glib, ins_ffi,
              ins_gettext, ins_iconv, ins_flac, ins_boost, ins_torrent, ins_rtmp,
              ins_flvmeta, ins_h264bitstream, ins_pixman, ins_cairo, ins_plplot,
              ins_pango, ins_gnuplot, ins_samplerate, ins_nanomsg, ins_rapidxml,
              ins_libyuv, ins_glxw, ins_faac, ins_libav, ins_websockets,
              ins_libharu, ins_anttweakbar, ins_libusb, ins_freenect, ins_opencv,
              ins_mpg123, ins_ao, ins_poly2tri, ins_cgal, ins_gmp, ins_mpfr,
              ins_openni2, ins_poppler, ins_fontconfig, ins_fftw, ins_rtaudio, ins_ccv,
              ins_cubeb, ins_libre,
              ins_roxlu]


#installers.sort(key=lambda i:i.name)

if rb_is_win():
    os.environ["PATH"] = os.environ["PATH"] +";" +config.base_dir +"tools\\curl\\";


# State vars; get set by getopt
installer = None
task = None             # what task do you want to perform

# On windows systems we need to check if perl and nasm have been installed
rb_check_windows_setup()
#sys.exit(2)


# Getopts
try:
    opts,args = getopt.getopt(sys.argv[1:], "a:s:t:c:b:", ["arch=", "script=", "task=", "compiler=","build_type="])
except getopt.GetoptError:
    rb_print_usage()
    sys.exit(2)

# Handle arguments
found_installers = []

for opt, arg in opts:
    if opt in ("-a", "--arch"):
        if arg == "32":
            config.arch = config.ARCH_M32
        elif arg == "64":
            config.arch = config.ARCH_M64
    elif opt in ("-s", "--script"):
        provided_scripts = arg.split(",")
        #rb_yellow_ln(provided_scripts)
        for ins in installers:
            for asked_installer in provided_scripts:
                if ins.name == asked_installer:
                    found_installers.append(ins)
        """
        print found_installers
        sys.exit(2)
        for ins in installers:
            if ins.name == arg:
                installer = ins
        """
    elif opt in ("-t", "--task"):
        if arg == "list":
            task = TASK_LIST
        elif arg == "build":
            task = TASK_BUILD
        elif arg == "download":
            task = TASK_DOWNLOAD
        else:
            #print "Unknown task: " +opt
            rb_yellow_ln("Unknown task.")
            sys.exit(2)
    elif opt in ("-b", "--build_type"):
        if arg == "release":
            config.build_type = config.BUILD_TYPE_RELEASE
        elif arg == "debug":
            config.build_type = config.BUILD_TYPE_DEBUG
        else:
            rb_red("Unknown build type " +arg +"\n")

    elif opt in ("-c", "--compiler"):
        if arg == "vs2010":
            config.compiler = config.COMPILER_WIN_MSVC2010
        elif arg == "vs2012":
            config.compiler = config.COMPILER_WIN_MSVC2012
        elif arg == "gcc":
            if rb_is_mac():
                config.compiler = config.COMPILER_MAC_GCC
            elif rb_is_unix():
                config.compiler = config.COMPILER_UNIX_GCC
        elif arg == "clang":
            if rb_is_mac():
                config.compiler = config.COMPILER_MAC_CLANG
            elif rb_is_unix():
                config.compiler = config.COMPILER_UNIX_CLANG
        else:
            rb_red("No compiler found.\n")
            sys.exit(2)

if task == None:
    rb_print_usage()
    sys.exit(2)

if task == TASK_BUILD:
    if len(found_installers) == 0:
        rb_yellow_ln("No installers found")
        sys.exit(2)

    """
    if not installer:
        print "No installer found"
        sys.exit(2)
    """

    for i in found_installers:
        rs = []
        rb_solve_dependencies(i, installers, rs)
        rs = rs[::-1]
        for r in rs:
            if not r.is_build():
                rb_red_ln("Found dependency: "+r.name)
                r.download()
                r.build()
                r.deploy()

        rb_yellow_ln("build: " +i.name)
        i.download()
        i.build()
        i.deploy()

    # build dependencies
    """
    rs = []
    rb_solve_dependencies(installer, installers, rs)
    rs = rs[::-1]
    for r in rs:
        if not r.is_build():
            rb_red_ln("Found dependency: "+r.name)
            r.build()
            r.deploy()
    """
    """
    rb_yellow_ln("build: " +installer.name)
    installer.build()
    installer.deploy()
    """

elif task == TASK_LIST:
    for ins in installers:
        rb_print_script_info(ins)

         #print Fore.RED +ins.name +" - " +ins.version;
elif task == TASK_DOWNLOAD:
    for ins in installers:
        rb_yellow_ln("download: " +ins.name)
        ins.download()



"""
for ins in installers:
    print ins.version


def rbs_download(installers):
    for ins in installers:
        ins.download()

def rbs_build(installers):
    for ins in installers:
        ins.build()

# rbs_download(installers)
rbs_build([ins_glfw])
"""

"""
class aap:
    name ="tester"

a = aap()

x = scripts.glfw()
#__import__("scripts.glfw")
scripts = os.listdir("./scripts")
for d in scripts:
    script_dir = "./" +d +"/" +d +".py"
    print script_dir
    #imp.load_source(d, script_dir)




#for dirname, dirnames, filenames in os.walk("./scripts"):
#    print dirname


"""
