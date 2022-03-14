# Smart-Email-Sorting
Email Suggesting Sorting System

This is a WIP.
Currently, there are three main python files

imap_gmail.py interacts with the gmail and fetch mail depending on the user-provided number

mailDB.py interacts with a local MySQL server so it can be easily sorted and safely interacted
without the fear of messing up with my emails

EmailSort.py directs the order of operation for imap_gmail.py and mailDB.

Feel free to test and bring issues to my attention

# Sorting Method:
WIP

Step 1: Assigning Categoies

Assign categorical flags w.r.t several categorical properties e.g.
Is there an attachment? Is there one or more recipient? Any CC or BCC

Step 2: Sender Analysis

Mail frequency? No-reply in name? Personal or Business email server?

Step 3: Subject Analysis

How common is the subject relative to other mail sent by that sender? 
Keyword analysis (Not sure what I'm do here yet)

Step 4: Text Analysis
Word Frequency Analysis? Identify words used more often than common speech. 
Any keywords for call to action

Step 5: Perform Clustering to sort similar email into categories with different action
i.e. Read urgently, Sort into "XXX" folder, Delete
There will be some level of supervised learning but I'm not to sure yet