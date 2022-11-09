from pandas._libs.tslibs import ccalendar
import pandas as pd
from google.colab import drive
import numpy as np
import matplotlib.pyplot as plt
import re  
import datetime
import calendar
import plotly.express as px
import itertools

drive.mount('/content/drive')
#path="/content/drive/MyDrive/Book2.csv"
df = pd.read_csv("/content/drive/MyDrive/Motor_Vehicle_Collisions_-_Vehicles.csv")
#df.describe
#changing the CRASH_DATE from string to datatime format
df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'])
#splitting the CRASH_DATE Into monthname and year columns
df['YEAR'], df['MONTH'] = df['CRASH_DATE'].dt.year, df['CRASH_DATE'].dt.month_name()
#extracting the data for the mentioned years acc to parameter file
start_date = '2017-06-01'
end_date = '2019-05-31'
mvc_data= df.query('CRASH_DATE >= @start_date and CRASH_DATE <= @end_date')
mvc_data.to_csv('/content/drive/MyDrive/MVCnew.csv')
# final file which will be used for analysis
df1 = pd.read_csv("/content/drive/MyDrive/MVCnew.csv",usecols=["CRASH_DATE","YEAR","MONTH","VEHICLE_MAKE","VEHICLE_TYPE"])
#dropping the null values in VEHICLE_MAKE COLUMN
df1 = df1.dropna(subset = ["VEHICLE_MAKE"])
#df10=df1.sample(2000, random_state = 2131998)
#Extracting the data into 3 diff DFs based on years
df2 = df1[df1['YEAR'] == 2017]
df3 = df1[df1['YEAR'] == 2018]
df4 = df1[df1['YEAR'] == 2019]

n=4
r = np.arange(n)
width = 0.25
fig = plt.figure(figsize = (15, 10))

#creating a new DF and counting the sum of each vehicle type in that specific year
Data2017 = [df2.VEHICLE_MAKE.str.count('CHRY').sum(),
         df2.VEHICLE_MAKE.str.count('JEEP').sum(),
         df2.VEHICLE_MAKE.str.count('NISS').sum(), 
         df2.VEHICLE_MAKE.str.count('LNDR').sum()]
bar1 = plt.bar(r, Data2017, width, color = 'r')


Data2018 = [df3.VEHICLE_MAKE.str.count('CHRY').sum(),
         df3.VEHICLE_MAKE.str.count('JEEP').sum(),
         df3.VEHICLE_MAKE.str.count('NISS').sum(), 
         df3.VEHICLE_MAKE.str.count('LNDR').sum()]
bar2 = plt.bar(r+width, Data2018, width, color = 'g')

Data2019 = [df4.VEHICLE_MAKE.str.count('CHRY').sum(),
         df4.VEHICLE_MAKE.str.count('JEEP').sum(),
         df4.VEHICLE_MAKE.str.count('NISS').sum(), 
         df4.VEHICLE_MAKE.str.count('LNDR').sum()]
bar3 = plt.bar(r+width+0.25, Data2019, width, color = 'b')

print ("Data2019 ======>",Data2019)
print ("Data2018======>",Data2018)
print ("Data2017======>",Data2017)

plt.xlabel("Vehicle make")
plt.ylabel("CRASH COUNT")
plt.title("NO OF CRASHES IN EACH YEAR")

plt.xticks(r + width,['CHRY','JEEP','NISS','LNDR'])
plt.legend((bar1, bar2, bar3), ('2017', '2018','2019') )

plt.show()
# Bar graph ends here

# line graph begins here
# moving each different type of VEHICLE_MAKE into 4 diff DFs
df21= df1[df1["VEHICLE_MAKE"].str.contains("CHRY", na=False)]
#df21.describe
df22 = df1[df1["VEHICLE_MAKE"].str.contains("JEEP", na=False)]
df23 = df1[df1["VEHICLE_MAKE"].str.contains("NISS", na=False)]
df24 = df1[df1["VEHICLE_MAKE"].str.contains("LNDR", na=False)]

# counting the number of accidents for each month for each vehicle type
datachry = df21['MONTH'].value_counts().rename_axis('MONTH').reset_index(name='CHRY')
datajeep = df22['MONTH'].value_counts().rename_axis('MONTH').reset_index(name='JEEP')
dataniss = df23['MONTH'].value_counts().rename_axis('MONTH').reset_index(name='NISS')
datalndr = df24['MONTH'].value_counts().rename_axis('MONTH').reset_index(name='LNDR')

