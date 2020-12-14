<h1>READ BELOW!!!</h1>

<h2>Open the command line and navigate to an easily accessible directory.</h2>

Install a virtual environment to run Django in
    type 'py -m pip install --user virtualenv'
    
    
Create a new vritual environment in the current directory
    py -m venv <env name> 

Navigate to the directory where the env was created and execute this command
    <env name>\Scripts\activate.bat
    
You should see the following at the left of the temrinal
    (<env name>)C:\\
    
    
Now, navigate to the cloned github repository 'sharefestsite' folder

Execute the following commands
    python manage.py collectstatic
    
    python manage.py runserver
