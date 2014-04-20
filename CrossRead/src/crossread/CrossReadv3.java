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
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import uk.ac.shef.wit.simmetrics.similaritymetrics.CosineSimilarity;
import utils.AccessUtils;
import utils.StopWordsUtils;

/**
 *
 * @author gferraro
 */
public class CrossReadv3 {
    
    public int position = 0;
    public HashMap<String, JSONArray> docs = new HashMap();    
    public static HashMap<Integer, String> ranking = new HashMap();
    public List<String> selectedParagraphs = new ArrayList();
    public List<String> simList = new ArrayList();
    
    String outpath = "/home/gferraro/Desktop/test";
    
    
    private void doAction(String path) throws ParseException, Exception
    {
        // Load the doc collection
        bulk(path);
        
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
                Long pid = (Long)paragraph.get("pid");
                
                String sim = getMaxSim(paraText, docID);
                
                // Add the current paragraph id 
                simList.add(docID + " " + Long.toString(pid));
                // Add the most similar 
                simList.add(sim);
                
                
                
                System.out.println("current: " + docID + " " + Long.toString(pid));
                System.out.println("next: " + sim);
            }
        }
        
        // Write simList in json
        JSONArray list = new JSONArray();
        org.json.JSONObject simVector = new org.json.JSONObject();          
        for (String s : simList) {
            list.add(s);
        }        
        simVector.put("sim", list);
        
        JSONWriter writer = new JSONWriter();
        writer.WriteJsonObj(simVector, outpath + File.separatorChar + "simVector.json");            

    }
    
    
     /**
     * Get the ID of the most similar paragraph of paragraphX
     * Some constraints applies, which are:
     *  - Document constraint:
     *  - Paragraph constraint: 
     * 
     *  
     * @param paragraphX String = the content of the paragraph X 
     * @param paraXDocID String = doc id of the paragraph X
     * @return String = doc-id and paragraph-id of the most similar paragraph of X
     * @throws Exception 
     */
    private String getMaxSim(String paragraphX, String paraXDocID) throws Exception 
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
            if (paraXDocID.equalsIgnoreCase(docIDY)) { continue; }    
                    
            Iterator paraIterator = paragraphs.iterator();
            while (paraIterator.hasNext())
            {
                JSONObject paragraph = (JSONObject)paraIterator.next();                
                Long pidY = (Long)paragraph.get("pid");
                String paragraphY = (String)paragraph.get("p");
                
                // One selection constraint: exclude already selected paragraphs
                if (selectedParagraphs.contains(docIDY + " " + pidY)) { continue; }
                
                // Remove stop words
                paragraphX = removeStopwords(paragraphX);
                paragraphY = removeStopwords(paragraphY);                
                
                // Calculate similarity(X, paraText)
                float sim = applySimMetric(paragraphX, paragraphY);                
                similarities.put(docIDY + " " + pidY, sim);
            }        
        }
        
        // Return the most similar paragraph of paraText from the doc collection
        if (similarities.size() > 0) 
        {        
            double max = utils.CollectionUtils.getMax(similarities);
            List<String> maxs = utils.CollectionUtils.getKeysFromValue(similarities, max);
            
            if (maxs.size() > 1) {
              System.out.println("More than one paragraph have the highst similarity (empate), I chose the first from the list of maximums");              
            }            
            // Update the selectedParagraphs list
            selectedParagraphs.add(maxs.get(0));
            // Return example "2 3" (docIDX = 2 pidX = 3)
            //return maxs.get(0);
            String pair = maxs.get(0);
            
             // Add the current paragraph id 
        //     simList.add(paraXDocID + " " + Long.toString(pid));
             // Add the most similar 
             simList.add(pair);
             
             String[] split = pair.split(" ");             
             
             getMaxSim(split[0], split[1]);
             
             JSONArray get = docs.get(split[0]);
            
            
            
            
        } else {
            System.out.println("Similarity list is empty :("); 
           // exit(0);
        }
        
        System.out.println("Warning, return an empty string! Similarity list is empty"); 
        System.out.println(paragraphX + " "  + paraXDocID );
        return "";
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
            //JSONObject jsonArray = (JSONObject)obj;
            
            return jsonArray;            
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    
    
    
    private String removeStopwords(String text) 
    {
        String cleanText = new String();
        StopWordsUtils stopApp = new StopWordsUtils();        
        
        for (String tok : text.split(" ")) {
            if (!stopApp.is(tok))
                cleanText = cleanText.concat(tok);
        }
        return cleanText;
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
        CrossReadv3 crossRead = new CrossReadv3();
        
        crossRead.doAction(args[0]);
    }
    
    
}
