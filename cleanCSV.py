#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

spark = SparkSession.builder     .appName("TwitterCSV")     .getOrCreate()

path = "/storage/home/mfl5839/work/englishtweets.csv"  # or .csv, name doesn't matter

df = spark.read     .option("header", "true")     .option("sep", ";")     .option("quote", '"')     .option("escape", '"')     .option("multiLine", "true")     .option("mode", "PERMISSIVE")     .csv(path)

clean_df = df.withColumn(
    "text",
    regexp_replace(
        regexp_replace(
            regexp_replace(col("text"), r'[\r\n]', ' '),  # replace newlines with space
            r'[\\\/]', ' '                                # replace backslashes and forward slashes with space
        ),
        r'"', '""'                                      # escape double quotes
    )
)

clean_df = clean_df.select('origen','date','username','user_fullname','n_replies','n_likes','n_retweets','text','tweet_language')

(clean_df.write
   .mode("overwrite")
   .option("header", True)
   .option("quoteAll", True)      # wrap everything in quotes
   .option("escape", '"')         # escape quotes inside text
   .option("multiLine", True)     # handle long text with internal newlines
   .csv("/storage/home/xxx/work/output_folder")) # change to your own directory


# In[ ]:




