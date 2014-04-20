/*
 * NumberUtils.java
 *
 * Created on 10 de marzo de 2008, 12:26
 *
 */

package utils;

/**
 *
 * @author Nedjet
 */
public class Counter {
     static int uniqueIdCounter=0;
    
     public static int getCounter() {                    
        return uniqueIdCounter;
    }
    
    /**
     *  This method can be used to ensure that the counter isn't lower than a given value.
     */
    public static void setCounter(int inValue) {
        if (uniqueIdCounter <= inValue) 
            uniqueIdCounter = inValue+1;                        
    }
    
    /**
     *  Use this method to get a number for a new ID (i.e. a new sentence).
     */
    public static int getNewNumber() {
        return uniqueIdCounter++;
    }
    
    public static int checkCounter(int inValue) {
        if (inValue <= uniqueIdCounter ) 
            inValue=uniqueIdCounter++; 
        return inValue;
    }
    
    
}
