/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package nlp.crossreads;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FilenameFilter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import nlp.nicta.ner.NERResultSet;
import nlp.nicta.ner.NamedEntityAnalyser;
import opennlp.tools.namefind.NameFinderME;
import opennlp.tools.namefind.TokenNameFinderModel;
import opennlp.tools.postag.POSModel;
import opennlp.tools.postag.POSTagger;
import opennlp.tools.postag.POSTaggerME;
import opennlp.tools.sentdetect.SentenceDetectorME;
import opennlp.tools.sentdetect.SentenceModel;
import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import opennlp.tools.util.Span;
import org.tartarus.snowball.ext.englishStemmer;
import util.AccessUtils;
import util.FileUtils;





/**
 *
 * @author gferraro
 */
public class Analyzer {
    
        public static String tmp;
        public static String inputpath;
        
        POSTagger _posTagger;                        
        
        NameFinderME _dateFinderME;
        NameFinderME _locationFinderME;
        NameFinderME _moneyFinderME;
        NameFinderME _organizationFinderME;
        NameFinderME _percentageFinderME;
        NameFinderME _personFinderME;
        NameFinderME _timeFinderME;
        
        englishStemmer _stemmer;
        NamedEntityAnalyser _ner;        
        SentenceDetectorME _sdetector;
	Tokenizer          _tokenizer;        
        
    
        public void init() throws IOException, Exception {
            
                InputStream modelIn = null;
            
                // Load models for Sentence Detector
                System.out.println("Loading models for Sentence Detector...");                
                SentenceModel sentModel = null;            		
                modelIn = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/sentdetect/en-sent.bin");
                try {
                    sentModel = new SentenceModel(modelIn);
                } catch (IOException e) {
                    e.printStackTrace();
                } finally {
                    if (modelIn != null) {
                        try {
                            modelIn.close();
                        } catch (IOException e) {
                        }
                    }
                }
                _sdetector = new SentenceDetectorME(sentModel);
		//_sdetector = new SharedSentenceDetector("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/sentdetect/EnglishSD.bin.gz");
            

		// Load models for Tokenizer
                System.out.println("Loading models for Tokenizer...");
                TokenizerModel tokModel = null;                
                InputStream modelInTok = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/tokenize/en-token.bin");
                try {
                    tokModel = new TokenizerModel(modelInTok);
                } catch (IOException e) {
                    e.printStackTrace();
                } finally {
                    if (modelIn != null) {
                        try {
                            modelIn.close();
                        } catch (IOException e) {
                        }
                    }
                }                		
                _tokenizer = new TokenizerME(tokModel);		//_tokenizer = new Tokenizer("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/tokenize/EnglishTok.bin.gz");
        
                // Snowball Stemmer 
                _stemmer = new englishStemmer();
            
               // POSTagging               
               System.out.println("Loading models for POSTagging...");
               POSModel POSTmodel = null; 
               InputStream modelInPOS = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/postag/en-pos-maxent.bin");
                try {                    
                    POSTmodel = new POSModel(modelInPOS);
                } catch (IOException e) {
                    // Model loading failed, handle the error
                    e.printStackTrace();
                } finally {
                    if (modelIn != null) {
                        try {
                            modelIn.close();
                        } catch (IOException e) {
                        }
                    }
                }
                _posTagger = new POSTaggerME(POSTmodel);                                
                
                // NICTA Named Entity Recognizer                
                // _ner = new NamedEntityAnalyser();   
                
                ////////////////////////////////////////////////////////////////////////
                /////////// NAME FINDER ////////////////////////////////////////////////                
                System.out.println("Loading models for Name Finder...");                

                // Loading Date Finder
                TokenNameFinderModel dateModel = null;
                modelIn = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/ner/en-ner-date.bin");
                try { dateModel = new TokenNameFinderModel(modelIn); System.out.println("Date Name Finder loaded!");                
                } catch (IOException e) { e.printStackTrace();}
                finally { if (modelIn != null) { try { modelIn.close(); } catch (IOException e) {} }}                
                _dateFinderME = new NameFinderME(dateModel);
                
                // Loading Location Finder
                TokenNameFinderModel locationModel = null;
                modelIn = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/ner/en-ner-location.bin");
                try { locationModel = new TokenNameFinderModel(modelIn); System.out.println("Location Name Finder loaded!");                
                } catch (IOException e) { e.printStackTrace(); } 
                finally { if (modelIn != null) { try { modelIn.close();} catch (IOException e) {} }}                
                _locationFinderME = new NameFinderME(locationModel);
                
                // Loading Money Finder
                TokenNameFinderModel moneyModel = null;
                modelIn = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/ner/en-ner-money.bin");
                try { moneyModel = new TokenNameFinderModel(modelIn); System.out.println("Money Name Finder loaded!");                
                } catch (IOException e) { e.printStackTrace();}  
                finally { if (modelIn != null) { try { modelIn.close(); } catch (IOException e) {} }}                
                _moneyFinderME = new NameFinderME(moneyModel);
                
                // Loading Organization Finder                
                TokenNameFinderModel organizationModel = null;
                modelIn = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/ner/en-ner-organization.bin");
                try { organizationModel = new TokenNameFinderModel(modelIn); System.out.println("Organization Name Finder loaded!");} 
                catch (IOException e) { e.printStackTrace(); } 
                finally { if (modelIn != null) { try { modelIn.close(); } catch (IOException e) {} }}                
                _organizationFinderME = new NameFinderME(organizationModel);
                
                // Loading Percentage Finder                                
                TokenNameFinderModel percentageModel = null;
                modelIn = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/ner/en-ner-percentage.bin");
                try { percentageModel = new TokenNameFinderModel(modelIn); System.out.println("Percentage Name Finder loaded!"); } 
                catch (IOException e) { e.printStackTrace();} 
                finally { if (modelIn != null) { try { modelIn.close(); } catch (IOException e) {} }}                
                _percentageFinderME = new NameFinderME(percentageModel);
                
                // Loading Person Finder                                
                TokenNameFinderModel personModel = null;
                modelIn = new FileInputStream("/home/gferraro/Documents/github/crossreads/3-crossreads/nlp/NLPTools/models/ner/en-ner-person.bin");
                try { personModel = new TokenNameFinderModel(modelIn); System.out.println("Person Name Finder loaded!");} 
                catch (IOException e) { e.printStackTrace(); } 
                finally { if (modelIn != null) { try { modelIn.close(); } catch (IOException e) {} }}                
                _personFinderME = new NameFinderME(personModel);
            }
    
     
    /**
     * Apply a lemmatizer to the input sentences  and save the lemmas in a file. 
     * Sentence segmentation is lost when saving all into a single file. 
     * @param tokens 
     * @param outputName
     * @param outpath
     * @throws IOException 
     */
     private void applyLemmatizer(String[][] sentences, String outputName, String outpath) throws IOException {
         
        String lemmas = "";              
        for (int sent_index = 0; sent_index < sentences.length; sent_index++) {            
            for (String token : sentences[sent_index]) {
                _stemmer.setCurrent(token);
                if (_stemmer.stem()) {                
                    lemmas = lemmas.concat(" " + _stemmer.getCurrent());
                    System.out.println(_stemmer.getCurrent());
                }
            }
	}
        
        // Write lemmas in a file
        File file = new File(outpath + File.separatorChar + outputName + ".lemmas");
        util.FileUtils.writeStringToFile(lemmas, file);        
    }
    
     
    /**
     * Apply POSTagger to sentences and save tags in file
     * @param sentences
     * @param outputName
     * @param outpath
     * @throws IOException 
     */
    private void applyPOSTagger(String[][] sentences, String outputName, String outpath) throws IOException {
        
            List<String[]> sentTags = new ArrayList();
            
            for (String[] sentence : sentences) {                
                String tags[] = _posTagger.tag(sentence);
                sentTags.add(tags);
            }
        
        // Write postags in a file
        File file = new File(outpath + File.separatorChar + outputName + ".POSTaggs");
          for (String[] tags : sentTags ) {
               util.FileUtils.writeStringToFile(Arrays.toString(tags), file);
         }
    }   

  
    //////////////////////////////////////////////////////////////////
    //                              NER
    //////////////////////////////////////////////////////////////////	
    
