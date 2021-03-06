# Vegan's Journal Blog

## Code Institute: Portfolio Project 4

### Full-Stack Toolkit site.

![Responsive](documentation/readme/responsive.jpg)

[Click here to view the live project.](https://vegansjournal.herokuapp.com/)

[Click here to view the repository.](https://github.com/PratimaGurav/vegans-journal)

## Table of Contents:
- [User Experience (UX)](https://github.com/PratimaGurav/vegans-journal#user-experience-ux)

- [Features](https://github.com/PratimaGurav/vegans-journal#features)
  
- [Technologies Used](https://github.com/PratimaGurav/vegans-journal#technologies-used)
  
- [Testing](https://github.com/PratimaGurav/vegans-journal#testing)
  
- [Deployment](https://github.com/PratimaGurav/vegans-journal#deployment)
 
- [Credits](https://github.com/PratimaGurav/vegans-journal#credits)

- [Acknowledgements](https://github.com/PratimaGurav/vegans-journal#acknowledgements)
    

## User Experience (UX)

### Introduction

Vegan's Journal is a full-stack application built using mainly the Django full-stack web framework. The purpose of the site is to create a community allowing users to connect and spread knowledge about Vegan. All visitors can read the blogs posted on the site by different users. The application provides a login mechanism where users can register themselves. Logged in users can like, comment and add new post or category of their choice. Comments would be approved by site admin to avoid objectional content being posted. Additionally it allows users to edit and delete their own post.

     
### Audience
The site is targetted to people of all age groups who aspire to be vegan and are willing to know more about veganism.    

### User stories
- Agile methodology was used to create user stories. 
- GitHub’s Kanban feature was used to track the progress of user stories. 

  #### Site User
   1. I want to easily understand the different navigation options offered by the site.
   2. I want to view a list of posts so that I can select one to read.
   3. I want to search a blog post (using relevant word) and ability to click on a post to read the full post.
   4. I want to know the author of one particular post and the date and time the post was created.
   5. I want to view the number of likes on each post so that I can see which is the most popular.
   6. I want to view comments on an individual post so that I can read the conversation.
   7. I want to register and create an account so that I can like existing post(s).
   8. I want to like or unlike a post so that I can interact with the content.
   9. I want to leave comments on a post so that I can be involved in the conversation(s).
   10. I want to create, edit and delete my post.
   11. I want to create a category of my own to add my own post on the site.
  

  #### Site Admin
   1. I want to create, read, update and delete posts so that I can manage the blog content.
   2. I can approve or disapprove comments so that I can filter out objectionable comments.
   3. I want to view the number of likes on each post so that I can see which is the most popular.
   4. I want to view comments on an individual post so that I can read the conversation.

    
### Design

  - #### Color Scheme
    As the theme of the site is all about vegan, the colours used are the classic vegetable colours. The rest of the colours complement each other and maintain good contrast levels.
    ![Color Palette](documentation/readme/site-palette.png)

  - #### Typography
    Raleway italic font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Montserrat italic is used for headings with Sans Serif as the fallback.  

  - #### Wireframes
    Balsamiq was used to create wireframes for mobile, tablet/ipad and desktop.
    
    [Desktop](documentation/wireframes/desktop.pdf) |
    [Tablet](documentation/wireframes/ipad.pdf) |
    [Mobile](documentation/wireframes/mobile.pdf) |
   
    
## Features

 ### Existing Features

  The website is comprised of:

  1. Home page.
  ![Home screenshot](documentation/readme/home.jpg)
  2. Blog page.
  ![Blogpage screenshot](documentation/readme/blog_page.jpg)
  3. Blog-categories page.
  ![Blog-categories screenshot](documentation/readme/blog_categories.jpg)
  4. Blog categories dropdown.
  ![Categories dropdown screenshot](documentation/readme/category_dropdown.jpg)
  5. Categories list page.
  ![Categories list screenshot](documentation/readme/category.jpg)
  6. Add category page.
  ![Add category screenshot](documentation/readme/add_category.jpg)
  7. Add post page.
  ![Add post screenshot](documentation/readme/add_post.jpg)
  8. Add dropdown.
  ![Add dropdown screenshot](documentation/readme/add_post_dropdown.jpg)
  9. Comments.
  ![Comments screenshot](documentation/readme/comments.jpg)
  10. Upvote.
  ![Upvote screenshot](documentation/readme/upvote.jpg)
      Downvote
  ![Downvote screenshot](documentation/readme/downvote.jpg)
  11. Register page.
  ![Register screenshot](documentation/readme/register.jpg)
  12. Login page.
  ![Login screenshot](documentation/readme/login.jpg)
  13. Logout page.
  ![Logout screenshot](documentation/readme/logout.jpg)
  14. Search bar.
  ![Search bar screenshot](documentation/readme/search_bar.jpg)
  15. Search page.
  ![Search page screenshot](documentation/readme/search_page.jpg)
  16. Message flyer.
  ![Message flyer screenshot](documentation/readme/message-flyer.jpg)
     
All Pages on the website have:

* A favicon icon.
    ![Favicon Icon](static/favicon/favicon-32x32.png)
* A responsive navbar.
    ![Navbar](documentation/readme/navbar.jpg)
* A responsive footer.
    ![Footer](documentation/readme/footer.jpg)


### Future Enhancements 
  - Add feature to create a user profile and edit / update profile setting with an option to add user details like first name, last name, last logged in.
  - Add feature to bookmark post(s) and option for particular user to view his/her own post(s).
  - Add subscribe page for users to receive weekly updates.
 
## Technologies Used

### Languages, Frameworks, Libraries & Programs Used

  - [HTML](https://en.wikipedia.org/wiki/HTML) was used to structure the site.
  - [CSS](https://en.wikipedia.org/wiki/CSS) was used to design the site. 
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used to display messages to the user.
  - [Python+Django](https://en.wikipedia.org/wiki/Django_(web_framework)) framework.
  - [PostgresSQL](https://en.wikipedia.org/wiki/PostgreSQL) was used as relational database. 
  - [MARKDOWN](https://en.wikipedia.org/wiki/Markdown) was used to update Readme.
  - [Google Fonts](https://fonts.google.com/) were used to import the font into the style.css file which is used on all pages throughout the project.
  - [Font Awesome](https://fontawesome.com/) was used on all pages throughout the website to add icons for aesthetic and UX purposes.
  - [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  - [GitHub](https://github.com/) was used to store the projects code after being pushed from Git.   
  - [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process. 
  - [Color Adobe](https://color.adobe.com/) was used to select different colours used on the website. 
  - [Cloudinary](https://cloudinary.com/home-3722) was used to store images. 
  - [Heroku](https://heroku.com/) was used for deployment and hosting environment. 
  - [Favicon](https://favicon.io/) was used to create favicon.
  - [Canva](https://www.canva.com/) was used to create free logo.
  - [TinyPNG](https://tinypng.com/) was used to compress images.

## Database Models
![Class Category](documentation/readme/category_dm.jpg)
![Class Post](documentation/readme/post_dm.png)
![Class Comment](documentation/readme/comment_dm.jpg)
    
## Testing

### Bugs
- Disorted form (add post page)
  - [Error](documentation/testing/bugs/add_post.png) no styling for the comments section.
    Used ckeditor to style the content section but the same was not displayed in the live site with a 404 [Error](documentation/testing/bugs/ckeditor-error.jpg). 
  - [Solution](documentation/testing/bugs/add-post-fix.jpg) The ckeditor was rescoped and used css styling to style the content form on all devices.


- NoReverseMatch 
  - [Error](documentation/testing/bugs/no-reverse-path.png) No Reverse match found while adding a post to the site.
    There was no slug to the model, when it was saved, the same slug (an empty string) was used over and over again.
  - [Solution](documentation/testing/bugs/sumbit_post_fix.png) Took the title of the post, and used that as the slug, that what is the save method if the model is doing, the second error was deleting posts that had no slug to tidy up. 

- Failed to load resources (css file) received 404 error
  - [Error](documentation/testing/bugs/404.png) Unable to load CSS file and received 404 error.
  - [Solution](documentation/testing/bugs/404-fix.png) Debug was set to automatic.

### Validation

- [W3C Markup Validator](https://validator.w3.org/nu/) was used to validate every HTML page of the project to ensure there are no  syntax errors. 
  Results of the same can be found [Here](documentation/testing/html)

- [PEP8](http://pep8online.com/) was used to validate python code.
 Results of the same can be found [Here](documentation/testing/pep8)

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate CSS.
  Results of the same can be found [Here](documentation/testing/css)


### Further Testing

 - User trying to register with no details provided.
 ![Register Blank](documentation/testing/manual/registerblank.jpg)

 - User trying to register with the username which already exists and password mismatch.
 ![Register Duplicate](documentation/testing/manual/register-duplicate.jpg)

 - User trying to register using password which does not meet standard password requirement guidelines.
 ![Register Wrong Password](documentation/testing/manual/register_error.jpg)

 - User trying to login with no details provided.
 ![Login blank](documentation/testing/manual/loginblank.jpg)

 - User trying to login with incorrect password.
 ![Wrong password](documentation/testing/manual/login_error.jpg)

 - User trying to submit a post without blog snippet.
 ![Blank blog snippet](documentation/testing/manual/post-blank.jpg)

 - User trying to submit a blank comment.
 ![Blank comment](documentation/testing/manual/comment-blank.jpg)

 - User gets prompted before deleting their post in order to avoid accidentally deleting their posts. 
 ![Delete post](documentation/testing/manual/deletepost.jpg)

### Known Bugs
  - Register form is distorted.
  - On Tablet screen only, the like icon and number of likes is distorted.

## Deployment

### Using Heroku
- Development Enviroment
  1.  Create env.py : It needs to contain these 3 variables.
    - [Cloudinary](https://cloudinary.com/)
    - Secret key is the password of your choice.
    - [Heroku](https://id.heroku.com/) postgreSQL.
    ![env file](documentation/readme/env.jpg)
  2. Create requirements.txt file.
  3. Create Procfile containing application name to ensure proper formatting to avoid the deployment to fail.
  4. Commit and push deployment changes to Github.
  5. Create an account and login to Heroku
    - Create a new app, with an appropriate app name and choose a region.
    ![Create App](documentation/readme/heroku-create-app.jpg)
    - In Resources add Heroku Postgres.
    ![Resources](documentation/readme/heroku-resources.jpg)
    - Within your newly created app go to settings go to Config Vars use the DATABASE_URL Value and add it to your env.py file also you need to connect it via settings.py.
    ![Config Vars](documentation/readme/heroku-configvars.jpg)
    - Create a SECRET_KEY Key and the Value as the desired key.
    - Then go to the Deploy tab next to Deployment Method, click GitHub to connect your account and repository.
    - At the bottom of the page hit deploy branch making sure it is set to main.

 

### Making a Local Clone

  1. Log in to GitHub and navigate to the [GitHub Repository](https://github.com/PratimaGurav/vegans-journal)
  2. To clone the repository using HTTPS, click Code and copy the address. 
  ![Clone Repository](documentation/readme/git-clone.jpg)
  3. Navigate to Git Bash and clone the repository. 
  ![Clone-Command](documentation/readme/git-clone-command.jpg)
  4. Press Enter and your local clone will be created. 
  ![Clone-Output](documentation/readme/git-clone-output.jpg)

## Credits

### Code
- Django walkthrough project in the Full Stack Toolkit was referred for designing and technical implementation.
- [Codemy.com](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) was used as an inspiration and referred to understand Python and Django better.
- [Stack Overflow](https://stackoverflow.com/) was referred for resloution of technical queries.


## Acknowledgements

  -   My Mentor for guidance.
  -   All the tutors, especially Sean for helping me understand and fix few bugs.


## [BACK TO TOP](https://github.com/PratimaGurav/vegans-journal#vegans-journal-blog)