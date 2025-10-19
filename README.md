# Simple-Key-Auth-Loader-For-Beginners-
a tiny loader for beginners who want to lock their own scripts behind keyauth light, readable, and works out of the box,  just swap in your info. ꉂ(˵˃ ᗜ ˂˵)

what this is?

a python example that:
asks users for their username + key (with hidden input)
verifies through keyauth’s seller api
launches your script if access is granted
basically a quick-start template for anyone learning or testing keyauth.

for setup open the file in any editor and fill in your own:

app_name

owner_id

seller_key

paste or call your code where it says # --- BEGIN CODE ---
run the file. if the info is right, it’ll verify + launch your script.

notes
don’t upload your real seller key or private scripts here
this is for educational / personal use
you can customize the ascii art, messages, and style however you want
i just made this to keep things neat and beginner-friendly

----------------------------------------------------------------------------

to put this to use, after you're done filling in the .py with the necessary information, turn the file into an .exe to send to others. 

# how to turn a file into an .exe

 pip install pyinstaller
 
```pyinstaller --onefile -n "SuperSecretLoader" -i "Loader.ico" SuperSecretLoader.py```

after "-n" quote name you want for the  .exe

after "-i" you put the name of the icon you want on your loader, remove that part if you don't wish to have one

finally name the .py you're turning into a .exe

credits
made by Kanra (@cigarfumes on discord)
