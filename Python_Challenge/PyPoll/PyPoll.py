
#------------------------------------------------------------------------------------------------------------------
#--------------------------------------PYTHON--CHALLENGE--PART-2-------------------------------------------------
#-------------------------------------------------------------------------------------------------------------


import os
import csv

pyPoll_csv = os.path.join("C:/Users/Marquis Sills/Python_Challenge/PyPoll/Resources/election_data.csv")

Ballot = []
County = []
Candidate = []


with open(pyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        
        #Since ballot id is not a number, I'll extract as string
        Ballot.append(str(row[0]))

        #Extract the Counties as strings for the same reason as previous
        County.append(str(row[1]))

        Candidate.append(str(row[2]))

# unique_candidates = list(set(Candidate))
# print(unique_candidates)
# I did this so I would know whose running and I got Diana DeGette, Raymon Anthony Doane, Charles Casper Stockham


#This is counting the number of votes per candidate
Count_DeGette = Candidate.count("Diana DeGette")
Count_Doane = Candidate.count("Raymon Anthony Doane")
Count_Stockham= Candidate.count("Charles Casper Stockham")


#Time to do some rounding
DeGette= round(Count_DeGette/len(Ballot) * 100,3)
Doane = round(Count_Doane/len(Ballot)*100,3) 
Stockham = round(Count_Stockham/len(Ballot)*100,3) 

#----------------------------------------------------------------------------------------------------------
#-------------------------Printing the Results----------------------------------------------------------
  
print("Total Votes: " + str(len(Ballot)))
print("Charles Casper Stockham: "   + str(Stockham) + "%" + " ("+ str(Count_Stockham) + ")")
print("Diana DeGette "   + str(DeGette) + "%" + " ("+ str(Count_DeGette) + ")")
print("Raymon Anthony Doane: "   + str(Doane)  + "%" + " ("+ str(Count_Doane) + ")")

if Count_DeGette > Count_Doane and Count_Stockham:
      print("Winner: " + "Diana DeGette")

elif Count_Doane > Count_Stockham and Count_DeGette:
    print("Winner: " + "Raymon Anthony Doane")

else: print("Winner: " + "Charles Casper Stockham")

#-----------------------------------------------------------------------------------------------------------


#Time to export the results

filename = "C:/Users/Marquis Sills/Python_Challenge/PyPoll/Analysis/PyPoll_Result.txt" # name of the output file

# ---------  "\n" creates spacing

with open(filename, "w") as file:
    file.write("\n")  
    file.write("Election Results" "\n") 
    file.write("\n")
    file.write("------------------------" + "\n")
    file.write("\n")
    file.write("Total Votes: " + str(len(Ballot)) + "\n")  
    file.write("\n")
    file.write("------------------------" + "\n")
    file.write("\n")
    file.write("Charles Casper Stockham: "   + str(Stockham) + "%" + " ("+ str(Count_Stockham) + ")" + "\n")
    file.write("\n")
    file.write("Diana DeGette: "   + str(DeGette) + "%" + " ("+ str(Count_DeGette) + ")" + "\n") 
    file.write("\n")
    file.write("Raymon Anthony Doane: "   + str(Doane)  + "%" + " ("+ str(Count_Doane) + ")" + "\n")
    file.write("\n")
    file.write("------------------------" + "\n")
    file.write("\n")
    if Count_DeGette > Count_Doane and Count_Stockham:
      file.write("Winner: " + "Diana DeGette")

    elif Count_Doane > Count_Stockham and Count_DeGette:
        file.write("Winner: " + "Raymon Anthony Doane")

    else: file.write("Winner: " + "Charles Casper Stockham")
    file.write("\n")
    file.write("\n")
    file.write("------------------------" + "\n")
