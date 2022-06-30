#!/usr/bin/env python3

pike_trikfoot={'Race':'Gnome','Team':' Vox Machina','Team_Members':'["Grog", "Keyleth", "Scanlan", "VexAhlia" , "VaxIldan", "Percy"]','Bestfriend':'Grog','age':40}

pike_trikfoot["Cleric_of"] = "Sarenrae"


print(pike_trikfoot.keys())

choice = input("choose a key")

if choice in pike_trikfoot:
    
    print("Pike's" + choice + "is:" + pike_trikfoot[choice])

else:

    print("This choice is not in dictionary")
