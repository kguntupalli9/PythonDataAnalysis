# PythonDataAnalysis
In this project, I would like you to familiarize and get hands-on experience with Python by analyzing
the NY Motor Vehicle Collisions data. The Motor Vehicle Collisions table contains details on each
vehicle involved in the crash. Each row represents a motor vehicle involved in a crash. The approach
is to perform some simple analysis on small data sets (taking random samples is the best way) first
to get the hang of analysis. I do realize that some of you are very new to Python; hence, I have
chosen simple problems to exercise different features and packages of Python. In order to get you
up to speed, this project will have sub-problems to solve as described below. You can use them as
milestones to pace yourself.

For this problem, you are given the Motor Vehicle Collisions (MVC) data file (has 3.7M rows, 25
columns) for analysis. The Motor Vehicle Collisions table contains details on each vehicle involved
in the crash. Each row represents a motor vehicle involved in a crash. Data is from 2012 to present
(10 years) daily. Initially, take a small sample of the data set for what you need to do (as given in
the parameters file) and develop your code to analyze them. Once you are convinced your
application is correct, you will run it on the larger specified data set and analyze it for the final
report you will submit. For manual verification, you can choose even a smaller sample set of your
own. Make sure the sample you choose is representative!
The data set has 25 attributes for each vehicle crash with various values for each field. You will only
use a few fields for this project instead of all fields. The data is not complete, as usual, and requires
pre-processing. For example, there are rows with blanks for some columns and some of “No value”
in the column. These need to be considered if they are in the fields that you are using for analysis.
Pre-processing is an integral part of analysis and you need to get used to it.

i) For the make of the vehicles (using the VEHICLE_MAKE attribute) to be processed by
each team, count the number of accidents that each one of those vehicles make were
involved in for each of the years given to you (in the parameter file). Plot them as a bar
graph with vehicle_make on the X-axis and count on the Y-axis. For each vehicle make,
there will be two bars and year can be shown at the top of the bar. This can also be
visualized in other ways. Analyze the vehicle makes for smallest and largest counts using
data from the internet.
ii) Compare monthly accidents (# of accidents in each month) for each vehicle make (using
the vehicle_make attribute) for given years (given to you in the parameter file). Plot
them as a line graph for each vehicle make for every month (as X-axis) and count as Yaxis. Analyze whether some months are more accident prone than others? Try to justify
your findings with data (summer vs winter months, holidays/long weekends, snow
season in New York City, any other events that happen in New York City for that given
