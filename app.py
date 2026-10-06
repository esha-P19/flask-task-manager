from flask import Flask, render_template, request,redirect
from db import cursor, mydb

app = Flask(__name__)


# adding task route
@app.route("/", methods=["GET" , "POST"] )
def task():
   if request.method == "POST":
      task = request.form["task"]

      cursor.execute(
         "insert into tasks(task,status) values(%s , %s)",
         (task,"Pending")
      )

      mydb.commit()
   cursor.execute("select * from tasks")
   all_task = cursor.fetchall()
   return render_template("task.html", tasks=all_task)

@app.route("/delete/<int:id>")
def delete(id):

    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    mydb.commit()

    return redirect("/")

@app.route("/complete/<int:id>")
def complete(id):

    cursor.execute(
        "UPDATE tasks SET status=%s WHERE id=%s",
        ("Completed", id)
    )

    mydb.commit()

    return redirect("/task")

app.run(debug=True)