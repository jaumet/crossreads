/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package jsonUtils;

import java.io.File;
import java.io.FilenameFilter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import org.json.JSONArray;
import org.json.JSONObject;

import org.json.simple.parser.ParseException;
import utils.AccessUtils;





/**
 *
 * @author gferraro
 */
public class Txt2JSON {
    
    
    // docID, doc content
    public HashMap<String, String> docs = new HashMap();    
    
    
    private void doAction(String inPath, String outPath) throws ParseException, Exception
    {
        // read the doc collection from path
        bulk(inPath);
        
        // Iterate through the docs collection
        Iterator<Map.Entry<String, String>> docsIterator = docs.entrySet().iterator();
        
        while (docsIterator.hasNext()) 
        {
            int pcounter = 0; // paragraphs names start in 0
            JSONArray list = new JSONArray();       
            
            Map.Entry<String, String> doc = docsIterator.next();            
            
            String content = doc.getValue();
            String[] paragraphs = content.split("\n\n");         
            
            for (String p: paragraphs)
            {
                // Clean p
                p = p.replaceAll("  ", " ");
                p = p.replaceAll("\n", " ");
                p = p.replaceAll("\u2013", "");
                p = p.replaceAll("\u201d", "");
                p = p.replaceAll("\u201c", "");
                p = p.replaceAll("\u2026", "");
                p = p.replaceAll("\u2019", "");
                p = p.replaceAll("\u2018", "");
                
                // remove spaces at the begining of a line
                // p = p.replaceAll("^ (.*)", "");
                
                // Create JSON object, add paragraph id and paragraph content     
                JSONObject obj = new JSONObject();
                obj.put("pid", pcounter++);
                obj.put("p",  p);                
                list.put(obj);
            }
            
            jsonUtils.JSONWriter.WriteJsonArray(list, outPath + File.separatorChar + doc.getKey() + ".json");
        }
    }
    
    
    
    /**
     * Read a doc collection from path
     * @param path Sring
     * @throws ParseException
     * @throws Exception 
     */
    private void bulk(String path) throws ParseException, Exception
    {
        File dir = new File(path);
        ArrayList<File> files = new ArrayList<>();
        AccessUtils.listFilesRecursive(dir, (FilenameFilter) new Filter(), files);
        Map<String, File> filenames = AccessUtils.getsortedFilepaths(files);
        
        for (Map.Entry e : filenames.entrySet()) 
        {
            File file = (File)e.getValue();
            String fpath = (String)e.getKey();
            
            // Example of doc named: 23_instalacion_hipermedio_def.txt
            // We want only the doc ID, which is 23
            String name = file.getName().replaceAll("(\\d+)(_[A-Za-z-_.,ó]+)", "$1");
            docs.put(name, utils.FileUtils.loadFileToString(fpath));
        }        
    }
    
    
    // Filter directories
    private class Filter implements FilenameFilter
    {
        public boolean accept(File dir, String name) {
            if (!name.contains(".")) { return false;}
            return true;
        }
    }
    
    
     /**
      * 
      * 
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ParseException, org.json.simple.parser.ParseException, Exception 
    {    
        Txt2JSON app = new Txt2JSON();
        
        app.doAction(args[0], args[1]);
    }
    
}
