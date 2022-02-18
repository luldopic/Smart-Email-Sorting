# imap_gmail.py


import imaplib
import json

class gmail:
    def __init__(self):
        super().__init__(self)
        self.loggedIn = False
 
    def login (self):
        while loggedIn == False:
            try:
                credentialsJSON = "credentialsGoogle.json"
                with open(credentialsJSON) as handler:
                    credentials = json.load(handler)
                result = self.imap_server.login(credentials["user"],credentials["password"])
                if result[0] == 'OK':
                    self.loggedIn = True
            except:
                print("Log in Failed")
         
    def logout (self):
        self.imap_server.close()
        self.imap_server.logout()
        self.loggedIn = False
    
    def get_all_mailboxes(self):
        self.AllMailboxes = mailboxes()
        for mailbox in 
    

class mailboxes:
    def __init__(self, **name):
        self.mailboxes = list()
 
    def load(self):
        if(not self.server.loggedIn):
            self.server.login()
 
        for box in self.server.imap_server.list()[1]:  #Ugly
            name = box.split(' "/" ')[1][1:-1]
            if( name != "[Gmail]"):  #ignore global [Gmail] mailbox
                self.mailboxes.append(name)
 
    def __repr__(self):
        return "<gmail_mailboxes: [%s]="">" %  (',  '.join(self.mailboxes))
 
    def __getitem__(self, key): return self.mailboxes[key]

def connectToGmail():
    handshake = False
    while handshake == False:
        try:
            handshake = True
            return gmail(imaplib.IMAP4_SSL("imap.gmail.com"))
        except:
            print("Handshake Failed")