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
wordLists = []
userList = []
files = []

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
        user_input = input(prompt).strip()

        # Check if filename ends with .txt (case-insensitive)
        if user_input.lower().endswith(".txt"):
            # Check if filename is already entered
            if any(temp["filename"].lower() == user_input.lower() for temp in files):
                print("ERROR: You have already entered that filename")
            else:
                return user_input
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
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()
            content = remove_punctuation(content).lower()
            words = content.split()
            files.append({
                "filename": filename,
                "words": words,
                "distinct": set(words)
            })
            return True
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return False

        

# main execution of program
print("This program reads in a txt file and allows you to query how many times a word appears in that file. All word count results are printed at the end of the program. Enjoy!")
# loop that runs the program
while userBool:
    flag = True
    # loop to get and read valid file
    while flag:
        filename = get_valid_txt("Enter txt filename(.txt): ")
        read_file(filename)
        # stop if 10 files have been entered
        if len(files) == 10:
            flag = False
        else:
            flag = userBool("Do you want to add another document(yes/no)? ")

        
    # loop to collect words and count occurences
    while True:
        # Ask user for word
        user_input = get_valid_word("Submit a word(a-z and hyphen): ")
        counts = {}
        for temp in files:
            counts[temp["filename"]] = temp["words"].count(user_input)
            
        print(f"\nOccurrences of '{user_input}':")
        for fname, cnt in counts.items():
            print(f"  {fname:<20} {cnt:>5}")

        userList.append({"word": user_input, "counts": counts})
        
        if not userBool("Do you want to enter another word(yes/no)? "):
            break

        
    # loop to print out word count results
    print("\nSearch Summary: ")
    for entry in userList:
        print(f"\nWord: {entry['word']}")
        for fname, cnt in entry["counts"].items():
            print(f"  {fname:<20} {cnt:>5}")
        
    # input to exit program
    input("Press Enter to exit the program.")
    sys.exit()
    
# End of program