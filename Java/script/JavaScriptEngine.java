import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class JavaScriptEngine {
    public static void main(String[] args) throws Exception{
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        String script = "print(\"Hello\", \"World!\");";
        engine.eval(script);
        script = "print(\"Hello World!\");";
        engine.eval(script);
    }
}
