



cmake -S . -B build-vs -G "Visual Studio 17 2022"
cmake --build ./build-vs/

or

cmake -S . -B build-gc -G "MinGW Makefiles" 
cmake --build ./build-gc/

 
