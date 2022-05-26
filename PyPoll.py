# #Pseudo
# #code

# # Assign a variable for the file to load and the path.
# import csv


# file_to_load='Resources/election_results.csv'

# # Open the election results and read the file
# #election_data = open(file_to_load,'r')
# with open(file_to_load) as election_data:

#     # to do: Perform Analysis
#     print (election_data)
# # Close the file.
# election_data.close()

#add dependencies
import csv
import os

#assign variable for full path to file to be read
file_to_load=os.path.join('Resources','election_results.csv')

#assign variable for full path to file to be written
file_to_save=os.path.join('analysis','election_analysis.txt')

#open election results and read the file
with open(file_to_load) as election_data:
    
    #to do: read and analyze data here
    file_reader=csv.reader(election_data)

    #read and print header row
    headers=next(file_reader)
    
    print(headers)
    # print(file_reader.dialect)
    # print(file_reader.line_num)
    # #print each row in csv file
    # for row in file_reader:
    #     print(row)

#use open stmt to open the file as a text file
#outfile = open(file_to_save,'w')

# #write some data to the file
# #outfile.write('Ahoy there world!')
# with open(file_to_save,'w') as txt_file:
#     #txt_file.write('Yay Derek!')
#     txt_file.write('Counties in the Election\n')
#     txt_file.write('------------------------\n')
#     txt_file.write('Arapahoe\n')
#     txt_file.write('Denver\n')
#     txt_file.write('Jefferson\n')
#     #txt_file.write
# #close the file
# #outfile.close()