
#------------------------------------------------------------------------------------------------------------------
#--------------------------------------PYTHON--CHALLENGE--PART-1-------------------------------------------------
#-------------------------------------------------------------------------------------------------------------


import os
import csv


Date = []
Profit_Loss = []
Change_Results = []

#Get the data set
pyBank_csv = os.path.join("C:/Users/Marquis Sills/Python_Challenge/PyBank/Resource/budget_data.csv")

with open(pyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        
        #Extract the date
        Date.append(row[0])

        #Extract the Profit vs Loss
        Profit_Loss.append(int(row[1]))

#Finding the Changes in Profit/Loss

for i in range(len(Profit_Loss)-1): # You discount by minus 1 because you are reducing the range.
    Change = Profit_Loss[i+1] -  Profit_Loss[i] # 
    Change_Results.append(Change)
    

#Connecting those arrays together
#I figured out the by [1:] we skip a row allowing for the correct output in the following dates
cleaned_csv = zip(Date[1:],Profit_Loss,Change_Results)



#Finding Both the max and min
Max_Change_Results = max(Change_Results)
Min_Change_Results = min(Change_Results)

# print(Max_Change_Results)
# print(Min_Change_Results)

for rows in cleaned_csv:
  
  if rows[2] == Max_Change_Results:
        Max_Date = rows[0] #This matches the maximum row to the corresponding date
  elif rows[2] == Min_Change_Results:
        Min_Date = rows[0] #This matches the minimum row to the corresponding date

      
#Summing the data
def Summation(numbers):
    total = 0.0
    for numbers in numbers:
        total = total + numbers
    return total 


#Averaging the data
def Average(num):
    length=len(num)
    total = 0.0
    for num in num:
        total = total + num
    return total/length

Total_Amount = round(Summation(Profit_Loss),1)
Average_Amount = round(Average(Change_Results),2)

#---------PRINTING THE OUTPUTS-----------
# I need to test the results

print("Total Months: " + str(len(Date)))
print("Total :" + "$"+str(Total_Amount))
print("The Average Change: "+ "$" + str(Average_Amount))
print("Greatest Increase in Profits: " + Max_Date + " " + "(" +"$"+  str(Max_Change_Results)+ ")" )
print("Greatest Decrease in Profits: " + Min_Date + " " + "(" +"$"+ str(Min_Change_Results) + ")" )


# # #-------------Exporting as TextFile-----------------

filename = "C:/Users/Marquis Sills/Python_Challenge/PyBank/Analysis/pyBank.txt" # name of the output file

# ---------  "\n" creates spacing

with open(filename, "w") as file:
    file.write("\n")  
    file.write("Financial Analysis" "\n") 
    file.write("\n")
    file.write("------------------------" + "\n")
    file.write("\n")
    file.write("Total Months: " + str(len(Date)) + "\n")
    file.write("\n")
    file.write("Total :" + "$"+str(Total_Amount) + "\n")
    file.write("\n")
    file.write("The Average Change: "+ "$" + str(Average_Amount) + "\n")
    file.write("\n")
    file.write("Greatest Increase in Profits: " + Max_Date + " " + "(" +"$"+  str(Max_Change_Results)+ ")" + "\n")
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + Min_Date + " " + "(" +"$"+ str(Min_Change_Results) + ")" + "\n")
    file.write("\n")

