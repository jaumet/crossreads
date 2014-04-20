/*
 * StringUtils.java
 *
 * Created on 9 de noviembre de 2006, 12:08
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package utils;

import java.util.*;
/**
 *
 * @author Ivan
 */
public class StringUtils {

    /** Creates a new instance of StringUtils */
    public StringUtils() {
    }

    /** Remove inital space and put first character in upper case */
    public static String cleanInitial(String line) {
        String initial = "^[\\p{Punct}\\s]*(.*)$";
        line = line.replaceFirst(initial,"$1");
        // put first char in upper case
        if (line.length() >0) {
            String firstCharacter = line.charAt(0) + "";
            firstCharacter = firstCharacter.toUpperCase();
            line = firstCharacter + line.substring(1);
        }
        return line;
    }

    /** Remove multiple spaces */
    public static String cleanSpaces(String line) {
        String initial = "^ +";
        line = line.replaceAll(initial," ");
        return line;
    }
    
    public static boolean emptyString(String aString) {
        if (aString==null)
            return true;
        if (aString.trim().length()==0)
            return true;
        return false;
    }
    
    public static int numberOfTokens(String string) {
        StringTokenizer thisStringTokenizer = new StringTokenizer(string);
        return thisStringTokenizer.countTokens();
    }
    
      /*
       * @param a string which is a positive or 0 number
       * @return the number as an int, or -1 if the string is empty or 0
       */
      public  static int stringToPositiveNumber(String aString) throws Exception {
          int anInt=-1;
           if (!emptyString(aString) || aString.equals("0")) {
               try {
                    anInt = Integer.parseInt(aString);
               } catch (NumberFormatException nfe) {
                   nfe.printStackTrace();
                   throw new Exception("Claim to summarize is not a number:"+aString);
               }
           }
          return anInt;
    }//stringToNumber
      
      public static int checkStringNumber(String aString) throws Exception {
        if (!emptyString(aString)) {
            try {
                int number = Integer.parseInt(aString);
                return number;
            } catch (NumberFormatException e) {
               e.printStackTrace();
               throw new Exception("String \""+aString+"\" is not a number");
            }
        }
        else {
            throw new Exception("String \""+aString+"\" is not a number");
        }
      }//isStringNumber
      
      public static String[] appendArrays(String[] array1, String[] array2) {
          String[] newArray = new String[array1.length + array2.length];
          System.arraycopy(array1, 0, newArray, 0, array1.length);
          System.arraycopy(array2, 0, newArray, array1.length, array2.length);
          return newArray;
     }//appendArrays
      
      public static String arrayToString(String[] array) {
          String output=null;
          for (int i=0;i<array.length;i++) {
              if (output==null)
                  output=array[i];
              else 
                  output=output + " " + array[i];
          }
          return output;
      }//arrayToString
  
   
}
