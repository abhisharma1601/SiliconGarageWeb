from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

 # def send_email(user, pwd, recipient, subject, body):
#     import smtplib

#     FROM = user
#     TO = recipient if isinstance(recipient, list) else [recipient]
#     SUBJECT = subject
#     TEXT = body

#     # Prepare actual message
#     message = """From: %s\nTo: %s\nSubject: %s\n\n%s
#     """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

#     with smtplib.SMTP_SSL(host="") as smtp:
#         smtp.login(user,pwd)
#         smtp.sendmail(user,TO,message)
#         smtp.quit()

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

@app.route("/terms&conditions")
def terms():
    return render_template("/data/terms.html")

@app.route("/PrivacyPolicy")
def privacy():
    return render_template("/data/privacy.html")

@app.route("/send_newsletter", methods = ['POST'])
def newsletter():
    email = request.form['email']
    send_email("info@silicongarage.in","Qazx1234@...","A new newsletter join","Mail: {0}".format(email))
    send_email("info@silicongarage.in","Qazx1234@...",email,"Thank You","Thank you for visiting our website.\nYou are registered as a member with subscription of our monthly news letter.\nThankyou for subscribing.\nTeam Silicon Garage")
    return redirect("/")

@app.route("/sendquery", methods = ["POST"])
def send_query():
    name = request.form['name1']
    email = request.form['email']
    phone = request.form['phone']
    query = request.form['message']
    send_email("","Qazx1234@...","A new Query","Name: {0}\nEmail: {1}\nPhone No. : {2}\nQuery: {3}".format(name,email,phone,query))
    send_email("","Qazx1234@...",email,"Thank You","Thank you for contacting us.\nOur representatives will reach out to you soon.\nTeam Silicon Garage")
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=False)
