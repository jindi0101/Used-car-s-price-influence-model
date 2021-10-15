import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;



public class Sum{
	public static class SumMapper extends Mapper<Object, Text, Text, IntWritable>{
		public void map(Object key, Text rows, Context context)
		throws IOException, InterruptedException{
			int num = Integer.parseInt(row[3]);
			String[] row = rows.toString().replace("'", "").replace(" ", "").split(",");
			float  elderly_population_ratio = Float.parseFloat(row[2]);
			if( elderly_population_ratio >= 20){
				context.write(new Text(row[0]), new IntWritable(num));
				System.out.println(context);
			}
		}
	}

   
	public static class SumReducer extends Reducer<Text, IntWritable, Text, IntWritable>{
		private IntWritable result = new IntWritable();
		public void reduce(Text province, Iterable<IntWritable> nur_count, Context context)
		throws IOException, InterruptedException{
			int a = 0;
			for (IntWritable i : nur_count){
				a += i.get();
			}
			result.set(a);
			context.write(province, result);
			System.out.println(context);
		}
	}

	public static void main(String[] args) throws Exception{
		Configuration con = new Configuration();
        Job j = Job.getInstance(con, "a");
        j.setNumReduceTasks(1);
        j.setJarByClass(Sum.class);
        j.setMapperClass(SumMapper.class);
        j.setReducerClass(SumReducer.class);
        j.setOutputKeyClass(Text.class);
        j.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(j, new Path(args[0]));
        FileOutputFormat.setOutputPath(j, new Path(args[1]));
        System.exit(j.waitForCompletion(true) ? 0 : 1);

	}

}