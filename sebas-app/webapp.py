from flask import Flask, request, render_template, url_for, redirect
import socket

app = Flask(__name__)

# A list to store the ToDo items
todo_items = []


@app.route("/", methods=["GET", "POST"])
def todo_list():
    if request.method == "POST":
        task = request.form["task"]
        if task:
            todo_items.append(task)
    return render_template("todo.html", hostname=socket.gethostname(), todo_items=todo_items)

@app.route("/remove/<task>", methods=["POST"])
def remove_todo(task):
    if task in todo_items:
        todo_items.remove(task)
    return redirect("/")


if __name__ == "__main__":
    app.run()
