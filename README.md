# My Recipes Book

Welcome to My Recipes Book! This is a web application designed to help you manage and organize your collection of recipes. Whether you're a seasoned chef or just starting out in the kitchen, this app is here to make your cooking experience more enjoyable and efficient.

## Existing Features

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

## Testing

- __RESPONSIVENESS:__
    - The deployed application was tested on multiple devices to check for responsiveness issues. The bootstrap classes were used to be as responsive as possible.

![Responsive](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/responsive.jpg)

- __BROWSER COMPABILITY TESTING:__
    - The deployed project was tested on multiple browsers to check for compatibility issues and works as expected.

__Photo of Microsoft Edge:__
      
![Edge](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/Edge.jpg)

__Photo of Firefox:__

![Firefox](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/mozila.jpg)
  
__Photo of Mobile:__

![Mobile](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/Mobile.jpeg)


- __CODE VALIDATION:__

__HTML__

[HTML Validator](https://validator.w3.org/nu/) to validate all HTML files. The result for each page is listed below:

__Home page__

On home page I found some simple errors:
 
![Error1](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/index1.jpg)

![Error2](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/index2.jpg)

All resolved:

![Home page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_index_page.jpg)

__View recipe page__

On view recipe I found some errors:

- Missing "alt" attribute on image files and and extra "< /i >" that were both resolved.

![View_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_view_recipe.jpg)

__Creating recipe page__

![Create_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_create_recipe.jpg)

__Editing recipe page__

![Edit_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_edit_recipe.jpg)

__Deleting recipe page__

![Delete_recipe](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_delete_recipe.jpg)

__Loging page__

![Login_page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_login_account.jpg)

__Signup page__

![Signup_page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_signup_account.jpg)

__Logout page:__

![Logout_page](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/HTML_logout_account.jpg)

__CSS__

[The CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS file.
 
I found one error with a pseudo class.

![CSS_error](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/css_error.jpg)

Error was resolved by removing that style as it was not necessary.

![CSS_test](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/CSS.jpg)

__JAVASCRIPT__

[The JShint Validator](https://jshint.com/) was used to validate the JavaScript file.

![Javascript_test](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/JAVASCRIPT.jpg)

__PYTHON:__

[The Code Institute Python Linterwas](https://pep8ci.herokuapp.com/) was used to validate all Python files.

__My recipe book - Settings__

![settings](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_settings.jpg)

__My Recipe book - URLs__

![Main URLs](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_settings.jpg)

__My recipes - Form__

![My recipes Form](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_form.jpg)

__My recipes - URLs__

![My recipes URLs](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_urls_my_recipe_book.jpg)

__My recipes - Views__

![My recipes Views](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_views.jpg)

__My recipes - Models__

![My recipes Models](https://github.com/Adriele-lima/My-Recipes-Book/blob/main/static/images/PYTHON_model.jpg)


LIGHTHOUSE TESTING OUTCOMES:

The deployed project was tested using the Lighthouse Audit tool to check for any major issues.
Photo of Lighthouse:


- I tested that this page works in differents browsers: Firefox and Microsoft Edge.

- I confirm that this project is responsive, looks good and functions on all standart screen sizes using the devtools device toolbar.

- I confirm that the login page and game page are all readable and easy to understand.

- I have confirmed that the form works. 

- Accessibility

    - I confirmed that the colors and fonts chosen are easy to read and acessible by running it through lighthouse in devtools.

## Deployment

- The site was deployed to GitHub pages and Heroku.
- Postgres is used for the Database.
- Cloudinary is used for the images.
   
The live link can be found here [My Recipes Book](https://my-recipes-book-pp4-3364500b645d.herokuapp.com/)
