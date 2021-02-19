#########################################################################
#Title: Project Scenario - Data Analysis
#Description: This program allows user to read content from the file and identity the top 3 countries of visitors to Singapore from a specific region over a span of 10 years. 
#Name: Jovan Lim
#Class: PN2004L
#Date: 19/2/2021
#Version: 3.8.2
#########################################################################

#########################################################################
#Class - calculate Utility
#Read content from the file and identity the top 3 countries of visitors to Singapore from a specific region over a span of 10 years.
#########################################################################
#Use pandas library for data analysis
import pandas as pd
#creates table-like custom objects from the items in CSV files
import csv

class top3countries:
  def __init__(self):
    #Function to calculate total visitors in each countries over a span of 10 years and list the top 3
    CalculateTotalVisitors()

#########################################################################
#Functon - CalculateTotalVisitors
#Read content from the file and calculate total visitors in each countries over a span of 10 years and list the top 3
#########################################################################
def CalculateTotalVisitors():

  path = 'MonthyVisitors.csv'
  #open file as READ-ONLY
  file = open(path, 'r')
  #Return a reader object which will iterate over lines in the given csvfile
  reader = csv.reader(file)
  # fetch next item from the collection and place it in the variable header 
  header = next(reader)
  #initialise lists and variables
  each_countries_total_visitors = []
  japan_visitors = []
  hk_visitors = []
  china_visitors = []
  taiwan_visitors = []
  korea_visitors = []
  data = []

  #Parse (remove irrelevant data regions) the data based on requirement
  for row in reader:
    # row = [Year,Month," Japan "," Hong Kong "," China "," Taiwan "," Korea, Republic Of "]
    year = int(row[0])
    month = str(row[1])
    japan = int(row[9])
    hk = int(row[10])
    china = int(row[11])
    taiwan = int(row[12])
    korea = int(row[13])

    data.append([year, month, japan, hk, china, taiwan, korea])
  #close the file
  file.close()
  #parse the required range of data (over a span of 10 years) into the lists
  for a in range(0, len(data)):
    dataSEA = data[a]
    japan_visitors.append(dataSEA[2])
    hk_visitors.append(dataSEA[3])
    china_visitors.append(dataSEA[4])
    taiwan_visitors.append(dataSEA[5])
    korea_visitors.append(dataSEA[6])
  #each countries total sum of visitors in Singapore over a span of 10 years
  total_japan_visitors = sum(japan_visitors)
  total_hk_visitors = sum(hk_visitors)
  total_china_visitors = sum(china_visitors)
  total_taiwan_visitors = sum(taiwan_visitors)
  total_korea_visitors = sum(korea_visitors)
  #add each countries total visitors value together to form a list
  each_countries_total_visitors.append(total_japan_visitors)
  each_countries_total_visitors.append(total_hk_visitors)
  each_countries_total_visitors.append(total_china_visitors)
  each_countries_total_visitors.append(total_taiwan_visitors)
  each_countries_total_visitors.append(total_korea_visitors)
  #sort the values from smallest to highest (left to right)
  each_countries_total_visitors.sort()
  #removes the items one by one from the lists starting from the highest and assigned a variable each to the return value
  first = each_countries_total_visitors.pop()
  second = each_countries_total_visitors.pop()
  third = each_countries_total_visitors.pop()
  fouth = each_countries_total_visitors.pop()
  fifth = each_countries_total_visitors.pop()
  #Find out which countries have the most visitors count
  #Check if the highest country visitors count is equal to any of the sum of visitors from each countries
  if first == total_japan_visitors:
    print("1st: " + header[9] + " - " + str(first))
  else:
    if first == total_hk_visitors:
      print("1st: " + header[10] + " - " + str(first))
    else:
      if first == total_china_visitors:
        print("1st: " + header[11] + " - " + str(first))
      else:
          if first == total_taiwan_visitors:
            print("1st: " + header[12] + " - " + str(first))
          else:
            if first == total_korea_visitors:
              print("1st: " + header[13] + " - " + str(first))
  #Check if the second highest country visitors count is equal to any of the sum of visitors from each countries
  if second == total_japan_visitors:
    print("2nd: " + header[9] + " - " + str(second))
  else:
    if second == total_hk_visitors:
      print("2nd: " + header[10] + " - " + str(second))
    else:
      if second == total_china_visitors:
        print("2nd: " + header[11] + " - " + str(second))
      else:
        if second == total_taiwan_visitors:
          print("2nd: " + header[12] + " - " + str(second))
        else:
          if fifth == total_korea_visitors:
            print("2nd: " + header[13] + " - " + str(second))
  #Check if the third highest country visitors count is equal to any of the sum of visitors from each countries
  if third == total_japan_visitors:
    print("3rd: " + header[9] + " - " + str(third))
  else:
    if third == total_hk_visitors:
      print("3rd: " + header[10] + " - " + str(third))
    else:
      if third == total_china_visitors:
        print("3rd: " + header[11] + " - " + str(third))
      else:
        if third == total_taiwan_visitors:
          print("3rd: " + header[12] + " - " + str(third))
        else:
          if third == total_korea_visitors:
            print("3rd: " + header[13] + " - " + str(third))
  #Check if the fouth highest country visitors count is equal to any of the sum of visitors from each countries
  if fouth == total_japan_visitors:
    print("Other: " + header[9] + " - " + str(fouth))
  else:
    if fouth == total_hk_visitors:
      print("Other: " + header[10] + " - " + str(fouth))
    else:
      if fouth == total_china_visitors:
        print("Other: " + header[11] + " - " + str(fouth))
      else:
        if fouth == total_taiwan_visitors:
          print("Other: " + header[12] + " - " + str(fouth))
        else:
          if fouth == total_korea_visitors:
            print("Other: " + header[13] + " - " + str(fouth))
  #Check if the smallest country visitors count is equal to any of the sum of visitors from each countries
  if fifth == total_japan_visitors:
    print("Other: " + header[9] + " - " + str(fifth))
  else:
    if fifth == total_hk_visitors:
      print("Other: " + header[10] + " - " + str(fifth))
    else:
      if fifth == total_china_visitors:
        print("Other: " + header[11] + " - " + str(fifth))
      else:
        if fifth == total_taiwan_visitors:
          print("Other: " + header[12] + " - " + str(fifth))
        else:
          if fifth == total_korea_visitors:
            print("Other: " + header[13] + " - " + str(fifth))

  return
