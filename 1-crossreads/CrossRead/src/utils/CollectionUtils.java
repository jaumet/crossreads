/*
 * CollectionUtils.java
 *
 * Created on 4 de julio de 2007, 10:12
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package utils;
import java.io.*;


/**
 *
 * @author Nedjet
 */
import java.util.*;
import org.json.simple.JSONArray;
public class CollectionUtils {
    
      public static ArrayList cloneArrayList(ArrayList arraylist) {
        ArrayList newArrayList = new ArrayList();
        Iterator it = arraylist.iterator();
        while (it.hasNext()) {
            String element = (String)it.next();
            newArrayList.add(element);
        }
        return newArrayList;
    }//cloneArrayList
    
   
	  
	public static void writeHashMap(HashMap inHashMap, File outputFilePath) throws Exception {			

		FileOutputStream outStream = new FileOutputStream(outputFilePath);
        PrintStream printStream = new PrintStream(outStream, true, "UTF-8");        
        
		Iterator iterator = inHashMap.keySet().iterator();

		while (iterator.hasNext()) {
			String key = iterator.next().toString();	
			String value = inHashMap.get(key).toString();
			printStream.print("\n" + key + "\n" + value);
		}		
		printStream.close();
        outStream.close();
	}
	  
        
        

     
        
        /**
         * 
         * @param hm
         * @param value
         * @return
         * @throws Exception 
         */
        public static List getKeysFromValue(HashMap<String, Float> hm, double value) throws Exception {
		
		ArrayList<String> keysList = new ArrayList();
		
		Set keys = hm.keySet();	

		for (Iterator i = keys.iterator(); i.hasNext();) {
			String key = (String) i.next();			
			double hmvalue = hm.get(key);									
			if (hmvalue == value) {	
				keysList.add(key);
			}
		}
		return keysList;
	}//getKeysFromValue
        
        /**
         * Find maximum element of Java HashSet using the 
         * static Object max(Collection c) method of Collections class.
         * This method returns the maximum element of Java HashSet according to
         * its natural ordering.
         * @param inMax : hash map input
         * @return double max value from the input hash values
         */
        public static Float getMax(HashMap inMax) {
            
                if (inMax != null && !inMax.isEmpty()) {
		
                    Object obj = Collections.max(inMax.values());			
                    String str = obj.toString();
                    Float maxValue = Float.valueOf(str);
                    //double maxValue = Double.valueOf(str).doubleValue();		

                    System.out.println("Max value: " + maxValue );

                    return maxValue;
                }
                return 0f;
	}
        
        /**
         * Find minimum element of Java HashSet using the 
         * static Object min(Collection c) method of Collections class.
         * This method returns the minimum element of Java HashSet according to
         * its natural ordering.
         * 
         * @param inMin : hash map input
         * @return double min value from the input hash values
         */
        public static double getMin(HashMap inMin) {	
            
            if (inMin != null && !inMin.isEmpty()) {
		
                Object obj = Collections.min(inMin.values());
		String str = obj.toString();
		double minValue = Double.valueOf(str).doubleValue();		
		
		System.out.println("Min value: " + minValue );
			
		return minValue;
            }
            return 0.0;
	}
	  
        
        
        public static List<String> removeEmptyStrings(List<String> inList) {

            List<String> stringList = new ArrayList<String>();

            for (String string : inList) {

                if (string != null && string.length() > 0) {
                    stringList.add(string);
                }
            }
            return stringList;
        }
        
        
        /**
         * @param inList
         * @return 
         */
        public static List<String> removeDuplicates(List<String> inList) {

            /** List order not maintained **/            
             HashSet h = new HashSet(inList);
             inList.clear();
             inList.addAll(h);
             
             return inList;
        }            
       
     
        public static Map sortByValueFloat(HashMap<String, Float> map) 
        {

            List list = new LinkedList(map.entrySet());
            Collections.sort(list, new Comparator() {

                public int compare(Object o1, Object o2) {
                    return ((Comparable) ((Map.Entry) (o1)).getValue()).compareTo(((Map.Entry) (o2)).getValue());
                }
            });

            Map result = new LinkedHashMap();
            for (Iterator it = list.iterator(); it.hasNext();) {
                Map.Entry entry = (Map.Entry) it.next();
                result.put(entry.getKey(), entry.getValue());
            }
            return result;
        }
	
        
        public static Map sortByValue(HashMap<String, Double> map) 
        {

            List list = new LinkedList(map.entrySet());
            Collections.sort(list, new Comparator() {

                public int compare(Object o1, Object o2) {
                    return ((Comparable) ((Map.Entry) (o1)).getValue()).compareTo(((Map.Entry) (o2)).getValue());
                }
            });

            Map result = new LinkedHashMap();
            for (Iterator it = list.iterator(); it.hasNext();) {
                Map.Entry entry = (Map.Entry) it.next();
                result.put(entry.getKey(), entry.getValue());
            }
            return result;
        }
        
        
        /**
         * Get the min value non-zero value from a hash map 
         * @param map
         * @return 
         */
        public static Double getMinNotZero(HashMap<String, Double> map)
        {
            Map sortByValue = sortByValue(map);
            
            Iterator iterator = sortByValue.entrySet().iterator();                       
            
            while (iterator.hasNext()) {
                
                Object next = iterator.next();               
                
                String toString = next.toString();
                String value =  toString.replaceAll("(.*=)", "");
                
                if (!value.equals("0.0")) {
                    
                    return Double.parseDouble(value);
                }                    
            }
            return 0.0;            
        }

  
    public static JSONArray getEntry(HashMap<String, JSONArray> hashMap, String Name) 
    {
        for (Object o : hashMap.entrySet()) 
        {
            Map.Entry entry = (Map.Entry) o;
            
            if (entry.getKey().equals(Name)) {
                JSONArray value = (JSONArray)entry.getValue();
                return value;
            }
        }
        return null;
    }
	  
	  
}
	  