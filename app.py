from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///projectsdatabases.db"
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']= False
app.secret_key = "secreate_key"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500),nullable=False )
    email = db.Column(db.String(500),nullable=False )
    pa = db.Column(db.String(500),nullable=False )  #message
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.name} - {self.pa}"






class projectdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(500),nullable=False )
    project_language = db.Column(db.String(500),nullable=False )
    project_link = db.Column(db.String(500),nullable=False )  
    project_reach_link = db.Column(db.String(500),nullable=False )  
    project_description = db.Column(db.String(500),nullable=False )  
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.project_name} - {self.project_link}"


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/contact' , methods=['GET','POST'])
def contact():
    if request.method == "POST":
        
        name = request.form['name']
        email = request.form['email']
        pa = request.form['pa']
        info = User(name=name, email=email, pa=pa)
        db.session.add(info)
        db.session.commit()
        if name=="" or email =="" or pa=="":
            flash("THIS FIELDS CANNOT BE EMPTY")
            info = User(name="name", email="email", pa="pa")
            allinfo=User.query.all()
            return render_template('contact.html' , allinfo =allinfo)
        if name == "tarun" and pa =="tarun" :
            info = User(name="name", email="email", pa="pa")
            allinfo=User.query.all()
            print("succcess")
            return render_template('admin.html', allinfo=allinfo)
        else:
            flash("MESSAGE SENT SUCESSFULLY! ")

    allinfo = User.query.all()
    return render_template('contact.html',  allinfo=allinfo)


@app.route('/delete/<int:id>')
def delete(id):
    infos = User.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = User(name="name", email="email", pa="pa")
    allinfo=User.query.all()
    # print(allinfo)
    return render_template("admin.html" , allinfo = allinfo)


@app.route('/deletee/<int:id>')
def deletee(id):
    infos = projectdb.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = projectdb(project_name="project_name", project_language="project_language", project_link="project_link", project_description="project_description", project_reach_link="project_reach_link")
    allinfo=projectdb.query.all()
    return render_template("upload.html" , allinfo = allinfo)




@app.route("/admin")
def admin():
    info = User(name="name", email="email", pa="pa")
    allinfo=User.query.all()
    return render_template('admin.html', allinfo = allinfo)


@app.route("/upload")
def upload():
    info = projectdb(project_name="project_name", project_language="project_language",project_link ="project_link" , project_description= "project_description", project_reach_link="project_reach_link")
    allinfo = projectdb.query.all()
    return render_template('upload.html',allinfo= allinfo)


@app.route("/project",  methods=['GET','POST'])
def project():
    if request.method == "POST":
        print("succcess")
        project_name = request.form['project_name']
        project_language = request.form['project_language']
        project_link = request.form['project_link']
        project_description = request.form['project_desc']
        project_reach_link = request.form['project_reach_link']
        info = projectdb(project_name=project_name, project_language=project_language, project_link=project_link, project_description= project_description, project_reach_link=project_reach_link)
        db.session.add(info)
        db.session.commit()
        info = projectdb(project_name="project_name", project_language="project_language",project_link ="project_link" , project_description= "project_description",project_reach_link="project_reach_link")
        allinfo=projectdb.query.all()
    info = projectdb(project_name="project_name", project_language="project_language",project_link ="project_link" , project_description= "project_description", project_reach_link="project_reach_link")
    allinfo = projectdb.query.all()
    return render_template('project.html', allinfo = allinfo)


@app.route("/about")
def about():
    return render_template('about.html')

    
@app.route("/projects")
def projects():
    info = projectdb(project_name="project_name", project_language="project_language",project_link ="project_link" , project_description= "project_description",project_reach_link="project_reach_link")
    allinfo = projectdb.query.all()
    return render_template('project.html')





@app.route('/logadmin' , methods=['GET','POST'])
def logadmin():
    if request.method == "POST":
        name = request.form['name']
        pa = request.form['pa']
        if name == "tarun" and pa =="tarun":
            allinfo=User.query.all()
            return render_template('admin.html', allinfo=allinfo)
    return render_template('logadmin.html')







if __name__=="__main__":

    app.run(debug=True, port=8000)