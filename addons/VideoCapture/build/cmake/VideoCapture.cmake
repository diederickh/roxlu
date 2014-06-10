roxlu_addon_begin("videocapture")

  # --------------------------------------------------------------------------------------
  roxlu_addon_add_source_file(videocapture/VideoCapture.cpp)
  roxlu_addon_add_source_file(videocapture/VideoCaptureBase.cpp)
  roxlu_addon_add_source_file(videocapture/Utils.cpp)
  roxlu_addon_add_source_file(videocapture/Types.cpp)

  if(APPLE) 
     roxlu_addon_add_source_file(videocapture/mac/VideoCaptureAVFoundation.mm)
     roxlu_addon_add_source_file(videocapture/mac/VideoCaptureMac.cpp)

     find_library(fr_core_foundation CoreFoundation)
     find_library(fr_cocoa Cocoa)
     find_library(fr_avfoundation AVFoundation)
     find_library(fr_core_video CoreVideo)
     find_library(fr_core_media CoreMedia)
     find_library(fr_core_media_io CoreMediaIO)
     
     roxlu_add_library(${fr_core_foundation})
     roxlu_add_library(${fr_cocoa})
     roxlu_add_library(${fr_avfoundation})
     roxlu_add_library(${fr_core_video})
     roxlu_add_library(${fr_core_media})
     roxlu_add_library(${fr_core_media_io})
  endif(APPLE)

  if(UNIX AND NOT APPLE)
    roxlu_add_extern_include_dir(videocapture/linux/)
    roxlu_addon_add_source_file(videocapture/linux/v4l2/VideoCaptureV4L2.cpp)
    roxlu_addon_add_source_file(videocapture/linux/v4l2/VideoCaptureV4L2Types.cpp)
    roxlu_addon_add_source_file(videocapture/linux/v4l2/VideoCaptureV4L2Utils.cpp) 

    roxlu_add_library(udev)
    add_definitions(-D__STDC_CONSTANT_MACROS)

  endif(UNIX AND NOT APPLE)


  if(WIN32) 
    find_package(WindowsSDK REQUIRED)
    file(TO_CMAKE_PATH ${WINDOWSSDK_PREFERRED_DIR} windows_sdk_dir)
    file(TO_CMAKE_PATH ${WINDOWSSDK_LATEST_DIR} windows_sdk_dir)
  
    roxlu_add_include_dir(${windows_sdk_dir}/Include)
    roxlu_add_library(${windows_sdk_dir}/Samples/multimedia/directshow/baseclasses/Release/strmbase.lib)

   roxlu_addon_add_source_file(videocapture/win/directshow/VideoCaptureDirectShow.cpp)
   roxlu_addon_add_source_file(videocapture/win/directshow/VideoCaptureDirectShowCB.cpp)
   roxlu_addon_add_source_file(videocapture/win/mediafoundation/VideoCaptureMediaFoundation.cpp)
   roxlu_addon_add_source_file(videocapture/win/mediafoundation/VideoCaptureMediaFoundationCB.cpp)
   roxlu_add_library(strmiids.lib)

  endif()

  # --------------------------------------------------------------------------------------

roxlu_addon_end()
