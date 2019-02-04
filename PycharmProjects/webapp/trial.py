from flask import Flask, redirect, render_template, request, url_for
import time
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def prg9serverFunction():
    if request.method == "GET":
        return render_template("prg.html")
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        gender=request.form['gender']
        download_dir = "hello.csv" #where you want the file to be downloaded to

        csv = open(download_dir, "w")
#"w" indicates that you're writing strings to the file

        columnTitleRow = "name, age, gender\n"
        csv.write(columnTitleRow)
        row = name + "," + age + "," + gender + "\n"
        csv.write(row)
        return render_template("success.html")



if __name__ == '__main__':
    app.run()