# from above we get the count (accidents in each month) but in descending order, to sort the months in chronological we use below
sort_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
datachry.index = pd.CategoricalIndex(datachry['MONTH'], categories=sort_order, ordered=True)
datachry = datachry.sort_index().reset_index(drop=True)

datajeep.index = pd.CategoricalIndex(datajeep['MONTH'], categories=sort_order, ordered=True)
datajeep = datajeep.sort_index().reset_index(drop=True)

dataniss.index = pd.CategoricalIndex(dataniss['MONTH'], categories=sort_order, ordered=True)
dataniss = dataniss.sort_index().reset_index(drop=True)

datalndr.index = pd.CategoricalIndex(datalndr['MONTH'], categories=sort_order, ordered=True)
datalndr = datalndr.sort_index().reset_index(drop=True)

print(datachry)
print(datajeep)
print(dataniss)
print(datalndr)
# Plot a simple line chart
plt.rcParams["figure.figsize"]=[11,5]
plt.rcParams["figure.autolayout"] = True
plt.title("MONTHLY ACCIDENTS COUNT")
plt.xlabel("MONTHS")
plt.ylabel("CRASH COUNT")
#xticks is used for length of x axis
plt.xticks(np.arange(12), sort_order)

plt.plot(dataniss['MONTH'], dataniss['NISS'],label = "NISS")
plt.plot(datajeep['MONTH'], datajeep['JEEP'], label = "JEEP")
plt.plot(datachry['MONTH'], datachry['CHRY'],label = "CHRY")
plt.plot(datalndr['MONTH'], datalndr['LNDR'],label = "LNDR")

plt.legend()
plt.show()
#line graph ends here

#piechart begins here
#Replacing the Vehicle_type according to the parameter file
#replace(to_replace ="oldvalue",value=newvalue) inplace = true is to make the changes in original dataframe
df1['VEHICLE_TYPE'].replace(to_replace="BUS",value="Bus",inplace = True)
df1['VEHICLE_TYPE'].replace(to_replace="MOTORCYCLE",value="Motorcycle",inplace = True)
df1['VEHICLE_TYPE'].replace(to_replace="TAXI",value="Taxi",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="VAN",value="Van",inplace = True)
df1['VEHICLE_TYPE'].replace(to_replace="PICK-UP TRUCK",value="Truck",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="Box truck",value="Truck",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="BICYCLE",value="Bicycle",inplace = True)
df1['VEHICLE_TYPE'].replace(to_replace="SPORT UTILITY",value="Sport Utility Vehicle",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="STATION WAGON",value="Sport Utility Vehicle",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="Station Wagon",value="Sport Utility Vehicle",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="Station Wagon/Sport Utility Vehicle",value="Sport Utility Vehicle",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="4 dr sedan",value="Sedan",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="SEDAN",value="Sedan",inplace =True)
df1['VEHICLE_TYPE'].replace(to_replace="2 dr sedan",value="Sedan",inplace =True)
#Dropping the VEHICLE_TYPE = UNKNOWN fields
df1= df1[df1.VEHICLE_TYPE!='UNKNOWN']
#printing the unique values for VEHICLE_TYPE for reference
#print(df1.VEHICLE_TYPE.unique())
#taking the 10 values referred in parameter file for file in VEHICLE_TYPE Column
df1=df1[(df1['VEHICLE_TYPE']=='Bus') | 
        (df1['VEHICLE_TYPE']=='Motorcycle') |
        (df1['VEHICLE_TYPE']=='Taxi') |
        (df1['VEHICLE_TYPE']=='Truck') |
        (df1['VEHICLE_TYPE']=='Sport Utility Vehicle') |
        (df1['VEHICLE_TYPE']=='Sedan') |
        (df1['VEHICLE_TYPE']=='Van') |
        (df1['VEHICLE_TYPE']=='Bike') |
        (df1['VEHICLE_TYPE']=='PASSENGER VEHICLE') |
        (df1['VEHICLE_TYPE']=='Bicycle')]
#counting the number od each VEHICLE_TYPE
values=df1.groupby('VEHICLE_TYPE').size()
label=sorted(set(df1['VEHICLE_TYPE']))
#autopct gives the percentage in piechart
plt_1 =plt.figure(figsize=(15,13))
plt.pie(values,labels=label,autopct='%1.1f%%', explode=None,shadow=True, startangle=0)
patches, texts = plt.pie(values,shadow=True, startangle=0,explode=None)

plt.legend(patches,label, loc="best")
plt.title('VEHICLE TYPE')
plt.axis('equal')
plt.show()

print(values)
