/*
 * AccessUtils.java
 *
 * Created on 3 de mayo de 2007, 1:17
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package utils;

import java.io.*;
import java.net.*;
import java.util.*;


/**
 *
 * @author Nedjet
 */
public class AccessUtils 
{

     public static boolean existsFile(String filePath) {
            if (StringUtils.emptyString(filePath))
                return false;
            File thisFile = new File(filePath);
            if (thisFile.exists())
                return true;
            return false;
        }  
     
      public static boolean existsDir(String dirPath) {
            if (StringUtils.emptyString(dirPath))
                return false;
            File thisFile = new File(dirPath);
            if (thisFile.exists() && thisFile.isDirectory())
                return true;
            return false;
        }
      
      public static String getFileNameWithoutExtension(String filePath) {
          return filePath.substring(0,filePath.lastIndexOf("."));
      }

	
      /**
       *    Read file to String using default encoding.
       */
       public static String loadFileToString(String inFilePath) throws Exception 
      {
         String thisString = "";
         if (!existsFile(inFilePath))
             throw new Exception("File does not exist: " + inFilePath);

 	try
	{
	     FileReader fr = new FileReader(inFilePath);
	     BufferedReader br = new BufferedReader(fr);
	     String line = br.readLine();
	     while (line != null) 
	     {
		 thisString = thisString + line + "\n";
		 line = br.readLine();
	     }

	     br.close();
	     fr.close();
	     return thisString;
	}
	catch (Exception e)
	{
	    throw new Exception("File can't be read: " + inFilePath + " (" + e.toString() + ")");
	}	
     }

      
      /**
       *    Read file to String enforcing UTF8 encoding.
       */
      public static String loadFileToStringUTF8(File inFile) throws Exception 
      {
         if (inFile.exists() == false)
             throw new Exception("File does not exist: " + inFile.getPath());

 	try
	{
	     FileInputStream fileStream = new FileInputStream(inFile);
	     BufferedReader fileReader = new BufferedReader(new InputStreamReader(fileStream, "UTF-8"));
	     String line = fileReader.readLine();
	     String contentsString = "";
	     
	     while (line != null) 
	     {
		 contentsString = contentsString + line + "\n";
		 line = fileReader.readLine();
	     }

	     fileReader.close();
	     fileStream.close();
	     
	     return contentsString;
	}
	catch (Exception e)
	{
	    throw new Exception("File can't be read: " + inFile.getPath() + " (" + e.toString() + ")");
	}	
     }

     
    /**
      *	Returns the path to a resource file as a url contained in a string.
      */
     public static String getResourcePath(String inResourceName) throws Exception 
     {
	URL resourcePath = AccessUtils.class.getResource(inResourceName);
        if (resourcePath == null)
	    throw new Exception("Resource does not exist: " + inResourceName);
	
	return resourcePath.toString();
	//String path = resourcePath.getPath();
	//return URLDecoder.decode(path, "UTF-8");
     }
     
 
     /**
      *	Returns the content of a resource file as a UTF-8 encoded string.
      */
     public static String loadResourceToString(String inResourceName) throws Exception 
     {
		InputStream resourceStream = AccessUtils.class.getResourceAsStream(inResourceName);
        if (resourceStream == null)
	    throw new Exception("Resource does not exist: " + inResourceName);

	try
	{
	    BufferedReader resourceReader = new BufferedReader(new InputStreamReader(resourceStream, "UTF-8"));
	    String line = resourceReader.readLine();
	    String contentsString = "";

	    while (line != null) 
	    {
		contentsString = contentsString + line + "\n";
		line = resourceReader.readLine();
	    }

	    resourceReader.close();
	    resourceStream.close();
	    
	    return contentsString;
	}
	catch (Exception e)
	{
	    throw new Exception("Resource can't be read: " + inResourceName + " (" + e.toString() + ")");
	}
    }

 
     public static boolean isAbsolute(String filePath) {
         File thisFile = new File(filePath);
         if (thisFile.isAbsolute())
             return true;
         else
             return false;
     }

     
     public static boolean existsURL(String URLName){
          try {
                        HttpURLConnection.setFollowRedirects(false);
                        // note : you may also need HttpURLConnection.setInstanceFollowRedirects(false)
                        HttpURLConnection con = (HttpURLConnection) new URL(URLName).openConnection();
                        con.setRequestMethod("HEAD");
                        return (con.getResponseCode() == HttpURLConnection.HTTP_OK);
          }
          catch (Exception e) {
                   e.printStackTrace();
                   return false;
          }
    }
       
