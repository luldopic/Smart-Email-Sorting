# imap_gmail.py
# From: https://verpa.wordpress.com/2010/01/23/python-gmail-imap-part-1/


import imaplib
import json
 
class gmail:
    def __init__ (self):
        self.imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
        self.loggedIn = False
 
        self.mailboxes = mailboxes(self.imap_server);
 
    def login (self):
        credentialsJSON = "credentialsGoogle.json"
        with open(credentialsJSON) as handler:
            credentials = json.load(handler)
        result = self.imap_server.login(credentials["user"],credentials["password"])
        if result[0] == 'OK':
            self.loggedIn = True
 
    def logout (self):
        self.imap_server.close()
        self.imap_server.logout()
        self.loggedIn = False
    

class mailboxes:
    def __init__(self, gmail_server):
        super.__init__(self)
        self.server = gmail_server
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

    def __init__(self):
        pass
    def __init__(self, gmail_server):
        self.server = gmail_server
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