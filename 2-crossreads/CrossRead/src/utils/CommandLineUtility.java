package utils;


import java.util.*;


/**
 *  Utility class to parse command line arguments.
 */
public class CommandLineUtility 
{

    static public HashMap <String, String> getArgs(String[] inArgs)  throws Exception
    {
        return CommandLineUtility.getArgs(inArgs, true);
    }

    
    static public HashMap <String, String> getArgs(String[] inArgs, boolean inMustBePairs)  throws Exception
    {
	if (inMustBePairs)
	    return CommandLineUtility.parseArgumentsPairs(inArgs);
	else
	    return CommandLineUtility.parseArgumentsNoPairs(inArgs);
    }
    
    
    /** 
     * Converts the args[] into a hashmap 
     */
    static private HashMap <String, String> parseArgumentsPairs(String[] inArgs) throws Exception 
    {
	HashMap <String, String> outArgs = new HashMap();		
        String currentKey = null;
	
        for (int i = 0; i < inArgs.length; ++i) 
	{
            String argument = inArgs[i];
            if ((argument != null) && (i % 2 == 0)) 
	    {
                if (!argument.startsWith("-"))
                    throw new Exception("Input arguments format must be: -arg1 value1 -arg2 value2...");

		currentKey = argument.substring(1);
            }
            else if (argument != null) 
	    {
                outArgs.put(currentKey.toLowerCase(), argument);
                currentKey = null;
            }   
        }
	
	return outArgs;
    }//parseArgumentsPairs

    
    /** 
     *	Converts the args[] into a hashmap, allowing args without value: -arg1 -arg2 value2 -arg3 -arg4 -value4...
     *
     *	If args can't be parsed then throw a dummy exception and let caller give wathever error message it wants (i.e. usage)
     */
    static private HashMap <String, String> parseArgumentsNoPairs(String[] args) throws Exception 
    {
	HashMap <String, String> outArgs = new HashMap();	
        String currentKey = null;
	
        for (int i = 0; i < args.length; ++i) 
	{
            String argument = args[i];
            if (argument.startsWith("-"))
	    {
		if (currentKey != null)
		    outArgs.put(currentKey, new String());
		currentKey = argument.substring(1).toLowerCase();
	    }
	    else
	    {
		if (currentKey != null)
		{
		    outArgs.put(currentKey, argument);
		    currentKey = null;
		}
		else
		    throw new Exception();
	    }
        }
	return outArgs;
    }//parseArgumentsNoPairs


    
}
