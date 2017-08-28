import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;

class Automator_Supermic {
	public static void main(String []args) throws IOException, InterruptedException{

    String source = " gsiftp://smic1.hpc.lsu.edu/work/akhanna/data/";
    String destination = " gsiftp://gridftp.bridges.psc.edu/pylon5/ci560np/avkhann2/data/";

		String dataset[] = {"tiny/", "small/", "medium/", "large/"};
		String setnames[] = {"Tiny", "Small", "Medium", "Large"};

		Writer writer = new BufferedWriter(new OutputStreamWriter(
              new FileOutputStream("supermic-bridges9.txt"), "utf-8"));

		String pp = " -ppq ";
		String cc = " -cc ";
		String p = " -p ";

		int[] pipelining = {10, 5, 3, 1};
		int[] concurrency = {1, 2, 4, 8, 16, 32};
		int[] parallelism = {1, 2, 4, 8, 16, 32};

		Process q;

		writer.write("Source: Supermic" + "\n" + "Destination: Bridges" + "\n");
		writer.flush();

		for (int j = 0; j < 4; j++)
		{
				for (int x = 0; x < 6; x++)
				{
						for (int y = 0; y < 6; y++)
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

								q = Runtime.getRuntime().exec(command);

								BufferedReader reader = new BufferedReader(new InputStreamReader(q.getInputStream()));
		 						String line = "";
		 						while((line = reader.readLine()) != null)
		 						{
				 					System.out.print(line + "\n");
		 						}

								q.waitFor();

								double end = System.currentTimeMillis();
								double time = end - start;
								writer.write("Time taken in seconds = " + (time/1000.0) + "\n");
								writer.flush();
						}
				}
		}
		writer.close();
   }
}
