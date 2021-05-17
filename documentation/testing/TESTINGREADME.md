# 7. Testing.

### Google DevTools Test.
Screenshot stored in /testing/images.

> Network test
> > Network test showed no significant drops in stability and/or prolonged responsetimes
> > Google Ligthouse showed green scores for all points besides SEO.  


## Validators.

## Site Functionality
### 1. Testing Link Functionality:
> All links result in a status 200/302. Links redirecting to a new site opens in a new tab and utilizes the rel="noreffer".<br>**All links works as intended**.<br>
### 2. Regestering a new User:
> Registering a new user completes as intended and returns a succesfull status=302 to redirect the user to its new profile. [*Screenshot from Heroku*](https://gyazo.com/7cb13215a02ae64a8d90ec0e148dbc9a)<br>
**Registering a new user works as intended**
### 3. Uploading a recipe:
> uploading a new recipe completes as intended and returns a succesfull status=302 to redirect the user to the frontpage. [*Screenshot from Heroku*](https://gyazo.com/70709a68659ef076b5de7b8829555b21)<br>
**Uploading a recipe works as intended**
### 4. Editing a recipe:
> Editing an existing recipe completes as intended and returns a succesfull status=302 to redirect the user to the frontpage. [*Screenshot from Heroku*](https://gyazo.com/60b80f7fdc08e09de2da59f4eddf1649)<br>
**Editing an existing recipe works as intended**
### 5. Deleting a recipe:
> Deleting an existing recipe completes as intended and returns a succesfull status=302 to redirect the user to the frontpage. [*Screenshot from Heroku*](https://gyazo.com/a84d1ad5c56312cfe8768b709374bcb4)

## K6 Performance 
screenshot stored in /testing/images
> K6 Stress Testing,
> > Testing POST/GET functionality with a stresstest hosted on K6.
> > The test runs for 5 minutes and 30 seconds specifically targets POST/GET functionality. However, as this the POST functions on the web application is either registration, login, or recipe uploading the test recieves information that is not specifically applicable to the POST functionality as the test can not write recipes nor register users. The test works on testing GET methods and recieved no error regarding functionality.

> Testing POST methods manually:<br>
> > 1. Registering a new user logs:<br>
> > [*Screenshot from Heroku*](https://gyazo.com/7cb13215a02ae64a8d90ec0e148dbc9a)<br>
> > 2. Uploading a new recipe logs:<br>
> > [*Screenshot from Heroku*](https://gyazo.com/70709a68659ef076b5de7b8829555b21)<br>
> > 3. Editing a new recipe logs:<br>
> > [*Screenshot from Heroku*](https://gyazo.com/60b80f7fdc08e09de2da59f4eddf1649)<br>
> > Looking at these screenshots shows us that when manually practicing the functionality of the application works as intended and redirects the user to the relevant page after performing the POST method.

## Python Tester
Testing syntax on [PythonTester](https://extendsclass.com/python-tester.html) returns no syntax errors in app.py, screenshot stored in /testing/images

## CSS Validator
Testing CSS validity with [W3C CSS Validating](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fwikipe.herokuapp.com%2Ffrontpage&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) returns a single error located in the materialize library.

## HTML validator
Testing HTML validity with [W3C HTML Validating](https://validator.w3.org/nu/?doc=http%3A%2F%2Fwikipe.herokuapp.com%2Ffrontpage) returns one warning that the sections lacks headings. As the page is centered around the recipes and there is nothing else on the page there are no other sections needing headers.