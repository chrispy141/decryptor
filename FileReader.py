import sys





def filecontent(filename):
    # Open a file
    fo = open(filename, "r")
    

    

    line = fo.read()
    

    # Close opend file
    fo.close()
    return line 

