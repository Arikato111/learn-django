import sys
import os
import platform

defaltManage = "python3 manage.py"
if("Windows" == platform.system()):
   defaltManage = "python manage.py"

scripts = {
    "dev": f"{defaltManage} runserver",
    "db-make": f"{defaltManage} makemigrations",
    "db-up": f"{defaltManage} migrate",
    "admin": f"{defaltManage} createsuperuser"
}

if len(sys.argv) > 1:
   if sys.argv[1] in scripts.keys():
      print("~run: ", scripts[sys.argv[1]], '\n')
      os.system(scripts[sys.argv[1]]) 
else:
   print("Not found script")