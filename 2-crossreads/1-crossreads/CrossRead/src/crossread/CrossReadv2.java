/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package crossread;

import jsonUtils.JSONWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FilenameFilter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import uk.ac.shef.wit.simmetrics.similaritymetrics.CosineSimilarity;
import utils.AccessUtils;

/**
 *
 * @author gferraro
 */
public class CrossReadv2 {
    
    public int position = 0;
    public HashMap<String, JSONArray> docs = new HashMap();    
    public static HashMap<Integer, String> ranking = new HashMap();
    public List<String> selectedParagraphs = new ArrayList();
    
    String outpath = "/home/gferraro/Desktop/test";
    
    
    private void doAction(String path) throws ParseException, Exception
    {
        // Load the doc collection
        bulk(path);
        
        HashMap<String, Map> list = new HashMap();
        
        // Iterate through the json docs collection
        Iterator<Map.Entry<String, JSONArray>> docsIterator = docs.entrySet().iterator();
        while (docsIterator.hasNext()) 
        {
            Map.Entry<String, JSONArray> doc = docsIterator.next();            
            String docID = doc.getKey();
            
            JSONArray paragraphs = doc.getValue();
            Iterator paraIterator = paragraphs.iterator();
            while (paraIterator.hasNext()) 
            {
                JSONObject paragraph = (JSONObject)paraIterator.next();                                
                String paraText = (String)paragraph.get("p");
                String pid = (String)paragraph.get("pid");
                
                Map simVector = getSimVector(paraText, pid, docID);
                list.put(pid, simVector);
            }
            
            // JSON objects
            org.json.JSONObject document = new org.json.JSONObject();  
            // Print json for docID
            Iterator<Entry<String, Map>> it = list.entrySet().iterator();            
            while (it.hasNext()) 
            {
                Entry<String, Map> entry = it.next();                
                String pid = entry.getKey();
                Map value = entry.getValue();
                document.put("pid", pid);
                document.put("sim", value.toString());
            }
            
            JSONWriter writer = new JSONWriter();
            writer.WriteJsonObj(document, outpath + File.separatorChar + docID + ".json");            
            
        }
    }
    
    
    /**
     * 
     * @param paragraphX String = the content of the paragraph X 
     * @param docID String = doc id of the paragraph 
     * @return Map
     * @throws Exception 
     */
    private Map getSimVector(String paragraphX, String pid, String docID) throws Exception 
    {
        HashMap<String, Float> similarities = new HashMap();
        
        // Iterate through the json docs collection
        Iterator<Map.Entry<String, JSONArray>> docsIterator = docs.entrySet().iterator();
        while (docsIterator.hasNext()) 
        {
            Map.Entry<String, JSONArray> doc = docsIterator.next();            
            JSONArray paragraphs = doc.getValue();
            String docIDY = doc.getKey();
            
            // Document constraint: exclude the doc of the current paragraph
            if (docID.equalsIgnoreCase(docIDY)) { continue; }    
                    
            Iterator paraIterator = paragraphs.iterator();
            while (paraIterator.hasNext())
            {
                JSONObject paragraph = (JSONObject)paraIterator.next();                
                String paraText = (String)paragraph.get("p");
                String pidY = (String)paragraph.get("pid");
                
                // One selection constraint: exclude already selected paragraphs
                if (selectedParagraphs.contains(docIDY + " " + pidY)) { continue; }
                
                // Calculate similarity(X, Y)
                float sim = applySimMetric(paragraphX, paraText);                
                similarities.put(docIDY + " " + pidY, sim);
                //selectedParagraphs.contains(docIDY + " " + pidY);
            }        
        }
        
        // Return the similarities in descending order 
        Map<String, Float> sortSim = new HashMap();
        if (similarities.size() > 0) 
        {       
            sortSim = utils.CollectionUtils.sortByValueFloat(similarities);
            
        } else {
            System.out.println("Similarity list is empty :("); 
           // exit(0);
        }
        
        System.out.println(docID + ", " + pid);
        Iterator iterator = sortSim.entrySet().iterator();        
        while (iterator.hasNext())
        {
            Object next = iterator.next();
            
            System.out.println(next.toString());
        }
        return sortSim;        
    }
    
    
    
    
    private float applySimMetric(String a, String b)
    {
        if (a == null || b == null){
          System.out.println("I cant calculate the similarity, one of the input string is null (I will return a sim = 0.0), a: " + a + " ,b: " + b);  
          return 0;
        }
        
        CosineSimilarity cosine = new CosineSimilarity();        
        //System.out.println(cosine.getSimilarityExplained(a, b));
        float sim = cosine.getSimilarity(a, b);
        return sim;
    }
    
    
    
     private void bulk(String path) throws ParseException
    {
        File dir = new File(path);
        ArrayList<File> files = new ArrayList<>();
        AccessUtils.listFilesRecursive(dir, (FilenameFilter) new Filter(), files);
        Map<String, File> filenames = AccessUtils.getsortedFilepaths(files);
        
        for (Map.Entry e : filenames.entrySet()) {
            File file = (File)e.getValue();
            String fpath = (String)e.getKey();
            
            docs.put(file.getName().replace(".json", ""), readJSON(fpath));
        }        
    }
    
     
    private  JSONArray readJSON(String path) throws ParseException {
        JSONParser parser = new JSONParser();
        try 
        {
            Object obj = parser.parse(new FileReader(path));                       
            JSONArray jsonArray = (JSONArray) obj; 
            
            return jsonArray;            
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    
      
      
    // Filter directories
    private class Filter implements FilenameFilter {
        public boolean accept(File dir, String name) {
            if (!name.contains(".")) { return false;}
            return true;
        }
    }
    
    
     /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ParseException, org.json.simple.parser.ParseException, Exception 
    {    
        CrossReadv2 crossRead = new CrossReadv2();
        
        crossRead.doAction(args[0]);
    }
    
    
}
