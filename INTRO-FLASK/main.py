from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', title = " Home Page")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return redirect(url_for('contact'))  # Redirect back to contact page after form submission
    
    # Render the contact form on GET request
    title = "Contact Page"
    return render_template('contact.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
