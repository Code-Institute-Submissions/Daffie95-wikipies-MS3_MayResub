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
> 0.2 **2021-03-15**
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
> > Added search element<br>
> > Added comments for base.html<br>
> > Added comments for JQuerys in scripts.js<br>
> > Added ellergens icons with tooltip<br>
> > Formatted Jinja output for recipes.<br>


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
> ~~Implement Search Function~~<br>
> Implement User auth<br>
> Implement Creating of Recipes<br>
> Implement Updating Recipes<br>
> Implement Deleting Recipes<br>
> ~~Implement Functional Registration~~<br>
> Update Project Planning<br>
> style buttons to all look the same
> style app with CSS

## 4. Bugs & Errors.
2. 2021-03-15
> **Expected Result:**
> > using the correct column size would display the search elements and the collapsible element as the same width

> **Actual Result:**
> > the search and collapsible elements does not align

> **Resolved Y/N:**
> > ***N***


1. 2021-03-14
> **Expected Result:**
> > Applying a Jinja for loop in front_page.html would render on screen in the preview.

> **Actual Result:**
> > The Jinja for loop renders the HTML element to store the database data from MongoDB but renders the elements empty, regardless of the database thats injected

> **Resolved Y/N:**
> > ***Y 2021-03-14***

## 5. Additional Comments.

## 6. Testing.

## 7. Conclusions.
Due to some extensive computer issues this project has ben put under intense time restraints, once again I would like to reach out and thank CI Student Counceling for their understanding and very helpful ways.