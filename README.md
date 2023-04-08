# Login-System

In this login system, we are creating a simple login system with a small backend server. FastAPI and SQlite is used for our backend and database while Javascript is used for our front end. 

## Install packages

To install the packages we are using, run the following command in terminal

```
pip install -r requirements.txt
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

SQlite is the database used to store information about the different usernames and passwords. The following table shows the different login details in the database when the user starts the server.

| Username | Password |  Token  |
| -------- | -------  | ------- |
| jp201    | fixer    |  False  |
| jc19     | colon    |  False  |
| lf12     | tiger    |  False  |

## How to use Login System

To use the login system, we simply input the username at the username input box and the password at the password input box. Depending on the input, the form will output either 'Valid Login' for correctly input login details or 'Invalid Login' for incorrect login details.

### Using the form after every submission

To insert more login details after a user has inputted some login details, we have to **refresh** the page every time to remove past login details so that we can validate more login details.

### Invalid Login
When the user enters an invalid login, the form will output 'Invalid Login' in red text as shown in the image below.

![img](https://github.com/jyc119/Login-System/blob/main/misc/invalid_login.png)

### Valid Login
On the other hand, when a user enters valid login details, the form will output 'Valid Login' as the details matches one of the records in the database table.

![img](https://github.com/jyc119/Login-System/blob/main/misc/valid_login.png)

### Remember me Token
To make the login system remember the user after they have input correct details:

* Correctly input login details and type in **yes** in the remember me input box.
* Click Login and refresh the page.
* Click on 'Look for Usernames'.
* A dropdown list will appear at usernames and when the user clicks on an option, the password field will automatically fill with the correct password with that username. 

An example of this can be seen below where we click on **Look for Usernames** and this creates the drop down box.
![img](https://github.com/jyc119/Login-System/blob/main/misc/dropdown_user.png)

When we click on the option **lf12**, the password field is automatically filled with lf12's password which is tiger. From here, we can submit and confirm it is a valid login. 
![img](https://github.com/jyc119/Login-System/blob/main/misc/dropdown_pass.png)

### Restarting the uvicorn Server

To restart the uvicorn server, we have to first shut down the server through the following command Ctrl+C/Cmd+C. Next, we have to delete the **logins.db** file that is created when the server is launch as the python file cannot create a databse file if an existing one is already there. Now we can run the command in step 2 of the setup section again to launch the server.

```
python -m uvicorn main:app --reload
```

## Implementation Details

### HTML interaction with Javascript

In the login button used to submit the form, I inserted an attribute in the input field called 'onclick'. The attribute is shown in the code below where we execute the function SubmitLogin() which is a Javascript function and disables the button when it is pressed. This is how the HTML file interacts with the JavaScript file.

```
onclick="SubmitLogin(); this.disabled = true;"
```

### Javascript with FastAPI

In the async function **'SubmitLogin()'**, we are converting the input field values into a json object and this is sent to the API with the fetch function. The location it is sent to is http://127.0.0.1:8000/check-login/ using the POST method. In the **'check_login()'** function of FastAPI, it updates the database with True in the remember me token if the username and password matches one of the records and the user typed 'yes'. Next, it checks if the details matches one of the records and returns a string in the following form:

<br><br>

True username1,password1 username2password2

<br><br>

The boolean at the beginning of the string represents if the login is valid. The lists of usernames and passwords after the boolean are the lists of login details that have the rememeber me token. This will be used later for the 'Look for usernames' button.

<br><br>

The Javascript obtains this result and outputs the results in a paragraph field below the submit button.

### Rememeber me Javascript implementation

To obtain the list of login details with a token, I created another button at the top called 'Look for Usernames'. When this button is clicked, the javascript function **getUsername()** is used where the list of login details received from FastAPI is used to insert into a dropdown list for the username field. The password input field will automatically be filled when a dropdown option in username is selected by altering the value attribute.
