/*
 * LangProperties.java
 *
 * Created on 1 de marzo de 2007, 17:21
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package utils;

import java.util.*;
import java.io.*;


/**
 *
 * @author Nedjet
 */
public class PropertiesUtils  {    
  
  

     
//--- Operation Section ---  
     
    /** Overload to trim result */
    static public String getStaticProperty(Properties theProperties,String key) {
        String result = theProperties.getProperty(key);
        if (result!=null)
            result=result.trim();
        return result;
    }//getProperty

    /** Overload to trim result */
    static public String getStaticProperty(Properties theProperties,String key,String defaultValue) {
        String result = theProperties.getProperty(key,defaultValue);
        if (result!=null)
            result=result.trim();
        return result;
    }//getProperty
    

	
   /** Get the value of this key or return the default */
   public static boolean getStaticProperty(Properties theProperties,String value, boolean defaultValue ) {
      String result;
      if (defaultValue==true)
        result = theProperties.getProperty(value,"true");  
      else
        result = theProperties.getProperty(value,"false");        

      if (result==null)
        return(defaultValue);
      else
        return(result.equalsIgnoreCase("true") ? true : false);
   }//getStaticProperty( String, boolean )
   
   public static TreeMap getKeyValueTreeMap(Properties theProperties,String root) {
        TreeMap results = new TreeMap();
        Iterator theKeysIt = theProperties.keySet().iterator();
        while (theKeysIt.hasNext()) {
            String key = (String) theKeysIt.next();    
            if (key.startsWith(root)) {
                String newkey = key.substring(root.length()+1);
                results.put(newkey,getStaticProperty(theProperties,key,(String)null));
            }
        }
        return results;
    }//getKeyValueTreeMap   
   
	//getList
      public static ArrayList getList(Properties theProperties,String root) {
        ArrayList results = new ArrayList();
        Iterator theKeysIt = theProperties.keySet().iterator();
        while (theKeysIt.hasNext()) {
            String key = (String) theKeysIt.next(); 
			if (key.startsWith(root)) {
				results.add(getStaticProperty(theProperties,key,(String)null));            
			}
			
        }
        return results;
    }//getList
   
   /*
    * The values in the treemap are arraylist
    */
    public static TreeMap getKeyValueTreeMapArrayList(Properties theProperties,String root) {
        TreeMap results = new TreeMap();
        Iterator theKeysIt = theProperties.keySet().iterator();
        while (theKeysIt.hasNext()) {
            String key = (String) theKeysIt.next();    
            if (key.startsWith(root)) {
                String newkey = key.substring(root.length()+1);
                String values = getStaticProperty(theProperties,key,(String)null);
                StringTokenizer st = new StringTokenizer(values,",");
                ArrayList valuesAL = new ArrayList();
                while (st.hasMoreTokens()) {
                    String token = st.nextToken();
                    valuesAL.add(token);
                }
                results.put(newkey,valuesAL);
            }
        }
        return results;
    }//getKeyValueTreeMapArrayList
   
     public static boolean getBoolean(Properties theProperties,String propName) throws Exception {
             String propValue = getStaticProperty(theProperties,propName);
             if (StringUtils.emptyString(propValue) || 
                 (!propValue.equalsIgnoreCase("true") && !propValue.equalsIgnoreCase("false")))
                 return false;
             else
                 return Boolean.valueOf(propValue);
         }//getBoolean
   
      /*
        * @returns full path of dir specified as property (if specified), returns exception if specified dir (absolute or relative) does not exist
        */
          public static String getDir(Properties theProperties,String path,String prop)  throws Exception  {
            String dir = getStaticProperty(theProperties,prop);
            if (StringUtils.emptyString(dir))
                throw new Exception("Directory property unspecified: "+prop);
            if (AccessUtils.isAbsolute(dir) && !AccessUtils.existsDir(dir))
                    throw new Exception("Directory path does not exist: "+prop+"="+dir);
            if (!AccessUtils.isAbsolute(dir)) {
                dir = path + File.separatorChar + dir;
                if (!AccessUtils.existsDir(dir))
                   throw new Exception("Directory does not exist: "+prop+"="+dir);
           }
            return dir;
     }//getDir
          
          
          /*
        * @returns full path of  file
        */
          public static String getOutFile(Properties theProperties,String path,String prop)  throws Exception  {
            String filePath = getStaticProperty(theProperties,prop);
            if (StringUtils.emptyString(filePath))
                throw new Exception("Property unspecified: "+prop);
            if (!AccessUtils.isAbsolute(filePath))
                filePath = path + File.separatorChar + filePath;
            if (!AccessUtils.existsFile(filePath))
                throw new Exception("File path does not exist: "+filePath);
            return filePath;
     }//getOutFile
        
      
}
