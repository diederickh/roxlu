roxlu_addon_begin("image")
 # --------------------------------------------------------------------------------------
 if(UNIX) 
   roxlu_add_extern_library(libpng16.a)
   roxlu_add_extern_library(libz.a)
   roxlu_add_extern_library(libjpeg.a)
 endif()

 if(WIN32) 
   roxlu_add_dll(libpng16.dll)
   roxlu_add_dll(zlib1.dll)

   roxlu_add_extern_library(libjpeg.lib)

   if(CMAKE_BUILD_TYPE STREQUAL Debug)
     roxlu_add_extern_library(libpng16-static.lib)
     message("NOTE THAT LIBPNG ON WINDOWS RESULTS IN UNEXPECTED CRASHES. RELEASE BUILDS WORK FINE, BUT I HAVENT FOUND TIME TO FIGURE OUT WHATS GOING WRONG, IT SEEMS A LINKER/CODE GENERATION PROBLEM")
   else()
     roxlu_add_extern_library(libpng15.lib)
   endif()

   roxlu_add_extern_library(zlib.lib)
 endif()

 roxlu_addon_add_source_file(image/Image.cpp)
 roxlu_addon_add_source_file(image/PNG.cpp)
 roxlu_addon_add_source_file(image/TGA.cpp)
 roxlu_addon_add_source_file(image/JPG.cpp)
 # --------------------------------------------------------------------------------------
roxlu_addon_end()
