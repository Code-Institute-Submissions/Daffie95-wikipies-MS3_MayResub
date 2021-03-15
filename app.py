import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# assigning PyMongo using app(flask) to the variable mongo
mongo = PyMongo(app)

# route function to ensure that any empty routes renders the frontpage
@app.route("/")
# route function to render the frontpage and all current recepies
@app.route("/frontpage")
def frontpage():
    recipes = list(mongo.db.recipes.find())
    return render_template('front_page.html', recipes=recipes)

# route function to render the search function
@app.route("/search", methods=["GET", "POST"])
def search():
    # using indexing on the database to create a search function
    search = request.form.get("search")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search}}))
    return render_template("front_page.html", recipes=recipes)

# route function to render the register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # looking in database for same username
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username already exists")
            return redirect(url_for("register"))
        # retrieve information from registration form
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password").lower())
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template('register_page.html')
# future return statement for profile page
# return redirect(url_for("profile", username=session["user"]))

# function to check wether user credentials are in the database and put user in session

# route function to render the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check stored usernames for match with user input
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # check hashed password to match it with user input
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hi {}, Welcome!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # flash to show user credentials was incorrect
                flash("Password and/or Username is Incorrect")
                return redirect(url_for("login"))

        else:
            # flash to show user credentials was incorrect
            flash("Password and/or Username is Incorrect")
            return redirect(url_for("login"))

    return render_template('login_page.html')

# route function to log out current session user with .pop()
@app.route("/logout")
def logout():
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))

# route function to render current session user's profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    recipes = list(mongo.db.recipes.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile_page.html", username=username, recipes=recipes)

# route function for uploading new recipes
@app.route("/upload_recipe", methods=["GET", "POST"])
def upload_recipe():
    if request.method == "POST":
        # function to make the switch toggle on/off in the dictionary "recipe"
        gluten = "on" if request.form.get("gluten") else "off"
        lactose = "on" if request.form.get("lactose") else "off"
        nuts = "on" if request.form.get("nuts") else "off"
        peanuts = "on" if request.form.get("peanuts") else "off"
        shellfish = "on" if request.form.get("shellfish") else "off"
        fish = "on" if request.form.get("fish") else "off"
        # the dictionary pulls content from the input fields on upload_page.html
        # and inserts it into the database
        recipe = {
            "recipe_name": request.form.get("recipe_name").lower(),
            "category": request.form.get("category").lower(),
            "gluten": gluten,
            "lactose": lactose,
            "nuts": nuts,
            "peanuts": peanuts,
            "shellfish": shellfish,
            "fish": fish,
            "ingredients": request.form.get("ingredients").lower(),
            "steps": request.form.get("steps").lower(),
            "recipe_desc": request.form.get("recipe_desc").lower(),
            "recipe_steps": request.form.get("recipe_steps").lower(),
            "created_by": session["user"].lower()
        }
        # inserts the dictionary "recipe" in the database
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe has been added!")
        return redirect(url_for("frontpage"))
    
    return render_template('upload_page.html')

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
