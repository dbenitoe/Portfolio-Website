import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 587  # Use 587 for TLS connection
    username = "dbenitoe@gmail.com"
    app_password = "znmxfhndellathix"
    receiver = "dbenitoe@kent.edu"
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(username, app_password)
        server.sendmail(username, receiver, message)


