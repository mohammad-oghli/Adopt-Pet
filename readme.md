## Adopt Pet Simple Flask App
In order to install flask dependency run this command in your terminal:

`pip install flask`

You need to set `FLASK_APP` environment variable to load the application:

Run CMD command:

`set FLASK_APP=app`

Or run Powershell command:

`$env:FLASK_APP = "app"`

You can run flask app on your local host by executing this command on your terminal:

`flask run`

It will run on `http://127.0.0.1:5000`

It's a simple flask app for pets site 

All the data of the app based on a predefined `dictionary` without using any database

The main functionalities of this app:
* Show available pets.
* List different pets according to its type.
* Show detailed profile page for each pet including:

    * **Name of the pet**
    * **Brief description of the pet**
    * **Breed of the pet**
    * **Age of the pet**
    * **Image of the pet**

**Made with ❤ by Mohamad Oghli**

Email: `mhd.sh.oghli@gmail.com`