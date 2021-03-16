# Wikipes
### The simple way to store your recipes, and share it with others.


<hr>

### Index
1. Project Planning.
2. Updates Timeline.
3. Planned Updates.
4. Bugs & Errors.
5. Additional Comments.
6. Testing.
7. Conclusion.


## 1. Project Planning.
Wireframe and user flowchart can be found in the documentation folder.


## 2. Updates Timeline.
> 0.3 **2021-03-16**
> > Made allergen switches occupy 3 spaces each and center align them on 2 rows<br>
> > Created edit functionality with conditional if statements to declare wether allergens were toggled in the original recipe.<br>
> > Created delete functionality to use .remove() on the ObjectId in the database.<br>

> 0.2 **2021-03-15**
> > Created edit page using the upload inserts
> > Created routing for edit_page
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
> > 

## 3. Planned Updates.
> ~~Create If statement on edit page to render all the allergens toggles was on or off before editing<br>~~
> Create function to display users recipes on profile page<br>
> Revamp how recipes display on frontpage<br>
> ~~Implement Search Function~~<br>
> Move flash messages to modal<br>
> ~~Implement User auth<br>~~<br>
> ~~Add more Allergen icons (on frontpage/view all recipes using ***if x on then***<br>~~
> ~~Implement Allergen functions in update/edit recipe to be toggles<br>~~
> ~~Implement Creating of Recipes<br>~~
> ~~Implement Updating Recipes<br>~~
> ~~Implement Deleting Recipes<br>~~
> ~~Implement Functional Registration~~<br>
> Update Project Planning<br>
> style buttons to all look the same<br>
> Style nav<br>
> Style text content<br>
> Style brand logo<br>
> Style Flash Messages<br>

## 4. Bugs & Errors.

1. 2021-03-14
> **Expected Result:**
> > Applying a Jinja for loop in front_page.html would render on screen in the preview.

> **Actual Result:**
> > The Jinja for loop renders the HTML element to store the database data from MongoDB but renders the elements empty, regardless of the database thats injected

> **Resolved Y/N:**
> > ***Y 2021-03-14***

2. 2021-03-15
> **Expected Result:**
> > using the correct column size would display the search elements and the collapsible element as the same width

> **Actual Result:**
> > the search and collapsible elements does not align

> **Resolved Y/N:**
> > ***N***

3. 2021-03-15
> **Expected Result:**
> > Using the implemented python function should render a fully functional and rendered login_page.html, that retrieves data from database to match<br>
> > user credentials. 
> 
> **Actual Result:**
> > Page does not load and [TO_MANY_REDIRECTS], and heroku returns a HTTP code of 302.

> **Resolved Y/N:**
> ***Y*** The 302 code indicates redirecting, but the log does not show an endpoint, leading to a probable error in the routing for the page.
> resolved by editing the /login function with correct indentation.

## 5. Additional Comments.
The commits are somewhat inconsistent, the later ones will use the description to specify the changes in the files. 
I am using GitHub Desktop and it was simply more effective for me to write in the description.
<hr>
I have not found a way to visualize functional previews of jinja code on VsCode, thus the large ammount of commits to the main branch.<br>
I pushed commits for testing to push changes to heroku and to display the changes made in the code. This did force me to push multiple commits with the same
description to declare what I was working on, more like workin on a separate branch, but instead doing testing on main.

## 6. Testing.

## 7. Conclusions.
Due to some extensive computer issues this project has ben put under intense time restraints, once again I would like to reach out and thank CI Student Counceling for their understanding and very helpful ways.