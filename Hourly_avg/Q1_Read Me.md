# CloudMapReduce



**Run the command**

#####hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/twitter/* -output myoutput -file *.py -mapper mapTweet.py -reducer reduceTweet.py

Get the output file from Hadoop filesystem to local filesystem as **cloudresults.txt** file using the below command

#####hadoop fs -get myoutput/part-00000 cloudresults.txt

Now run the final program and capture the **final output into output.csv file**. The above text fle and this program should be in the same directory to run.

#####./hourlyAverage.py > output.csv

Using Excel, from output.csv file, we can plot the details.

From output.csv file, we can infer the following.

Total number of tweets the program has parsed and count of tweets that were successfully parsed and also error count saying no. of tweets that were skipped due to an error.

Total no. of days of twitter data parsed, average/expected number of tweets made by president are available for each hour.

**Note:** UTC hours are converted to Eastern Time, by reducing 4 hours’ time, this calculation is done using excel. After conversion, the plots are plotted in excel.
