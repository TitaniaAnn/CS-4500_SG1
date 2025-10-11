"""
Program built using Python 3 compiled using Thonny IDE.
CS-4500 SG1
Group Members: Cynthia Brown, Kayla Gaynor, Brandon Schettler
Start Date: 09/11/25
Revision Date: 09/18/2025
Revision Date 09/30/2025
Revision Date 10/09/2025
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
# wordLists = []
userList = []
files = []
        
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
            print("Collected 10 files. Proceeding...")
            flag = False
        else:
            flag = userBool("Do you want to add another document(yes/no)? ")
            
     
     
    print("\nFile Statistics:")

    # Find the max character length of filenames, total words, and distinct words. Fwidth = file, twidth = total words, dwidth = distinct words
    fwidth = max(len("Filename"), max(len(f["filename"]) for f in files))
    twidth = max(len("Total Words"), max(len(str(len(f["words"]))) for f in files))
    dwidth = max(len("Distinct Words"), max(len(str(len(f["distinct"]))) for f in files))

    # Instructions don't say headers should be right aligned, but it looks awkward otherwise. Also the double spaces between
    print(
        f'{"Filename".rjust(fwidth)}  '
        f'{"Total Words".rjust(twidth)}  '
        f'{"Distinct Words".rjust(dwidth)}'
    )

    # Actual data under headers. Filename, total words, then distinct words, right aligned. Or 'right justified' as instructions say
    for f in files:
        words = len(f["words"])
        distinct = len(f["distinct"])
        print(
            f'{f["filename"].rjust(fwidth)}  '
            f'{str(words).rjust(twidth)}  '
            f'{str(distinct).rjust(dwidth)}'
        )


    # loop to collect words and count occurences
    while True:
        # Ask user for word
        user_input = get_valid_word("Submit a word(a-z and hyphen): ")
        counts = {}
        num = 0
        for temp in files:
            counts[temp["filename"]] = temp["words"].count(user_input)
            num = num +  counts[temp["filename"]]
            
        print(f"\nOccurrences of '{user_input}':")
        for fname, cnt in counts.items():
            print(f"  {fname:<20} {cnt:>5}")

        userList.append({"word": user_input, "counts": counts, "total":num})
        
        if not userBool("Do you want to enter another word(yes/no)? "):
            break
        
    # loop to print out word count results
    lg = len(max((u['word'] for u in userList), key=len)) + len(str(max((u['total'] for u in userList)))) + 4
    print("\nSearch Summary: ")
    bdr = "" + "=" * ((lg*2)+8)
    print(bdr)
    num = 0
    temp = ""
    if userList:
        alphaUserList = sorted(userList, key=lambda x: x["word"])
        numUserList = sorted(userList, key=lambda x: x["total"])
        lenUserList = sorted(userList, key=lambda x: len(x["word"]))
        for entry in alphaUserList:
            t = f"{entry['word']} - {entry['total']}"
            temp = temp + f"|  {t:<{lg}}  |"
            num = num + 1
            if num == 2:
                print(temp)
                temp = ""
                num = 0
    print(bdr)
    
    # input to exit program
    input("Press Enter to exit the program.")
    sys.exit()
    
# End of program