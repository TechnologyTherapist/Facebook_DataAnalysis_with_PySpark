# Facebook_DataAnalysis_with_PySpark
This project demonstrates the analysis of a Facebook dataset using PySpark, a Python library for distributed data processing. The dataset contains information about Facebook users, including their demographics, relationship status, friend count, and likes received.

Getting Started
To run this project, follow the steps below:
Prerequisites
•	Python 3.x
•	Apache Spark (with PySpark)
•	Jupyter Notebook (optional)
Installation
1.	Clone the repository:
https://github.com/TechnologyTherapist/Facebook_DataAnalysis_with_PySpark.git

2.	Install the required dependencies:
pip install findspark

3.	Download the Facebook dataset (pseudo_facebook.csv) and place it in the project directory.
Usage
1.	Import the required modules and initialize SparkSession.
2.	Read the dataset from the CSV file into a DataFrame.
3.	Perform various data analysis tasks using Spark SQL and DataFrame operations. The tasks include:
•	Displaying the data from the dataset.
•	Counting the total number of records.
•	Calculating the average age of the individuals.
•	Counting the number of males and females.
•	Calculating the average age based on gender.
•	Counting the number of users with mobile likes received.
•	Counting the number of users with a registered mobile number.
•	Finding the average likes received for each gender and sorting in descending order.
•	Finding the average friend count for individuals aged between 18 and 50.
•	Finding the average mobile likes and website likes based on gender for individuals aged between 18 and 50.
•	Finding the average friend count for each age group and sorting by age in ascending order.
•	Calculating the correlation between age, friend count, and likes received.
4.	Run the code and observe the results.
Results
The results of the data analysis tasks are displayed in the console output. The insights obtained from the analysis include:
•	Distribution of relationship statuses among Facebook users.
•	Average age of the individuals in the dataset.
•	Count of males and females in the dataset.
•	Average age based on gender.
•	Number of users with mobile likes received.
•	Number of users with a registered mobile number.
•	Average likes received for each gender.
•	Average friend count for individuals aged between 18 and 50.
•	Average mobile likes and website likes based on gender for individuals aged between 18 and 50.
•	Average friend count for each age group.

The project also calculates the correlation between age, friend count, and likes received, providing insights into potential relationships between these variables.

Contributing
Contributions to this project are welcome. You can contribute by opening an issue to suggest improvements or submitting a pull request with new features or bug fixes.

License
This project is licensed under the MIT License.

Acknowledgments
•	The Facebook dataset used in this project is provided by YourDataTeacher.
•	The project is based on the PySpark library, developed by the Apache Spark community.


