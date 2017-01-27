import smtplib

# Connect to the SMTP Server
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()

# Ask for user's login credentials
username = input("Email Address: ")
password = input("Password: ")
mail.login(username, password)

email_sender = True
while email_sender:
    # Email Attributes
    receiver = input("Receiver: ")
    subject = 'Subject: ' + input("Subject: ")
    message = '\n' + input("Type Message: ")

    # Send Email
    mail.sendmail(username, receiver, subject+message)
    print("\n Email Sent...")
    new_email = input("\n New Email? (yes/no): ")
    if new_email == 'yes':
        print("\n")
        email_sender=True
    else:
        print("\n Thank you for using the Ez Messaging service. Have a nice day!")
        mail.quit()
        break





