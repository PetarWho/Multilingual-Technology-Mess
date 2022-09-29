import smtplib
import ssl

# NOTE: If you want to send mails you have to use server or create a local one
# More info here: https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server

my_email = input('Enter Sender Email => ')
my_pass = input('Enter Email Password => ')

recipient_mail = input('\nEnter Recipient Email => ')
message = input('\nEnter message to send...\n')


sent_from = my_email
to = [recipient_mail, "zyra@mail.bg"]
subject = 'Lorem ipsum dolor sit amet'
body = message

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(my_email, my_pass)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)


# Here is another method, using starttls

try:
    #Create your SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

   #Use TLS to add security
    smtp.starttls()

    #User Authentication
    smtp.login(my_email, my_pass)

    #Sending the Email
    smtp.sendmail(my_email, recipient_mail, message)

    #Terminating the session
    smtp.quit()
    print ("Email sent successfully!")

except Exception as ex:
    print("Something went wrong....",ex)