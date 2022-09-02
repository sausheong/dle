from flask import Flask, request, render_template, redirect
from threading import Thread
from dle import generate_images
import uuid

app = Flask(__name__)
# app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.get("/")
def main():
    return render_template("index.html")

@app.get("/view/<id>")
def view(id=None):
    return render_template("view.html", id=id)

@app.post("/dle")
def generate():
    prompt = request.form["prompt"]
    id = str(uuid.uuid4())
    thread = Thread(target=generate_images, args=([prompt], id))
    thread.daemon = True
    thread.start()
    return redirect(f"/view/{id}")
