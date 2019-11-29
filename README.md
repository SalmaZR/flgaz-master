# flgaz-master

Here's the steps taken to improve the project :

- Add authentication to the application.
- Prevent usage of the pages without authorization.
- Force authentication.
- Allow caching and cache control.
- Limit the number of characters in a tweet.
- Allow search of messages by user.
- Secure the credentials for the database.
- Remove the duplicated messages.

Here are the needed steps to make the application better :

- Prevent SQL Injections.
- Access-Control Allow Origin.

This list will be updated depending on our advancement on the project.

*Adding authentication.*

The process to add authentication took a lot of time to set up, however here are explainations of how we set it up.
The database was the first step, as such, we created one in Pythonanywhere and started it up.

`CREATE TABLE example ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );
INSERT INTO example ( id, name ) VALUES ( null, 'Sample data' );`

With these commands, we created a table, named SalmaZR$flask-project and inside, a user called "Salma", so we could later test if the Database is connected to the instance. With the Database ready, we made some modifications on the main python script, as well as create some new html file for us to use :

- formulaire.html (used to fill in your name and message)
- index.html (our login page, leading to the login and registering)
- register.html (the registering page, allowing users to create their profile)
- timeline.html (the user timeline)

Along with those files, we also modified the .app file to make it better suit our needs :

- Redirection from the main page to the login page :
*`@app.route('/')
def home():
    #print ('Bienvenue !')
    return redirect(url_for('login'))`*

- Redirection if not authentified, otherwise allow the user to either GET or POST :
`@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
    if not session.get('loggedin'):
	    return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            print(request.form)
            dump_to_csv(request.form)
            return redirect(url_for('timeline'))
		#return "OK"
        if request.method == 'GET':
            return render_template('formulaire.html')`
            
- Function defining Login and redirecting to /gaz if right :
`def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']`
[...]
`        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            #return 'Logged in successfully!'
            return redirect(url_for('save_gazouille'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)`
    
- Added a logout function at /logout.
- Added a function to register users inside of the Base.

Cache was added and allows public caching.
In order to start the website, use `app.py`in Pythonanywhere and reload the website.

# Documentation used :

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
- https://codeshack.io/login-system-python-flask-mysql/
- https://www.pythonanywhere.com/forums/topic/11589/
- https://pythonspot.com/login-authentication-with-flask/
- https://blog.pythonanywhere.com/121/
- https://pythonhosted.org/Flask-Cache/
- https://www.w3schools.com/python/python_howto_remove_duplicates.asp
- https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
