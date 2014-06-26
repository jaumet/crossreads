
package utils;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Collections;
import java.util.Date;
import java.util.Enumeration;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Vector;

/**
 * 
 * 
 * Class that can test whether a given string is a stop word.
 * Lowercases all words before the test. 

* The format for reading and writing is one word per line, lines starting * with '#' are interpreted as comments and therefore skipped.

* The default stopwords are based on Rainbow.

* * Accepts the following parameter:

* * -i file
* loads the stopwords from the given file

* * -o file
* saves the stopwords to the given file

* * -p
* outputs the current stopwords on stdout

* * Any additional parameters are interpreted as words to test as stopwords. * 
* @author Eibe Frank (eibe@cs.waikato.ac.nz) 
* @author Ashraf M. Kibriya (amk14@cs.waikato.ac.nz) 
* @author FracPete (fracpete at waikato dot ac dot nz) 
* @version $Revision: 8034 $ */

public final class StopWordsUtils
{
 
  
  
          /** The hash set containing the list of stopwords */
          protected HashSet m_Words = null;

          /** The default stopwords object (stoplist based on Rainbow) */
          protected static StopWordsUtils m_Stopwords;

          static {
            if (m_Stopwords == null) {
              m_Stopwords = new StopWordsUtils();
            }
          }

          /**
           * initializes the stopwords (English based on Rainbow).
           */
          public StopWordsUtils() {
            m_Words = new HashSet();

            //Stopwords list 
            add("un");
            add("una");
            add("unas");
            add("unos");
            add("uno");
            add("sobre");
            add("todo");
            add("también");
            add("tras");
            add("otro");
            add("algún");
            add("alguno");
            add("alguna");
            add("algunos");
            add("algunas");
            add("ser");
            add("es");
            add("soy");
            add("eres");
            add("somos");
            add("sois");
            add("estoy");
            add("esta");
            add("estamos");
            add("estais");
            add("estan");
            add("como");
            add("en");
            add("para");
            add("atras");
            add("porque");
            add("por");
            add("qué");
            add("estado");
            add("estaba");
            add("ante");
            add("antes");
            add("siendo");
            add("ambos");
            add("pero");
            add("por");
            add("poder");
            add("puede");
            add("puedo");
            add("podemos");
            add("podeis");
            add("pueden");
            add("fui");
            add("fue");
            add("fuimos");
            add("fueron");
            add("hacer");
            add("hago");
            add("hace");
            add("hacemos");
            add("haceis");
            add("hacen");
            add("cada");
            add("fin");
            add("incluso");
            add("primero");
            add("desde");
            add("conseguir");
            add("consigo");
            add("consigue");
            add("consigues");
            add("conseguimos");
            add("consiguen");
            add("ir");
            add("voy");
            add("va");
            add("vamos");
            add("vais");
            add("van");
            add("vaya");
            add("gueno");
            add("ha");
            add("tener");
            add("tengo");
            add("tiene");
            add("tenemos");
            add("teneis");
            add("tienen");
            add("el");
            add("la");
            add("lo");
            add("las");
            add("los");
            add("su");
            add("aqui");
            add("mio");
            add("tuyo");
            add("ellos");
            add("ellas");
            add("nos");
            add("nosotros");
            add("vosotros");
            add("vosotras");
            add("si");
            add("dentro");
            add("solo");
            add("solamente");
            add("saber");
            add("sabes");
            add("sabe");
            add("sabemos");
            add("sabeis");
            add("saben");
            add("ultimo");
            add("largo");
            add("bastante");
            add("haces");
            add("muchos");
            add("aquellos");
            add("aquellas");
            add("sus");
            add("entonces");
            add("tiempo");
            add("verdad");
            add("verdadero");
            add("verdadera");
            add("cierto");
            add("ciertos");
            add("cierta");
            add("ciertas");
            add("intentar");
            add("intento");
            add("intenta");
            add("intentas");
            add("intentamos");
            add("intentais");
            add("intentan");
            add("dos");
            add("bajo");
            add("arriba");
            add("encima");
            add("usar");
            add("uso");
            add("usas");
            add("usa");
            add("usamos");
            add("usais");
            add("usan");
            add("emplear");
            add("empleo");
            add("empleas");
            add("emplean");
            add("ampleamos");
            add("empleais");
            add("valor");
            add("muy");
            add("era");
            add("eras");
            add("eramos");
            add("eran");
            add("modo");
            add("bien");
            add("cual");
            add("cuando");
            add("donde");
            add("mientras");
            add("quien");
            add("con");
            add("entre");
            add("sin");
            add("trabajo");
            add("trabajar");
            add("trabajas");
            add("trabaja");
            add("trabajamos");
            add("trabajais");
            add("trabajan");
            add("podria");
            add("podrias");
            add("podriamos");
            add("podrian");
            add("podriais");
            add("yo");
            add("aquel");
          }
  
  
  

      /**
       * removes all stopwords
       */
      public void clear() {
        m_Words.clear();
      }

