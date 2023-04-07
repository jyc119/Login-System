# Login-System

## Install packages

To install the packages we are using, run the following commands in terminal

```
pip install fastapi
pip install uvicorn
```

## Setup 

To start and setup the login system follow the steps shown below

### 1) Download Repo

Clone the repository and open it in the saved location.

### 2) Start Uvicorn server

Start the Uvicorn server by using the command 

```
python -m uvicorn main:app --reload
```
The terminal should show the following code if the server is running correctly.

![img](https://github.com/jyc119/Login-System/blob/main/misc/univorn_server.png)

### 3) Open login.html

Open login.html, right click the contents and select Open with live server. Alternatively, Alt+L Alt+O. This will open up the login form.

![img](https://github.com/jyc119/Login-System/blob/main/misc/login-page.png)

## Accessing the API

Once we started the Univcorn server, we can access the API using this link: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Structure

![img](https://github.com/jyc119/Login-System/blob/main/misc/Project_structure.png)

The project structure is shown above where the information is written to the HTML form and passed into Javascript. From the Javascript file, the information is sent to FastAPI where it checks if the details match any of the records in the database. Based on this information, it goes all the way back to the HTML file to output the results

## Database 

Sqlite3 is the database used to store information about the different usernames and passwords. The following table shows the different login details in the database when the user starts the server.

| Username | Password |  Token  |
| -------- | -------  | ------- |
| jp201    | fixer    |  False  |
| jc19     | colon    |  False  |
| lf12     | tiger    |  False  |

## How to use Login System

To use the login system, we simply input the username at the username input box and the password at the password input box. Depending on the input, the form will output either 'Valid Login' for correctly input login details or 'Invalid Login' for incorrect login details. To insert more login details, we have to **refresh** the page every time to remove past login details.

### Invalid Login
When the user enters an invalid login, the form will output 'Invalid Login' in red text as shown in the image below.

![img](https://github.com/jyc119/Login-System/blob/main/misc/invalid_login.png)

### Valid Login
On the other hand, when a user enters valid login details, the form will output 'Valid Login' as the details matches one of the records in the database table.

![img](https://github.com/jyc119/Login-System/blob/main/misc/valid_login.png)

### Remember me Token
To make the login system remember the user after they have input correct details:

* Type in **yes** in the remember me input box.
* Refresh the page and click on 'Look for usernames'
* A dropdown list will appear at usernames and when the user clicks on an option, the password field will automatically fill with the correct password with that username. 

An example of this can be seen below where we click on **Look for usernames** and this creates the drop down box.
![img](https://github.com/jyc119/Login-System/blob/main/misc/dropdown_user.png)

When we click on the option **lf12**, the password field is automatically filled with lf12's password which is tiger. From here, we can submit and confirm it is a valid login. 
![img](https://github.com/jyc119/Login-System/blob/main/misc/dropdown_pass.png)

