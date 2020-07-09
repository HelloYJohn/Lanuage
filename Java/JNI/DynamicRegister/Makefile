run: NativeUtils.class
	java -Djava.library.path='.' NativeUtils
NativeUtils.class : NativeUtils.java libDynamicRegister.so
	javac NativeUtils.java
libDynamicRegister.so: DynamicRegister.cpp
	g++ -shared -fPIC -I /usr/lib/jvm/java/include/ -I /usr/lib/jvm/java/include/linux DynamicRegister.cpp -o $@
.PHONY : clean
clean:
	rm -fr *.class *.so
