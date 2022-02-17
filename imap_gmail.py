# imap_gmail.py
# From: https://verpa.wordpress.com/2010/01/23/python-gmail-imap-part-1/


import imaplib
 
class gmail_imap:
 
    def __init__ (self, username, password):
        self.imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
        self.username = username
        self.password = password
        self.loggedIn = False
 
        self.mailboxes = gmail_mailboxes(self.imap_server);
        self.messages = gmail_messages.gmail_messages(self);
 
    def login (self):
        self.imap_server.login(self.username,self.password)
        self.loggedIn = True
 
    def logout (self):
        self.imap_server.close()
        self.imap_server.logout()
        self.loggedIn = False
    

class gmail_mailboxes:
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


class gmail_messages:
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