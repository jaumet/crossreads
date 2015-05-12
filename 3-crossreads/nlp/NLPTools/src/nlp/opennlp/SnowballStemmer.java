/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package nlp.opennlp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.Writer;

import org.tartarus.snowball.ext.englishStemmer;




/**
 *
 * @author gferraro
 */
public class SnowballStemmer {
    
  
    
    
    public static void main(String [] args) throws Throwable {
    
        englishStemmer stemmer = new englishStemmer();
        stemmer.setCurrent("cats");
        if (stemmer.stem()){
            System.out.println(stemmer.getCurrent());
        }
    }
    
    
}
    
    
 
    
    

