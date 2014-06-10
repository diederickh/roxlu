roxlu_addon_begin("opengl")
  # --------------------------------------------------------------------------------------
  roxlu_addon_add_source_file(opengl/Camera.cpp)
  roxlu_add_source_file(${extern_source_dir}/GLXW/glxw.c)

  if(UNIX)
    roxlu_add_extern_library(libglfw3.a)
    roxlu_add_source_file(${extern_source_dir}/GLXW/glxw.c)
  endif()

  if(APPLE)
    find_library(fr_corefoundation CoreFoundation)
    find_library(fr_cocoa Cocoa)
    find_library(fr_opengl OpenGL)
    find_library(fr_iokit IOKit)
    find_library(fr_corevideo CoreVideo )
    
    roxlu_add_library(${fr_corefoundation})
    roxlu_add_library(${fr_cocoa})
    roxlu_add_library(${fr_opengl})
    roxlu_add_library(${fr_iokit})
    roxlu_add_library(${fr_corevideo})
  endif()

  if(NOT APPLE AND UNIX)
    roxlu_add_library(GL)
    roxlu_add_library(X11)
    roxlu_add_library(Xxf86vm)
    roxlu_add_library(rt)
    roxlu_add_library(libXrandr.so)
    roxlu_add_library(pthread)
    roxlu_add_library(Xi)
    roxlu_add_library(dl)
  endif()
  # --------------------------------------------------------------------------------------
roxlu_addon_end()

