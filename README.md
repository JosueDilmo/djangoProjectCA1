# Back-end Web Development - BSC30922 - Semester 1 & 2 

* Student Name: `Josue Santos` 
* Student Number: `24061` 

## Django Project

## Continuous Assesment 3 - Semester 2

### Assignment 3 Description
Using an existing full stack web application using Python, Django, MySQL that can perform CRUD operations that you created already for CA1, CA2, or use the template tutorial code from github from the geoff-wright repo. Do the following tasks to extend the App.
Test one or more modules for positive tests – data that is acceptable and for negative tests – data that is unacceptable.

`[10%]`	Add manual testing using one of the unit test libraries and one or more module/function.

`[10%]`	Add automatic (dynamic) testing using one of the unit test libraries and one or more module/functions.

`[10%]`	Document the testing of the function and the assertions being used.

`[10%]`	Ensure that the tests include:-  positive tests – for data that is acceptable and negative tests – for data that is unacceptable.

`[20%]`	Configure the system with a config file for development and another file for test

`[20%]`	The application is accompanied by a short report (max. 500 words) or a ReadMe file. The
	report should explain the testing methodology and coverage.
	
`[20%]`	Extend the web app to include at least 2 additional anti-hacking security checks such as CSS, SQL injection, redirection.

### Assignment 3 Solution

<b>Run in terminal:</b><br>
<i> python manage.py test</i></br>

The code provided includes three test cases for a Django web application. The tests are checking different aspects of the application.

-	<b>Test_security.py</b>

The first test case is checking for security issues such as CSS attacks, SQL injection attacks, and redirection attacks. It includes three methods to test these different types of attacks. The first method tests for CSS attacks, where it checks if the response does not contain the <script> tag. The second method tests for SQL injection attacks by passing a SQL injection attack string as a parameter to the URL and checking if the response status code is 404. The third method tests for redirection attacks by checking if the response URL is not equal to the Google website's URL.

-	<b>Test_accounts.py</b>

The second test case is for testing the built-in Django accounts app. It includes three methods to test logging in, logging out, and registration. The first method tests logging in by making a GET request to the login page, followed by a POST request with correct login credentials. It checks if the response is redirected to the home page and the session contains the `_auth_user_id` key. The second method tests logging out by logging in first, then making a GET request to the logout page and checking if the response is redirected to the home page and the session does not contain the `_auth_user_id` key. The third method tests registration by making a GET request to the registration page, followed by a POST request with valid registration data. It checks if the response is redirected to the login page and the database contains a user with the provided credentials.

-	<b>Test_views.py & test_models.py</b>

The third test case is for testing the views of the application. It includes two methods to test the question index view and the question detail view. The first method tests the question index view by creating different types of questions and checking if they are displayed correctly on the index page. The second method tests the question detail view by creating a future question and checking if accessing its detail page returns a 404-status code, and creating a past question and checking if accessing its detail page displays the question's text.

-	<b>Test_settings.py</b>

This is a configuration file which sets various parameters such as `tests` app to be available for testing, some `Middleware` were disable in this settings file and the `Databases` selected is SQLite3 which is separate from the regular development database keeping the testing environment isolated from the development environment.

Overall, the test cases are testing different aspects of the web application, including security, authentication, and views. These test cases are useful for ensuring that the web application is working as expected and is secure from common attacks.


## Continuous Assessment 1 & 2 - Semester 1

### Assignment 1 Description
Develop a web application API using Python and the Django framework that can perform CRUD operations on a MySQL database. 
You are free to choose the type of data the application will store (e.g. users, cars, animals, etc.). 
The data should be complex enough, containing different types of values (Strings, ints, Booleans, etc.).

`[40%]`	All CRUD operations are working as intended (e.g. the right data is retrieved while using an index, data is being deleted by a criteria, retrieve one or multiple records).

`[10%]`	The application is connecting to the right database. 

`[10%]`	The data is complex: it contains at least one index (unique entry); has at least 3 types of variables and there are sufficient entries already in the database.

`[10%]` Code is readable: consistency, right identification, comments.

`[20%]`	The application is accompanied by a short report (max. 500 words) or a ReadMe file. The
	report should explain the developing process of the application.

`[10%]`	Creativity: Do your own research and add any other functionality to your application. (e.g.
	multiple variable types – Boolean, array, array, etc.; basic front-end; database
	complexity; multiple objects, etc.)


