from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

# make fake DB
db = {} 

# 누간가가 / 입력으로 들어오면
@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    #print(request.args.get()) # 모든 argument를 보여줌
    #print(request.args.get("word")) #word 라는 argument 를 print
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")

    return render_template(
        "report.html", 
        searchingBy=word, 
        resultsNumber=len(jobs),
        jobs=jobs
        )

# @ is decorate 함수만을 봄
@app.route("/contact")
def potato(): 
    return "Contact me!!"

@app.route("/<username>")
def potato1(username): 
    return f"Hello {username} how are you doing"

#app.run(host = "0.0.0.0")repl.it 에 쓰일 것임
app.run()