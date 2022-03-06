# Connect to imap_gmail.py


from imap_tools import MailBox, AND, OR, NOT
import json

class gmail(MailBox):
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
                super().login(credentials["user"],credentials["password"])
                self.loggedIn = True
                print("Log in Succeed")
            except:
                print("Log in Failed")
         
    def logout (self):
        try:
            self.close()
        except:
            pass
        finally:
            super().logout()
            self.loggedIn = False
    
    def __get_mailfromInbox__(self):
        self.folder.set('Inbox')
        

