from flask import Flask,render_template, request,session, redirect, url_for, flash

import pymysql.cursors
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "abdhghsbghddvbnbds"

con = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="resumeshortlisting")
cur = con.cursor()

my_links = ()
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signin", methods=['GET','POST'])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        check_email = "SELECT * FROM recruiter WHERE company_email = '"+email+"'"
        con.ping(reconnect = True)
        cur.execute(check_email)
        get_one_email = cur.fetchone()

        sql4 = "SELECT count(*) from jobposting where c_name = '"+get_one_email[2]+"'"
        cur.execute(sql4)
        mycnt = cur.fetchall()
        global my_postings
        my_postings = mycnt[0][0]

        sql5 = "SELECT generated_link from jobposting WHERE c_name ='"+get_one_email[2]+"'"
        cur.execute(sql5)
        global my_links
        my_links = cur.fetchall()
       
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
            sql2 = "SELECT * FROM recruiter WHERE company_email = '"+email+"'"
            cur.execute(sql2)
            myid = cur.fetchone()
            print(myid[2])
           
            session['id'] = myid[0]
          
            
            newid = session['id']
            session['loggedin'] = True
            return redirect(url_for('dashboard'))
        else:
            flash("The email is already in use! Try using another")
            return redirect(url_for('signup'))
    return render_template('signup.html')

my_postings = 0

@app.route("/jobPost" , methods=["GET" , "POST"])
def jobPost():

    if request.method == "POST":
    
        c_name = request.form["cname"]
       
        
        n=int(request.form.get('hidden'))
        # print(n)/
        skills=""
        for i in range(0,n+1):
            skill = request.form["skill["+str(i)+"]"]              
            skills=skills+skill+","
    
        experience = request.form["experience"]
        education=request.form["education"]
        city=request.form["city"]
        # sql1= "SELECT r.id FROM recruiter r inner join jobposting j on j.c_name = r.company_name WHERE j.c_name = '"+c_name+"'"
        # cur.execute(sql1)
        # sql = "INSERT INTO jobposting(company_id,c_name,skills,experience ,education ,city) VALUES (%s,%s,%s,%s,%s,%s)"
        # val = ( cur.execute(sql1), c_name,skills,experience ,education ,city)
        # cur.execute(sql,val)
        # con.commit()
        sql = "SELECT * FROM recruiter WHERE company_name = '"+c_name+"'"
        cur.execute(sql)
        one_company_name = cur.fetchone()
        company_id = one_company_name[0]

        sql2 = "INSERT INTO jobposting (company_id, c_name, skills, experience, education, city) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (company_id, c_name, skills,experience,  education, city)
        cur.execute(sql2, val)
        con.commit()
        sql2="UPDATE jobposting SET generated_link=CONCAT(id)"
        cur.execute(sql2)
        con.commit()
        sql4 = "SELECT count(*) from jobposting where c_name = '"+c_name+"'"
        cur.execute(sql4)
        mycnt = cur.fetchall()
        global my_postings
        my_postings = mycnt[0][0]

        # sql5 = "SELECT * FROM jobposting WHERE c_name = '"+c_name+"'"
        # cur.execute(sql5)
        # all_details = cur.fetchone()
        # global mycompany
        # mycompany = all_details[2]

        sql5 = "SELECT generated_link from jobposting WHERE c_name ='"+c_name+"'"
        cur.execute(sql5)
        global my_links
        my_links = cur.fetchall()
        
        
        return redirect(url_for('dashboard'))
    return render_template('jobPost.html')

@app.route("/dashboard")
def dashboard():
    if 'loggedin' in session:
       
        return render_template('dashboard.html', job_posting_number = my_postings, my_links=my_links)
    else:
        return redirect(url_for('login'))


myid=6
# mycompany = "company"
@app.route("/<id>")
def job_id(id):
    global myid
    # global mycompany
    # mycompany = company
    myid = id
    print(myid)

    # print(mycompany)
    session['my_id']  = myid
    return redirect(url_for('student_resume'))

