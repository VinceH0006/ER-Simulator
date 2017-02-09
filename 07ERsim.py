#  File: ERsim.py
#  Description: This program simulates the ER and creates a queue for each level of severity in their condition and treats them all in the appropriate order
#  Student's Name: Vincent Hochstein
#  Student's UT EID: VLH546
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/27/2015
#  Date Last Modified: 10/30/2015

# This extremely basic function just takes in the current queues, and prints it in an appealing way
def print_seq(critical, serious, fair):
  print ("Queues are:")
  print ("Critical: ")
  print (critical)
  print ("Serious: ")
  print (serious)
  print ("Fair: ")
  print (fair)
  print ()

# Main file
def main():

  # Open the file
  in_file = open("ERsim.txt", "r")

  # Initialize the empty queues
  critical = []
  serious = []
  fair = []

  # Set the initial value of the line
  line = ("blank")
  # So long as the next line isn't blank the program continues
  while (line != ""):
    # Read in the line and prepare it for processing
    line = in_file.readline()
    line = line.strip()
    input = line.split(" ")

    # If the file says to exit, you exit
    if (input[0] == "exit"):
      print (">>> Exit")
      exit

    # If it is telling you to add, you next read in which queue they should be added to, and do that
    # Then make a call to the printing function to inform the consol of the current state
    if (input[0] == "add"):
      if (input[2] == "Critical"):
        print (">>> Add patient '" + input[1] + "' to Critical queue")
        critical.append(input[1])
      if (input[2] == "Serious"):
        print (">>> Add patient '" + input[1] + "' to Serious queue")
        serious.append(input[1])
      if (input[2] == "Fair"):
        print (">>> Add patient '" + input[1] + "' to Fair queue")
        fair.append(input[1])
      print_seq(critical, serious, fair)

    # If the input file says to treat you then must figure out if you are treating all or next
    if (input[0] == "treat"):
      # If all then you announce that to consol and enter a loop which completes when all queues are empty
      if (input[1] == "all"):
        print (">>> Treat all patients")
        # The loop goes through in order of importance which queue to pop and treat from and then continues to the next itteration
        while ((len(critical) > 0) or (len(serious) > 0) or (len(fair) > 0)):
          if (len(critical) > 0):
            output = critical.pop(0)
            print ("Treating '" + output + "' from Critical queue.")
            print_seq(critical, serious, fair)
          elif (len(serious) > 0):
            output = serious.pop(0)
            print ("Treating '" + output + "' from Serious queue.")
            print_seq(critical, serious, fair)
          elif (len(fair) > 0):
            output = fair.pop(0)
            print ("Treating '" + output + "' from Fair queue.")
            print_seq(critical, serious, fair)
        # Once this loop completes then all queues should be empty
        print ("No patients in queues")
        print ()

      # If the input file wants you to treat next then the exact same function as before is performed
      # However it is only performed once rather than as a loop until everything is empty
      if (input[1] == "next"):
        print (">>> Treat next patient")
        if (len(critical) > 0):
          output = critical.pop(0)
          print ("Treating '" + output + "' from Critical queue.")
          print_seq(critical, serious, fair)
        elif (len(serious) > 0):
          output = serious.pop(0)
          print ("Treating '" + output + "' from Serious queue.")
          print_seq(critical, serious, fair)
        elif (len(fair) > 0):
          output = fair.pop(0)
          print ("Treating '" + output + "' from Fair queue.")
          print_seq(critical, serious, fair)
        # If all queues are empty then print that as such
        else:
          print ("No patients in queues")
          print ()

  # Close the file, although technically you will never actually close is since the program will have been exitted before this line is reached
  in_file.close()

main()