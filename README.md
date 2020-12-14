<h1>READ BELOW!!!</h1>

<h2>Open the command line and navigate to an easily accessible directory.</h2>

<h2>Install a virtual environment to run Django in</h2>
    type 'py -m pip install --user virtualenv'
    
    
<h2>Create a new virtual environment in the current directory</h2>
    py -m venv [env name]

<h2>Navigate to the directory where the env was created and execute this command</h2>
    <env name>\Scripts\activate.bat
    
<h2>You should see the following at the left of the terminal</h2>
    ([env name])C:\\
    
    
<h2>Now, navigate to the cloned github repository 'sharefestsite' folder</h2>

<h2>Execute the following commands</h2>
    python manage.py collectstatic
    
    python manage.py runserver
