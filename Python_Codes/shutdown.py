import os
import subprocess

ask = input("What do you wants the computer to do?\n Restart?\n off?\n Sleep?\n\n").lower()

if ask == "restart":
    confirm = input("\nAre you sure you wants to restart your pc?\nyes or no?\n").lower()
    if confirm == "yes":
        os.system("shutdown /r /t 1")
    elif confirm == "no":
        print("\nOkay!\n You've aborted the process.")
elif ask == "off":
    confirm = input("\nAre you sure you wants to shutdown your pc?\nyes or no?\n").lower()
    if confirm == "yes":
        os.system("shutdown /s /t 1") 
    elif confirm == "no":
        print("\nOkay!\n You've aborted the process.")
elif ask == "sleep": 
    confirm = input("\nAre you sure you wants to sleep your pc?\nyes or no?\n").lower()
    if confirm == "yes":
        subprocess.call(["shutdown", "/h"])
    elif confirm == "no":
        print("\nOkay!\n You've aborted the process.")

