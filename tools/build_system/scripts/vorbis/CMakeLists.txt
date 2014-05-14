cmake_minimum_required(VERSION 2.8)

# CMake file for vorbis, only tested with 32 bit, on windows MSVC

set(bd ${CMAKE_CURRENT_LIST_DIR})
set(sd ${bd}/src)
set(id ${bd}/include)

set(libvorbis_sources
  ${bd}/lib/analysis.c
  ${bd}/lib/bitrate.c
  ${bd}/lib/block.c
  ${bd}/lib/codebook.c
  ${bd}/lib/envelope.c
  ${bd}/lib/floor0.c
  ${bd}/lib/floor1.c
  ${bd}/lib/info.c
  ${bd}/lib/lookup.c
  ${bd}/lib/lpc.c
  ${bd}/lib/lsp.c
  ${bd}/lib/mapping0.c
  ${bd}/lib/mdct.c
  ${bd}/lib/res0.c
  ${bd}/lib/sharedbook.c
  ${bd}/lib/smallft.c
  ${bd}/lib/synthesis.c
  ${bd}/lib/vorbisenc.c
  ${bd}/lib/window.c
  )

set(libvorbis_headers
  ${id}/vorbis/codec.h
  ${id}/vorbis/vorbisenc.h
  ${id}/vorbis/vorbisfile.h
  )

set(libvorbisfile_sources
  ${bd}/lib/vorbisfile.c
  )

include_directories(
  ${id}
  ${bd}/lib/
  )

add_definitions(
  -DLIBVORBIS_EXPORTS
  -D_UNICODE
  -DUNICODE
  -D_WINDOWS
  -DWIN32
  -DUSRDLL
  )


add_library(libvorbis_static ${libvorbis_sources})
add_library(libvorbisfile_static ${libvorbisfile_sources})

install(TARGETS libvorbis_static ARCHIVE DESTINATION lib)
install(TARGETS libvorbisfile_static ARCHIVE DESTINATION lib)
install(FILES ${libvorbis_headers} DESTINATION include/vorbis)