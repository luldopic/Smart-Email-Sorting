from mailDB import emailDB
import mailDB
import imap_gmail


class Mail:
    def __init__(self, DB, msg):
        self.uid = msg.uid
        self.sender = msg.from_
        self.subject = msg.subject
        self.date = msg.date
        self.text = msg.text
        [self.numberOfAttachments, self.AttachmentList] = self.getAttachments(msg)
        dictEntry = self.createdict()
        emailDB.addEntry(DB, "Email", dictEntry)

    def createdict(self):
        dictEntry = {
            "uid": self.uid,
            "sender": self.sender,
            "subject": self.subject,
            "date": self.date,
            "text": self.text,
            "numberOfAttachments": self.numberOfAttachments
        }
        return dictEntry

    def getAttachments(self,msg):
        attachmentList = []
        for att in msg.attachments:
            attachmentList.append(att)
        return [len(attachmentList), attachmentList]


class Sorter:
    def __init__(self):
        self.IMAP = imap_gmail.gmail()
        self.IMAP.login()
        self.DB = mailDB.emailDB()
