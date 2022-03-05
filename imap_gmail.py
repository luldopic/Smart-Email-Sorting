# Connect to imap_gmail.py


import imaplib
import json

class gmail(imaplib.IMAP4_SSL):
    def __init__(self):
        self.connectToGmail()
        self.loggedIn = False
 
    def connectToGmail(self):
        handshake = False
        while handshake == False:
            try:
                super().__init__("imap.gmail.com")
                handshake = True
                print("Handshake Succeed")
            except:
                print("Handshake Failed")
 
    def login (self):
        while self.loggedIn == False:
            try:
                credentialsJSON = "credentialsGoogle.json"
                with open(credentialsJSON) as handler:
                    credentials = json.load(handler)
                result = super().login(credentials["user"],credentials["password"])
                if result[0] == 'OK':
                    self.loggedIn = True
            except:
                print("Log in Failed")
         
    def logout (self):
        self.close()
        super().logout()
        self.loggedIn = False
    
    def get_all_mail(self): return mailboxes("[Gmail]/All Mail")

class mailboxes:
    def __init__(self, **name):
        self.mailboxes = list(name)
        self.name = name
 
    def load(self):
        if(not self.server.loggedIn):
            self.server.login()
 
        for box in self.server.imap_server.list()[1]:  #Ugly
            name = box.split(' "/" ')[1][1:-1]
            if( name != "[Gmail]"):  #ignore global [Gmail] mailbox
                self.mailboxes.append(name)
 
    def __getitem__(self, key): return self.mailboxes[key]

