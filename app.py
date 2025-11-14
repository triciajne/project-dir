
#Initialize the Flask application
app = Flask(__name__)

# --- Login Route ---
# Maps the root URL '/' to the login_page function.
@app.route('/')
def login_page():
    # Renders the 'index.html' file from the 'templates' folder.
    # We are assuming 'index.html' contains the Login form.
    return render_template('index.html')

# --- Register Route ---
# Maps the URL '/register' to the register_page function.
@app.route('/register')
def register_page():
    # Renders the 'register.html' file (you need to create this in /templates).
    return render_template('register.html')


#Run the application (This part is often protected by an 'if __name__ == "__main__":' block)
if __name__ == '__main__':
    # Set debug=True for easier development.
    app.run(debug=True)


