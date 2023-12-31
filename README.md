# :books: My Recipes Book

Welcome to [My Recipes Book!](https://my-recipes-book-pp4-3364500b645d.herokuapp.com/) This is a web application designed to help you manage and organize your collection of recipes. Whether you're a seasoned chef or just starting out in the kitchen, this app is here to make your cooking experience more enjoyable and efficient.

## Table of Contents

* [UX Design](#heavy_check_mark-ux-design)
    * [The Strategy Plane](#round_pushpin-the-strategy-plane)
    * [The Sites Ideal User](#round_pushpin-the-sites-ideal-user)
    * [Site Goals](#round_pushpin-site-goals)
    * [User Stories](#round_pushpin-user-stories)
    * [The Scope Planned](#round_pushpin-the-scope-plane)
    * [Future Enhancements](#round_pushpin-future-enhancements)
* [Technologies](#heavy_check_mark-technologies)
* [Exiting Features](#heavy_check_mark-existing-features)
* [Testing](#heavy_check_mark-testing)
    * [Responsiveness](#round_pushpin-responsiveness)
    * [Browser Compatibility](#round_pushpin-browser-compability-testing)
    * [Light House](#round_pushpin-lighthouse)
    * [Agile and Milestones](#round_pushpin-agile-and-milestone)
    * [Bugs]()
    * [Code Validation](#round_pushpin-code-validation)
        * [HTML](#round_pushpin-html)
        * [CSS](#round_pushpin-css)
        * [Java Script](#round_pushpin-javascript)
        * [Python](#round_pushpin-python)
* [Deployment](#heavy_check_mark-deployment)
    * [How to Fork](#round_pushpin-how-to-fork)
    * [How to Deploy](#round_pushpin-how-to-deploy)
* [Credits](#heavy_check_mark-credits)


## :heavy_check_mark: UX Design

### :round_pushpin: The Strategy Plane

*  Recipes Book is intended to be a friendly community site for users to create and share their own recipes with others.
Users will also be able to find recipes created by other users from around the world. The graphical elements and overall
design of the site provide the user with a fun and enjoyable environment.

### :round_pushpin: The Sites Ideal User

* Food lover looking to share their favourite recipes with others
* Someone looking to expand their recipe knowledge
* Someone looking for inspiration for new things to try
* Someone looking build their cooking social media following

### :round_pushpin: Site Goals

* To provide users with a place to find recipes
* To provide users with a place to share their own recipes
* To provide users with a place to discover new meals

### :round_pushpin: User stories

From the Epics, 15 User stories were developed. Each story was assigned a classification of Must-Have and Could-Have.
I will however revisit them at a later time for a redevelopment of the project. 

These are the user stories that were completed within the projects first release.

![Milestones](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/user-stories.jpg)

### :round_pushpin: The Scope Plane

**Features planned:**

* User Profile
* Recipes - Users can create, read, update and delete their own recipes
* Other Users Recipes - Users can read and like
* Users can login to their account
* Users can logout of their account
* Users need to be registered and logged in to access recipe creation, likes, and edit their own recipes.

### :round_pushpin: Future Enhancements

There are several items of functionality that I would like to add in the future. 
The key areas I would like to add to the site in the future are:

* The ability for users to message other users
* The ability for users to comment on recipes
* The ability for users to login via social networks such as google or facebook
* Save recipes that they like on their profile
* Search functionality
  
## :heavy_check_mark: Technologies

* Python
    * The following python modules were used on this project:
        * asgiref==3.7.2
        * cloudinary==1.34.0
        * dj-database-url==0.5.0
        * dj3-cloudinary-storage==0.0.6
        * Django==3.2.20
        * django-allauth==0.55.0
        * django-summernote==0.8.20.0
        * gunicorn==21.2.0
        * oauthlib==3.2.2
        * psycopg2==2.9.7
        * PyJWT==2.8.0
        * python3-openid==3.2.0
        * requests-oauthlib==1.3.1
        * sqlparse==0.4.4
        * urllib3==1.26.16

* Django
    * Django was used as the main python framework in the development of this project.
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Heroku Was used as the cloud based platform to deploy the site on.
* ElephantSQL - Postgres
    * ElephantSQL was used as the database for this project during development and in production.
* Cloudinary
    * Cloudinary was used to storage all the images files from recipes.   
* JavaScript
    * Custom JavaScript was utilised to set time for messages.
* Bootstrap 5.13
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

## :heavy_check_mark: Existing Features

- __Initial Page__

    - Allow the anyone to see the list of recipes, but only the user that added the recipe will have the options to edit and delete the recipe.

![Initial-Page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/initial_page.jpg)

- __View a Recipe__

    - Allow anyone to read the recipe ingredients and methods.

![View-Recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/view_recipe.jpg)

- __Editing a Recipe__

    - A registered user will be allowed to update their own recipe only.

![Edit-Recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/edit_page.jpg)

- __Deleting a Recipe__

    - A registered user will be allowed to delete their own recipe only. An alert will be raised to the user for confirmation before delete the recipe.

![Delete-Recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/delete_page.jpg)

- __Register User__

    - A user can create their account.

![Create-Account](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/register_page.jpg)

- __Login__

    - A user can login on their account.

![Login](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/login_page.jpg)

- __Logout__

    - A user can confirm if they want to logout before it gets logged out.

![Logout](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/logout_page.jpg)

## :heavy_check_mark: Testing

### :round_pushpin: RESPONSIVENESS:

- The deployed application was tested on multiple devices to check for responsiveness issues. The bootstrap classes were used to be as responsive as possible.

![Responsive](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/responsive.jpg)

### :round_pushpin: BROWSER COMPABILITY TESTING:

The deployed project was tested on multiple browsers to check for compatibility issues and works as expected.

- __Photo of Microsoft Edge:__
      
![Edge](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/Edge.jpg)

- __Photo of Firefox:__

![Firefox](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/mozila.jpg)
  
- __Photo of Mobile:__

![Mobile](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/Mobile.jpeg)


### :round_pushpin: LIGHTHOUSE

The deployed project was tested using the Lighthouse Audit tool to check for any major issues.

![Light House](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/light_house.jpg)


### :round_pushpin: Agile and Milestone

![Agile](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/agile.jpg)

![Milestones](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/milestones.jpg)

### :round_pushpin: Bugs

:x: One bug found when testing the user registration. I found that I missed to add the Account Email verification on Setting.py.

:white_check_mark: After I add the missing information the error was gone.

![Bug error](https://github.com/Adriele-lima/My-recipes-Book/blob/main/static/images/Error_signup.png)

### :round_pushpin: CODE VALIDATION:

### :round_pushpin: HTML

[HTML Validator](https://validator.w3.org/nu/) to validate all HTML files. The result for each page is listed below:

- __Home page__

:x: On home page I found some simple errors:
 
![Error1](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/index1.jpg)

![Error2](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/index2.jpg)

:white_check_mark: All resolved by adding the language to the html, adding "alt" to images and removing duplicated ID.

![Home page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_index_page.jpg)

- __View recipe page__

:x: On view recipe I found some errors:
    Missing "alt" attribute on image files and and extra "< /i >" 
    
:white_check_mark: Both resolved.

![View_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_view_recipe.jpg)

- __Creating recipe page__

:white_check_mark: No errors found.

![Create_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_create_recipe.jpg)

- __Editing recipe page__

:white_check_mark: No errors found.

![Edit_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_edit_recipe.jpg)

- __Deleting recipe page__

:white_check_mark: No errors found.

![Delete_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_delete_recipe.jpg)

- __Loging page__

:white_check_mark: No errors found.

![Login_page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_login_account.jpg)

- __Signup page__

:white_check_mark: No errors found.

![Signup_page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_signup_account.jpg)

- __Logout page:__

:white_check_mark: No errors found.

![Logout_page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_logout_account.jpg)

### :round_pushpin: CSS

[The CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS file.
 
:x: I found one error with a pseudo class.

![CSS_error](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/css_error.jpg)

:white_check_mark: Error was resolved by removing that style as it was not necessary.

![CSS_test](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/CSS.jpg)

### :round_pushpin: JAVASCRIPT

[The JShint Validator](https://jshint.com/) was used to validate the JavaScript file.

:white_check_mark: No errors found.

![Javascript_test](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/JAVASCRIPT.jpg)

### :round_pushpin: PYTHON:

[The Code Institute Python Linterwas](https://pep8ci.herokuapp.com/) was used to validate all Python files.

- __My recipe book - Settings__

:white_check_mark: No errors found.

![settings](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_settings.jpg)

- __My Recipe book - URLs__

:white_check_mark: No errors found.

![Main URLs](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_settings.jpg)

- __My recipes - Form__

:white_check_mark: No errors found.

![My recipes Form](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_form.jpg)

- __My recipes - URLs__

:white_check_mark: No errors found.

![My recipes URLs](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_urls_my_recipe_book.jpg)

- __My recipes - Views__

:white_check_mark: No errors found.

![My recipes Views](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_views.jpg)

- __My recipes - Models__

:white_check_mark: No errors found.

![My recipes Models](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_model.jpg)

## :heavy_check_mark: Deployment

### :round_pushpin: How to Fork

To fork the repository:

1. Log in (or sign up) to Github.

2. Go to the repository for this project.

3. Click the Fork button in the top right corner.
   
### :round_pushpin: How to deploy

How to deploy the repository:

1. On terminal - Install all the necessary applications:
    - Install Django and gunicorn:

            pip3 install 'django<4' gunicorn
      
    - Install supporting libraries:

            pip3 install dj_database_url==0.5.0 psycopg2
      
    - Install Cloudinary Libraries:

            pip3 install dj3-cloudinary-storage
            pip3 install urllib3==1.26.15
      
2. On terminal - Create requirements file:

       pip3 freeze --local > requirements.txt
   
3. On [Elephantsql](https://customer.elephantsql.com/login):
     - Log in to your ElephantSQL account
     - Click “Create New Instance”
     - Set up your plan:
        - Give your plan a Name (this is commonly the name of the project)
        - Select the Tiny Turtle (Free) plan
        - You can leave the Tags field blank
     - Click “Select Region”
     - Click “Review”
     - Return to the ElephantSQL dashboard and click on the database instance name for this project
     - Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://

4.	On [Cloudinary](https://cloudinary.com/):
     - Login to your Cloudinary account:
     - Copy your CLOUDINARY_URL from your Cloudinary Dashboard.
     - Add Cloudinary URL to env.py:

           os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
           
5.	On [Heroku](https://id.heroku.com/login):
     - Login to your Heroku account
     - Create new Heroku App
     - Open the settings tab
     - Click Reveal Config Vars
         - Add a Config Var called DATABASE_URL: The value should be the ElephantSQL database url you copied from step 3.
         - Add a Config Var called CLOUDINARY_URL: The value should be the Cloudinary database url you copied from step 4.
         - Add a Config Var called PORT: The value should be: 8000
         - Add a Config Var called MY_SECRET_KEY: The value should be of your choice, but keep ot secret. (Should be the same as set on your env.py file)
6. 	On your settings.py:
     - Reference env.py by adding on the top:
       
           import os
           import dj_database_url
           if os.path.isfile("env.py"):
           import env

     - Remove the insecure secret key (if any) and replace with:
       
           SECRET_KEY = os.environ.get('SECRET_KEY')
       
     - Comment out the old dataBases section:

           # DATABASES = {
           #     'default': {
           #         'ENGINE': 'django.db.backends.sqlite3',
           #         'NAME': BASE_DIR / 'db.sqlite3',
           #     }
           # }
       
     - Add new DATABASES Section:
  
           DATABASES = {
               'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
           }

     - Add Cloudinary Libraries to installed apps:
  
               INSTALLED_APPS = [
               …,
               'cloudinary_storage',
               'cloudinary',
     - Tell Django to use Cloudinary to store media and static files:
  
            STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
            STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
            STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
            
            MEDIA_URL = '/media/'
            DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

     - Link file to the templates directory in Heroku:
  
            TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

     - Change the templates directory to TEMPLATES_DIR:
  
           TEMPLATES = [
                {
                   …,
                    'DIRS': [TEMPLATES_DIR],
                   …,
                        ],
                    },
                },
            ]
     - Add Heroku Hostname to ALLOWED_HOSTS:

           ALLOWED_HOSTS = ["**PROJ_NAME**.herokuapp.com", "**YOUR_HOSTNAME**"]

7. Create a Procfile on the top level directory, and add the code below inside:

        web: gunicorn **PROJ_NAME**.wsgi

8. Create the env.py file on the top level directory, and add the secret keys:

    import os
    os.environ['DATABASE_URL'] = '** Secret database from step 3**'
    os.environ['SECRET_KEY'] = '** Your secret key **'
    os.environ['CLOUDINARY_URL'] = '** Secret database from step 4**'
       
    
9. Make sure you have debug set to False on Settings.py:

        DEBUG = False

10. Commit your changes to github:

        git add .
        git commit -m "YOUR MESSAGE"
        git push

11. On Heroku, you can manually deploy it our set up an automatic deployment.
   
12. The live link can be found here [My Recipes Book](https://my-recipes-book-pp4-3364500b645d.herokuapp.com/)

## :heavy_check_mark: Credits

The useful support needed came from:

[Code Institute](https://codeinstitute.net/ie/)
[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
[GitHub - Markdown Guide](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

