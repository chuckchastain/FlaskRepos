from flask import Flask
from flask import render_template
from AppDir import app


@app.route('/')
@app.route('/index')
def index():
    user = "Chuck"
    return render_template(
      "index.html",
       title = "Home Page",
        message = "Hello Flask!",
        username = user  )