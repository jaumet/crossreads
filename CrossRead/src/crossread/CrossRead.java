/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package crossread;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FilenameFilter;
import java.io.IOException;
import static java.lang.System.exit;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import jsonUtils.JSONWriter;
import nlp.nicta.ner.NERResultSet;
import nlp.nicta.ner.NamedEntityAnalyser;
import static nlp.nicta.ner.NamedEntityAnalyser.ReadFileAsString;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import uk.ac.shef.wit.simmetrics.similaritymetrics.CosineSimilarity;
import utils.AccessUtils;
import utils.CollectionUtils;
import utils.StopWordsUtils;

/**
 *
 * @author gferraro
 */
public class CrossRead {
    
    public int position = 0;    
    public static String outpath = null;    
    public static String EMPTYString = "";
    public List<String> simList = new ArrayList();  // stores the output similarity vector
    public List<String> visitedParagraphs = new ArrayList();   //
    public HashMap<String, JSONArray> docs = new HashMap();    
    
    public static NamedEntityAnalyser nea = null;
    
    /**
     * Set the similarity of xid
     * Sim(x, docCollection)
     * Recursive method
     * x = an instance is a paragraph from a doc. 
     * Instance id name = docIDYX pidX e.g. "2_3" (doc=2 paragraph=3) 
     * @param id 
     */
    private void setSim(String id) throws Exception    
    {
        String paraX;
        
        // Parse x id (e.g. "2_3")
        if (id == null || id.isEmpty()) { System.out.println("I cant parse instance id because it is null or empty: " + id);}               
        String[] split = id.split("_");                
        if (split == null )    { System.out.println("I cant parse instance id, because splitid is null: " + id); }
        if (1 == split.length) { System.out.println("I cant parse instance id, split lenght is 1:" + id); }        
        String docIDX = split[0];
        String pidX = split[1];        
        if (docIDX == null || pidX == null || docIDX.isEmpty() || pidX.isEmpty() ) {System.out.println("I cant parse instance id, docID or pid are null or empty: " + id); }
 
       // Update similarity list
        simList.add(id);
        
        // Get doc x (e.g. "2")
        JSONArray doc = utils.CollectionUtils.getEntry(docs, docIDX);        
        Iterator paras = doc.iterator();
        while (paras.hasNext())
        {   
            // Get a paragraph from x
            JSONObject para = (JSONObject)paras.next();            
            Long pid = (Long)para.get("pid");
            // Check desire id, e.g. "3"
            if (Long.toString(pid).equalsIgnoreCase(pidX))
            {
                // Get the paragraph (e.g. "3")
                paraX = (String)para.get("p");
                
                // Get max similarity of paraX againgts all the collection, restricted by docIDX
                String sim = getMaxSim(paraX, docIDX);
                
                if (sim.isEmpty()) {
                    System.out.println("Sim is empty!");
                    break;
                }
                setSim(sim);
               // System.out.println("next: " + sim);
            }
        }
        
        // Write simList in json
        JSONArray list = new JSONArray();
        org.json.JSONObject simVector = new org.json.JSONObject();          
        for (String s : simList) {
            list.add(s);
        }        
        simVector.put("sim", list);
        JSONWriter.WriteJsonObj(simVector, outpath + File.separatorChar + "simVector.json"); 
    }

    

