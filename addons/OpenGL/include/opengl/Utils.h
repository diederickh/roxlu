#ifndef ROXLU_OPENGL_UTILS_H
#define ROXLU_OPENGL_UTILS_H

#include <opengl/Error.h>
#include <opengl/GL.h>

// Creates a shader
inline GLuint rx_create_shader(GLenum type, const char* code) {
  GLuint shader = glCreateShader(type);
  glShaderSource(shader, 1, &code, NULL);
  glCompileShader(shader);
  eglGetShaderInfoLog(shader);
  return shader;
}

// Creates a GL program for the given vertex and fragment shader, does not link them!
inline GLuint rx_create_program(GLuint vert, GLuint frag) {
  GLuint prog = glCreateProgram();
  glAttachShader(prog, vert);
  glAttachShader(prog, frag);
  return prog;
}

// Sets some default texture parameters
inline void rx_set_texture_parameters() {
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
}
#endif
