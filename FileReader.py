import sys





def filecontent(filename):
    # Open a file
    fo = open(filename, "r")
    

    # Assuming file has following 5 lines
    # This is 1st line
    # This is 2nd line
    # This is 3rd line
    # This is 4th line
    # This is 5th line

    line = fo.read()
    

    # Close opend file
    fo.close()
    return line 

