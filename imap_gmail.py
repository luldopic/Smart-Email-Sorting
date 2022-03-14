# Connect to Gmail Server and Fetch Mail


from imap_tools import MailBox, U, A
import json


class gmail(MailBox):
    def __init__(self):
        self.connectToGmail()
        self.loggedIn = False
 
    def connectToGmail(self):
        handshake = False
        while not handshake:
            try:
                super().__init__("imap.gmail.com")
                handshake = True
                print("Handshake Succeed")
            except:
                print("Handshake Failed")
 
    def login(self):
        for login_attempt in range(3):
            try:
                credentialsJSON = "credentialsGoogle.json"
                with open(credentialsJSON) as handler:
                    credentials = json.load(handler)
                super().login(credentials["user"], credentials["password"], initial_folder='Inbox')
                self.loggedIn = True
                del credentials
                print("Log in Succeed")
                break
            except Exception as e:
                print("Log in Failed due to ", e)
         
    def logout(self):
        try:
            super().close()
        except:
            pass
        finally:
            super().logout()
            self.loggedIn = False
    
    def fetchMail(self, fetchFrom="latest", fetchNumber="ALL", bulk=False, UID_RANGE = None):
        self.folder.set('Inbox')
        if fetchNumber == "ALL":
            nlimit = None
        else:
            nlimit = fetchNumber
        if fetchFrom == "latest":
            reversebool = True
        else:
            reversebool = False

        msglist = []
        for msg in self.fetch(A(U(UID_RANGE[0],UID_RANGE[1])), limit=nlimit, reverse=reversebool, bulk=bulk):
            msglist.append(msg)
            print(msg.uid)
        return msglist
