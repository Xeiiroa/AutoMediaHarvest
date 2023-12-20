import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.SQLException;
import io.github.cdimascio.dotenv.Dotenv;
import Tools;

public class Database {
    
    public static void main(String[] args) {
        
    }

    public static void CreateDatabaseAndImportModel() {
        String dburl = "DB_URL";
        String url = "jbdc:sqlite" + dotenv.get("DEFAULT_VIDEO_SAVEPATH");

        try (Connection conn = DriverManager.getConnection(url)) {
            if (conn != null) {
                DatabaseMetaData meta = conn.getMetaData();
                System.out.println("driver: " + meta.getDriverName());
                System.out.println("A new database has been created");
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }
}
