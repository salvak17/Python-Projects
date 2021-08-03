
import sqlite3



# Create database subAssign.db and creates connection
conn = sqlite3.connect('subAssign.db')
# Creates table tbl_txtDocs w/primary key and column col_txtDoc as string
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtDocs(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_txtDoc STRING)")
    conn.commit()



# Creates connection
conn = sqlite3.connect('subAssign.db')
#tuple of docs
fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf', \
            'myPhoto.jpg')



# Loop through each object in the tuple to find the txt docs that end w/".txt"
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple therefore (x,) will denote
        # a one element tuple for each doc ending w/".txt"
            cur.execute("INSERT INTO tbl_txtDocs (col_txtDoc) VALUES (?)", (x,))
            print(x)
conn.close()
