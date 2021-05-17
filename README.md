# Wikipes
### The simple way to store your recipes, and share it with others.


<hr>

### Index
1. Project Planning.
2. Updates Timeline.
3. Planned Updates.
4. Bugs & Errors.
5. Additional Comments.
6. External Resources.
7. Testing. (see separate folder in /documentation)
8. Deployment
9. Conclusion.


## 1. Project Planning.
I wanted to create a recipe database long before I started the Code Institute program. As a chef, there are flaws in keeping things like this on paper or in notes on my phone. I want Wikipes to be a hub for users to store their own recipes, and potentially read others. Using user profiles to store specific users own recipes to easily be found on their individual pages. Users that do not log in will still be able to read the recipes but not upload, edit, or delete any recipes on the site. 
<br>
### Potential User Stories.

> *New Users*
> > A new user enters the site with an intention to either read older recipes or upload their own recipes. If the new user wants to upload one of their own recipes, the user have to navigate to the profile and create their own new profile, then the user will ge given access to the page that is used for uploading a new recipe. 

> *Existing Users*
> > An existing user navigates to the site with intentions to either, read old recipes, upload a new recipe and/or delete or update an existing recipe. 
The existing user has to be logged in to the site to be able to view their profile which will view the users uploaded recipes that's tied to the userID stored in a database. By this measure the logged in user has full CRUD rights to their own uploaded recipes, but not users with a different userID's. 

> *Admin Users*
> > Admin users using wikipes for a "admin purpose" will have CRUD rights to any recipe to prevent spam and/or content that is not relevant to storing recipes.

**User flowchart and project wireframe can be found in /documentation**

> *CRUD Functionality for users*
> > To create a new recipe the loged in user navigates to the "Upload Recipe" page, found in the top right corner. (if the user is not logged in the use will be prompted before being able to upload a new recipe) Here the user will fill in valuable information regarding the recipe. Category, A name, description, ingredients and allergens. If the user wants to edit one of his/hers existing recipes, navigating to your recipes will list your uploaded recipes and give the user an option to edit the recipe, this will also show on the frontpage for the specific recipes tied to the userID. <br> The steps to delete a recipe is very similar to editing a recipe, the delete option is located next to the edit button on either the "Your recipe" and frontpages.




## 2. Updates Timeline.
> 0.4 **2021-05-17**
> > Added overline styling to recipe names.<br>
> > added text on the frontpage to lead users towards functionality on the page.<br>
> > Added toast callback with information about the toast button to be re-clickable.<br>
> > Added allergens button with toast to display information to what which icon means.<br>
> > removed allergens tooltipped JQuery as it was no longer used.<br>
> > added footer text, links and color to match the rest of the page<br>
> > Included a footer<br>


> 0.3 **2021-03-16**
> > Styled webpage globally with button colors, card panels, and label texts.<br>
> > Editing recipes now looks as intended<br>
> > Editing recipes now works as intended<br>
> > Fixed nested IF statements messing with displayin allergn icons only if the previous was checked.
> > Made allergen switches occupy 3 spaces each and center align them on 2 rows<br>
> > Created edit functionality with conditional if statements to declare wether allergens were toggled in the original recipe.<br>
> > Created delete functionality to use .remove() on the ObjectId in the database.<br>

> 0.2 **2021-03-15**
> > Created edit page using the upload inserts<br>
> > Created routing for edit_page<br>
> > Created submit button for upload recipe<br>
> > tested allergens toggle and viewed output<br>
> > Created dictionary to retrieve info from the input fields on upload_page.html<br>
> > Created variables for allergens to utilize toggles (easier to display on the recipes using ***if toggle on*** statement to display icon)<br>
> > Created routing for upload_page and function to use .insertOne into the<br> database using the input values from the page.<br>
> > Created placeholder input field on upload_recipe for testing.<br>
> > Created routing for login with functions to read hashed password and put user in session<br>
> > Starting development of login page/route<br>
> > Finished registration page<br>
> > Registration function works and uses Werkzeug password hashing<br>
> > Built the function for new registrated users to be stored in the database<br>
> > finished registration page layout<br>
> > Updated index to be able to search categories<br>
> > Added routing for register page<br>
> > Added register page<br>
> > Finished working on frontpage<br>
> > reset the search function resets the current index, returning user to view all recipes<br>
> > search function works, filtering the index<br>
> > Created recipe index in MongoDB to use in the search functionality<br>
> > Added search route<br>
> > Added search elements<br>
> > Added comments for base.html<br>
> > Added comments for JQuerys in scripts.js<br>
> > Added ellergens icons with tooltip<br>
> > Formatted Jinja output for recipes.<br>
> > Configured .dockerfile for GitPod functionality


> 0.1 **2021-03-14**
> > Created app on heroku and configured Config Vars<br>
> > Added User Flowchart <br>
> > Added wireframe <br>
> > Added Static and Templates folder <br>
> > Set up app.py with dependencies<br>
> > set up requirements.txt<br>
> > set up env.py<br>
> > added template extentions from base.html<br>
> > extended base.html to front_page.html<br>
> > frontpage now renders current recipes from MongoDB<br>


