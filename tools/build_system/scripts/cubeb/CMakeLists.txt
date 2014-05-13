# cubeb
#
# Minimal CMake file to compile the wonderfull cross platform
# audio output-library on Windows. Tested on Win 7
#
# See: https://github.com/kinetiknz/cubeb

cmake_minimum_required(VERSION 2.8)

set(bd ${CMAKE_CURRENT_LIST_DIR})
set(sd ${bd}/src)
set(id ${bd}/include)

set(cubeb_sources 
  ${sd}/cubeb.c
  ${sd}/cubeb_wasapi.cpp
  ${sd}/speex/resample.c
)

set(cubeb_headers
  ${id}/cubeb/cubeb.h
  ${id}/cubeb/cubeb-stdint.h
)

include_directories(
  ${id}
  ${sd}
)

add_definitions(
  -DUSE_WASAPI
  -DOUTSIDE_SPEEX
  -DRANDOM_PREFIX=speex
  -DFLOATING_POINT
  -DEXPORT=
)

if(NOT EXISTS ${id}/cubeb/cubeb-stdint.h)
  file(WRITE ${id}/cubeb/cubeb-stdint.h "#include <stdint.h>")
endif()

add_library(cubeb_static ${cubeb_sources})
install(TARGETS cubeb_static ARCHIVE DESTINATION lib)
install(FILES ${cubeb_headers} DESTINATION include/cubeb)

add_executable(test_tone ${bd}/test/test_tone.cpp)
target_link_libraries(test_tone cubeb_static)
install(TARGETS test_tone DESTINATION bin)

add_executable(test_audio ${bd}/test/test_audio.cpp)
target_link_libraries(test_audio cubeb_static)
install(TARGETS test_audio DESTINATION bin)

add_executable(test_latency ${bd}/test/test_latency.cpp)
target_link_libraries(test_latency cubeb_static)
install(TARGETS test_latency DESTINATION bin)

add_executable(test_sanity ${bd}/test/test_sanity.cpp)
target_link_libraries(test_sanity cubeb_static)
install(TARGETS test_sanity DESTINATION bin)