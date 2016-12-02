from flask import Flask, render_template
app = Flask(__name__)
''' Function to return the root html page'''
@app.route('/')
def IndexBody():
    return render_template('index.html')
''' Function to render html jinja template. (as below) '''
@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/gwork')
def gwork():
	return render_template('gwork.html')

@app.route('/photo')
def photo():
	return render_template('photo.html')

@app.route('/video')
def video():
	return render_template('video.html')

@app.route('/poetry')
def poetry():
	return render_template('poetry.html')

@app.route('/links')
def links():
	return render_template('links.html')



if __name__ == "__main__":
    app.run()

