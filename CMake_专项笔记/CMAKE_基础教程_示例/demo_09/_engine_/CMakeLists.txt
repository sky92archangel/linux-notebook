
add_executable(_engine_ src/main.cpp)  # 生成时启用和add_library不兼容
 
target_include_directories(_engine_ 
PUBLIC 
	include
	include/common 
    # ${PROJECT_SOURCE_DIR}/_vendor_/eigen
    # tomlplusplus
) 
 
#将vendor中打包的 Eigen库引入main程序scope
target_link_libraries(_engine_ PUBLIC Eigen)

# PRIVATE 头文件搜索路径不会顺延  
# PUBLIC则会扩展顺延  即 B依赖hpp   A依赖B 则 A也可寻得hpp
# INTERFACE 单纯依赖 用于不编译的头文件  纯头文件库可使用
# target一类命令中 前者依赖后者 
target_compile_features(_engine_ PUBLIC cxx_std_17)	#指定语言版本