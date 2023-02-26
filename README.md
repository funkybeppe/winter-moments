

This is the 4th portfolio project developed as part of the Code Institute Diploma in Full Stack Development. It was created to demonstrate skills acquired using Django to design and develop websites that offer full CRUD (create, read, update and delete) functionality.


User Experience (UX)

Project Aims
The initial aims of the project which formed the basis for user story creation were identified as the following:


User Stories




Agile Methodology


Design

Wireframes
I created Wireframes to visualize the site's design and act as a template to use when developing the templates. When designing the site I wanted to ensure the site looked and functioned just as well on mobile as larger viewports. Customers may use phones as their primary device to raise and view requests and this also offers flexibility to support staff to work from any device.

Colour Scheme



Typography


Images and Iconography


Database Schema


Features


Features Not Implemented


Future Features


Technologies Used
Languages Used


Python Modules and Packages/Frameworks Used


Programs and Tools Used


Testing



Bugs
Fixed Bugs


Remaining Bugs
No known errors remaining.


Deployment

Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

Log in to GitHub and locate the GitHub Repository
At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
Click the button (not the number to the right) and you should now have a copy of the original repository in your GitHub account.
Making a Local Clone
NOTE: It is a requirement of the is project that you have Python version 3.8 or higher installed locally.

Log in to GitHub and locate the GitHub Repository.

Under the repository name, click "Code".

To clone the repository using HTTPS, under "HTTPS", copy the link.

Open your local terminal with git installed

Change the current working directory to the location where you want the cloned directory to be created.

Type git clone, and then paste the URL you copied in Step 3.

Press Enter. Your local clone will be created.

Change the current working directory to the cloned project folder (this will be a child directory in the location you cloned the project).

It is recommended to use a virtual environment during development (learn more about virtual environments). If you would prefer not to use on please skip the following steps:

Create a virtual environment in the projects working directory by entering the following command in the same terminal window used for the steps above python3 -m venv .venv.
Before use, the virtual environment will need to be activated using the command source .venv/bin/activate in the same terminal window used previously.
Packages required by the project can now using the command pip install -r requirements.txt

In the cloned directory, rename the file .env-example to .env and populate it with the information required.

Make django migrations using the command ./manage.py migrate.


Deploying with Heroku
NOTE: It is a prerequisite of deployment to Heroku that you already have access to the following:

A Cloudinary account, create one for free at https://cloudinary.com.

NOTE: It is assumed you have followed all deployment instructions listed in this readme starting with the section titled 'Forking the GitHub Repository'.

Log in to Heroku and if not taken there automatically, navigate to your personal app dashboard.
At the top of the page locate the 'New' drop down, click it and then select 'Create new app'.
Give your application a unique name, select a region appropriate to your location and click the 'Create app' button.
Your app should now be created, so from the menu towards the top of the page select the 'Resources' section.
Search for 'Heroku Postgres' under the Add-ons section and add it.
From the menu towards the top of the page select the 'Settings' section and lick 'Reveal Config Vars' in the Config vars section. Enter the following key / value pairings:
Key as ALLOWED_HOSTS and the value as the name of you project with '.herokuapp.com' appended to the end e.g. example-app.herokuapp.com. Click the Add button.
Key as CLOUDINARY_URL and the value as your cloudinary API Environment variable e.g. cloudinary://**************:**************@*********. Click the Add button.
Key as EMAIL_HOST_PASSWORD and the value as the password or value provided by your email service of choice. Click the Add button.
Key as EMAIL_HOST_USER and the value as the the email address or value provided by your email service of choice. Click the Add button.
Key as SECRET_KEY and the value as a complex string which will be used to provide cryptographic signing. The use of a secret key generator is recommended such as https://djecrety.ir. Click the Add button.
Ensure the key DATABASE_URL is already populated. This should have been created automatically by Heroku.
The DATABASE_URL should be copied into your local .env, created during the cloning process.
Open the .env file in the project directory and delete the key / value pair DEV_ENVIRONMENT_DATABASE = True before saving the file. This can be added back after the next step to ensure local development changes will not alter the remote database.
Running migrations on the remote database
Open your local terminal and change the current working directory to that of the project folder.
Make django migrations using the command ./manage.py migrate.
Navigate to the 'Deploy' page using the menu towards the top of the page.
Select 'GitHub' from the 'Deployment method' section and you will be prompted to 'Connect to GitHub'.
Once connected to your GitHub account you will be able to search for your repository which contains the forked 'Support-Hub' repository.
Once the repository is found click 'Connect'.
At the bottom of the page find the section named 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.
Once deployment is complete, click the 'View' button to load the URL of the deployed application.

Credits
Online resources


Code
The following credits represent cases where code was adapted or used from external resources. 


Media


Acknowledgments