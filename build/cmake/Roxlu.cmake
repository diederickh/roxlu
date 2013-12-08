cmake_minimum_required(VERSION 2.8)

# ------------------------------------------------------------------------------------
# R O X L U 
# ------------------------------------------------------------------------------------

# ${roxlu_base_dir}       - path to the 'root' of the roxlu repository
# ${roxlu_source_files}   - the .c/.cpp files of the core roxlu library
# ${roxlu_libraries}      - any dependencies that the core roxlu library needs
# ${roxlu_include_dirs}   - include dirs to the roxlu library and dependencies
# ${roxlu_source_dirs}    - if you want to copy sources on install (e.g. to package for OF, Cinder, Polycode etc..)
# ${roxlu_install_files}  - add these to the install command (FILES)
# ${roxlu_definitions}    - add these to the preprocessor definitions
#
# roxlu_add_library(filepath)        - add a library to the roxlu_libraries
# roxlu_add_extern_library(filename) - add a library which is found in the extern directory (for the current platform,compiler,architecture)
# roxlu_add_source_file(filepath)    - add a source file which must be compiled as part of the roxlu library
# roxlu_add_include_dir(path)        - add an include directory for the roxlu library

include(${CMAKE_CURRENT_LIST_DIR}/Triplet.cmake)

set(roxlu_base_dir   ${CMAKE_CURRENT_LIST_DIR}/../../)
#set(roxlu_source_dir ${CMAKE_CURRENT_LIST_DIR}/../../src/roxlu)

# set(roxlu_source_files
#   ${roxlu_source_dir}/core/Utils.cpp
#   ${roxlu_source_dir}/core/Log.cpp
#   ${roxlu_source_dir}/core/StringUtil.cpp
#   ${roxlu_source_dir}/io/Buffer.cpp
#   ${roxlu_source_dir}/io/RingBuffer.cpp
#   ${roxlu_source_dir}/io/File.cpp
#   ${roxlu_source_dir}/math/Quat.cpp
#   ${roxlu_source_dir}/math/Mat4.cpp
#   ${roxlu_source_dir}/math/Mat3.cpp
#   ${roxlu_source_dir}/math/Vec4.cpp
#   ${roxlu_source_dir}/math/Vec3.cpp
#   ${roxlu_source_dir}/math/Vec2.cpp
#   ${roxlu_source_dir}/math/Noise.cpp
#   ${roxlu_source_dir}/math/Perlin.cpp
# )
# 
# set(roxlu_source_dirs
#   ${roxlu_source_dir}/core
#   ${roxlu_source_dir}/io
#   ${roxlu_source_dir}/math
# )

set(roxlu_include_dirs 
  ${CMAKE_CURRENT_LIST_DIR}/../../include
  ${extern_include_dir}
)

macro(roxlu_add_library lib)
  list(APPEND roxlu_libraries ${lib})
endmacro()

macro(roxlu_add_extern_library lib)
  roxlu_add_library(${extern_lib_dir}/${lib})
endmacro()

macro(roxlu_add_source_file file)
  list(APPEND roxlu_source_files ${file})
endmacro()

macro(roxlu_add_include_dir dir)
  list(APPEND roxlu_include_dirs ${dir})
endmacro()

# ------------------------------------------------------------------------------------
# A D D O N S 
# ------------------------------------------------------------------------------------

# roxlu_add_addon(name)             - add an addon, e.g. roxlu_add_addon(SceneManager)
# roxlu_addon_begin(name)           - used by addons, see an addon for the usage. marks the start of an addon
# roxlu_addon_end()                 - after adding all addon related files (libraries, source files, include dirs etc..) call this
# roxlu_addon_add_source_file(file) - used by addons, adds a source file
 
macro(roxlu_add_addon name)
  include(${roxlu_base_dir}/addons/${name}/build/cmake/${name}.cmake)
endmacro()

macro(roxlu_addon_begin name)
  set(roxlu_addon_name ${name})
  set(roxlu_addon_include_dir ${CMAKE_CURRENT_LIST_DIR}/../../include/)
  set(roxlu_addon_source_dir ${CMAKE_CURRENT_LIST_DIR}/../../src/)
  roxlu_add_include_dir(${roxlu_addon_include_dir})
endmacro()

macro(roxlu_addon_end)
  message(STATUS "Added addon: ${roxlu_addon_name}")
endmacro()

macro(roxlu_addon_add_source_file file)
  list(APPEND ${roxlu_addon_name}_source_files ${roxlu_addon_source_dir}/${file})
  roxlu_add_source_file(${roxlu_addon_source_dir}/${file})
endmacro()

# ------------------------------------------------------------------------------------
# A P P L I C A T I O N 
# ------------------------------------------------------------------------------------

# roxlu_app_initialize()          - sets up a couple of application variables (app_name, app_source_dir, etc..)
# roxlu_app_add_source_file(path) - add a source file which will be compiled for your app
# roxlu_app_install()             - makes sure the application is installed into the correct directory.

macro(roxlu_app_initialize)

  get_filename_component(app_base_dir ${CMAKE_CURRENT_LIST_DIR}/../../ REALPATH)  
  get_filename_component(app_name ${app_base_dir} NAME) 

  if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(app_name "${app_name}_debug")
  endif()

  set(app_source_dir ${app_base_dir}/src)
  set(app_include_dir ${app_base_dir}/src)
  set(app_source_dirs ${app_source_dir})
  set(app_install_dir ${app_base_dir}/bin)
  set(CMAKE_INSTALL_PREFIX ${app_install_dir})

  roxlu_add_include_dir(${app_include_dir})

endmacro()

macro(roxlu_app_add_source_file file)
  list(APPEND app_source_files ${app_source_dir}/${file})
endmacro()
 
macro(roxlu_app_install)
  message(STATUS "Using triplet: ${tri_triplet}")
  message(STATUS "Include directories: ${roxlu_include_dirs}")

  add_definitions(${roxlu_definitions})
  include_directories(${roxlu_include_dirs})
  add_executable(${app_name} ${app_source_files} ${roxlu_source_files})
  target_link_libraries(${app_name} ${roxlu_libraries})
  install(TARGETS ${app_name} RUNTIME DESTINATION ${app_install_dir})
endmacro()
