import tkinter as tk
import smtplib

def show_entry_fields():
    #print("Recipient Email: %s\nPassword: %s" % (e1.get(), e2.get()))
    print(e1.get(),e2.get())




master = tk.Tk()
tk.Label(master, 
         text="Recipient Email").grid(row=0)
tk.Label(master, 
         text="Password").grid(row=1)

var = tk.StringVar()
var2 = tk.StringVar()
e1 = tk.Entry(master,textvariable = var)
e2 = tk.Entry(master,textvariable = var2)





e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def sendMail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    #passwrd = input("What is your password: ")
    smtpObj.login(' CAlfano1999@gmail.com ', e2.get())
    #email = input("Who is this email being sent to?: ")

    body = "Subject: GUI\nDear Bhussain,\nThe GUI is now functional"
    print('Sending email to %s...' % e1.get())
    sendmailStatus = smtpObj.sendmail('my_email_address@gmail.com', e1.get(), body)

    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' % (e1.get(),
        sendmailStatus))
    smtpObj.quit()

tk.Button(master, 
          text='Send', 
          command=sendMail).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()