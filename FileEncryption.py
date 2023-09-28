codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '2', 'c': '7',
    'D': '6', 'd': '*', 'E': '&', 'e': '3', 'F': '5', 'f': '!', 
    'G': '+', 'g': '^', 'H': '$', 'h': '1', 'I': '8', 'i': '|',
    'J': '0', 'j': '4', 'K': '?', 'k': '(', 'L': ')', 'l': '=',
    'M': '_', 'm': '[', 'N': ']', 'n': '{', 'O': '}', 'o': '/',
    'P': '\\', 'p': '<', 'Q': '>', 'q': ':', 'R': ';', 'r': ',',
    'S': '.', 's': '~', 'T': '`', 't': '!', 'U': '@', 'u': '#',
    'V': '$', 'v': '%', 'W': '^', 'w': '&', 'X': '*', 'x': '(',
    'Y': ')', 'y': '-', 'Z': '=', 'z': '+'
}



infile = open('info_security.txt','r')
outfile = open('encrypted.txt','w')

file_read = infile.read()

for i in file_read:
    if i in codes:
        outfile.write(codes[i])
    else:
        outfile.write(i)

infile.close()
outfile.close()