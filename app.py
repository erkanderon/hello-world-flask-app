from flask import Flask, render_template
import datetime
import socket
host = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
	time = datetime.datetime.now()
	machine = host
	return render_template("index.html", data={"time": time, "machine": host })



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)