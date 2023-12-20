package tools;

import io.github.cdimascio.dotenv.Dotenv;

public class EnvUtils {
    private static final Dotenv dotenv = Dotenv.configure().load();
    
    public static String getVariable(String key) {
        return dotenv.get(key);
    }
}
