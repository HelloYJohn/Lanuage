h_add.so : add.c add.h add_wrap.c
	gcc -shared -fPIC -o _add.so -I/usr/include/python2.7/ add.c add_wrap.c
add_wrap.c : add.i
	swig -python -py3 add.i
clean :
	rm _add.so add_wrap.c add.py
