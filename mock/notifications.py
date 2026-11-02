import smtplib

def send_email(to, subject):
    server = smtplib.SMTP("smtp.example.com")
    server.sendmail("noreply@app.com", to, subject)
    server.quit()
    return True

def notify_user(user_email):
    send_email(user_email,  "Welcome to our service!")
    return f"Notified {user_email}"