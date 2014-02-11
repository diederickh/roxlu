cmake_minimum_required(VERSION 2.8)

project(jansson)

set(bd ${CMAKE_CURRENT_LIST_DIR})

set(jansson_sources
  ${bd}/src/dump.c
  ${bd}/src/error.c
  ${bd}/src/hashtable.c
  ${bd}/src/load.c
  ${bd}/src/memory.c
  ${bd}/src/pack_unpack.c
  ${bd}/src/strbuffer.c
  ${bd}/src/strconv.c
  ${bd}/src/utf.c
  ${bd}/src/value.c
  ${bd}/src/jansson.def
)

set(jansson_headers
  ${bd}/src/jansson.h
  ${bd}/src/jansson_config.h
)

if(WIN32)
  include_directories(${bd}/win32)
  add_definitions(
    -DWIN32
    -D_WINDOWS
    -DUSRDLL
    -DJANSSON_DLL_EXPORTS
    )
endif()
  
add_library(jansson SHARED ${jansson_sources})

add_library(jansson_static STATIC ${jansson_sources})

install(TARGETS jansson 
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  )

install(TARGETS jansson_static ARCHIVE DESTINATION lib)
install(FILES ${jansson_headers} DESTINATION include)
