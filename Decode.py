def decode(string, shift):
    newstr = ""
    for c in string:

        if c == ' ':
            newstr = newstr + c
        else:

            newchar = ord(c) + shift
            if newchar < ord('a'):
                newchar = newchar + 26
            if newchar > ord('z'):
                newchar = newchar - 26
            newstr = newstr + chr(newchar) 
    return newstr