### Assignment 1 Solution

<b>To run the web application:</b><br>
<i> py manage.py runserver</i></br>
http://127.0.0.1:8000/<br>

The project root directory is called djangoProject (outer directory) and it is the container folder for the project. 
Inside this directory, there are:

-	<b>manage.py</b> – Command-line utility to interact with Django project.<br>
-	<b>Inner directory djangoProject</b> – This is the actual Python package and contains anything important (e.g., urls.py, settings.py).<br>
-	<b>djangoProject/__init__.py</b> – This empty file tells Python that this directory should be considered a Python package.<br>
-	<b>djangoProject/settings.py</b> – This file contains the settings or configurations for this Django project.<br>
-	<b>djangoProject/urls.py</b> – The URL declarations for this Django project, this is a “table of contents”.<br>
-	<b>djangoProject/asgi.py</b> – An entry-point for ASGI-compatible web servers.<br>
-	<b>djangoProject/wsgi.py</b> – An entry-point for WSGI-compatible web servers.<br>
-	<b>polls</b> – The web application developed in this project.<br>
-	<b>templates</b> – A folder responsible for storing the files which will give style to the web application and how it will look like.<br>
-	<b>venv</b> – Project virtual environment.

The polls app has few key files responsible for managing, displaying, accessing, and modifying the information in the database.

-	<b>polls/views.py</b> – responsible for displaying information in the web page.<br>
-	<b>polls/urls.py</b> – responsible for mapping the views in the polls application.<br>
	
An important step is to point the root <b>URLconf (djangoProject/urls.py)</b> at the <b>polls.urls</b> module.<br>
In the URLconf (inside <b>djangoProject</b> python package), is necessary to add few functions:<br>
-	<b>include()</b> – function allows referencing other URLconfs.<br>
-	<b>path()</b> – function is passed four arguments, two required: route and view and two optional: kwargs, and name.<br>
--	<i>route:</i> Is a string that contains a URL pattern.<br>
--	<i>view:</i> When Django finds a matching pattern, it calls the specified view function.<br>

To set up the MySQL database, the first step was to install the mysqlclient. <br>
Using the terminal window, the command is:<br>
	<i>pip install mysqlclient</i><br>
<br>After the installation it was necessary to create the database using the MySQL Workbench, 
once it was created the last step was to define it at <b>djangoProject/settings.py:</b><br>
<b>ENGINE</b> – backend engine which is 'django.db.backends.mysql'<br>
<b>NAME</b> – The name of the database (‘trainingdb’)<br>
<b>USER/ PASSWORD, HOST and PORT</b> – This configuration was kept as default which is 
respectively (<i>‘root’/’root’, ‘localhost’, ‘3306’</i>).<br>
With the configuration complete the next step was to run the command:<br>
<i>python manage.py migrate</i><br>
This command looks at the <b>INSTALLED_APPS</b> setting and create any necessary database
tables according to the database settings define at <b>djangoProject/settings.py</b>.<br>
The <b>djangoProject/settings.py</b> also include the Django applications that are activated
in this Django instance. By default, <b>INSTALLED_APPS</b> contains the following apps,
all of which come with Django:<br>
- <b>django.contrib.admin</b> – The admin site. <br>
- <b>django.contrib.auth</b> – An authentication system.<br>
- <b>django.contrib.contenttypes</b> – A framework for content types.<br>
- <b>django.contrib.sessions</b> – A session framework.<br>
- <b>django.contrib.messages</b> – A messaging framework.<br>
- <b>django.contrib.staticfiles</b> – A framework for managing static files.<br>

And for this project, <b>'polls.apps.PollsConfig'</b> was included.<br>
This line of code points to the configuration class for the polls app.<br>
The <b>PollsConfig class</b> can be found at <b>polls/apps.py.</b><br>
A particular modification made was to include bootstrap:<br>
<b>'bootstrap5'</b> – Is a library for HTML/CSS style used on the templates of this project.

The next step of this project was to define the models which is responsible for 
defining the database layout.<br>
In this poll app, we’ll create two models: <b>Question</b> and <b>Choice</b>. <br>
- Question has a question and a publication date.<br>
- Choice has two fields: the text of the choice and a vote tally.<br>

Each <b>Choice</b> is associated with a <b>Question</b>.<br>

Class variables used in this file:<br>
- class Question<br>
-- question_text = CharField which has the (max_length=200) characters.<br>
-- pub_date = DateTimeField which is the date when published.<br><br>

