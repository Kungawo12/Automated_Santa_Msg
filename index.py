from dotenv import load_dotenv
import os
import random
import smtplib
import ssl

load_dotenv()



def send_email(sender, receiver, recipient):
    print(f"Preparing to send email to {receiver} with recipient {recipient}")
    password = os.environ['password']
    if not password:
        print("Password not found in environment variables.")
        return
    body_msg = f''' \
    From : {sender}
    Subject: Your Secret Santa Present 
        
    Hi! Your secret santa is: {recipient}! 🎅
    Remember to spent 10$- 20$ on your gift,but don't stress about it being the perfect gift.
    '''
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, body_msg)
        print(f"Email sent to {receiver}")
    except Exception as e:
        print(f"Failed to send email to {receiver}: {e}")

    name_list =['Tenzin', 'Tsering', 'Rigzin', 'Norbu', 'Jugney', 'Kunga'] 
    names_and_emails = [
        ['Tenzin', 'tkunga662@gmail.com'],
        ['Tsering', 'tenzinkuga31@gmail.com'],
        ['Rigzin', 'tenzin.kunga082024@gmail.com'],
        ['Norbu', 'kungatenzin320@gmail.com'],
        ['Jugney', 'jampa@gmail.com'],
        ['Kunga', 'ten71860@fairview.org']
    ]
    
    if len(name_list ) <= 1:
        print('Not enough people to play Secret Santa')
        quit()
        
    first_name = names_and_emails[0][0]
    
    while len(name_list) >= 2:
        send_email('officialtenzin.kunga@gmail.com', names_and_emails[0][1], names_and_emails[1][0])
        names_and_emails.pop(0)
        print('names_and_emails before shuffle:', names_and_emails)  # Debug print statement
        random.shuffle(names_and_emails)
    
print(f"Sending final email to {names_and_emails[0][1]} with recipient {first_name}")
send_email('officialtenzin.kunga@gmail.com', names_and_emails[0][1], first_name)
    
print("Emails have been sent.")