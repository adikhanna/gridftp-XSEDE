import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;

class Automator_Stampede {
	public static void main(String []args) throws IOException, InterruptedException{

    String source = " gsiftp://gridftp.stampede.tacc.xsede.org/scratch/04917/tg842162/data/";
    String destination = " gsiftp://oasis-dm.sdsc.edu/oasis/projects/nsf/sub102/avkhann2/data/";

		// Datasets defined below

		String dataset[] = {"tiny/", "small/", "medium/", "large/"};
		String setnames[] = {"Tiny", "Small", "Medium", "Large"};

		// Writer to data collection file

		Writer writer = new BufferedWriter(new OutputStreamWriter(
									new FileOutputStream("stampede-comet6.txt"), "utf-8"));

		String pp = " -ppq ";
		String cc = " -cc ";
		String p = " -p ";

		// Levels of different parameters

		int[] pipelining = {10, 5, 3, 1};
		int[] concurrency = {1, 2, 4, 8, 16, 32};
		int[] parallelism = {1, 2, 4, 8, 16, 32};

		Process q;

		writer.write("Source: Stampede" + "\n" + "Destination: Comet" + "\n");
		writer.flush();

		for (int j = 0; j < 4; j++)																									// For each dataset
		{
				for (int x = 0; x < 6; x++)																							// For every level of parallelism
				{
						for (int y = 0; y < 6; y++)																					// For every level of concurrency
						{
								String command = "globus-url-copy -vb -nodcau -st 0" + pp + pipelining[j] + p + parallelism[x] + cc + concurrency[y] + source + dataset[j] + destination + dataset[j];
								writer.write("\n" + command + "\n");
								writer.flush();

								writer.write("Dataset: " + setnames[j] + "\n");
								writer.flush();
								writer.write("Pipelining = " + pipelining[j] + ", Parallelism = " + parallelism[x] + ", Concurrency = " + concurrency[y] + "\n");
								writer.flush();

								java.util.Date date = new java.util.Date();
					    	writer.write("Date & Time of transfer: " + date + "\n");
								writer.flush();

								double start = System.currentTimeMillis();

								// Execute file transfer

								q = Runtime.getRuntime().exec(command);

								// Displays terminal output while command is being executed

								BufferedReader reader = new BufferedReader(new InputStreamReader(q.getInputStream()));
								String line = "";
								while((line = reader.readLine()) != null)
								{
									System.out.print(line + "\n");
								}

								q.waitFor();

								double end = System.currentTimeMillis();

								// Calculates time duration of transfer

								double time = end - start;
								writer.write("Time taken in seconds = " + (time/1000.0) + "\n");
								writer.flush();
						}
				}
		}
		writer.close();
   }
}