- class Choice<br>
-- question = ForeignKey (Question, on_delete=models.CASCADE)<br>
-- choice_text = CharField which has the (max_length=200) <br>
-- votes = IntegerField (default=0) default value.<br>

The relationship is defined by using <b>ForeignKey</b>.
It tells Django that each <b>Choice</b> is related to a single <b>Question</b>.<br>
Once the project models were defined and the polls app included in the <b>djangoProject/settings.py - INSTALLED_APPS.</b><br> 
The next step was to run the command:<br>
<i>python manage.py makemigrations polls</i><br>
This command tells Django there are some changes in the models file and these changes needs 
to be stored as a migration.<br>
Once it is complete the next command is:<br>
<i>python manage.py migrate<br></i>
This command is used to create those model tables in the database. 
To be able to manage the models in an easier way, Django provides an entirely automated 
administrator interface. To use this interface is necessary to create a super user (admin).<br> 
On the terminal:<br>
<i>python manage.py createsuperuser</i> 
 
After defining the credentials and creating the admin super user the next step was to 
define the admin interface at <b>polls/admin.py</b>, this part of the project can be found 
in the <b>Django tutorial part 07</b>.<br>
<b>Django tutorial part 03 and 04</b> explained how to use the templates folder and how to 
customize this project and to make the polls application interactive.<br>
<b>polls/views.py</b>:<br>
- <b>class IndexView</b> – Display the list of questions in the web page.<br>
-- <b>def get_queryset</b> - Return the last five published questions.<br><br>
- <b>class DetailView</b> – Display the question with details and the options for vote.<br><br>

- <b>class ResultsView</b> – Display the result of the poll and the number of votes in each choice.<br>
-- def vote – Responsible for doing the action of vote and recording into the database.<br>

The file <b>polls/test.py</b> is responsible for executing few test routines it is necessary because when writing new code, 
the developer can use tests to validate the code and confirm it works as expected and 
because when refactoring or modifying old code, test cases can ensure the new changes 
haven’t affected the application’s behaviour unexpectedly.<br>
Using the documentation available in <b>bootstrap website</b> was possible to design a 
better front-end.<br><br>
<i><u><b>The other functionalities of the project still under construction and will be explained in the next assignment.</b></i></u>


### Assignment 2 Description
Develop a full stack web application using Python, Django, MySQL that can perform CRUD operations. 
You are free to choose the type of data the application will store (e.g. users, cars, animals, etc.). 
The data should be complex enough, containing different types of values (Strings, ints, Booleans, etc.). 
You can reuse the code for CA1 for your server-side code.

`[10%]`	All CRUD operations are working as intended.

`[10%]`	The application is connecting to the right database.

`[10%]`	The data is complex enough.

`[10%]`	Code is readable: consistency, right identification, comments.

`[20%]`	Code added to include a log-in system.

`[20%]`	The application is accompanied by a short report (max. 500 words) or a ReadMe file. The
	report should explain the developing process of the application.

`[20%]`	Creativity: Do your own research and add any other functionality to your application (e.g., multiple variable types – image, Boolean, array, array, etc.; CSS styling - bootstrap,
	search/filtering button)
	

### Assignment 2 Solution

This project started with the first continuous assignment which created all the structure, database, and views. This second assignment implemented the authentication system which is responsible for the login/ logout, signup and reset of password which are handled by the Django Auth System.
Following the tutorials of Django Login and Logout, Signup and Password Reset was possible to create and implement in an easy, quicker, and friendly way this robust authentication system.
The Django Auth system is a built-in functionality which handles user accounts, groups, permissions and cookie-based user sessions, this system works out of the box and is customizable to suits the project needs.

Started with this tutorial:
[Django Login and Logout](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

Second:
[Django Signup](https://learndjango.com/tutorials/django-signup-tutorial)

Third:
[Django Password Reset](https://learndjango.com/tutorials/django-password-reset-tutorial)


## References:
- [ Django Tutorial ](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- [ Django Authentication](https://docs.djangoproject.com/en/4.0/topics/auth/)
- [ Django Templates ](https://docs.djangoproject.com/en/4.1/topics/templates/)
- [ Django Documentation ](https://docs.djangoproject.com/en/4.1/)
- [ Django Test Documentation](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)
- [ Bootstrap Documentation ](https://mdbootstrap.com/)
