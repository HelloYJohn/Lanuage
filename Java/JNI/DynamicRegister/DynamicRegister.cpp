#include <jni.h>
#include <iostream>

using std::cout;
using std::endl;


static const char* const kClass = "NativeUtils";

static void nativeInit(JNIEnv *env, jclass type) {
  cout << "nativeInit" << endl;
}

static JNINativeMethod gMethods[] = {

                                     {
                                      "nativeInit",
                                      "()V",
                                      (void*)nativeInit
                                     },

};


extern "C"
JNIEXPORT jint JNICALL
JNI_OnLoad(JavaVM* vm, void* reserved){
  JNIEnv *env = NULL;
  if (vm->GetEnv((void **) &env, JNI_VERSION_1_4) != JNI_OK) {
    return JNI_FALSE;
  }
  jclass jclazz= env->FindClass(kClass);
  if(env -> RegisterNatives(jclazz, gMethods, sizeof(gMethods)/ sizeof(gMethods[0])) < 0) {
    return JNI_FALSE;
  }
  return JNI_VERSION_1_4;
}
