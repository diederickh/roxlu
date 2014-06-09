#ifndef ROXLU_OPENGL_HEADERS_H
#define ROXLU_OPENGL_HEADERS_H

#if defined(__APPLE__)
#  undef GLFW_INCLUDE_GLCOREARB
#  define GLFW_INCLUDE_NONE
#  define GLFW_INCLUDE_GLCOREARB
#  include <GLFW/glfw3.h>
#endif

#endif