    /**
     * 
     * @param tokens
     * @param outputName
     * @param absolutePath 
     */
    private void applyNameFinder(String[][] sentences, String outputName, String outpath) throws Exception {
        // DATES      
        List<String> sentsNers = new ArrayList();
        List<String> ners = new ArrayList();        
        for (String[] sentence : sentences) {
            // do something with the names
            Span[] nameSpans = _dateFinderME.find(sentence);            
            if (nameSpans.length > 1 ) {
                System.out.println("Spans:" + Arrays.toString(nameSpans));
                // acumulate name spans    
                sentsNers.add(Arrays.toString(nameSpans));                
                // acumulate names 
                for (Span spans : nameSpans) {          
                    String a = sentence[spans.getStart()];
                    //String b = sentence[spans.getEnd()-1];                    
                    System.out.println("Names:" + a);
                    ners.add(a);
                }
            }
        }
        _dateFinderME.clearAdaptiveData();          
        // write to file
        if (sentsNers.size() > 0) {        
            try (FileOutputStream fos = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".datesSpans")); 
                    PrintStream ps = new PrintStream(fos)) {                
                for (String s : sentsNers) { ps.println(s); }
                ps.close();
            }
        }
        // write to file
        if (ners.size() > 0) {
            try (FileOutputStream fos2 = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".dates")); 
                    PrintStream ps2 = new PrintStream(fos2)) {
                for (String t : ners) { ps2.println(t); }
                ps2.close();
            }
        }
        sentsNers.clear();
        ners.clear();        
        
        // LOCATION           
        for (String[] sentence : sentences) {
            // do something with the names
            Span[] nameSpans = _locationFinderME.find(sentence);            
            if (nameSpans.length > 1 ) {
                System.out.println("Spans:" + Arrays.toString(nameSpans));
                // acumulate name spans    
                sentsNers.add(Arrays.toString(nameSpans));                
                // acumulate names 
                for (Span spans : nameSpans) {          
                    String a = sentence[spans.getStart()];
                    //String b = sentence[spans.getEnd()-1];                    
                    System.out.println("Names:" + a);
                    ners.add(a);
                }
            }
        }
        _locationFinderME.clearAdaptiveData();          
        // write to file
        if (sentsNers.size() > 0) {        
            try (FileOutputStream fos = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".locationSpans")); 
                    PrintStream ps = new PrintStream(fos)) {                
                for (String s : sentsNers) { ps.println(s); }
                ps.close();
            }
        }
        // write to file
        if (ners.size() > 0) {
            try (FileOutputStream fos2 = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".location")); 
                    PrintStream ps2 = new PrintStream(fos2)) {
                for (String t : ners) { ps2.println(t); }
                ps2.close();
            }
        }
        sentsNers.clear();
        ners.clear();
        
        // MONEY    
        for (String[] sentence : sentences) {
            // do something with the names
            Span[] nameSpans = _moneyFinderME.find(sentence);            
            if (nameSpans.length > 1 ) {
                System.out.println("Spans:" + Arrays.toString(nameSpans));
                // acumulate name spans    
                sentsNers.add(Arrays.toString(nameSpans));                
                // acumulate names 
                for (Span spans : nameSpans) {          
                    String a = sentence[spans.getStart()];
                    //String b = sentence[spans.getEnd()-1];                    
                    System.out.println("Names:" + a);
                    ners.add(a);
                }
            }
        }
        _moneyFinderME.clearAdaptiveData();          
        // write to file
        if (sentsNers.size() > 0) {        
            try (FileOutputStream fos = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".moneySpans")); 
                    PrintStream ps = new PrintStream(fos)) {                
                for (String s : sentsNers) { ps.println(s); }
                ps.close();
            }
        }
        // write to file
        if (ners.size() > 0) {
            try (FileOutputStream fos2 = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".money")); 
                    PrintStream ps2 = new PrintStream(fos2)) {
                for (String t : ners) { ps2.println(t); }
                ps2.close();
            }
        }
        sentsNers.clear();
        ners.clear();
        
        // ORGANIZATION
        for (String[] sentence : sentences) {
            // do something with the names
            Span[] nameSpans = _organizationFinderME.find(sentence);            
            if (nameSpans.length > 1 ) {
                System.out.println("Spans:" + Arrays.toString(nameSpans));
                // acumulate name spans    
                sentsNers.add(Arrays.toString(nameSpans));                
                // acumulate names 
                for (Span spans : nameSpans) {          
                    String a = sentence[spans.getStart()];
                    //String b = sentence[spans.getEnd()-1];                    
                    System.out.println("Names:" + a);
                    ners.add(a);
                }
            }
        }
        _organizationFinderME.clearAdaptiveData();          
        // write to file
        if (sentsNers.size() > 0) {        
            try (FileOutputStream fos = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".organizationSpans")); 
                    PrintStream ps = new PrintStream(fos)) {                
                for (String s : sentsNers) { ps.println(s); }
                ps.close();
            }
        }
        // write to file
        if (ners.size() > 0) {
            try (FileOutputStream fos2 = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".organization")); 
                    PrintStream ps2 = new PrintStream(fos2)) {
                for (String t : ners) { ps2.println(t); }
                ps2.close();
            }
        }
        sentsNers.clear();
        ners.clear();
        
        // PERCENTAGE      
        for (String[] sentence : sentences) {
            // do something with the names
            Span[] nameSpans = _percentageFinderME.find(sentence);            
            if (nameSpans.length > 1 ) {
                System.out.println("Spans:" + Arrays.toString(nameSpans));
                // acumulate name spans    
                sentsNers.add(Arrays.toString(nameSpans));                
                // acumulate names 
                for (Span spans : nameSpans) {          
                    String a = sentence[spans.getStart()];
                    //String b = sentence[spans.getEnd()-1];                    
                    System.out.println("Names:" + a);
                    ners.add(a);
                }
            }
        }
        _percentageFinderME.clearAdaptiveData();          
        // write to file
        if (sentsNers.size() > 0) {        
            try (FileOutputStream fos = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".percentageSpans")); 
                    PrintStream ps = new PrintStream(fos)) {                
                for (String s : sentsNers) { ps.println(s); }
                ps.close();
            }
        }
        // write to file
        if (ners.size() > 0) {
            try (FileOutputStream fos2 = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".percentage")); 
                    PrintStream ps2 = new PrintStream(fos2)) {
                for (String t : ners) { ps2.println(t); }
                ps2.close();
            }
        }
        sentsNers.clear();
        ners.clear();
        
        // PERSON
        for (String[] sentence : sentences) {
            // do something with the names
            Span[] nameSpans = _personFinderME.find(sentence);            
            if (nameSpans.length > 1 ) {
                System.out.println("Spans:" + Arrays.toString(nameSpans));
                // acumulate name spans    
                sentsNers.add(Arrays.toString(nameSpans));                
                // acumulate names 
                for (Span spans : nameSpans) {          
                    String a = sentence[spans.getStart()];
                    //String b = sentence[spans.getEnd()-1];                    
                    System.out.println("Names:" + a);
                    ners.add(a);
                }
            }
        }
        _personFinderME.clearAdaptiveData();          
        // write to file
        if (sentsNers.size() > 0) {        
            try (FileOutputStream fos = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".personSpans")); 
                    PrintStream ps = new PrintStream(fos)) {                
                for (String s : sentsNers) { ps.println(s); }
                ps.close();
            }
        }
        // write to file
        if (ners.size() > 0) {
            try (FileOutputStream fos2 = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".person")); 
                    PrintStream ps2 = new PrintStream(fos2)) {
                for (String t : ners) { ps2.println(t); }
                ps2.close();
            }
        }
        sentsNers.clear();
        ners.clear();
        
        // TIME
        for (String[] sentence : sentences) {
            // do something with the names
            Span[] nameSpans = _timeFinderME.find(sentence);            
            if (nameSpans.length > 1 ) {
                System.out.println("Spans:" + Arrays.toString(nameSpans));
                // acumulate name spans    
                sentsNers.add(Arrays.toString(nameSpans));                
                // acumulate names 
                for (Span spans : nameSpans) {          
                    String a = sentence[spans.getStart()];
                    //String b = sentence[spans.getEnd()-1];                    
                    System.out.println("Names:" + a);
                    ners.add(a);
                }
            }
        }
        _timeFinderME.clearAdaptiveData();          
        // write to file
        if (sentsNers.size() > 0) {        
            try (FileOutputStream fos = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".timeSpans")); 
                    PrintStream ps = new PrintStream(fos)) {                
                for (String s : sentsNers) { ps.println(s); }
                ps.close();
            }
        }
        // write to file
        if (ners.size() > 0) {
            try (FileOutputStream fos2 = new FileOutputStream(new File(outpath + File.separatorChar + outputName + ".time")); 
                    PrintStream ps2 = new PrintStream(fos2)) {
                for (String t : ners) { ps2.println(t);}
                ps2.close();
            }
        }
        sentsNers.clear();
        ners.clear();
        
    }
    
    
    
    
   
    
        
        
    /**
     *
     * @param file
     * @param outputName
     * @param outputPath
     */
    private void doAction(File file, String outputName, String outputPath) throws FileNotFoundException, IOException {

        String text = "";
        BufferedReader br = new BufferedReader(new FileReader(file));
        try {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();
            while (line != null) {
                sb.append(line);
                sb.append(System.lineSeparator());
                line = br.readLine();
            }
            text = sb.toString();
        } finally {
            br.close();
        }

        try {                  
            // Extract sentences
            String[] sents = _sdetector.sentDetect(text);

            // Extract tokens
            String[][] tokens = new String[sents.length][];
            for (int n = 0; n < sents.length; n++)
            tokens[n] = _tokenizer.tokenize(sents[n]);

            // Perform Lemmatization and save to file
            // applyLemmatizer(tokens, outputName, outputPath);

            // Perform POS tagging and save to file	                
            // applyPOSTagger(tokens, outputName, outputPath);

            // Perform NER
            // applyNER(tokens, outputName, outputPath);
            applyNameFinder(tokens, outputName, outputPath);                

        } catch (Exception e) {
            System.out.println("Analyzers error: " + file.getPath() + " (" + e.toString() + ")");
        }
        // print table results
        //doPrint(outputName, inOutputpath);
        
    }//doAction

    

                   
      /**
     * Apply an action to every file given in inputsPath
     * 
     * see doAction()
     *
     * @throws Exception
     */
    public void doBulkFileAction() throws Exception {
        File tmpDir = new File(tmp);

        File dir = new File(inputpath);
        ArrayList<File> files = new ArrayList<File>();
        AccessUtils.listFilesRecursive(dir, (FilenameFilter) new Filter(), files);
        Map<String, File> filenames = AccessUtils.getsortedFilepaths(files);

        Iterator it = filenames.entrySet().iterator();
        while (it.hasNext()) {
            try {
                Map.Entry e = (Map.Entry) it.next();
                File file = (File) e.getValue();

                String outputName = file.getName().replaceAll(".txt", "");

                System.out.println("Processing file " + (String) e.getKey());                

                //check if folder already exists
                if (!FileUtils.existsDir(tmpDir + file.getParentFile().getName())) {
                    //create folder
                    File folder = AccessUtils.createFolder(tmpDir, file.getParentFile().getName());
                    doAction(file, outputName, folder.getAbsolutePath());
                    
                } else {
                    doAction(file, outputName, tmpDir + file.getParentFile().getName());
                }
                
            } catch (Exception n) {
                System.out.println("doBulkFileAction io error: " + n.getMessage());                
            }
        }
        System.out.println();
    }//doBulkFileAction

    

   
    
    // Filter directories
    private class Filter implements FilenameFilter {
        public boolean accept(File dir, String name) {
            if (!name.contains(".")) {
                return false;
            }
            return true;
        }
    }
    
    
    
    private static void usage() {
        System.err.println("Usage: Analyzer <input folder> <tmp path>]");
    }

	//////////////////////////////////////////////////////////////////
	//                              MAIN
	//////////////////////////////////////////////////////////////////	
	public static void main(String[] args) throws IOException, Exception 
        {
            if (args.length < 2) {
                usage();
                return;
            }
                
            inputpath = args[0];
            tmp = args[1];
            
            Analyzer analyzer = new Analyzer();
            
            // Initialize the tools
            analyzer.init();            
            
            analyzer.doBulkFileAction();
            
            
	}
        
}
