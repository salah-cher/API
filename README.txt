Creating Web APIs with Python and Flask
Author: SALAH CHERKAOUI
Requirements:  python, pip, flask, Firefox, ubuntu, sqlite3
Check installed packages: 
# python --version
# pip --version

if need to install flask 
# pip install flask
# pip install connexion

for more information about installing a virtual environment  : https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/
The database used is SQLite, a lightweight database engine that is supported in Python by default. SQLite files typically end with the .db file extension.
File is attached and should be copied to the same API folder 
SQLite DB install 
# apt-get install sqlite3
Optional we can install sqlite browser to add data.  
# apt-get install sqlitebrowser
for more information about using sqlite browser on ubuntu. 
https://linuxhint.com/install_sqlite_browser_ubuntu_1804/

How it works:
Check folder content : 
-rw-r--r--  1 root root  1480 Feb  6 14:01 myapp.py
-rw-r--r--  1 root root  8192 Feb  6 14:04 names.db
Running the python script : 
root@spinnaker:/opt/vmfarm# python myapp.py
you should see: 
* Serving Flask app "myapp" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 299-585-001

Access the API via web: 
Open Firefox on the local computer 
http://127.0.0.1:5000/
you should see 
Distant Reading Names
A prototype API for distant reading of Names.
This python API will list names in JSON format, here is the syntax to interact with the API: 
To list all names:
http://127.0.0.1:5000/api/v1/resources/names/all
search by name ex: Max
http://127.0.0.1:5000/api/v1/resources/names?name=Max
2


