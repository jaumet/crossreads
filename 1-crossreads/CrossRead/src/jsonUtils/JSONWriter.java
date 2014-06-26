/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package jsonUtils;


import java.io.FileWriter;
import java.io.IOException;
import java.util.Iterator;
import org.json.JSONArray;
import org.json.JSONObject;
;
//import org.json.simple.JSONObject;

/**
 *
 * @author gferraro
 */
public class JSONWriter {
    
    
    public void JsonSimpleExample() throws org.json.JSONException 
    {
	JSONObject obj = new JSONObject();        
	obj.put("name", "mkyong.com");
	obj.put("age", new Integer(100));
 
	JSONArray list = new JSONArray();
        /*
	list.add("msg 1");
	list.add("msg 2");
	list.add("msg 3");        
        */
	obj.put("messages", list); 
	try {
            FileWriter file = new FileWriter("test.json");
            file.write(obj.toString(PRETTY_PRINT_INDENT_FACTOR));
            file.flush();
            file.close();
 
	} catch (IOException e) {
		e.printStackTrace();
	}
	System.out.print(obj);
     }


    
    /**
     * 
     * { 
        "command": "login",
        "uid": "123",
        "params":
            { 
            "username": "pepe",
            "password": "11"
            }
        }
     * 
     * @throws Exception 
     */
    public void JsonNestedExample() throws Exception 
    {
        JSONObject parentData = new JSONObject();
        JSONObject childData = new JSONObject();

        parentData.put("command", "login");
        parentData.put("uid", "123");

        childData.put("username", "pepe");
        childData.put("password", "11");
        parentData.put("params", childData);
    }
    
    
    
    public static int PRETTY_PRINT_INDENT_FACTOR = 4;
    
    public static void WriteJsonObj(JSONObject obj, String outPath) throws org.json.JSONException 
    {   
	try {
            FileWriter file = new FileWriter(outPath);
            file.write(obj.toString(PRETTY_PRINT_INDENT_FACTOR));            
            file.flush();
            file.close();
 
	} catch (IOException e) {
            
		e.printStackTrace();
	}
	//System.out.print(obj);
     }
    
    public static void WriteJsonArray(JSONArray list, String outPath) throws org.json.JSONException 
    {   
	try {
            FileWriter file = new FileWriter(outPath);
            String toJSONObject = list.toString(PRETTY_PRINT_INDENT_FACTOR);
            
            file.write(toJSONObject);          
            file.flush();
            file.close();
 
	} catch (IOException e) {
		e.printStackTrace();
	}
	//System.out.print(obj);
     }
    
    
}
