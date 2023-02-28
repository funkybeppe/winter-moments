# Milestone Project 4


## Purpose

This is the 4th portfolio project developed as part of the Code Institute Diploma in Full Stack Development. It was created to demonstrate skills acquired using Django to design and develop websites that offer full CRUD (create, read, update and delete) functionality.

# Winter Moments

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

## CRUD Functionality

* Winter Moments handles data with full CRUD Functionality:

* Create - Users can create, account, profile, post a blog

* Read - Users can view the posts of other users and their own.

* Update - Users can update their blog posts with new context

* Delete - Users can delete their own blog posts


## Design

### Wireframes

I created Wireframes to visualize the site's design and act as a template to use when developing the templates. When designing the site I wanted to ensure the site looked and functioned just as well on mobile as larger viewports. Customers may use phones as their primary device to access the blog


<img width="669" alt="Screenshot 2023-02-28 at 10 27 14" src="https://user-images.githubusercontent.com/105980082/221827873-e2bcb836-0b87-4da1-a2a7-d0050159cb11.png">

<img width="424" alt="Screenshot 2023-02-28 at 10 27 28" src="https://user-images.githubusercontent.com/105980082/221827912-50be9bbd-6617-45c0-93f6-d9a01c312bcd.png">

<img width="661" alt="Screenshot 2023-02-28 at 10 27 38" src="https://user-images.githubusercontent.com/105980082/221827926-a158cfe1-ef47-4348-8022-2e3c3e9c0c0a.png">

<img width="392" alt="Screenshot 2023-02-28 at 10 28 02" src="https://user-images.githubusercontent.com/105980082/221827962-4664c622-ef93-4a57-8374-65655d2a50ce.png">

<img width="670" alt="Screenshot 2023-02-28 at 10 28 12" src="https://user-images.githubusercontent.com/105980082/221827987-f6d67c04-6918-450e-8131-7770ba1b748f.png">

<img width="390" alt="Screenshot 2023-02-28 at 10 28 25" src="https://user-images.githubusercontent.com/105980082/221828011-2038ee3f-d9a6-4646-8416-a80f5b8cdcc7.png">

