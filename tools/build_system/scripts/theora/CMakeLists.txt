cmake_minimum_required(VERSION 2.8)

# CMake file for theora, only tested with 32 bit, on windows MSVC
# 64bit doesn't compile because it doesn't allow inline assembly

set(bd ${CMAKE_CURRENT_LIST_DIR})
set(id ${bd}/include)

set(libtheora_sources
  ${bd}/lib/analyze.c
  ${bd}/lib/apiwrapper.c
  ${bd}/lib/bitpack.c
#  ${bd}/lib/collect.c
  ${bd}/lib/decapiwrapper.c
  ${bd}/lib/decinfo.c
  ${bd}/lib/decode.c
  ${bd}/lib/dequant.c
  ${bd}/lib/encapiwrapper.c
  ${bd}/lib/encfrag.c
  ${bd}/lib/encinfo.c
  ${bd}/lib/encode.c
#  ${bd}/lib/encoder_disabled.c
  ${bd}/lib/enquant.c
  ${bd}/lib/fdct.c
  ${bd}/lib/fragment.c
  ${bd}/lib/huffdec.c
  ${bd}/lib/huffenc.c
  ${bd}/lib/idct.c
  ${bd}/lib/info.c
  ${bd}/lib/internal.c
  ${bd}/lib/mathops.c
  ${bd}/lib/mcenc.c
  ${bd}/lib/x86_vc/mmxencfrag.c
  ${bd}/lib/x86_vc/mmxfdct.c
  ${bd}/lib/x86_vc/mmxfrag.c
  ${bd}/lib/x86_vc/mmxidct.c
  ${bd}/lib/x86_vc/mmxstate.c
  ${bd}/lib/x86_vc/x86cpu.c
  ${bd}/lib/x86_vc/x86enc.c
  ${bd}/lib/x86_vc/x86state.c
  ${bd}/lib/quant.c
  ${bd}/lib/rate.c
  ${bd}/lib/state.c
  ${bd}/lib/tokenize.c
  )

set(libtheora_headers
  ${id}/theora/theora.h
  ${id}/theora/theoradec.h
  ${id}/theora/theoraenc.h
  ${id}/theora/codec.h
  )

include_directories(
  ${id}
  ${bd}/lib/
  )

add_definitions(
  -D_CRT_SECURE_NO_DEPRECATE
  -D_CRT_NONSTDC_NO_DEPRECATE
  -D_BIND_TO_CURRENT_CRT_VERSION
  -DWIN32
  -D_WINDOWS
  -D_USRDLL
  -DLIBTHEORA_EXPORTS
  -DOC_X86_ASM
  -D_UNICODE
  -DUNICODE
  )


add_library(libtheora_static ${libtheora_sources})
install(TARGETS libtheora_static ARCHIVE DESTINATION lib)
install(FILES ${libtheora_headers} DESTINATION include/theora)
