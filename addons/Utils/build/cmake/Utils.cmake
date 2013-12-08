
roxlu_addon_begin("utils")
  # --------------------------------------------------------------------------------------
  roxlu_addon_add_source_file(utils/Utils.cpp)
  roxlu_addon_add_source_file(utils/Log.cpp)
  roxlu_addon_add_source_file(utils/RingBuffer.cpp)

  if(APPLE)
    roxlu_add_extern_library(libuv.a)
    find_library(fr_foundation CoreFoundation)
    find_library(fr_cs CoreServices)
    roxlu_add_library(${fr_foundation})
    roxlu_add_library(${fr_cs})
  endif()

  # --------------------------------------------------------------------------------------
roxlu_addon_end()