    /**
     * Calculate the similarity between xid and doc collection, 
     * restricted by two constraints: 
     * // Document constraint: exclude the doc of the current paragraph
       // One selection constraint: exclude already visited/selected paragraphs
     * @param paragraphX String the content of the paragraph X 
     * @param paraXDocID String = doc id of the paragraph 
     * @return String id The id of the most similar paragraph of xid
     * @throws Exception 
     */
    private String getMaxSim(String paragraphX, String paraXDocID) throws Exception 
    {
        // Records the similarity between x and each paragraph in the collection
        // String: id, Float: similarity score 
        HashMap<String, Float> similarities = new HashMap();
        
        // Iterate through the json docs collection
        Iterator<Map.Entry<String, JSONArray>> docsIterator = docs.entrySet().iterator();
        while (docsIterator.hasNext()) 
        {
            Map.Entry<String, JSONArray> doc = docsIterator.next();            
            JSONArray paragraphs = doc.getValue();
            String docIDY = doc.getKey();
            
            //System.out.println("Doc id: " + doc.getKey());
            
            // Document constraint: exclude the doc of the current paragraph
            if (paraXDocID.equalsIgnoreCase(docIDY)) { continue; }    
                    
            Iterator paraIterator = paragraphs.iterator();
            while (paraIterator.hasNext())
            {
                JSONObject paragraph = (JSONObject)paraIterator.next();                
                Long pidY = (Long)paragraph.get("pid");
                String paragraphY = (String)paragraph.get("p");
                
                // One selection constraint: exclude already visited/selected paragraphs
                if (visitedParagraphs.contains(docIDY + "_" + pidY)) { continue; }
                
                // Calculate similarity(X, paragraphY)
                float sim = applySimMetric(paragraphX, paragraphY);       
                
                if (Float.isNaN(sim))                 {
                    similarities.put(docIDY + "_" + pidY, 0f);
                //    System.out.println("Warning! NaN va=lue, returning similarity 0");
                }
                else 
                    similarities.put(docIDY + "_" + pidY, sim);
                    // System.out.println(sim + " = " + paragraphX + "vs. " + paragraphY);
            }        
        }
        // Return the most similar paragraph from the similarities list
        if (similarities.size() > 0) 
        {        
            double max = utils.CollectionUtils.getMax(similarities);
            List<String> maxs = utils.CollectionUtils.getKeysFromValue(similarities, max);
            
            if (maxs.isEmpty()) {
              System.out.println("Warning! List of maxs sims is empty");     
              return "0";
            }
            
            if (maxs.size() > 1) {
              //System.out.println("More than one paragraph have the highst similarity (empate), I chose the first from the list of maximums");              
            }
            
            // return example "2 3" (docIDX = 2 pidX = 3)
            visitedParagraphs.add(maxs.get(0));
            //System.out.println("Returning id of the most similar paragraph : " + maxs.get(0));
            return maxs.get(0);
            
        } else {
            System.out.println("Similarity list is empty :("); 
           // System.out.println(paragraphX + " "  + paraXDocID );
            return EMPTYString;
           // exit(0);
        }
    }

    
    
    
    /**
     * 
     * @param text
     * @return
     * @throws Exception 
     */
    public HashMap<String, String> getNER(String text) throws Exception
    {
        
        // Extract named entities
        NERResultSet results = nea.process(text);

        // Display named entities, stored as name -> type pairs
        HashMap<String, String> map = results.getMappedResult();
        for (Map.Entry<String, String> e : map.entrySet()) {
            //System.out.println(e.getKey() + " -> " + e.getValue());
        }
        
        return map;
    }

    
  
    
    
    
    
    
    private float applySimMetric(String a, String b) throws Exception
    {
        CosineSimilarity cosine = new CosineSimilarity();        
        
        if (a == null || b == null || a.isEmpty() || b.isEmpty()){
           //  System.out.println("I cant calculate the similarity, one of the input string is null or empty (I will return a sim = 0.0), a: " + a + " ,b: " + b);  
          return 0;
        }
        
        // Remove stop words
        a = removeStopwords(a);
        b = removeStopwords(b);
        // System.out.println(paragraphX + "vs. " + paragraphY);
        
        // Token Cosine Sim
        float Toksim = cosine.getSimilarity(a, b);
        
        // Get NERs 
        HashMap<String, String> aNer = getNER(a);
        HashMap<String, String> bNer = getNER(b);   
        
        // a
        String apersons = getInstances(aNer, "PERSON");
        String adates = getInstances(aNer, "DATE");
        String alocs = getInstances(aNer, "LOC");
        
        // b
        String bpersons = getInstances(bNer, "PERSON");    
        String bdates = getInstances(bNer, "DATE");
        String blocs = getInstances(bNer, "LOC");
        
        // nan
        
        float Namesim = cosine.getSimilarity(apersons, bpersons);
        
        float Datesim = cosine.getSimilarity(adates, bdates);
     
        float Locsim = cosine.getSimilarity(alocs, blocs);
     
        // TokenSim + NameSim + DateSim + LocationSim / 4
        Float similarityScore = (Toksim + Namesim + Datesim + Locsim)/ 4 ;
        
        return similarityScore;
    }
    

    /**
     * 
     * @param path
     * @return
     * @throws ParseException 
     */
    private  JSONArray readJSON(String path) throws ParseException
    {
        JSONParser parser = new JSONParser();
        try 
        {
            System.out.println("Loading: " + path);
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
    
    
     private String removeStopwords(String text) 
    {
        String cleanText = new String();
        StopWordsUtils stopApp = new StopWordsUtils();        
        
        for (String tok : text.split(" ")) {
            if (!stopApp.is(tok))
                cleanText = cleanText.concat(tok + " ");
        }
        return cleanText.replaceAll("  ", " ");
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

    private String getInstances(HashMap<String, String> ners, String category)
    {
        String instances = new String(); 
                
        Iterator<Map.Entry<String, String>> iterator = ners.entrySet().iterator();
        
        while (iterator.hasNext())
        {
            Map.Entry<String, String> instance = iterator.next();
            
            if (instance.getValue().equalsIgnoreCase(category))
            {
                String key = instance.getKey();
                System.out.println("key: " + key);
                instances = instances.concat(key + " ");
            }
        }
        return instances;
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
        CrossRead crossRead = new CrossRead();
        
        // Load the doc collection
        crossRead.bulk(args[0]);
        
        // Set the output path
        outpath = args[1];
       
         nea = new NamedEntityAnalyser();
        
        // Require an id as input (id = docid_paragraphid) 
        crossRead.setSim("20_1");        // v.1
    }
    
}
