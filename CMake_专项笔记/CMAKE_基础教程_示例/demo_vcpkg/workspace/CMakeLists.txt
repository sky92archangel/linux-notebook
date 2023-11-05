add_executable( vckpg_test ) 


find_package(spdlog CONFIG REQUIRED)
target_link_libraries(main PRIVATE spdlog::spdlog)
 
aux_source_directory(./src DIR_SRCS) 
target_sources(vckpg_test PUBLIC ${DIR_SRCS})  #然后对执行者添加源文件
