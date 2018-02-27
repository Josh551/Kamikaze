import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("emysamuel39@gmail.com","hellohiyo")
message="How are you"
s.sendmail("emysamuel39@gmail.com","joshuaniteesh551@gmail.com",message)
s.quit()
