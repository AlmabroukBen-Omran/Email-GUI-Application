#Imports

from tkinter import *

from email.message import EmailMessage

from PIL import Image, ImageTk

import ssl

import smtplib


#Functions
def show_password():

    if password_input.cget("show") == "*":

        password_input.config(show = "")

    else:

        password_input.config(show = "*")


def reset_form():

    sender_input.delete(0, "end")

    password_input.delete(0, "end")

    receiver_input.delete(0, "end")

    subject_input.delete(0, "end")

    body_input.delete(0, "end")

    notification_label.config(text=" ")


def send_email():

    sender = temp_sender.get()

    password = temp_password.get()

    receiver = temp_receiver.get()

    subject = temp_subject.get()

    body = temp_body.get()

    email_provider_dict = {"@gmail.com": "smtp.gmail.com",
                           "@outlook.com": "smtp.office365.com",
                           "@icloud.com": "smtp.mail.me.com",
                           "@yahoo.com": "smtp.mail.yahoo.com",
                           "@yahoo.ca": "smtp.mail.yahoo.com",
                           "@hotmail.com": "smtp.office365.com",
                           "@aol.com": "smtp.aol.com"}

    try:

        if sender == "" or password == "" or receiver == "" or subject == "" or body == "":

            notification_label.config(text = "All fields must be filled in !", fg = "red")

            return
        
        else:

            email = EmailMessage()

            email["From"] = sender

            email["To"] = receiver

            email["subject"] = subject

            email.set_content(body)

            context = ssl.create_default_context()

            for domain in email_provider_dict.keys():

                if domain in sender:

                    smtp_server = email_provider_dict[domain]
            
            server = smtplib.SMTP(smtp_server, 587)

            server.starttls(context = context)

            server.login(sender, password)

            server.sendmail(sender, receiver, email.as_string())
                
            notification_label.config(text = "Email has been successfuly sent !", fg = "green")

    except:

        notification_label.config(text = "An error occured while sending the email !", fg = "red")

    finally:

        server.quit()




#Main screen
window = Tk()

window.title("Email GUI Application")

window.geometry("920x600")


#App image
img = Image.open("email_logo.png")

resized = img.resize((50, 50), Image.ANTIALIAS)

new_img = ImageTk.PhotoImage(resized)


#App Labels
heading = Label(window, 
                text = "Email Application Client", 
                font = ("Calibri", 25), 
                image = new_img, 
                compound = "right",
                padx = 10)

heading.place(x = 280, y = 10)

subheading = Label(window, text = "Email Sender Form:", font = ("Calibri", 20))
subheading.place(x = 10, y = 80)

requirements = Label(window, text = "App Requirements:", font = ("Calibri", 20))
requirements.place(x = 630, y = 80)

step1 = Label(window, text = "- Enable two factor authentication on sender's email", font = ("Calibri", 18))
step1.place(x = 480, y = 140)

step2 = Label(window, text = "- Generate app password via email security settings", font = ("Calibri", 18))
step2.place(x = 480, y = 200)

note = Label(window, text = "Note: Not all email providers require an app password", font = ("Calibri", 18))
note.place(x = 480, y = 260)

sender_label = Label(window, text = "From", font = ("Calibri", 18))
sender_label.place(x = 10, y = 140)

password_label = Label(window, text = "Email App Password", font = ("Calibri", 18))
password_label.place(x = 10, y = 190)

show_label = Label(window, text = "Show Password", font = ("Calibri", 13))
show_label.place(x = 10, y = 240)

receiver_label = Label(window, text = "To", font = ("Calibri", 18))
receiver_label.place(x = 10, y = 290)

subject_label = Label(window, text = "Subject", font = ("Calibri", 18))
subject_label.place(x = 10, y = 340)

body_label = Label(window, text = "Body", font = ("Calibri", 18))
body_label.place(x = 10, y = 390)

notification_label = Label(window, text = "", font = ("Calibri", 18))
notification_label.place(x = 10, y = 440)


#Input storage
temp_sender = StringVar()

temp_password = StringVar()

temp_receiver = StringVar()

temp_subject = StringVar()

temp_body = StringVar()

temp_notification = StringVar()


#App inputs
sender_input = Entry(window,
                     textvariable = temp_sender, 
                     font = ("Calibri", 15), 
                     width = 25, 
                     relief = "raised", 
                     bd=2)

sender_input.place(x = 70, y = 140)

password_input = Entry(window,
                     textvariable = temp_password, 
                     font = ("Calibri", 15), 
                     width = 25, 
                     relief = "raised", 
                     bd=2,
                     show = "*")

password_input.place(x = 190, y = 190)

show_input = Checkbutton(window, command = show_password)

show_input.place(x = 115, y = 240)

receiver_input = Entry(window,
                     textvariable = temp_receiver, 
                     font = ("Calibri", 15), 
                     width = 25, 
                     relief = "raised", 
                     bd=2)

receiver_input.place(x = 50, y = 290)

subject_input = Entry(window,
                     textvariable = temp_subject, 
                     font = ("Calibri", 15), 
                     width = 25, 
                     relief = "raised", 
                     bd=2)

subject_input.place(x = 90, y = 340)

body_input = Entry(window,
                     textvariable = temp_body, 
                     font = ("Calibri", 15), 
                     width = 25, 
                     relief = "raised", 
                     bd=2)

body_input.place(x = 70, y = 390, height = 40, width = 550)


#App Buttons
send_button = Button(window, text = "Send Email", padx = 4, pady = 5, command = send_email)
send_button.place(x = 10, y = 550)

reset_button = Button(window, text = "Reset Form", padx = 4, pady = 5, command = reset_form)
reset_button.place(x = 150, y = 550)


#Display GUI window output
window.mainloop()