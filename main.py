"""
Program built using Python 3 compiled using Thonny IDE.
CS-4500 SG1
Group Members: Cynthia Brown, TODO:: Add Team member names
Start Date: 09/11/25
Revision Date: 09/18/2025
Revision Date 09/30/2025
Submission Date: 
Sources: Google AI for quick syntax lookup
         Used for used to help track down weird functionallity of Python
             Stack Overflow
             GeeksforGeeks
             Reddit

"""
# library imports
import sys
import re

# global variables
docList = []
wordLists = []
userList = []

# defined objects
class word: # Yes I know this could have been handled another way but user defined objects are the best
    def __init__(self, text, count):
        self.text = text
        self.count = count
        
# defined functions
def remove_punctuation(text):
    # Finds and removes all punctuation from the string
    pattern = r'[^\w\s-]|(?<!\w)-(?!\w)'
    return re.sub(pattern, '', text)

def userBool(prompt):
    # Gets the user response on if they want to continue or not
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ('yes', 'y'):
            return True
        elif user_input in ('no', 'n'):
            return False
        else:
            print("Error: Please enter a valid response (yes/no).")

# user input functions
def get_valid_txt(prompt):
    while True:
        # Get the file name from user
        user_input = input(prompt).strip().lower()

        # Check if ends in .txt ignoring case
        if user_input.endswith(".txt"):
            if not docList or docList.count(user_input) == 0:
                return user_input
            else:
                print("ERROR: You have already entered that filename")
        else:
                print("ERROR: Please enter a filename ending with .txt")

def get_valid_word(prompt):
    while True:
        # Get the file name from user
        user_input = input(prompt).strip().lower()

        # Check if ends in .txt
        if re.fullmatch(r"^[a-zA-Z-]+$", user_input) and not user_input.startswith('-') and not user_input.endswith('-') and not ' ' in user_input:
            return user_input
        else:
            print("ERROR: Please enter a valid word")
                
# read file function
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read file contents
            content = file.read()
            content = remove_punctuation(content).lower()
            temp = content.lower().split()
            # Yes Python made me loop through the list to append it to wordLists instead of allowing me to overwrite the variable.
            # This does allows you to later on add the ability to search multiple documents at once.
            docList.append(filename)
            wordLists.append(temp)
            print(docList)
            print(wordLists)
            return True
    except FileNotFoundError:
        # Throw if file does not exist
        print(f"Error: file '{filename}' not found.")
        return False
    except Exception as e:
        # catch any additional errors
        print(f"An error occured: {e}")
        return False
        

# main execution of program
print("This program reads in a txt file and allows you to query how many times a word appears in that file. All word count results are printed at the end of the program. Enjoy!")
# loop that runs the program
while True:
    flag = True
    # loop to get and read valid file
    while flag:
        filename = get_valid_txt("Enter txt filename(.txt): ")
        read_file(filename)
        if len(docList) == 10:
            flag = False
        else:
            flag = userBool("Do you want to add another document(yes/no)? ")
        
    # loop to collect words and count occurences
    flag = True
    while flag:
        # Ask user for word
        user_input = get_valid_word("Submit a word(a-z and hyphen): ")
        wordCount = 0
        for t in wordLists:
            wordCount = wordCount + t[1:].count(user_input)
        # Add to user list with count
        userList.append(word(user_input, wordCount))
        flag = userBool("Do you want to enter another word(yes/no)? ")
        
    # loop to print out word count results
    for w in userList:
        print(f"'{w.text}': '{w.count}'")
        
    # input to exit program
    input("Press Enter to exit the program.")
    sys.exit()
    
# End of program