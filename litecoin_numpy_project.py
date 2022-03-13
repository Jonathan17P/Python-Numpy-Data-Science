from numpy import *                #Imports everything from the NumPy package
import pandas as pd                #Imports Pandas as pd, which means we specify what we need from the Pandas package 

open=pd.read_csv('/Users/jonathanprince/python/litecoin_numpy_project.csv')['Open'].values      #Transforms data from csv file within the "open"column into an array, called "open".
 
close=pd.read_csv('/Users/jonathanprince/python/litecoin_numpy_project.csv')['Close'].values    #Transforms data from csv file within the "close"column into an array, called "close". 

date=pd.read_csv('/Users/jonathanprince/python/litecoin_numpy_project.csv')['Date'].values      #Transforms data from csv file within the "date"column into an array, called "date". 

open_close=hstack([open,close])       #Horizontally concatenates the "open" array with the "close" array.   

open_close_diff=close-open            #Computes the element wise difference between the "close" and "open" array.

print("The first day of the 90 days analyzed was:  ", date[0])        #Prints the first entry within the "date" array.

print("While the last day of the 90 days analyzed was:  ", date[89])  #Prints the last entry within the "date" array.

print("Over the last 90 days, Litecoin has had an average opening price of:  ", round(open.mean(),2))       #Computes the average value from thevalues found within the "open" array and then reports the average to within a hundreth of a decimal place. 

print("Over the last 90 days, Litecoin has had an average closing price of:  ", round(close.mean(),2))      #Computes the average value from thevalues found within the "close" array and then reports the average to within a hundreth of a decimal place.


print("Over the last 90 days, Litecoin has had an average price of:  ", round(open_close.mean(),2))         #Computes the average value from thevalues found within the "open_close" array and then reports the average to within a hundreth of a decimal place.

print("With a standard deviation of:  ", round(open_close.std(),2))      #Computes the standard deviation of the "open_close" average" and then reports the standard deviation to within a hundreth of a decimal place.

print("Which means out of the last 90 days, the number of days which opened with a price higher then the average is:  ",sum(open>open_close.mean()))     #Computes and then displays the total number of values within the "open" array that are greater then the 90 day average.

print("And the number of days which closed at a higher price then the 90 day average would be:  ",sum(close>open_close.mean()))    #Computes andthen displays the total number of values within the "open" array that are greater then the 90 day average.

print("Over the last 90 days, the minimum price of Litecoin was:  ", open_close.min())     #Finds and then displays the smallest value within the "open_close" array. 

print("While the maximum price of Litecoin over the last 90 days was:  ", open_close.max())    #Finds and then displays the largest value withinthe "open_close" array. 

print("Over the last 90 days, the median price of Litecoin was:  ", median(open_close))        #Computes and then displays the median value from the "open_close" array.

print("Which can be seen looking at the data:  ", sort(open_close))      #Rearranges the data found within the "open_close" array such that the smallest value is the first value within the array, while the largest value is the last value within the "open_close" array. The sorted array isthen displayed.

print("The 90 day price of Litecoin in which 25% of the 90 day prices fall below it is:  ", percentile(open_close,25))     #Computes and then displays the 25th percentile price (to within the hundreths place) of Litecoin over the 90 days analyzed.  

print("The 90 day price of Litecoin in which 75% of the 90 day prices fall below it is:  ", round(percentile(open_close,75),2))     #Computes and then displays the 75th percentile price (to within the hundreths place) of Litecoin over the 90 days analyzed.     

print("Looking at the data, we see that on average, the difference between the opening price of Litecoin and the closing price of Litecoin is:  ",round(open_close_diff.mean(),2))     #Computes and then displays the average value of the element wise difference between members of the "close" array and the "open" array.
print("Which is interesting, because that tells us, on average, Litecoin opens at a higher price then it closes at. So, if you're an investor, you may want to wait until closing to invest in Litecoin")     #Displays the implication of the result by taking the element wise difference between the "close" array and the "open" array.