## 3. Planned Updates.
> ~~Create cancel button on edit recipe page to redirect user to frontpage<br>~~
> ~~Create If statement on edit page to render all the allergens toggles was on or off before editing<br>~~
> ~~Create function to display users recipes on profile page<br>~~
> ~~Revamp how recipes display on frontpage and profilepage(Add steps)<br>~~
> ~~Implement Search Function~~<br>
> ~~Move flash messages to modal<br>~~(focusing on styling instead, if there is time I will try this)
> ~~Implement User auth<br>~~<br>
> ~~Add more Allergen icons (on frontpage/view all recipes using ***if x on then***<br>~~
> ~~Implement Allergen functions in update/edit recipe to be toggles<br>~~
> ~~Implement Creating of Recipes<br>~~
> ~~Implement Updating Recipes<br>~~
> ~~Implement Deleting Recipes<br>~~
> ~~Implement Functional Registration~~<br>
> ~~Update Project Planning<br>~~
> ~~style buttons to all look the same<br>~~
> ~~Style nav<br>~~
> ~~Style text content<br>~~
> ~~Style brand logo<br>~~
> ~~Style Flash Messages<br>~~

## 4. Bugs & Errors.

1. 2021-03-14
> **Expected Result:**
> > Applying a Jinja for loop in front_page.html would render on-screen in the preview.

> **Actual Result:**
> > The Jinja for loop renders the HTML element to store the database data from MongoDB but renders the elements empty, regardless of the database that's injected

> **Resolved Y/N:**
> > ***Y 2021-03-14***

2. 2021-03-15
> **Expected Result:**
> > using the correct column size would display the search elements and the collapsible element as the same width

> **Actual Result:**
> > the search and collapsible elements does not align

> **Resolved Y/N:**
> > ***Y 2021-03-15***

3. 2021-03-15
> **Expected Result:**
> > Using the implemented python function should render a fully functional and rendered login_page.html, that retrieves data from database to match<br>
> > user credentials. 
> 
> **Actual Result:**
> > Page does not load and [TO_MANY_REDIRECTS], and heroku returns a HTTP code of 302.

> **Resolved Y/N:**
> > ***Y 2021-03-15*** - The 302 code indicates redirecting, but the log does not show an endpoint, leading to a probable error in the routing for the page.
> resolved by editing the /login function with correct indentation.

4. 2021-03-16
> **Expected Result:**
> > creating CSS code targeting elements in the HTML should change the appearance of the output

> **Actual Result:**
> > The CSS code does not change the appearance of the HTML, it does work with in-line customization, however.

> **Resolved Y/N:**
> > ***Y 2021-03-16*** - Due to not having an online preview that could read jinja I had to push the CSS changes to main to display them on the live page. (not best practice)

## 5. Additional Comments.
The commits are somewhat inconsistent, the later ones will use the description to specify the changes in the files. 
I am using GitHub Desktop and it was simply more effective for me to write in the description.
<hr>
I have not found a way to visualize functional previews of jinja code on VsCode, thus a large number of commits to the main branch.<br>
I pushed commits for testing to push changes to Heroku and to display the changes made in the code. This did force me to push multiple commits with the same
description to declare what I was working on, more like working on a separate branch, but instead doing testing on main. I apologize for the large amounts of commits.

## 6. External Resources.
[MaterializeCSS Documentation](https://materializecss.com/)<br>
[StackOverflow]([www.stackoverflow.com](https://stackoverflow.com/))<br>
CI Data Centric Modules (MongoDB / Mini Project)

## 8. Deployment
> Deployment will be processed trough Heroku and uses automatic deploys trough GitHub connections. Sensitive information is stored in Config Vars hosted on the Heroku backend.
> > This site is catering to an easy access for users to find and store recipes and should be simple to access. <br>
> > 1. A procfile is created to declare that the application we want to run is a webb application that uses Python and runs trough the app.py python file.<br>
> > 2. A requirements.txt file is created using the *pip3 freeze* command to make sure that Heroku has the required assets to run the application. <br>
> > 3. Add the relevant config variables to Herokus Config vars, this makes sure that critical information stays hidden to users that uses the site. Such as ports and IP's used, aswell as the connection to the Database.<br>
> > 4. Connect the GitHub repository to the Heroku webb app and enable automatic deployment to keep the live webb app automatically up to date.<br>
> > 5. test webb application functionality (read more in testing)

## 9. Conclusions.
Due to some extensive computer issues, this project has been put under intense time restraints, once again I would like to reach out and thank CI Student Counseling for their understanding and very helpful ways.
<hr>
Even with the time restrictions, I enjoyed this project very much. This is probably because I had extended amounts of time instead of having to go away and focus on people that are sick (that do need my help), this helped me massively with focus and dedication.
I very much enjoy working with Back-End integration and I have learned massively from this.
<hr>

Some jinja rendering is basic, and the output for recipes from the database could have been "prettier", but to me, it does its job and works.
<hr>
While this project is heavily influenced by the mini-project, I only researched the source code when there were issues I did not know how to fix and I implemented it myself. 
<hr>
While I believe this could have been made much flashier, (as always) I wanted to focus my time where I felt it needed, with the time limit I had I chose to not do extensive styling or use crazy images, the goal I had was a simple database collection that's integrated on the page to be displayed and accessed by users. 
<hr>
MS2 was quite horrible for me, as there were too many things pulling me away from my studies, and this time around I had some really bad PC issues with bluescreens and having to run the computer in safe mode without a network to try to fix it. Eventually, I fixed the issue and here we are. This project made me prove to myself that this is something I enjoy and am capable of completing, and I am so happy I pulled through and completed it. 