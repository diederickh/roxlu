cmake_minimum_required(VERSION 2.8)

set(bd ${CMAKE_CURRENT_LIST_DIR})
set(shared ${bd}/shared)

set(webmtools_sources
  ${shared}/indent.cc
  ${shared}/webm_chunk_writer.cc
  ${shared}/webm_endian.cc
  ${shared}/webm_file.cc
  ${shared}/webm_incremental_reader.cc
  ${shared}/webm_live_muxer.cc
)

set(webmtools_headers
  ${shared}/indent.h
  ${shared}/webm_chunk_writer.h
  ${shared}/webm_constants.h
  ${shared}/webm_endian.h
  ${shared}/webm_file.h
  ${shared}/webm_incremental_reader.h
  ${shared}/webm_live_muxer.h
  ${shared}/webm_tools_types.h
)

include_directories(
  ${shared}
  ${bd}/../libwebm/
  )

add_library(webmtools STATIC ${webmtools_sources})

install(TARGETS webmtools DESTINATION lib)
install(FILES ${webmtools_headers} DESTINATION include/webmtools)
install(TARGETS webmtools DESTINATION lib)

