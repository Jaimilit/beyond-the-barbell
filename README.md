Beyond the Barbell

The deployed app: [Heroku](https://beyond-the-barbell-0789d667f147.herokuapp.com/)

GitHub Repository: [GitHub](https://github.com/Jaimilit/beyond-the-barbell)

# Table of Contents

- [Project Goals](#project-goals)
- [UX](#ux)
    - [Agile Tools](#Agile-Tools)
- [Design and Structure](#design-and-structure)
    - [Kanban Boards](#kanban-boards)
    - [Functional Structure](#functional-structure)
- [WireFrames](#Wireframes)
- [Features](#features)
    - [Navigation Bar](#navigation-bar)
    - [Pages](#pages)
- [Responsive Design](#responsive-design)
- [Future Features](#future-features)
- [Technology Used](#technology-used)
    - [Languages](#languages)
    - [Frameworks, Libraries, and Programs](#frameworks-libraries-and-programs)
    - [Database](#database)
    - [Program and Tools](#program-and-tools)
- [Testing](#testing)
    - [Bugs](#bugs)
        - [Manual Testing](#manual-testing)
        - [Browser Testing](#browser-testing)
    - [Validation](#validation)
        - [HTML Validation](#html-validation)
        - [CSS Validation](#css-validation)
        - [Python Validation](#python-validation)
        - [Lighthouse](#lighthouse)
- [Deployment](#deployment)
    - [Github](#github)
    - [Heroku](#heroku)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Inspiration](#inspiration)


Project Goals

This project is for an e-commerce website for a hypothetical business called Beyond the Barbell.

Beyond the Barbell is a business to customer (B2C) e-commerce site, selling products to users - such as health products, clothes, and gear. Additionally, users can subscribe to the box/gym with different variations of subscriptions as well as buy personal training sessions. As a member, the user can also write reviews of personal trainers, as well as sign up for competitions offered.

Features of this business-focused website include a shopping cart, a catalogue of products, an online payment system that can save the customer’s preferred mode of payment, sign up for an email newsletter, contact us page, and private policy statement.

The site was developed using Python in the Django framework and styled using CSS and Bootstrap. ElephantSQL is used for the database and Heroku for deployment.

# UX

User stories

As a first time visitor, I want:

* To easily understand the main purpose of the site
* To be able to easily navigate through the site
* To be able to register a user account to access all content without restrictions
* To be able to view products, memberships, read reviews, contact us, & subscribe with us
* To be able to search and sort products easily
* To be able to create an account and log out of a user account
* To be able to purchase products, memberships, write reviews, contact us, & subscribe
* To be able to receive confirmation of my actions via messages


Returning and frequent user goals

As a returning user, I want:

* To sign into my user account
* To be able to search and sort products easily
* To make a booking for a competition
* To view and delete my competitions
* To purchase products, view cart, & checkout
* To view orders
* Receive confirmation of my actions via messages
* Be able to make secure payments
* To view my profile

Site Administrator goals

* As a Site Administrator I would like to be able to add, edit, & delete products
* As a Site Administrator I can approve reviews written
* As a Site Administrator I can update competitions

## Agile Tools

The Projects section in GitHub was used for this project. A Kanban board was used for the development of this project, which made it possible to break down the project into subtasks and make it easier to complete and track project progress.  In addition, labels were used to further define the priority of each user story in the Kanban board.

# Design and Structure

The layout and design of this site was kept basic and simple. Minimal color was used to keep it simple. [Coolors](https://coolors.co/) was used for simple color choices. This website is meant to be functional and therefore I kept the color palette simple and something similiar to what you would see in an actual gym.  


## Kanban Boards

[Kanban Board](https://github.com/users/Jaimilit/projects/6) was used to create this project.
User Stories were moved through the process from To do >> In Progress >> Done on the Kanban Board.
All User Stories were prioritized: Must Have, Should Have, & Would Like to Have. Each user story was also linked to a milestone as well.

Here you can see my overview of my kanban board and moving items around as I was working on them.
![Kanban Boards](./media/kanbanprogress.png)

Here is an example and this one has the can see the labels and milestones connected to it.
![Kanban Boards Example](./media/kanbanexample.png)
![Kanban Boards Example](./media/kanbanmilestones.png)


## Functional Structure
Home page: The home page contains a navigation menu, logo, and an image that gives the user an idea of what the website is about. Here users are given a option to join or go to any of the  links in which they are interested in.

Registration page: The user must create an account to make a purhcase or to sign up for a competition. To do this, they are asked to fill out a form on the page with the required fields: Email, username, & password. They will need to confirm their email address.

Sign In/Login page: A username/email and password are required to log in for existing users. Once signed in, they are directed to the home page.

Logout page: Logging out of the account is done through the menu, after which the user is redirected to the logout page where they must confirm their desire to log out of the account. After a successful logout, the user is returned to the home page.

Products page: A user can view all the products offered and sort through the products offered. Can sort by category, rating, & price. 

Train With Us: There are two options here: Memberships & Personal training sessions. Memberships to purchase are 3, 6, & 12 months, while a user can purhcase personal training sessions in 1, 5, or 10 sessions.

Competitions: You must be logged in to join a competition, but here users can see which competitions they are join. They can also view and delete their competitions as well.

Connect With Us: Here users have a few different views: Contact Us, Reviews, Newsletter & Private Policy. The contact us page the user can complete a form to contact us. The reviews page a user can view personal training reviews and write their own review which will be approved by admin prior to posting. Users can also sign up for a newsletter, as well as view the private policy statement.


# Wireframes

Wireframes were used to create the basic layout of the project. The wireframes pages can be seen below:

Homepage:
![wireframes-homepage](./media/wfhomepage.png)

Products:
![wireframes-Webshop](./media/wfwebshop.png)

Train With Us:
![wireframes-Train With Us](./media/wftrainwithus.png)

Competitions:
![wireframes-Challenges](./media/wfchallengespage.png)

Models:
![wireframes-Models](./media/modelspage.png)

Moscow:
![wireframes-Moscow](./media/moscow.png)


# Responsive Design

The site has been designed to be responsive and adapted for use on both desktop and mobile devices. The project has been tested using a multi-device emulator with different screen sizes in the Google Chrome Developer Dashboard.
![responsive](./static/assets/images/validations/iamresponsive.png)

# FEATURES

## Navigation Bar

The navigation bar is present on all pages of the site. The nav bar as different sections:
Navigation for an unauthorized user: All Products, Train With Us, Memberships, Competitions, Connect With Us, Account, & Checkout Bag.
![nav bar](./media/navigation.png)

Also, the navigation bar is an adaptive element, and on mobile screens it collapses into a hamburger icon.

Navigation on Mobile:
![nav on mobile](./media/navmobile.png)

## Pages

Registration Page - Where a user can sign up to use the platform:
![registration](./media/registration.png)

Sign-In Page - Where a returning user can log-in:
![sign-in](./media/signinpage.png)

Log Out Page - Where a user can log out. It asks for confirmation to log out: 
![logout](./media/logout.png)

Home Page - Where a user is first brought to on the site: 
![home page](./media/homepage.png)

Products Page - Where a user can view products to purchase: 
![Products page](./media/allproducts.png)

Train With Us - Where a user can buy memberships & personal training subscriptions:
![Train With Us](./media/trainwithus.png)

Webshop Products - Where a user can view products by categories:
![Webshop](./media/webshopproducts.png)

Competitions - Where a user can view competitions to join if they are signed up and logged in: 
![Competitions page](./media/joincomp.png)

Competition Booking Page - Where a user can view the competitions they are booked and/or delete their bookings.
![Competition Booking page](./media/competitionbooking.png)

Connect With Us - This is where users can do severl things - contact us, read/write reviews, join newsletter, read the private policy.
![contact us page](./media/contactus.png)
![reviews page](./media/reviews.png)
![newsletter page](./media/subscribe.png)
![newsletter joined page](./media/subscribemessage.png)
![private policy page](./media/privatepolicy.png)

Profile Page - Where a user can complete their profile page:
![My Pofile page](./media/myprofile.png)

Add to Cart - Where a user can add a product to their cart:
![Add to Cart page](./media/addtocart.png)

Shopping Bag - User can view their shopping bag/cart:
![Shopping Bag page](./media/shoppingbag.png)

Check Out - User can go to checkout to buy their products:
![Check Out page](./media/checkout.png)

Order Success - User is informed that their order was successful:
![Order page](./media/ordersuccess.png)

Edit or Delete Product - Where Admin can edit and delete products:
![Edit or Delete Product page](./media/editanddeleteproducts.png)

Messages - Where users are informed of their actions
![Message Notifications page](./media/messagenotifications.png)

Footer - Information that it was created by me plus appropriate links:
![footer](./static/assets/images/features/footer.png)

# Future Features

* Page with information about the personal trainers
* Page where user can view past competitions
* Page where users can connect with other users


# Technology Used:

## Languages:

* Python
* JavaScript
* HTML5
* CSS3

## Frameworks, Libraries, and Programs:

* [Django](https://pypi.org/project/Django/3.2.14/): Python framework used to create all the backend
* [Bootstrap](https://getbootstrap.com/): Frontend framework used to provide structure, style, and responsive behaviour


## Database:
* [PostgreSQL](https://www.elephantsql.com/): The database used to store all the data 

## Programs and Tools:

* [Google Fonts](https://fonts.google.com/): Was used to to incorporate font styles
* [Font Awesome](https://fontawesome.com/): Was used to create the icons used on the website
* [Gitpod](https://gitpod.io/workspaces): Gitpod was used as IDE to commit and push the project to GitHub, though I started with Codeanywhere, but most of it was in Gitpod
* [GitHub](https://github.com/): Was used to store my code
* [Am I Responsive](https://ui.dev/amiresponsive): To generate an image showcasing the website's responsiveness to different screen sizes
* [Pip3](https://pypi.org/project/pip/): To install Python modules and libraries
* [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Requests for Python to understand
* [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python
* [AWS](https://aws.amazon.com/): The image hosting service used to upload images and other media
* [Heroku](https://dashboard.heroku.com/apps): The hosting service used to host the website
* [VSCode](https://code.visualstudio.com/): The IDE used to develop the website
* [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/): Was used to debug the website
* [W3C Validator](https://validator.w3.org/): Was used to validate HTML5 code for the website
* [W3C CSS validator](https://jigsaw.w3.org/css-validator/): Was used to validate CSS code for the website
* [Pep8 Validator](https://pep8ci.herokuapp.com/): Was used to validate python code for the website
* [Github Projects](https://github.com/): Kanban board was used to track the progress of the project in general and of every application in the project
* [Wireframes](https://balsamiq.com/learn/articles/what-are-wireframes/): Was used to created the outline for my project


# Testing

## Bugs

###
No known bugs remaining

### Manual Testing

Testing was done throughout the process while developing the project by the use of Django debug pages and printing statements to check that the code functioned accordingly. In addition, thorough testing has been performed and is described below, it contains manual test to check that all user stories and acceptance criteria are met, as well as testing and validating the code with different online tools as presented below.


### Browser Testing

Testing has been carried out on the following browsers:

* Google Chrome
* Firefox
* Safari

The site was constantly tested during the process of creating the site in the Gitpod Environment and the deployed site on Heroku was also tested in terms of user experience. The available functionality and user experience is reflected in the table below.

| Goals and Actions | As a Guest | As a User | Comment |
| -------- | -------- |  -------- | -------- |
| I can use the menu and navigate through the pages   | X | X | Click on items
| I can see the Home Page   | X | X | Click on items
| I can see the Registration Page  | X | X | Click on items and this disappears from the nav bar once registered
| I can see the Bookings Page |   | X | Need to be authorized to see
| I can see the My Bookings page  |  | X | Need to be authorized to see
| I can see the Sign Up Page | X | X | Click on items
| I can see the Login/Logout Pages | X | X | You see one or the other depending on if you are logged in or logged out
| I can complete the Registration form  | X | X | Click on items
| I can complete the Sign In form  | X | X | Click on items
| I can make a booking for a particular session/class |  | X | Need to be authorized to do
| I can delete a particular session/class |   | X | Need to be authorized to do
| I can edit a particular session/class by adding a note |   | X | Need to be authorized to do
| I can see if I have made a booking successfully  |   | X | Need to be authorized to do
| I can see if I have already made a booking for a session  |  | X | Need to be authorized to do
| I can see if a session has availability (max 20)  |  | X | Need to be authorized to do

* Example of format error was not putting the different days in the right place. It was putting all the workouts under Monday which was the default. This was later recified.
![Layout Format](./static/assets/images/bugs/bug-layout-gym-session.png)

* Example of format issue for the layout of the success page.
![Layout Format for Success Page](./static/assets/images/bugs/bug-layout-success.png)

* Example of issues with functions between booking and booking_session not working correctly. Automated testing to fix issue.
![Booking Issues](./static/assets/images/bugs/bug-testing.png)

| Bug| Solution | 
| ------- | ------- |  
|  Issue with bookings showing all on Mondays | Need to adjust the book_session and booking functions |
| Issue with filtering objects if booking_exists to be able to later change the booking  | Use print states and True/False to find the error |
| CSS issues on Successful Booking Page | Ensure all classes were correct, as well as divs | 
| Delete Booking wouldn't go to delete_booking page | Needed to rework delete function and return renders outcomes | 
| When Debug was set to False, none of the CSS was displayed in Heroku app| Python command to collect static files | 
| When trying to implement 20 max for session, it would write none instead of a message when at 20 spots| Change functions and create error page | 
| When I was creating the editing function I first used the booking form to edit, but then the user could change the username and workout session | I created a new form which was just the note so that could be edited| 


## Validation

### HTML Validation:
The W3C Markup Validation Service was used to validate the HTML of the website. There were errors and warnings in the reports about unclosed elements and tags, incorrect values ​​and types of elements, and unnecessary trailing slashes. All errors and warnings have been fixed, the project's HTML code has been re-checked without significant errors.

It shows one error here and I have fixed it, but it still shows.
![HTMl Validation](./static/assets/images/validations/html.png)


### CSS Validation:
The website CSS style has successfully passed the W3C Jigsaw CSS Validation Service.
![CSS](./static/assets/images/validations/css-validation.png)

### Python Validation (PEP8)
All Python code was manually checked using CI Python Linter. The Linter reports had messages about exceeding the string length of 79 characters, which have been fixed. Re-testing did not reveal any errors.

* urls.py
![urs.py](./static/assets/images/validations/urls-linter.png)
* urls.py for signup
![urs.py](./static/assets/images/validations/linter-urls-signup.png)
* models.py
![models.py](./static/assets/images/validations/linter-models.png)
* forms.py
![forms.py](./static/assets/images/validations/linter-forms.png)
* views.py
![views.py](./static/assets/images/validations/linter-views.png)
* admin.py
![admin.py](./static/assets/images/validations/linter-admin.png)

During testing a few issues were identified and corrected:

* Extra whitespace was deleted
* Indentations were corrected
* Two lines spaces between functions and classes
* All lines adjusted to <80 characters
* Minor errors with missing closing tags

### Lighthouse

![Lighthouse](.media/lighthouse.png)


# Deployment
I followed the below steps using the Code Institute tutorial. The project was first created in GitHub. The project code is stored on GitHub, and then deployed to Heroku. To deploy, follow these steps:

## Github

1. Create an account at GitHub or login to an existing account.
2. Go to the GitHub repository for Beyond-the-Barbell.
3. Click the 'Code' button and copy and paste code into Gitpod workspace.
4. A copy of the repository will be available in your own workspace.

## Heroku
The site is deployed to Heroku through the following steps:

1. Log in to Heroku or create an account, if required. On the Welcome page in the top right corner click the button labeled 'New'.
2. From the drop-down menu select 'Create new app'. Enter a preferred app name. Select the relevant geographical region. Click to 'Create App'.
3. Navigate to 'Settings' and scroll down to the 'Config Vars' section. Click 'Reveal Config Vars' and enter 'PORT' for the key and '8000' for the value. Then click 'Add'. Add CLOUDINARY_URL, DATABASE_URL and SECRET_KEY. URL variable values ​​must be copied from your [CLOUDINARY](https://cloudinary.com/) account and [ElephantSQL](https://www.elephantsql.com/) account. To create a SECRET KEY, use the online service or come up with your own.
4. Click on the 'Deploy' tab. Next to 'Deployment method' select 'GitHub'. Connect the relevant GitHub repository. Under 'Manual deploy' choose the correct branch and click 'Deploy Branch'. Also you can select 'Automatic Deploys' so that the site updates when updates are pushed to GitHub.
5. After successful deployment message in the page top right corner click the button labeled 'Open app' and you can access live app.

# Credits

## Code
The structure and the code of the project was based on two walkthroughs by the Code Institute:

* Hello Django - I created CRUD functionalities based on the examples of this walkthrough.
[Django Documenation](https://www.djangoproject.com/) was used to provide examples of code solutions and Django functionality.
* [Bootstrap Documenation](https://getbootstrap.com/)  was used to provide examples of Bootstrap functionality and building blocks.
* [Code Institute WalkThroughs](https://codeinstitute.net/se/) "Boutique Ado" worked as inspiration and code examples.

## Content

Information is fictional and created by me and I was inspired by my own CrossFit box 
[CrossFit Fabriken](https://www.cf-fabriken.com/). This is my CrossFit box and my inspiration for this project. I also used
[Nordic Wellness](https://nordicwellness.se) as inspiration as I belong to this gymn as well.

Though this information is in Swedish. 

## Media

My images were free to use from [Pexels](https://www.pexels.com/) and [Unsplash](https://www.unsplash.com/).

## Inspiration

* This project was inspired by the "Boutique" and other projects from Code Institute.
 * Farah Maria's Readme.md file was used as a template for writing my own Readme.md.
 * CrossFit Fabriken website was used as inspiration as well as Nordic Wellness.