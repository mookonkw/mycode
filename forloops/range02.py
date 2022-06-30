#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""
#1
# open file in read mode
#dnsfile = open("dnsservers.txt", "r")

# create list of lines
#dnslist = dnsfile.readlines()

# loop over lines
#for svr in dnslist:
    #print and end without a newline
 #   print(svr, end="") # the line we read ALREADY contains a \n (newline)
    
# close the file (we created the list of lines)
#dnsfile.close() # best practice to close your file

#2
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'"""

# open file in read mode
#with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # create list of lines
 #   dnslist = dnsfile.readlines()
    # loop over lines
 #   for svr in dnslist:
        #print and end without a newline
  #      print(svr, end="")

# no need to close our file - closed automatically

#3
#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption.
         Sort domains ending in .org and .com into files
         org-domain.txt and com-domain.txt."""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:   # 'r' is read mode
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if exists
                               # would exists on all but last line
        # IF the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")

# no need to close our file - closed automatically

