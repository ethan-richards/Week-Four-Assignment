_author_ = "Ethan Richards"
# CIS 125
#piggetty
# piggetty.py
#Converts words from a file to pig latin and puts them into a new file. 

vowels = "aeiouAEIOU"
#create a function that pigifies each word.
def pigify(word):
    n = 0
    endWord ="" 
    for letter in word:
        if letter in vowels:
    	    if n == 0:
    		    pig = word + "yay" 
    		    return pig
    	    else:
    		    pig = word[n:] + endWord + "ay"
    		    return pig
        else:
            endWord += word[n]
            n += 1

# Open the file *getty.txt* for reading.

infile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.

outfile = open("piggy.txt", "w")

# Read the getty.txt file into a string. 

getString = infile.readline()
# Create a new empty string. 
    
pigString = ""
    
# Strip out bad characters (, - .). 

getString = getString.replace(",","")
getString = getString.replace("-","")
getString = getString.replace(".","")

# Split the string into a list of words.

getList = getString.split()

# Loop through the list of words, pigifying each one.  		

for word in getList:
    
# Add the pigified word (and a space) to the new string.     
    
    pigString += str(pigify(word)) + " "

# Write the new string to piggy.txt. 

outfile.write(pigString)

# close the files.
infile.close
outfile.close

 





 

 



# Add the pigified word (and a space) to the new string.  

# Write the new string to piggy.txt.  

# close the files.