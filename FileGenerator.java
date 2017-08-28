
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Random;


class FileGenerator {
	public static void main(String []args) throws IOException, InterruptedException{

		String path = "/home/avkhann2/Desktop/data";
		Process p;
		Random rand = new Random();

		int i = 0;
		int count = 0;

		int min = 1;
		int max = 10;

		/* Tiny file sizes are between 1 and 10 MB, hence the min & max values are
				set to  1 and 10 respectively */

		

		System.out.println("Tiny files");

                count += 15000;
		for (; i < count; i++)
		{
			int random = rand.nextInt(max-min+1)+min;
			//System.out.println(random);
			//String command = "dd if=/dev/zero of="+path+i+" bs=1K count=0 seek="+random;
 			String command = "dd if=/dev/zero of="+path + "/tiny/"+i+" bs=1M count="+random;
			System.out.println(i+")"+printSize(random));
			p = Runtime.getRuntime().exec(command);
			p.waitFor();
		}


		//System.out.println("Small files");

		

		/* Small file sizes are between 10 and 50 MB, hence the min & max values are
				set to 10 and 50 respectively */

/*

				min = 10;
				max = 50;


		count+=1200;
		for (; i < count; i++) {
			int random = rand.nextInt(max-min+1)+min;
			//System.out.println(random);
			//String command = "dd if=/dev/zero of="+path+i+" bs=1K count=0 seek="+random;
			 String command = "dd if=/dev/zero of="+path+"/small/"+i+" bs=1M count="+random;
			System.out.println(i+")"+printSize(random));
			p = Runtime.getRuntime().exec(command);
			p.waitFor();
		}

		min = 50;
		max = 250;

*/

		/* Medium file sizes are between 50 and 250 MB, hence the min & max values are
				set to 50 and 250 respectively */

/*
for (; i < count; i++) {
		System.out.println("Medium files");

		count+=270;
			int random = rand.nextInt(max-min+1)+min;
	    //String command = "dd if=/dev/zero of="+path+i+" bs=1K count=0 seek="+random;
			String command = "dd if=/dev/zero of="+path+"/medium/"+i+" bs=1M count="+random;
			System.out.println(i+")"+printSize(random));
			p = Runtime.getRuntime().exec(command);
			p.waitFor();
		}

		min =  250;
		max = 1000;

		/* Large file sizes are between 250 MB and 1 GB, hence the min & max values are
				set to 250 and 1000 */

		//System.out.println("Large files");

		/* Hardcoded to generate 30 3 GB files */

		//count += 30;

		//for (; i < count; i++) {
			//int random = rand.nextInt(max-min+1)+min;
		//	int random = 3000;
			//System.out.println(random);
			//String command = "dd if=/dev/zero of="+path+i+" bs=1K count=0 seek="+random;
		//	System.out.println(i+")"+printSize(random));
		//	String command = "dd if=/dev/zero of="+path +"/large_new/"+i+" bs=1M count="+random;
		//	p = Runtime.getRuntime().exec(command);
		//	p.waitFor();
		//}

		/*
		min = 10*1024*1024; //10G
		max = 20*1024*1024; //20G
		count+=3;
		for (; i < count; i++) {
			int random = rand.nextInt(max-min+1)+min;
			//System.out.printf("%d",random);
			//String command = "dd if=/dev/zero of="+path+i+" bs=1K count=0 seek="+random;
			String command = "dd if=/dev/zero of="+path + "/huge/" +i+" bs=1K count="+random;
			System.out.println(i+")"+printSize(random));
			p = Runtime.getRuntime().exec(command);
			p.waitFor();
		}
		*/
	}
	static String printSize(int random)
	{
		String output;
		double size ;
		DecimalFormat df = new DecimalFormat("###.#");
		if(random<1024)
			return df.format(random)+"MB";
		else if(random<1024*1024)
			return df.format(random/1024.0)+"GB";
		else
			return df.format(random/(1024*1024))+"TB";
	}
}
