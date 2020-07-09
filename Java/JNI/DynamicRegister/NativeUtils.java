public class NativeUtils {
    static {
        System.loadLibrary("DynamicRegister");
    }
    public static native void nativeInit();
    public static void main(String[] argv) {
        nativeInit();
    }
}