![Screenshot 2023-02-28 at 10 28 58](https://user-images.githubusercontent.com/105980082/221828037-f280bd70-7420-4c64-9638-178cf31ec270.png)

![Screenshot 2023-02-28 at 10 29 09](https://user-images.githubusercontent.com/105980082/221828084-bfd45db6-eb7a-4336-ac34-698f7e4fe772.png)


## Colour Scheme

Colours used throughout the site were kept to a minimum to keep its focus clear, allowing the blog posts to stand out.

* The website uses Bootstrap dark theme for Navigation, Footer and forms.

* Post cards are in a white shade and text in dark, "View Post" buttons in dark theme color to provide contrast.

* Edit button is provided with a grey color from Bootstrap, Delete button with a red color to stand out.

<img width="934" alt="Screenshot 2023-02-26 at 15 00 19" src="https://user-images.githubusercontent.com/105980082/221435116-4069fa00-c11c-417d-bfba-1b726bdb8f24.png">

## Typography

Google fonts was used in this project with both fonts selected for their legibility and simplicity.

Poppins - Use in headings. Cabin - Use in paragraphs and labels.


## Images and Iconography

The icons are from [Font Awesome](https://fontawesome.com).

The default profile picture was taken from [Flaticon](https://www.flaticon.com/)

The main background image was taken from [Pexels](https://www.pexels.com). Light editing work was undertaken using the [Cloudinary](https://cloudinary.com) editing tool to ensure the image matched the site's aesthetic.

The blog posts pictures are partially taken from my camera album and Pexels.

The Winter Moments logo was created with [Logo.com](https://app.logo.com/)


## Database Schema

4 custom models were created based on the initial database schema design as below. The Post model was created first, then the Profile model after and then extended for the Comment model.

<img width="775" alt="Screenshot 2023-02-27 at 17 59 58" src="https://user-images.githubusercontent.com/105980082/221646104-60950acd-5499-4d00-ad06-be59fcc4c32f.png">


## Features

1. Landing Page

<img width="87" alt="Screenshot 2023-02-26 at 15 02 51" src="https://user-images.githubusercontent.com/105980082/221435031-649932e0-b9da-4c38-a0ed-ec55a44404d9.png">

<img width="1512" alt="Screenshot 2023-02-26 at 14 59 28" src="https://user-images.githubusercontent.com/105980082/221428380-ad6b99ab-e30a-4a39-aa29-0c0a8691d815.png">

<img width="960" alt="Screenshot 2023-02-26 at 15 02 03" src="https://user-images.githubusercontent.com/105980082/221428414-18f728bd-d6b3-49ab-90cc-45fa5a814522.png">

<img width="1291" alt="Screenshot 2023-02-26 at 15 02 16" src="https://user-images.githubusercontent.com/105980082/221428429-5b0027a3-aa60-49f2-a3a5-05cdcec85af4.png">

<img width="1107" alt="Screenshot 2023-02-26 at 15 02 33" src="https://user-images.githubusercontent.com/105980082/221428464-2a6f2c86-41f2-4181-af07-0600ac8c5db0.png">

2. Navigation

* The main navigation bar was designed from the outset to be kept clean and simple. The purpose of this design is to highlight the main functionality of the site (viewing and submitting requests). While links to the site's main functionality are always visible when authenticated, other links were moved to a bootstrap dropdown. The username dropdown function is to contain links to the profile, edit profile page, settings and logout links but it also informs the authenticated user which account they are currently logged in with.

* Authenticated users will be shown their current username in a dropdown at the middle/left of the navigation bar 

* The navigation bar is responsive and will collapse to a 'hamburger' style menu when viewed on devices with smaller viewports. The drop down will be hidden and the links to other features displayed in a list to prevent the nesting of dropdowns.

![Screenshot 2023-02-26 at 15 04 17](https://user-images.githubusercontent.com/105980082/221428484-9c8ba68a-9a1f-4357-bde3-b156e1e770fc.png)

* Unauthenticated users are shown the logo which redirects to landing page

![Screenshot 2023-02-26 at 15 04 27](https://user-images.githubusercontent.com/105980082/221428492-31d250a0-a964-4252-841a-8300c9aaed2a.png)

<img width="425" alt="Screenshot 2023-02-26 at 15 07 47" src="https://user-images.githubusercontent.com/105980082/221429062-647d50b6-133a-432a-9e51-7feca0f450be.png">

* Navigation on smaller viewports

![Screenshot 2023-02-26 at 15 10 09](https://user-images.githubusercontent.com/105980082/221429080-62ac45dd-32dc-4b59-8392-4e54b2aa1b2e.png)



3. Register and Login

* The django-auth module was used to authenticate users, create new users and change their details such as passwords.

<img width="710" alt="Screenshot 2023-02-26 at 15 03 06" src="https://user-images.githubusercontent.com/105980082/221428572-4c83926c-00b4-48de-af27-b4ae6dad22a9.png">

![Screenshot 2023-02-26 at 15 03 37](https://user-images.githubusercontent.com/105980082/221428586-c21034b9-bec8-451d-b9b5-a26c74c0df3d.png)


4. Home Page

* Posts
  * Bootstrap cards were used to contain the posts. Posts can be viewed by clicking on the "view post" button within the card.
  * Post's author profile page can be viewed by clicking the author's name just under the picture.
  * The creation date is shown in the bottom left of the post.
  * The number of likes and comments is shown just next to the creation date.
  * Posts can be with an image or without.

* Post with image

![Screenshot 2023-02-26 at 15 04 54](https://user-images.githubusercontent.com/105980082/221428677-e338e4af-b33c-4188-9456-fd8fa27c9fcf.png)

* Post without an image

![Screenshot 2023-02-26 at 15 10 39](https://user-images.githubusercontent.com/105980082/221429217-6515ab6e-5b98-4943-8a48-31f72687da4a.png)

* New Post
 * The new post link redirects to the "Add Post" form allowing users to create a new blog post
 
 <img width="705" alt="Screenshot 2023-02-26 at 15 05 14" src="https://user-images.githubusercontent.com/105980082/221429668-c2f7b7c5-4ffe-4aa6-9703-846287d52566.png">

* Categories

* Posts are stored in selected categories, only the Admin or Staff member can add a category.
* Users can decide to see only posts of a certain category
* If there aren't any posts under the selected category a message is displayed on the screen.

 * Navigation dropdown menu

 <img width="425" alt="Screenshot 2023-02-26 at 15 07 47" src="https://user-images.githubusercontent.com/105980082/221429735-75af00a3-cdbf-4e91-a1dd-8af8077b87e6.png">

 * Posts under the selected category are listed 

 <img width="752" alt="Screenshot 2023-02-26 at 15 08 10" src="https://user-images.githubusercontent.com/105980082/221429743-cfa7674a-f3e2-425b-96e8-ed4077b70143.png">

 * Category list

 <img width="519" alt="Screenshot 2023-02-26 at 15 07 36" src="https://user-images.githubusercontent.com/105980082/221429749-ffac4a67-979b-4fb2-8f84-5917c0cbbf8c.png">

 * If a category hasn't got any posts

 <img width="957" alt="Screenshot 2023-02-26 at 15 08 31" src="https://user-images.githubusercontent.com/105980082/221429762-560006d5-f4a9-429b-8340-50d383e0dc13.png">



5. Post View

* Upon clicking on the "View Post" button in the home page, the user will be redirected to the actual post page.
* The View Post page shows the Username and Profile picture on the top of the card, the post picture, post description, likes and comments, date of creation. 

* Post with image

![Screenshot 2023-02-26 at 15 09 18](https://user-images.githubusercontent.com/105980082/221428705-b46bf417-e082-4ada-8437-95472250ce31.png)

* Post without an image

![Screenshot 2023-02-26 at 15 10 51](https://user-images.githubusercontent.com/105980082/221429292-665520ae-79c6-48be-bcfe-a1ef33c430ff.png)


* Username and Profile Picture
 * Users can click on the author's name to view their profile page.

![Screenshot 2023-02-26 at 15 12 08](https://user-images.githubusercontent.com/105980082/221429330-09cef8e6-c21e-475d-b15a-d27e35048f28.png)

* Likes and Comments
 * Users can leave likes by clicking on the heart icon, the icon will change color to red if liked.

![Screenshot 2023-02-26 at 15 11 51](https://user-images.githubusercontent.com/105980082/221429355-29fcfc56-c39e-4e91-b8cc-6945954a3e9c.png)


* Comments

 * Users can leave comments under the post by clicking the "Add Comment" link, redirecting to the Add Comment page.
 * Comments are displayed in this way:
   * The commenter's username, the actual comment, comment date.

![Screenshot 2023-02-26 at 15 09 44](https://user-images.githubusercontent.com/105980082/221428777-7f5d6747-8e10-4866-a45d-bb85b5412c65.png)

* Add Comment

![Screenshot 2023-02-26 at 15 09 54](https://user-images.githubusercontent.com/105980082/221429371-7608d712-8015-40d8-8ee7-85a51245b864.png)

* Delete and Edit Post
 * Users can Edit and Delete their posts only, Edit and Delete buttons are provided below the post.

![Screenshot 2023-02-26 at 18 30 17](https://user-images.githubusercontent.com/105980082/221429495-88a7d8a2-74e1-4c69-a909-cf8a36925c63.png)


* Edit Post

![Screenshot 2023-02-26 at 15 11 04](https://user-images.githubusercontent.com/105980082/221429527-cc500042-6ccf-450b-a5d4-c75c6d41b7f9.png)


* Delete Post

![Screenshot 2023-02-26 at 15 11 25](https://user-images.githubusercontent.com/105980082/221429502-a46e6a2c-b96d-44ff-af51-3eb1fd3a250e.png)




6. Account Management

* User
 * Users can update their profile page and their account settings.

<img width="554" alt="Screenshot 2023-02-26 at 15 15 03" src="https://user-images.githubusercontent.com/105980082/221428836-392a3036-837f-4778-a675-d820e09af660.png">

<img width="698" alt="Screenshot 2023-02-26 at 15 06 20" src="https://user-images.githubusercontent.com/105980082/221428904-b1f87aba-d75c-49fb-9e0b-b6866e34ba41.png">

<img width="709" alt="Screenshot 2023-02-26 at 15 07 02" src="https://user-images.githubusercontent.com/105980082/221428931-0d86c1d4-bbb2-4bb9-bc3a-3136b9e5c31a.png">

<img width="705" alt="Screenshot 2023-02-26 at 15 07 16" src="https://user-images.githubusercontent.com/105980082/221428950-876da880-9ab3-4695-aa44-d6c410bd9a65.png">

* Admin
 * Users with Admin position are able to access Django admin panel from the dropdown menu

<img width="547" alt="Screenshot 2023-02-26 at 15 05 42" src="https://user-images.githubusercontent.com/105980082/221428875-e77035e6-9bad-44d2-9525-a3ec62b90d0b.png">

<img width="699" alt="Screenshot 2023-02-26 at 15 06 42" src="https://user-images.githubusercontent.com/105980082/221429033-bf5750a9-93ac-4f1c-9559-757a0dd8b408.png">



7. Footer
* Footer includes link to social networks and the website author name.

<img width="1107" alt="Screenshot 2023-02-26 at 15 02 33" src="https://user-images.githubusercontent.com/105980082/221428503-56fb3a51-e6c3-42a5-ac5f-6fc0052cedf4.png">

8. Profile Page
* Every user has their personal profile page:
  * Profile page contains profile picture, Username, First and Last Name, Bio and Social Links
  * Profile is editable
  * Profile can be without picture, however a default picture will be selected if users does not provide one.

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

### Manual Tests

Manual testing occurred regularly throughout local development, making use of statements that would print information to the console and use of the Django debug pages.

#### Tests Cases

##### Registration
| Testing | Steps | Expected Outcome | Results |
| ------- | ----- | ---------------- | ------- |
| Form Validation | Try to submit empty form | Form validation will prompt for user action | PASS |
| Form Validation | Try to submit invalid email address | Form validation will prompt for user action | PASS |
| Form Validation | Try to submit username that is already taken | Form validation will prompt for user action | PASS |
| Form Validation | Try to submit non-complex, not matching passwords | Form validation will prompt for user action | PASS |
| Form Validation | Remove the required attribute using browser console tools and submit with no first or last name but other valid fields| Form validation will prompt for user action | PASS |
| Registration Success | Enter unique, valid information for all fields | User is notified with a success message and redirected to the email verification page. Verification email is send to email address entered in registration form. Account can be seen in the Django admin panel | PASS |

##### Create and Edit Posts
| Testing | Steps | Expected Outcome | Results |
| ------- | ----- | ---------------- | ------- |
| Text Field Validation | Try to submit empty form |  | PASS |
| Text Field Validation | Enter a description and title with more characters than the required amount and submit the form | Form validation will prompt for user action | PASS |
| Image Field Validation | Try to submit a video instead of a picture | Form validation will notify the user the image format is not valid or corrupted | PASS |
| Image Field Validation | Enter valid information for all fields | Post submitted, user redirected to home page, post matches all informations as entered in the form | PASS |

##### Post Deletion
| Testing | Steps | Expected Outcome | Results |
| ------- | ----- | ---------------- | ------- |
| Delete button visible on posts| Log in as user, navigate to a post of your creation detail view and ensure delete button is visible | Delete button visible | PASS |
| Delete button redirects to delete post page| When looged in as user on a post of your creation, click delete button and a deletion confirmation page will be shown | Delete page redirect with deletion confirmation message and delete button | PASS |
| Others users posts cannot be deleted | Log in as user, navigate to a post that is not yours, ensure there's no delete button visible | Only edit and delete buttons are visible in the post details of your creations | PASS |
| Post can be deleted | Click the deletion confirmation button in the deletion page | Post is deleted, post images (if any) are removed from Cloudinary. User is redirected to the post list view | PASS |

##### Navigation
| Testing | Steps | Expected Outcome | Results |
| ------- | ----- | ---------------- | ------- |
| Users can view their posts | Navigate to a post detail URL | Post detail is visible | PASS |
| Users can view other users posts | Navigate to a post detail URL that is not of your creation | Post detail is visible | PASS |
| Users can view their profile page | Navigate to my profile page | Profile page is visible and showing only the data user added| PASS |
| Users can view other users profile page | Navigate to a user profile page by clicking on their name on a post | Profile page is visible and showing only the data user added| PASS |
| Categories | Navigate to Category page | Category list is displayimng only the categories added by admin | Categories are displayed in a dropdown menu | PASS |
| Posts in Categories | Navigate to a category in the categories list | Only posts with the same shared category should be listed | Only posts with the same category are listed | PASS |
| Empty Category selection | Navigate to a category in the categories list | A message should be displayed in case of no posts in the selected category | A message is displayed saying "No Posts yet in this category" | PASS |

##### Profile View and Edit
| Testing | Steps | Expected Outcome | Results |
| ------- | ----- | ---------------- | ------- |
| Form Validation | Change first and last name and try to submit | Form validation will prompt for user action | PASS |
| Form Validation | Enter username that is already taken | Form validation will prompt for user action | PASS |
| Form Validation | Enter unique | Valid information for all fields | PASS - User is notified with a message and redirected profile detail page |
| Form Validation | Change password and try to submit with empty fields | Form validation will prompt for user action | PASS |
| Form Validation | Change password and try to submit with wrong fields | Form validation will prompt for user action | PASS |
| Form Validation | Change password and with correct details and submit | User is redirected to a success page displaying a message confirming that password has been changed | PASS |

##### Browser Tests
| Testing | Steps | Expected Outcome | Results |
| ------- | ----- | ---------------- | ------- |
| Safari Navigation Test | Navigate to website on Safari browser | All the content is displayed correctly and responsive | PASS |
| Safari Navigation Test Mobile | Navigate to website on Safari browser from mobile device | All the content is displayed correctly and responsive | PASS |
| Chrome Navigation Test | Navigate to website on Chrome browser | All the content is displayed correctly and responsive | PASS |
| Chrome Navigation Test Mobile | Navigate to website on Chrome browser from mobile device | All the content is displayed correctly and responsive | PASS |
| Firefox Navigation Test | Navigate to website on Firefox browser | All the content is displayed correctly and responsive | PASS |
| Firefox Navigation Test Mobile | Navigate to website on Firefox browser mobile | All the content is displayed correctly and responsive | PASS |

### Code Validation

#### HTML

The W3C Markup Validator and W3C CSS Validator Services were used to validate the project's HTML and CSS files to ensure there were no syntax errors or warnings.


#### CSS

No validation errors reported.


#### Python

No validation error reported when using the [PEP8 Online Check Tool](http://ww12.pep8online.com/).


#### JavaScript

No validation errors reported testing with [JSHint](https://jshint.com/).

## Bugs
### Fixed Bugs

* When admin logs out from admin page redirects to index page instead of home page, however user still logged in.

### Remaining Bugs

  No known errors remaining.

#### Accessibility

* Best Practices score lower due to image resize to fit logo, performances are not alterated.

![Screenshot 2023-02-26 at 20 12 36](https://user-images.githubusercontent.com/105980082/221434664-49cac971-fb60-49b1-a577-8e82033a033b.png)

### Devices user for manual testing

* Site was tested using the following desktop and mobile browsers:
   * Chrome, Firefox, Safari
   * Iphone 14 Pro Max
   * iPad 6th Gen


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
  
* [Django Documentation](https://www.djangoproject.com/)
* [Bootstrap Documentation](https://getbootstrap.com/)
* [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
* [Webkit](https://webkit.org/)
* [LearnDjango](https://learndjango.com/)
* [Cloudinary](https://cloudinary.com/)
* [Code institute](https://learn.codeinstitute.net/) for Django Tutorial modules and read me template

# Code

  * Code snippet for messages dismissal taken from Code Institute I Think Therefore I Blog project.
  * Like buttons color and css styles taken from Code Institute I Think Therefore I Blog project.
  * Card pagination adapted from Code Institute Django Tutorial
  * Pass request.user from ListView:
     * CREDIT: TS Jee and nishant - Stack Overflow
     * URL: https://stackoverflow.com/questions/54069084/passing-request-user-to-a-queryset-in-modelchoicefilter
  * Set first and last name as required fields for the update form:
     * CREDIT: andreaspelme - Stack Overflow
     * URL:  https://stackoverflow.com/a/7683392
  * Add data to form when using CreateView
     * CREDIT: Piyush Maurya - Stack Overflow
     * URL: https://stackoverflow.com/a/45221181
   * Understanding get absolute url and reverse in Django
     * CREDIT: CodingEntrepreneurs - Python & Django 3.2 Tutorial Series
     * URL: Video 44 (get absolute url) & 45 (Django URLs Reverse)
  

# Media

* Post pictures partially taken from Pexels and partially from my personal camera.
* The Winter Moments logo was created with [Logo.com](https://app.logo.com/)

# Acknowledgments

As always a huge thank you to my mentor Ronan McLelland and the Code Institute Slack community members for their advice and support during the development of this project.
