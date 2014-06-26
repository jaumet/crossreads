package utils;


import java.io.*;
/**
 *
 * @author Nedjet
 */    
    class StreamGobbler extends Thread {
    InputStream is;
    OutputStream os;
    String type;
    
    StreamGobbler(InputStream is, OutputStream os,String type) {
        this.is = is;
        this.os = os;
        this.type = type;
    }
    
    public void run()
    {
        try
        {
            PrintWriter pw = null;
            if (os != null)
                pw = new PrintWriter(os);
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            String line=null;   
            while ( (line = br.readLine()) != null)  {
                if (type.equals("ERROR")) {
                    System.out.println(line);
                }
                else if (type.equals("OUTPUT")) {
                    if (pw==null)
                        System.out.println(line);
                    else
                        pw.println(line);  
                }       
            }
            if (pw != null)
                pw.flush();

            } catch (IOException ioe)
              {
                ioe.printStackTrace();  
              }
    }
}

public class Execs {
        public static final String WIN_COMMAND_0 = "cmd.exe";
        public static final String WIN_COMMAND_1 = "/C";
        public static final String LINUX_COMMAND_0 = "/bin/sh";
        public static final String LINUX_COMMAND_1 = "-c";
	public static boolean verbose = false; //please! :P
        

	public static void execCommand(String command) throws Exception {
            try {            
                String[] cmd = new String[1];
                cmd[0] = command;
                cmd = setOSCommand(cmd);
                command = StringUtils.arrayToString(cmd);
                if (verbose) System.out.println("Executing command: "+command);
             
                Runtime rt = Runtime.getRuntime();
                Process proc = rt.exec(cmd);
                // any error message?
                StreamGobbler errorGobbler = new StreamGobbler(proc.getErrorStream(),null,"ERROR");            
    
                // any output?
                StreamGobbler outputGobbler = new StreamGobbler(proc.getInputStream(),null,"OUTPUT");

                // kick them off
                errorGobbler.start();
                outputGobbler.start();

                int exitVal = proc.waitFor();
                while (errorGobbler.isAlive() ||outputGobbler.isAlive()) 
		{
                    if (verbose) System.out.print(".");
                    Thread.sleep(10);
                }
                //proc.destroy();       
                if (verbose) System.out.println("Done!");
            } catch (Throwable t)
              {
                t.printStackTrace();
              }
	}//execCommand
        
        public static void execCommand(String command,String outputFile) throws Exception {
           try {            
                String[] cmd = new String[1];
                cmd[0] = command;
                cmd = setOSCommand(cmd);
                command = StringUtils.arrayToString(cmd);
                if (verbose) System.out.println("Executing command: "+command);
                FileOutputStream thisFileOutputStream = new FileOutputStream(outputFile);
                
                Runtime rt = Runtime.getRuntime();
                Process proc = rt.exec(cmd);
                // any error message?
                StreamGobbler errorGobbler = new StreamGobbler(proc.getErrorStream(),thisFileOutputStream,"ERROR");            
    
                // any output?
                StreamGobbler outputGobbler = new StreamGobbler(proc.getInputStream(),thisFileOutputStream,"OUTPUT");
                
                // kick them off
                errorGobbler.start();
                outputGobbler.start();

                int exitVal = proc.waitFor();
                while (errorGobbler.isAlive() ||outputGobbler.isAlive()) 
		{
                    if (verbose) System.out.print(".");
                    Thread.sleep(10);
                }
                //proc.destroy();     
                thisFileOutputStream.flush();
                thisFileOutputStream.close();
                if (verbose) System.out.println("Done!");
            } catch (Throwable t)
              {
                t.printStackTrace();               
              }
        }         
        
     public static String doCommand(String dir,String command,String label,String identifier,boolean stdout) throws Exception {
           String outputFile = dir + "/" + label + "_" + identifier + ".txt";
           if (stdout) {
               Execs.execCommand(command,outputFile);
           }
           else {
               command = command +" "+outputFile;
               Execs.execCommand(command);
           }
           return outputFile;
    }
     
     /*
      * if operating system is Windows then append cmd.exe, else return command
      */
     public static String[] setOSCommand(String cmd) {
         String[] cmdArray = new String[1];
         cmdArray[0] = cmd;
         return setOSCommand(cmdArray);
     }
     
    
      public static String[] setOSCommand(String[] cmd) {
        String os = System.getProperty("os.name");
        String[] newCmd=cmd;
        if (os.startsWith("Windows")) {
            newCmd = new String[cmd.length+2];
            newCmd[0] = WIN_COMMAND_0;;
            newCmd[1] = WIN_COMMAND_1;
            for (int i=0;i<cmd.length;i++) {
                newCmd[i+2]=cmd[i];
              //  newCmd[i+2] = newCmd[i+2].replaceAll("\"","");
            }
        }
        else if (os.startsWith("Linux") || os.startsWith("Mac OS X")) 
        {
            newCmd = new String[cmd.length+2];
            newCmd[0] = LINUX_COMMAND_0;
            newCmd[1] = LINUX_COMMAND_1;
            for (int i=0;i<cmd.length;i++) {
                newCmd[i+2]=cmd[i];
                //newCmd[i+2] = newCmd[i+2].replaceAll("\"","");
            }
        }
            
       return newCmd;
    }
      
}

