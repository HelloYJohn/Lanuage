run: HelloNative.class
	java -Djava.library.path='.' HelloNative
HelloNative.class : HelloNative.class libHelloNative.so
	javac HelloNative.java
libHelloNative.so: HelloNative.c
	g++ -shared -fPIC -I /usr/lib/jvm/java/include/ -I /usr/lib/jvm/java/include/linux HelloNative.c -o $@
.PHONY : clean
clean:
	rm -fr *.class *.so
