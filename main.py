import findspark 
findspark.init()
from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local[*]").getOrCreate()

# Data Import
# import pandas as pd

# from tkinter import tk     # from tkinter import Tk for Python 3.x
# from tkinter.filedialog import askopenfilename

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# Initializing and configuring SparkSession
# Setting up the SparkSession to run locally with all available cores
spark = SparkSession.builder.master("local[*]").getOrCreate()

# Reading the data from a CSV file into a DataFrame
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").option("mode", "failfast").load("/Volumes/DATA/Datasets/pseudo_facebook.csv")

# Creating a temporary view for the DataFrame to perform SQL queries
df.createOrReplaceTempView('fb')

# Displaying the data from the temporary view
spark.sql("select * from fb").show()

# Counting the total number of records in the DataFrame
spark.sql("select count(*) from fb").show()

# Calculating the average age of the individuals in the dataset
spark.sql("select round(avg(age),0) from fb").show()

# Counting the number of Males and Females in the dataset
spark.sql("select gender,count(gender) from fb group by gender").show()

# Calculating the average age of individuals based on gender
spark.sql("select gender,avg(age) from fb group by gender").show()

# Calculating the average age and adding 2 to the result
x = spark.sql("select avg(age) from fb").collect()[0][0]
print(x + 2)

# Counting the number of users who have received mobile likes on Facebook
spark.sql("select count(mobile_likes_received) from fb").show()

# Counting the number of users who have registered their mobile number on Facebook
spark.sql("select count(*) from fb where mobile_likes_received is not null").show()

# Finding the average likes received for each gender and sorting in descending order
spark.sql("select gender,avg(likes_received) as avg_likes from fb group by gender order by avg_likes desc").show()

# Finding the average friend count for individuals aged between 18 and 50
spark.sql("select avg(friend_count) from fb where age >= 18 and age <= 50").show()

# Finding the average mobile likes and website likes based on gender for individuals aged between 18 and 50
spark.sql("select gender,avg(mobile_likes),avg(www_likes) from fb where age >= 18 and age <= 50 group by gender").show()

# Finding the average friend count for each age group and sorting by age in ascending order
df.groupBy("age").avg("friend_count").orderBy("age").show(100)

# Calculating the correlation between age, friend count, and likes received
corr_matrix = df.stat.corr("age", "friend_count")
corr_matrix = df.stat.corr("age", "likes_received")
corr_matrix = df.stat.corr("likes_received", "friend_count")
print(corr_matrix)