      /**
       * adds the given word to the stopword list (is automatically converted to
       * lower case and trimmed)
       *
       * @param word the word to add
       */
      public void add(String word) {
        if (word.trim().length() > 0)
          m_Words.add(word.trim().toLowerCase());
      }

      /**
       * removes the word from the stopword list
       *
       * @param word the word to remove
       * @return true if the word was found in the list and then removed
       */
      public boolean remove(String word) {
        return m_Words.remove(word);
      }

      /** 
       * Returns true if the given string is a stop word.
       * 
       * @param word the word to test
       * @return true if the word is a stopword
       */
      public boolean is(String word) {
        return m_Words.contains(word.toLowerCase());
      }

      /**
       * Returns a sorted enumeration over all stored stopwords
       *
       * @return the enumeration over all stopwords
       */
      public Enumeration elements() {
        Iterator    iter;
        Vector      list;

        iter = m_Words.iterator();
        list = new Vector();

        while (iter.hasNext())
          list.add(iter.next());

        // sort list
        Collections.sort(list);

        return list.elements();
      }

      /**
       * Generates a new Stopwords object from the given file
       *
       * @param filename the file to read the stopwords from
       * @throws Exception if reading fails
       */
      public void read(String filename) throws Exception {
        read(new File(filename));
      }

      /**
       * Generates a new Stopwords object from the given file
       *
       * @param file the file to read the stopwords from
       * @throws Exception if reading fails
       */
      public void read(File file) throws Exception {
        read(new BufferedReader(new FileReader(file)));
      }

      /**
       * Generates a new Stopwords object from the reader. The reader is
       * closed automatically.
       *
       * @param reader the reader to get the stopwords from
       * @throws Exception if reading fails
       */
      public void read(BufferedReader reader) throws Exception {
        String      line;

        clear();

        while ((line = reader.readLine()) != null) {
          line = line.trim();
          // comment?
          if (line.startsWith("#"))
            continue;
          add(line);
        }

        reader.close();
      }

      /**
       * Writes the current stopwords to the given file
       *
       * @param filename the file to write the stopwords to
       * @throws Exception if writing fails
       */
      public void write(String filename) throws Exception {
        write(new File(filename));
      }

      /**
       * Writes the current stopwords to the given file
       *
       * @param file the file to write the stopwords to
       * @throws Exception if writing fails
       */
      public void write(File file) throws Exception {
        write(new BufferedWriter(new FileWriter(file)));
      }

      /**
       * Writes the current stopwords to the given writer. The writer is closed
       * automatically.
       *
       * @param writer the writer to get the stopwords from
       * @throws Exception if writing fails
       */
      public void write(BufferedWriter writer) throws Exception {
        Enumeration   enm;

        // header
        writer.write("# generated " + new Date());
        writer.newLine();

        enm = elements();

        while (enm.hasMoreElements()) {
          writer.write(enm.nextElement().toString());
          writer.newLine();
        }

        writer.flush();
        writer.close();
      }

      /**
       * returns the current stopwords in a string
       *
       * @return the current stopwords
       */
      public String toString() {
        Enumeration   enm;
        StringBuffer  result;

        result = new StringBuffer();
        enm    = elements();
        while (enm.hasMoreElements()) {
          result.append(enm.nextElement().toString());
          if (enm.hasMoreElements())
            result.append(",");
        }

        return result.toString();
      }

      /** 
       * Returns true if the given string is a stop word.
       * 
       * @param str the word to test
       * @return true if the word is a stopword
       */
      public static boolean isStopword(String str) {
        return m_Stopwords.is(str.toLowerCase());
      }




      /** * Accepts the following parameter:

    * * -i file
    * loads the stopwords from the given file

    * * -o file
    * saves the stopwords to the given file

    * * -p
    * outputs the current stopwords on stdout

    * 
    * Any additional parameters are interpreted as words to test as stopwords. 
    * 
    * @param args commandline parameters 
    * @throws Exception if something goes wrong 
    */


      public static void main(String[] args) throws Exception 
      {
        String input = "";// Utils.getOption('i', args);
        String output = ""; // Utils.getOption('o', args);
        boolean print = true; // Utils.getFlag('p', args);

        // words to process?
        Vector words = new Vector();
        for (int i = 0; i < args.length; i++) {
          if (args[i].trim().length() > 0)
            words.add(args[i].trim());
        }

        StopWordsUtils stopwords = new StopWordsUtils();

        // load from file?
        if (input.length() != 0)
          stopwords.read(input);

        // write to file?
        if (output.length() != 0)
          stopwords.write(output);

        // output to stdout?
        if (print) {
          System.out.println("\nStopwords:");
          Enumeration enm = stopwords.elements();
          int i = 0;
          while (enm.hasMoreElements()) {
            System.out.println((i+1) + ". " + enm.nextElement());
            i++;
          }
        }

        // check words for being a stopword
        if (words.size() > 0) {
          System.out.println("\nChecking for stopwords:");
          for (int i = 0; i < words.size(); i++) {
            System.out.println(
                (i+1) + ". " + words.get(i) + ": " 
                + stopwords.is(words.get(i).toString()));
          }
        }
      }
      
      
}