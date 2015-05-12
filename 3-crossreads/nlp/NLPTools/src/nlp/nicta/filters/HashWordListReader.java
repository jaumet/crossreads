package nlp.nicta.filters;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.HashSet;

public class HashWordListReader {

	public final static Integer ZERO = new Integer(0);
	
	public HashMap<String,Integer> _wordInfo;
	public String _delimiter = null;
	public boolean _stem = false;
	public SnowballStemmer _stemmer = null;

	public HashWordListReader(String src) {
		this(src, "[\\s]", false);
	}
	
	public HashWordListReader(String src, String delimiter, boolean stem) {
		_wordInfo = new HashMap<String,Integer>();
		_delimiter = delimiter;
		_stem = stem;
		if (_stem)
			_stemmer = new SnowballStemmer();
		loadWords(src);
	}

	public void loadWords(String src) {
        try {
            String line;
            BufferedReader br = new BufferedReader(new FileReader(src));
            while ((line = br.readLine()) != null) {
            	String[] segments = line.trim().split(_delimiter);
            	if (_stem)
            		segments[0] = _stemmer.stem(segments[0].trim().toLowerCase());
                _wordInfo.put(segments[0],
                		segments.length > 1 
                		  ? (int)(new Double(segments[1].trim().toLowerCase()).doubleValue())
                		  : ZERO);
                //System.out.println("Added: " + segments[0].trim().toLowerCase() + " -> " +
                //		(segments.length > 1 ? new Integer(segments[1].trim().toLowerCase()) : ZERO));
            }
            br.close();
        } catch (Exception e) {
            System.out.println("File not found");
            e.printStackTrace();
        }

	}
	
	public Integer getWordInfo(String s) {
		if (_stem)
			s = _stemmer.stem(s);
		return _wordInfo.get(s.toLowerCase());
	}
		
	public static void main(String args[]) {
		MultiTest(new HashWordListReader("./src/nlp/nicta/filters/non_name_single_words_and_freq.txt", "[\\s]", false));
		MultiTest(new HashWordListReader("./src/nlp/nicta/filters/non_name_single_words_and_freq.txt", "[\\s]", true));
		MultiTest(new HashWordListReader("./src/nlp/nicta/filters/top_freq_no_countries.txt", "[\\s]", true));
		MultiTest(new HashWordListReader("./src/nlp/nicta/filters/countries.txt", "[\\t]", true));
	}
	
	public static void MultiTest(HashWordListReader r) {
		System.out.println("=== BEGIN TEST ===");
		Test(r, "is");
		Test(r, "Scott");
		Test(r, "had");
		Test(r, "went");
		Test(r, "crawled");
		Test(r, "United States");
		System.out.println("=== END TEST ===\n\n");

	}
	
	public static void Test(HashWordListReader r, String s) {
		System.out.println("'" + s + "' info: " + r.getWordInfo(s));
	}
}
