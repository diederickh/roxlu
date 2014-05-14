cmake_minimum_required(VERSION 2.8)

# CMake file for ogg, only tested with 32 bit, on windows MSVC

set(bd ${CMAKE_CURRENT_LIST_DIR})
set(sd ${bd}/src)
set(id ${bd}/include)

set(ogg_sources
  ${sd}/bitwise.c
  ${sd}/framing.c
  )

set(ogg_headers
  ${id}/ogg/ogg.h
  ${id}/ogg/os_types.h
  )

include_directories(${id})

add_definitions(
  -DLIBOGG_EXPORTS
  -D_UNICODE
  -DUNICODE
  -D_WINDOWS
  -DWIN32
  -DUSRDLL
  )

add_library(libogg_static ${ogg_sources})

install(TARGETS libogg_static ARCHIVE DESTINATION lib)
install(FILES ${ogg_headers} DESTINATION include/ogg)