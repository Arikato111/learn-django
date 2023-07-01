import sys
import os

scripts = {
    "dev": "python3 manage.py runserver",
    "make": "python3 manage.py makemigrations"
}

if sys.argv[1] in scripts.keys():
   print("~run: ", scripts[sys.argv[1]], '\n')
   os.system(scripts[sys.argv[1]]) 
else:
   print("Not found script")