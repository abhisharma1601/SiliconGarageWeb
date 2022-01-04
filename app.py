from flask import Flask, render_template, request
from werkzeug.utils import redirect



app = Flask(__name__)

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    with smtplib.SMTP_SSL(host="mail.stackx.online") as smtp:
        smtp.login(user,pwd)
        smtp.sendmail(user,TO,message)
        smtp.quit()

@app.route("/")
def start():
    return render_template("/index.html")

@app.route("/portfolio/efruithub")
def portfolioefruit():
    return render_template("/portfolios/efruit.html")

@app.route("/portfolio/infinite_trails")
def portfolioinfinite():
    return render_template("/portfolios/infinitetrails.html")

@app.route("/portfolio/gamebent")
def portfoliogamebent():
    return render_template("/portfolios/gamebent.html")

@app.route("/portfolio/craffic")
def portfoliocraffic():
    return render_template("/portfolios/craffic.html")

@app.route("/portfolio/BJP")
def portfoliobjp():
    return render_template("/portfolios/bjp.html")

@app.route("/portfolio/astrodrishti")
def portfolioastrodrishti():
    return render_template("/portfolios/astrodrishti.html")

@app.route("/sendquery", methods = ["POST"])
def send_query():
    name = request.form['name1']
    email = request.form['email']
    phone = request.form['phone']
    query = request.form['message']
    send_email("astrodrishti@stackx.online","StackX@123","4abhi45@gmail.com","A new Query","Name: {0}\nEmail: {1}\nPhone No. : {2}\nQuery: {3}".format(name,email,phone,query))
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)