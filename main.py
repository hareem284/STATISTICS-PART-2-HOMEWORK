

#SORRY THAT I DID NOT DO THE BIN RANGE I FORGOT HOW SO AFTER THIS I AM GOING TO PRACTICE ON BIN RANGE....


#importing matplotlib
import matplotlib.pyplot as plt
#importing statistics
import statistics as st
#importing pandas
import pandas as pd
#reading dataframe
rdf=pd.read_csv("Bestsellers with categories (1).csv")
print(rdf.info())
#checking for any null values
rdf.isnull().any()
#checking the standard deviation
sduserrating=st.stdev(rdf['User Rating'])
print("The standard deviation of User rating is ",sduserrating)
#
#
sdPrice=st.stdev(rdf['Price'])
print("The standard deviation of price is ",sdPrice)
#
#
#creating a histogram
plt.hist(rdf,x='User Rating')
plt.show()