#########################################################################
# FUNCTION Branch: End of Code
#########################################################################

#########################################################################
# Main Branch
#########################################################################
if __name__ == '__main__':
  #program Title
  print("#######################################################################################")
  print("data analyses - top 3 countries of visitors in the Asia-Pacific Region to Singapore over a span of 10 years")
  print("#######################################################################################")
  #identify top 3
  top3countries()

  # load excel data (CSV format) to dataframe - 'df'
  df = pd.read_csv('MonthyVisitors.csv')

  path = 'MonthyVisitors.csv'
  #open file as READ-ONLY
  file = open(path, 'r')
  #Return a reader object which will iterate over lines in the given csvfile
  reader = csv.reader(file)
  # fetch next item from the collection and place it in the variable header 
  header = next(reader)
  # show available regions to user
  available_Regions = ['Southeast Asia', 'Asia Pacific', 'South Asia Pacific', 'Middle East', 'Europe', 'North America', 'Australia', 'Africa']
  print( "\n\n" + "Available regions:", available_Regions)
  # prompt user to enter a region
  region = str(input("Enter a region: "))
  print("")
  # error checking for each region, if region isdigit, prompt error. Else (if no error), initialize each of the region's respective variable with their respective dataframe
  while True:
    # variable
    i = 0
    # if user enter empty string, loop input until valid
    if region == "":
      region = str(input("Please enter a region: "))
    elif region.isdigit():
      print("Invalid format.")
      break
    else:
      if region == 'Southeast Asia':
        print( "\n\n" + "Available countries:", header[2:9])
        i += 1
        break
      elif region == 'Asia Pacific':
        print( "\n\n" + "Available countries:", header[9:14])
        i += 1
        break
      elif region == 'South Asia Pacific':
        print( "\n\n" + "Available countries:", header[14:17])
        i += 1
        break
      elif region == 'Middle East':
        print( "\n\n" + "Available countries:", header[17:20])
        i += 1
        break
      elif region == 'Europe':
        print( "\n\n" + "Available countries:", header[20:31])
        i += 1
        break
      elif region == 'North America':
        print( "\n\n" + "Available countries:", header[31:33])
        i += 1
        break
      elif region == 'Australia':
        print( "\n\n" + "Available countries:", header[33:35])
        i += 1
        break
      elif region == 'Africa':
        print( "\n\n" + "Available countries:", header[35:36])
        i += 1
        break
      else:
        print("Error. Please check for spelling errors.")
        break
  
  if i >= 1: # the variable 'i' will be the indicator for whether the program will run this part of code or not
    # show available year range to user
    year_range = ['1978 - 1987', '1988 - 1997', '1998 - 2007', '2008 - 2017']
    while True:
      print("Year range:", year_range)
      year = input("Enter the starting year: ")
      try:
        year = int(year)
      except:
        print("Invalid format.")
        break
      else:
        # 1978
        if year == 1978 and region == 'Southeast Asia':
          SEA_region = df.iloc[:120,:9]
          print(SEA_region)
          break
        elif year == 1978 and region == 'Asia Pacific':
          # print out result of the combination of dataframes
          years = df.iloc[:120,:2]
          AP_region = df.iloc[:120,9:14]
          result = years.join(AP_region)
          print(result)
          break
        # same process for the rest below
        elif year == 1978 and region == 'South Asia Pacific':
          years = df.iloc[:120,:2]
          SAP_region = df.iloc[:120,14:17]
          result = years.join(SAP_region)
          print(result)
          break
        elif year == 1978 and region == 'Middle East':
          years = df.iloc[:120,:2]
          ME_region = df.iloc[:120,17:20]
          result = years.join(ME_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          break
        elif year == 1978 and region == 'Europe':
          years = df.iloc[:120,:2]
          EU_region = df.iloc[:120,20:31]
          result = years.join(EU_region)
          print(result)
          break
        elif year == 1978 and region == 'North America':
          years = df.iloc[:120,:2]
          NA_region = df.iloc[:120,31:33]
          result = years.join(NA_region)
          print(result)
          break
        elif year == 1978 and region == 'Australia':
          years = df.iloc[:120,:2]
          AUS_region = df.iloc[:120,33:35]
          result = years.join(AUS_region)
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Africa':
          years = df.iloc[:120,:2]
          AF_region = df.iloc[:120,35:36]
          result = years.join(AF_region)
          print(result)
          i += 1
          break
        # 1988
        elif year == 1988 and region == 'Southeast Asia':
          SEA_region = df.iloc[120:240,:9]
          print(SEA_region)
          i += 1
          break
        elif year == 1988 and region == 'Asia Pacific':
          years = df.iloc[120:240,:2]
          AP_region = df.iloc[120:240,9:14]
          result = years.join(AP_region)
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'South Asia Pacific':
          years = df.iloc[120:240,:2]
          SAP_region = df.iloc[120:240,14:17]
          result = years.join(SAP_region)
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Middle East':
          years = df.iloc[120:240,:2]
          ME_region = df.iloc[120:240,17:20]
          result = years.join(ME_region)
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Europe':
          years = df.iloc[120:240,:2]
          EU_region = df.iloc[120:240,20:31]
          result = years.join(EU_region)
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'North America':
          years = df.iloc[120:240,:2]
          NA_region = df.iloc[120:240,31:33]
          result = years.join(NA_region)
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Australia':
          years = df.iloc[120:240,:2]
          AUS_region = df.iloc[120:240,33:35]
          result = years.join(AUS_region)
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Africa':
          years = df.iloc[120:240,:2]
          AF_region = df.iloc[120:240,35:36]
          result = years.join(AF_region)
          print(result)
          i += 1
          break
        # 1998
        elif year == 1998 and region == 'Southeast Asia':
          SEA_region = df.iloc[240:360,:9]
          print(SEA_region)
          i += 1
          break
        elif year == 1998 and region == 'Asia Pacific':
          years = df.iloc[240:360,:2]
          AP_region = df.iloc[240:360,9:14]
          result = years.join(AP_region)
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'South Asia Pacific':
          years = df.iloc[240:360,:2]
          SAP_region = df.iloc[240:360,14:17]
          result = years.join(SAP_region)
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Middle East':
          years = df.iloc[240:360,:2]
          ME_region = df.iloc[240:360,17:20]
          result = years.join(ME_region)
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Europe':
          years = df.iloc[240:360,:2]
          EU_region = df.iloc[240:360,20:31]
          result = years.join(EU_region)
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'North America':
          years = df.iloc[240:360,:2]
          NA_region = df.iloc[240:360,31:33]
          result = years.join(NA_region)
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Australia':
          years = df.iloc[240:360,:2]
          AUS_region = df.iloc[240:360,33:35]
          result = years.join(AUS_region)
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Africa':
          years = df.iloc[240:360,:2]
          AF_region = df.iloc[240:360,35:36]
          result = years.join(AF_region)
          print(result)
          i += 1
          break
        # 2008
        elif year == 2008 and region == 'Southeast Asia':
          SEA_region = df.iloc[360:,:9]
          print(SEA_region)
          i += 1
          break
        elif year == 2008 and region == 'Asia Pacific':
          years = df.iloc[360:,:2]
          AP_region = df.iloc[360:,9:14]
          result = years.join(AP_region)
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'South Asia Pacific':
          years = df.iloc[360:,:2]
          SAP_region = df.iloc[360:,14:17]
          result = years.join(SAP_region)
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Middle East':
          years = df.iloc[360:,:2]
          ME_region = df.iloc[360:,17:20]
          result = years.join(ME_region)
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Europe':
          years = df.iloc[360:,:2]
          EU_region = df.iloc[360:,20:31]
          result = years.join(EU_region)
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'North America':
          years = df.iloc[360:,:2]
          NA_region = df.iloc[360:,31:33]
          result = years.join(NA_region)
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Australia':
          years = df.iloc[360:,:2]
          AUS_region = df.iloc[360:,33:35]
          result = years.join(AUS_region)
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Africa':
          years = df.iloc[360:,:2]
          AF_region = df.iloc[360:,35:36]
          result = years.join(AF_region)
          print(result)
          column_name = df.iloc[9:10]
          column_sum = df[column_name].sum()
          print(column_sum)
          i += 1
          break
        else:
          print("Error. Please ensure that you picked a valid year.")
          break
  #import time for delay        
  import time
  #number of seconds delay
  time.sleep(1) 
  #import matplotlib.pyplot for pie chart
  import matplotlib.pyplot as pit

  #The list for top 3 countries of the most amount of visitors in all region between the year 1978-2017
  activities = ['Indonesia', 'Japan', 'China']

  #The list for the amount of visitors in S.E.A region between the year 1978-2017
  slices = [42860566, 27353174, 26781571]

  #The list for the colours 
  colours = ['r', 'g', 'm']

  #creating the pie chart
  pit.pie(slices,
  labels=activities,
  startangle=90,
  shadow=True,
  explode=(0.2, 0, 0),
  autopct='%1.2f%%')
        
  #creating the legend
  pit.legend()
  #Showing the pie chart
  pit.show()

 
#########################################################################
# Main Branch: End of Code
#########################################################################