myresume_link = ""
@app.route("/student_resume", methods=['GET','POST'])
def student_resume():
    if request.method=="POST":
        m=int(request.form.get('hidden1'))
        languages_known=""
        for i in range(0,m+1):
            lang = request.form["language["+str(i)+"]"]
            languages_known=languages_known+lang+","
            
        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]
        contact_number=request.form["number"]
        address=request.form["address"]
        title = request.form["title"]
        #skills= request.form["technical-skill"]
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
        #languages_known=request.form["language"]
        template_id = request.form['template_id']
        n=int(request.form.get('hidden'))
        skills=""
        for i in range(0,n+1):
            skill = request.form["technical-skill["+str(i)+"]"]
            skills=skills+skill+","
        
        # sql2="SELECT J.id FROM jobposting J INNER JOIN resume_details R ON r.job_id = J.id"
        # val2 = cur.execute(sql2)
        # print(val2)

        mine_id = session.get('my_id')
        sql = "INSERT INTO resume_details(job_id, template_id, name, dob, email ,contact_number ,address ,title ,skills,company_name ,position,worked_from ,worked_to ,description ,project_title ,project_description ,tech_used ,education,languages_known,project2_title,project2_description) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (mine_id,template_id,name, dob, email ,contact_number ,address ,title ,skills,company_name ,position,worked_from ,worked_to ,description ,project_title ,project_description ,tech_used ,education ,languages_known, project2_title , project2)
        cur.execute(sql,val)
        con.commit()       

        sql2 = "SELECT id FROM resume_details WHERE email = '"+email+"'"
        cur.execute(sql2)
        link_id = cur.fetchone()

        resume_link = f"{link_id[0]}"
        print(resume_link)

        sql3="UPDATE resume_details SET resume_link= '"+resume_link+"'"
        cur.execute(sql3)
        con.commit()

        global myresume_link
        myresume_link = resume_link

        return redirect(url_for('student_generated_resume'))
    
    return render_template('student_resume.html')

@app.route('/student_generated_resume')
def student_generated_resume():
    return render_template("resume_link.html", myresume_link = myresume_link)


all_student_data = ""
lang_cnt = 0
skill_cnt = 0
@app.route("/resume/<id>")
def show_student_resume(id):
    sql ="SELECT * FROM resume_details WHERE id = '"+id+"'"
    cur.execute(sql)
    global all_student_data
    all_student_data = cur.fetchone()
    print(all_student_data)
    template_id = all_student_data[2]
    
    print(len(all_student_data[19].split(',')))
    global lang_cnt
    lang_cnt = len(all_student_data[19].split(','))
    lang_cnt = int(lang_cnt)
    global skill_cnt
    skill_cnt = len(all_student_data[9].split(','))
    skill_cnt = int(skill_cnt)

    if template_id == 1:   
        return redirect(url_for("newTemplate1"))
    elif template_id == 2:
        return redirect(url_for("newTemplate2"))
    else : 
        return redirect(url_for("newTemplate3"))


@app.route('/new_template1')
def newTemplate1():
    return render_template('newTemplate1.html' , all_data = all_student_data, lang_cnt = lang_cnt , skill_cnt = skill_cnt)

@app.route('/new_template2')
def newTemplate2():
        return render_template('newTemplate2.html' , all_data = all_student_data, lang_cnt = lang_cnt , skill_cnt = skill_cnt )

@app.route('/new_template3')
def newTemplate3():
        return render_template('newTemplate3.html' , all_data = all_student_data, lang_cnt = lang_cnt , skill_cnt = skill_cnt )

@app.route("/resume1")
def template():
    return render_template("template1.html")

@app.route("/resume2")
def template2():
    return render_template("template2.html")

@app.route("/resume3")
def template3():
    return render_template("template3.html")

@app.route("/student-dashboard")
def studentDashboard():
    return render_template("studentdashboard.html")

# @app.route("/company/<id>")
# def myid(id):~
#     print(id)
#     return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True)
