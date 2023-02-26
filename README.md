# Milestone Project 4


## Purpose

This is the 4th portfolio project developed as part of the Code Institute Diploma in Full Stack Development. It was created to demonstrate skills acquired using Django to design and develop websites that offer full CRUD (create, read, update and delete) functionality.

## Winter Moments

Winter Moments is a picture blog where winter sports enthusiasts can share their experiences with other users upon registration.

* Users can create blog posts, add title and upload pictures with description.
* Users can also create posts without pictures by simply skipping the upload field.
* Likes and comments can be left on posts.
* Users can edit or delete their posts.
* The Admin can delete other users posts and comments if they're not following blog guidelines or if content is offensive.
* The Admin as superuser can configure the site using the Django admin portal.


![Screenshot 2023-02-26 at 15 35 01](https://user-images.githubusercontent.com/105980082/221420521-987d702d-e926-46f6-b803-410e954a5c38.png)


The live link can be found here - [Winter Moments](https://winter-moments.herokuapp.com/).


# User Experience (UX)

## Project Aims

The initial aims of the project which formed the basis for user story creation were identified as the following:

  * Create a blog post, upload a picture and description.

  * Allow users to like and comment other users posts, view their profiles.
  
  * Allow users to edit their profiles and update settings.

## User Stories

1. View post list: As a Site User I can view a list of posts so that I can select one to read
2. Open a post: As a Site User I can click on a post so that I can read the full text
3. View likes: As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
4. View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation
5. Account registration: As a Site User I can register an account so that I can access the website
6. Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation
7. Like / Unlike: As a Site User I can like or unlike a post so that I can interact with the content
8. Manage posts: As a Site User/ Admin I can create, read, update and delete my posts
9. Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
10. Manage roles: As a Site Admin I can change user roles so that I can convert users to staff
11. As a Site User, I can maintain a profile so that I can add and update contact information
12. As a Site User, I can change password without supervision so that I can keep my account secure


## Agile Methodology

All user stories were entered as issues in a GitHub Kanban project, however [Notion](https://notion.so) software was used during development and all the issues were added in later.


## Design

### Wireframes

I created Wireframes to visualize the site's design and act as a template to use when developing the templates. When designing the site I wanted to ensure the site looked and functioned just as well on mobile as larger viewports. Customers may use phones as their primary device to raise and view requests and this also offers flexibility to support staff to work from any device.

## Colour Scheme

Colours used throughout the site were kept to a minimum to keep its focus clear, allowing the blog posts to stand out.
The website uses Bootstrap dark theme for Navigation, Footer and forms.
Post cards are in a white shade and text in dark, "View Post" buttons in dark theme color to provide contrast.
Edit button is provided with a grey color from Bootstrap, Delete button with a red color to stand out.


## Typography

Bootstrap fonts were used in this project with both fonts selected for their legibility and simplicity.

![Screenshot 2023-02-26 at 18 06 32](https://user-images.githubusercontent.com/105980082/221428277-7be2a0fa-cef5-4745-928d-5260120b2440.png)
![Screenshot 2023-02-26 at 18 07 50](https://user-images.githubusercontent.com/105980082/221428312-61754e45-77e9-416c-af3c-36b41d4d7383.png)


## Images and Iconography

The icons are from [Font Awesome](https://fontawesome.com).

The default profile picture was taken from [Flaticon](https://www.flaticon.com/)

The main background image was taken from [Pexels](https://www.pexels.com). Light editing work was undertaken using the [Cloudinary](https://cloudinary.com) editing tool to ensure the image matched the site's aesthetic.

The blog posts pictures are partially taken from my camera album and Pexels.

The Winter Moments logo was created with [Logo.com](https://app.logo.com/)


## Database Schema


## Features

1. Landing Page
<img width="1512" alt="Screenshot 2023-02-26 at 14 59 28" src="https://user-images.githubusercontent.com/105980082/221428380-ad6b99ab-e30a-4a39-aa29-0c0a8691d815.png">

<img width="960" alt="Screenshot 2023-02-26 at 15 02 03" src="https://user-images.githubusercontent.com/105980082/221428414-18f728bd-d6b3-49ab-90cc-45fa5a814522.png">

<img width="1291" alt="Screenshot 2023-02-26 at 15 02 16" src="https://user-images.githubusercontent.com/105980082/221428429-5b0027a3-aa60-49f2-a3a5-05cdcec85af4.png">

<img width="1107" alt="Screenshot 2023-02-26 at 15 02 33" src="https://user-images.githubusercontent.com/105980082/221428464-2a6f2c86-41f2-4181-af07-0600ac8c5db0.png">

2. Navigation

![Screenshot 2023-02-26 at 15 04 17](https://user-images.githubusercontent.com/105980082/221428484-9c8ba68a-9a1f-4357-bde3-b156e1e770fc.png)

![Screenshot 2023-02-26 at 15 04 27](https://user-images.githubusercontent.com/105980082/221428492-31d250a0-a964-4252-841a-8300c9aaed2a.png)

<img width="425" alt="Screenshot 2023-02-26 at 15 07 47" src="https://user-images.githubusercontent.com/105980082/221429062-647d50b6-133a-432a-9e51-7feca0f450be.png">

![Screenshot 2023-02-26 at 15 10 09](https://user-images.githubusercontent.com/105980082/221429080-62ac45dd-32dc-4b59-8392-4e54b2aa1b2e.png)



3. Register and Login

<img width="710" alt="Screenshot 2023-02-26 at 15 03 06" src="https://user-images.githubusercontent.com/105980082/221428572-4c83926c-00b4-48de-af27-b4ae6dad22a9.png">

![Screenshot 2023-02-26 at 15 03 37](https://user-images.githubusercontent.com/105980082/221428586-c21034b9-bec8-451d-b9b5-a26c74c0df3d.png)

* Forms error 

4. Home Page

* Post with image

![Screenshot 2023-02-26 at 15 04 54](https://user-images.githubusercontent.com/105980082/221428677-e338e4af-b33c-4188-9456-fd8fa27c9fcf.png)

* Post without an image

![Screenshot 2023-02-26 at 15 10 39](https://user-images.githubusercontent.com/105980082/221429217-6515ab6e-5b98-4943-8a48-31f72687da4a.png)

* New Post

<img width="705" alt="Screenshot 2023-02-26 at 15 05 14" src="https://user-images.githubusercontent.com/105980082/221429668-c2f7b7c5-4ffe-4aa6-9703-846287d52566.png">

* Categories

* Navigation dropdown menu

<img width="425" alt="Screenshot 2023-02-26 at 15 07 47" src="https://user-images.githubusercontent.com/105980082/221429735-75af00a3-cdbf-4e91-a1dd-8af8077b87e6.png">

* Posts under the selected category are listed 

<img width="752" alt="Screenshot 2023-02-26 at 15 08 10" src="https://user-images.githubusercontent.com/105980082/221429743-cfa7674a-f3e2-425b-96e8-ed4077b70143.png">

* Category list

<img width="519" alt="Screenshot 2023-02-26 at 15 07 36" src="https://user-images.githubusercontent.com/105980082/221429749-ffac4a67-979b-4fb2-8f84-5917c0cbbf8c.png">

* If a category hasn't got any posts

<img width="957" alt="Screenshot 2023-02-26 at 15 08 31" src="https://user-images.githubusercontent.com/105980082/221429762-560006d5-f4a9-429b-8340-50d383e0dc13.png">




5. Post View

* Post with image

![Screenshot 2023-02-26 at 15 09 18](https://user-images.githubusercontent.com/105980082/221428705-b46bf417-e082-4ada-8437-95472250ce31.png)

* Post without an image

![Screenshot 2023-02-26 at 15 10 51](https://user-images.githubusercontent.com/105980082/221429292-665520ae-79c6-48be-bcfe-a1ef33c430ff.png)


* Username and Profile Picture

![Screenshot 2023-02-26 at 15 12 08](https://user-images.githubusercontent.com/105980082/221429330-09cef8e6-c21e-475d-b15a-d27e35048f28.png)

* Likes and Comments

![Screenshot 2023-02-26 at 15 11 51](https://user-images.githubusercontent.com/105980082/221429355-29fcfc56-c39e-4e91-b8cc-6945954a3e9c.png)


* Comments

![Screenshot 2023-02-26 at 15 09 44](https://user-images.githubusercontent.com/105980082/221428777-7f5d6747-8e10-4866-a45d-bb85b5412c65.png)

* Add Comment

![Screenshot 2023-02-26 at 15 09 54](https://user-images.githubusercontent.com/105980082/221429371-7608d712-8015-40d8-8ee7-85a51245b864.png)

* Delete and Edit Post

![Screenshot 2023-02-26 at 18 30 17](https://user-images.githubusercontent.com/105980082/221429495-88a7d8a2-74e1-4c69-a909-cf8a36925c63.png)


* Edit Post

![Screenshot 2023-02-26 at 15 11 04](https://user-images.githubusercontent.com/105980082/221429527-cc500042-6ccf-450b-a5d4-c75c6d41b7f9.png)


* Delete Post

![Screenshot 2023-02-26 at 15 11 25](https://user-images.githubusercontent.com/105980082/221429502-a46e6a2c-b96d-44ff-af51-3eb1fd3a250e.png)




6. Account Management

* User

<img width="554" alt="Screenshot 2023-02-26 at 15 15 03" src="https://user-images.githubusercontent.com/105980082/221428836-392a3036-837f-4778-a675-d820e09af660.png">

<img width="698" alt="Screenshot 2023-02-26 at 15 06 20" src="https://user-images.githubusercontent.com/105980082/221428904-b1f87aba-d75c-49fb-9e0b-b6866e34ba41.png">

<img width="709" alt="Screenshot 2023-02-26 at 15 07 02" src="https://user-images.githubusercontent.com/105980082/221428931-0d86c1d4-bbb2-4bb9-bc3a-3136b9e5c31a.png">

<img width="705" alt="Screenshot 2023-02-26 at 15 07 16" src="https://user-images.githubusercontent.com/105980082/221428950-876da880-9ab3-4695-aa44-d6c410bd9a65.png">

* Admin

<img width="547" alt="Screenshot 2023-02-26 at 15 05 42" src="https://user-images.githubusercontent.com/105980082/221428875-e77035e6-9bad-44d2-9525-a3ec62b90d0b.png">

<img width="699" alt="Screenshot 2023-02-26 at 15 06 42" src="https://user-images.githubusercontent.com/105980082/221429033-bf5750a9-93ac-4f1c-9559-757a0dd8b408.png">



7. Footer

<img width="1107" alt="Screenshot 2023-02-26 at 15 02 33" src="https://user-images.githubusercontent.com/105980082/221428503-56fb3a51-e6c3-42a5-ac5f-6fc0052cedf4.png">

8. Profile Page

* With Profile Picture

<img width="804" alt="Screenshot 2023-02-26 at 15 06 01" src="https://user-images.githubusercontent.com/105980082/221429599-1fec51c6-80ce-4daa-9105-39bce6b02cfa.png">

* Without Profile Picture

![Screenshot 2023-02-26 at 15 12 21](https://user-images.githubusercontent.com/105980082/221429631-a3b074c0-82d1-48de-8e19-f95c56f18d23.png)




## Features Not Implemented

1. Follow and Unfollow

2. Password reset
    * Due to lack of time, I was not able to implement a proper account backup, so at the moment it is not possible to recover a lost password.

## Future Features

* Social Login
    * The ability for users to use social accounts when registering for a new account would remove the requirement for the site to store password     information and encourage trust among users who are wary when signing up for new services.

* Editable fields shown directly on the detail page, rather than having to edit on a separate page.
   * This would be to allow users to quickly update their posts.

* Follow and Unfollow
    * Users can view posts only from users they follow.

* Password reset

* User search
    * User can research other users

* Site Style Customization
    * User can decide to have a light or dark theme


## Technologies Used

### Languages Used

* HTML5
* CSS3
* Python
* Javascript

### Python Modules and Packages/Frameworks Used

* Built-in Packages/Modules

    * datetime - Used to get current time in a timezone aware format to use when creating a post
    * os - This module provides a portable way of using operating system dependent functionality.

* External Python Packages

    * cloudinary - Used for the Post Image Model field, Image upload and deletion.
    * dj-database-url - Allows the use of 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
    * dj3-cloudinary-storage - Facilitates integration with Cloudinary by implementing Django Storage API.
    * Django - High-level Python Web framework used to develop the project.
    * django-auth - Set of Django application used for account registration, management and authentication.
    * gunicorn - Python WSGI HTTP Server
    * Pillow - Fork of PIL, the Python Imaging Library which provides image processing capabilities.
    * psycopg2 - Python PostgreSQL database adapter


### Programs and Tools Used

* Bootstrap
  * Bootstrap was used through the project to style the project and create responsive elements/layouts.
* drawSQL - Create Database Schema/ERD
* Visual Studio Code:
  * Visual Studio Code was used as my code editor for this project. A full list of plugins used can be found later in this section.
* Git
  * Git was used for version control, using the terminal to commit to Git and Push to GitHub.
* GitHub:
  * GitHub is used to store the projects code after being pushed from Git.
* Balsamiq:
  * Balsamiq was used to create the wireframes during the design process.


## Testing



## Bugs
### Fixed Bugs


### Remaining Bugs

  No known errors remaining.


## Deployment

### Forking the GitHub Repository

  By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

  1. Log in to GitHub and locate the GitHub Repository

  2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

  3. Click the button (not the number to the right) and you should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

  NOTE: It is a requirement of the is project that you have Python version 3.8 or higher installed locally.

  1. Log in to GitHub and locate the GitHub Repository.

  2. Under the repository name, click "Code".

  3. To clone the repository using HTTPS, under "HTTPS", copy the link.

  4. Open your local terminal with git installed

  5. Change the current working directory to the location where you want the cloned directory to be created.

  6. Type `git clone`, and then paste the URL you copied in Step 3.

  7. Press Enter. Your local clone will be created.

  8. Change the current working directory to the cloned project folder (this will be a child directory in the location you cloned the project).

  9. It is recommended to use a virtual environment during development. If you would prefer not to use on please skip the following steps:

      * Create a virtual environment in the projects working directory by entering the following command in the same terminal window used for the steps above `python3 -m venv .venv`.

      * Before use, the virtual environment will need to be activated using the command `source .venv/bin/activate` in the same terminal window used previously.

  10. Packages required by the project can now using the command `pip install -r requirements.txt`

  11. In the cloned directory, rename the file `.env-example` to `.env` and populate it with the information required.

  12. Make django migrations using the command `./manage.py migrate`.


### Deploying with Heroku

  NOTE: It is a prerequisite of deployment to Heroku that you already have access to the following:

  * A Cloudinary account, create one for free at https://cloudinary.com.

  NOTE: It is assumed you have followed all deployment instructions listed in this readme starting with the section titled 'Forking the GitHub Repository'.

  1. Log in to [Heroku](https://heroku.com) and if not taken there automatically, navigate to your personal app dashboard.

  2. At the top of the page locate the 'New' drop down, click it and then select 'Create new app'.

  3. Give your application a unique name, select a region appropriate to your location and click the 'Create app' button.

  4. Your app should now be created, so from the menu towards the top of the page select the 'Resources' section.

  5. Search for 'Heroku Postgres' under the Add-ons section and add it.

  6. From the menu towards the top of the page select the 'Settings' section and lick 'Reveal Config Vars' in the Config vars section. Enter the following key / value pairings:
      * Key as `ALLOWED_HOSTS` and the value as the name of you project with '.herokuapp.com' appended to the end e.g. `example-app.herokuapp.com`. Click the Add button.
      * Key as `CLOUDINARY_URL` and the value as your cloudinary API Environment variable e.g. `cloudinary://**************:**************@*********`. Click the Add button.
      * Key as `EMAIL_HOST_PASSWORD` and the value as the password or value provided by your email service of choice. Click the Add button.
      * Key as `EMAIL_HOST_USER` and the value as the the email address or value provided by your email service of choice. Click the Add button.
      * Key as `SECRET_KEY` and the value as a complex string which will be used to provide cryptographic signing. The use of a secret key generator is recommended such as https://djecrety.ir. Click the Add button.
      * Ensure the key `DATABASE_URL` is already populated. This should have been created automatically by Heroku.
      * The `DATABASE_URL` should be copied into your local `.env`, created during the cloning process.
  7. Running migrations on the remote database
      * Open your local terminal and change the current working directory to that of the project folder.
      * Make django migrations using the command `./manage.py migrate`.

  8. Navigate to the 'Deploy' page using the menu towards the top of the page.

  9. Select 'GitHub' from the 'Deployment method' section and you will be prompted to 'Connect to GitHub'.

  10. Once connected to your GitHub account you will be able to search for your repository which contains the forked 'Winter-Moments' repository.

  11. Once the repository is found click 'Connect'.

  12. At the bottom of the page find the section named 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.

  13. Once deployment is complete, click the 'View' button to load the URL of the deployed application.

# Credits
  ### Online resources


# Code
  The following credits represent cases where code was adapted or used from external resources. 


# Media


# Acknowledgments
