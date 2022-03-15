from mailDB import emailDB
import mailDB
import imap_gmail


class Mail:
    def __init__(self, msg):
        self.uid = int(msg.uid)
        self.sender = msg.from_
        self.subject = msg.subject
        date = msg.date.strftime('%Y-%m-%d %H:%M:%S')
        self.date = date
        self.text = msg.text
        [self.numberOfAttachments, self.AttachmentList] = self.getAttachments(msg)
        self.dictEntry = self.createdict()

    def createdict(self, withText=False):
        dictEntry = {
            "uid": self.uid,
            "sender": self.sender,
            "subject": self.subject,
            "date": self.date,
            "text": self.text,
            #"numberOfAttachments": self.numberOfAttachments,
            "InputError": 0
        }
        if not withText:
            dictEntry.pop("text")
        else:
            pass
        return dictEntry

    def getAttachments(self,msg):
        attachmentList = []
        for att in msg.attachments:
            attachmentList.append(att)
        return [len(attachmentList), attachmentList]


    def addToDB(self, DB):
        emailDB.addEntry(DB, "Email", self.dictEntry)

    def __checkifAlreadyExisting__(self, DB):
        SQL = "SELECT * FROM Email WHERE uid = {uid}".format(uid=self.uid)
        res = emailDB.executeSQLCursor(SQL)
        if len(res) != 0:
            return True
        else:
            return False

class Sorter:
    def __init__(self):
        self.IMAP = imap_gmail.gmail()
        self.IMAP.login()
        self.DB = mailDB.emailDB()
