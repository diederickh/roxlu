cmake_minimum_required(VERSION 2.8)

set(bd ${CMAKE_CURRENT_LIST_DIR})
set(sd ${bd}/src)

set(tpl_sources
  ${sd}/tpl.c
  )

set(tpl_headers
  ${sd}/tpl.h
  )

include_directories(
  ${sd}
  )

add_library(tpl ${tpl_sources})

install(TARGETS tpl ARCHIVE DESTINATION lib)
install(FILES ${tpl_headers} DESTINATION include/)