   /*
    * We replace the hostname with localhost:8080 before checking URL exists 
    * Needed for patexpert server name, as due to some configuration issues, patexpert server cannot check itself 
    * (as name means redirect to other server...)
    * In the future, port number should be from properties file...
    */
    public static boolean existsLocalHostURL(String URLName) throws Exception
    { 
	try {
	    String localURLName = URLName;
	    String regex = "([^:]+://)[^/]+(/.+)";
	    if (localURLName.matches(regex)) {
	    localURLName = localURLName.replaceFirst(regex,"$1localhost:8080$2");
	    }
	    else {
		throw new Exception("URL name cannot be matched to localhost: "+URLName);
	    }

	    HttpURLConnection.setFollowRedirects(false);
	    // note : you may also need HttpURLConnection.setInstanceFollowRedirects(false)
	    HttpURLConnection con = (HttpURLConnection) new URL(localURLName).openConnection();
	    con.setRequestMethod("HEAD");
	    return (con.getResponseCode() == HttpURLConnection.HTTP_OK);
	}
	catch (Exception e) {
		e.printStackTrace();
		return false;
	}
    }
	
	
    /**
    *	Recursive method, returns all files under inFolder tree, filtered with inFilter.
    */
    public static void listFilesRecursive(File inFolder, FilenameFilter inFilter, List<File> inOutFiles)
    {
	// First add the files filtered by inFilter
	List<File> filteredFiles = Arrays.asList(inFolder.listFiles(inFilter));
	inOutFiles.addAll(filteredFiles);
	
	// Then call this method for each subfolder
	List<File> allFles = Arrays.asList(inFolder.listFiles());
	for (File item : allFles)
	{
	    if (item.isDirectory())
		listFilesRecursive(item, inFilter, inOutFiles);
	}
    }
    
    
    /**
     *	Given an list of File objects returns a map containing their respective filenames associated to the File objects,
     *	all sorted lexicographically.
     */
    public static TreeMap<String, File> getSortedFilenames(List<File> inFiles)
    {
	TreeMap<String, File> filenames = new TreeMap<String, File>();
  	for (File file : inFiles)
	{
	    //filenames.put(file.getName(), file);

            filenames.put(file.getPath(), file);

	}
	
	return filenames;
    }

    /**
     *	Given an list of File objects returns a map containing their respective filenamespaths associated to the File objects,
     *	all sorted lexicographically. This method assure that all the file are map, even those with the same file name in different folders names
     */
    public static TreeMap<String, File> getsortedFilepaths(List<File> inFiles)
    {
	TreeMap<String, File> filenames = new TreeMap<String, File>();
  	for (File file : inFiles)
	{
	    //filenames.put(file.getName(), file);

            filenames.put(file.getPath(), file);

	}

	return filenames;
    }

	
	/**
	 * Just create a file named inFileName relative to inParentFolder.
	 */
	public static File createFile(File inParentFolder, String inFileName) throws IOException
	{
		File file = new File(inParentFolder, inFileName);
		if (!file.exists())
			file.createNewFile();

		return file;
	}
	
	/**
	 * Create folder named infolderName relative to inParentFolder. FILE.UTILS
	 */
	public static File createFolder(File inParentFolder, String inFolderName) throws IOException
	{
		File folder = new File(inParentFolder, inFolderName);
		if (!folder.exists())
			folder.mkdir();
		
		return folder;
	}
	
	
}
        
