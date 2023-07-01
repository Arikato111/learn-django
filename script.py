import sys
import os

defaltManage = "python3 manage.py"
scripts = {
    "dev": f"{defaltManage} runserver",
    "db-make": f"{defaltManage} makemigrations",
    "db-up": f"{defaltManage} migrate",
    "admin": f"{defaltManage} createsuperuser"
}

if sys.argv[1] in scripts.keys():
   print("~run: ", scripts[sys.argv[1]], '\n')
   os.system(scripts[sys.argv[1]]) 
else:
   print("Not found script")