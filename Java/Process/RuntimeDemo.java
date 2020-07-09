import java.io.File;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class RuntimeDemo {

    public static void main(String[] args) {
        try {
            for (int i = 0; i < 200; i++) {
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        // TODO Auto-generated method stub
                        System.out.println(Thread.currentThread().getName()+":使用正常方法创建线程");
                        // print a message

                        try {
                            // create a process and execute notepad.exe and currect environment
                            Thread.sleep(1000);
                            Process process = Runtime.getRuntime().exec("cat /tmp/test2.log");
                            process.waitFor();


                            BufferedReader bufrIn = new BufferedReader(new InputStreamReader(process.getInputStream(), "UTF-8"));
                            BufferedReader bufrError = new BufferedReader(new InputStreamReader(process.getErrorStream(), "UTF-8"));

                            // 读取输出
                            String line = null;
                            StringBuilder result = new StringBuilder();
                            while ((line = bufrIn.readLine()) != null) {
                                result.append(line).append('\n');
                            }
                            while ((line = bufrError.readLine()) != null) {
                                result.append(line).append('\n');
                            }

                            //  System.out.println(Thread.currentThread().getId() + ": " + result);
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    }
                }).start();
            }
            // print another message
            System.out.println("Notepad should now open.");

        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
