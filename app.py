from flask import Flask,render_template, request,session, redirect, url_for, flash

import pymysql.cursors
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "abdhghsbghddvbnbds"

con = pymysql.connect(host="localhost",port=3307,user="root",passwd="",db="resumeshortlisting")
cur = con.cursor()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signin", methods=['GET','POST'])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        check_email = "SELECT * FROM recruiter WHERE company_email = '"+email+"'"
        cur.execute(check_email)
        get_one_email = cur.fetchone()
        if (not get_one_email):
            flash("You entered wrong email address")
            return redirect(url_for('login'))
        elif(get_one_email[3]!=password):
            flash("Wrong Password")
            return redirect(url_for('login'))
        else:
            session['loggedin'] = True
            return redirect(url_for('dashboard'))
    return render_template('signin.html')

global newid
@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method=="POST":
        email = request.form["email"]
        check_email = "SELECT company_email FROM recruiter WHERE company_email = '"+email+"'"
        cur.execute(check_email)
        first_email = cur.fetchone()
        if(not first_email):
            company_name = request.form["cname"]
            password = request.form["password"]
            cpassword = request.form["cpassword"]
            sql = "INSERT INTO recruiter(company_email, company_name, password ) VALUES (%s,%s,%s)"
            val = (email, company_name, password)
            if(cpassword == password):
                cur.execute(sql,val)
                con.commit()
            else:
                flash("Password and confirm password should be same!")
                return redirect(url_for('signup'))
            sql2 = "SELECT id FROM recruiter WHERE company_email = '"+email+"'"
            cur.execute(sql2)
            myid = cur.fetchone()
            # print(myid[0])
           
            session['id'] = myid[0]
            
            newid = session['id']
            session['loggedin'] = True
            return redirect(url_for('dashboard'))
        else:
            flash("The email is already in use! Try using another")
            return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route("/dashboard")
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route("/jobPost" , methods=["GET" , "POST"])
def jobPost():
     if 'loggedin' in session:
        if request.method == "POST":
           # check_id = "select id from recruiter where company_name = '"+company_name+"'"
            c_name = request.form["cname"]
            columns = request.form.getlist('skill[]')
            print(columns)
            skills = request.form["skill[]"]
            #skill_query=[]
            #for x in columns:
             #  skill = request.form["skill[]"]
              # skill_query.append(getattr(skill,x))
            experience = request.form["experience"]
            education=request.form["education"]
            city=request.form["city"]
            sql2="UPDATE jobposting SET generated_link=CONCAT( 'www.',c_name,'/' , id,'/',company_id)"
            sql3="SELECT recruiter.id FROM recruiter where company_name='"+c_name+"';"
            val3 = cur.execute(sql3)
            print(val3)
            sql = "INSERT INTO jobposting(company_id,c_name,skills ,experience ,education ,city) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (val3, c_name,skills,experience ,education ,city)
            cur.execute(sql,val)
            cur.execute(sql2)
            
            con.commit()
            return redirect(url_for('dashboard'))
        return render_template('jobPost.html')

@app.route("/student_resume", methods=['GET','POST'])
def student_resume():
    if request.method=="POST":
        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]
        contact_number=request.form["number"]
        address=request.form["address"]
        title = request.form["title"]
        skills= request.form["technical-skill"]
        position=request.form["position"]
        company_name=request.form["company-name"]
        worked_from=request.form["period-from"]
        worked_to = request.form["period-to"]
        description = request.form["job-description"]
        project_title=request.form["project1-title"]
        project_description=request.form["project1"]
        tech_used=request.form["project1-tech"]
        project2_title=request.form["project2-title"]
        project2=request.form["project2"]
        project2_tech=request.form["project2-tech"]
        education=request.form["education"]
        languages_known=request.form["language"]
        sql2="SELECT J.id FROM jobposting J INNER JOIN resume_details R ON r.job_id = j.id"
        val2 = cur.execute(sql2)
        sql = "INSERT INTO resume_details(job_id, template_id, name, dob, email ,contact_number ,address ,title ,skills,company_name ,position,worked_from ,worked_to ,description ,project_title ,project_description ,tech_used ,education,languages_known ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (val2,1,name, dob, email ,contact_number ,address ,title ,skills,company_name ,position,worked_from ,worked_to ,description ,project_title ,project_description ,tech_used ,education ,languages_known)
        cur.execute(sql,val)
        con.commit()
        return redirect(url_for('home'))
    return render_template('student_resume.html')

@app.route("/resume1")
def template():
    return render_template("template1.html")

@app.route("/resume2")
def template2():
    return render_template("template2.html")

@app.route("/resume3")
def template3():
    return render_template("template3.html")

if __name__=='__main__':
    app.run(debug=True)
