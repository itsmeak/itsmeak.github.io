from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
	password = request.form['password']
	listuser = ['pravesh']
	listpassword = ['Pain@3108']
	if username in listuser :
		if password in listpassword:
			return redirect('/greetings.html')
		else:
			return redirect('/wrong.html')


if __name__ == "__main__":
    app.run()