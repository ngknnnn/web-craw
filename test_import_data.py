import pymysql

f = open(r"C:/Users/Admin/Desktop/WebCrawler-Project/sample_labels.csv", "r")
fString =f.read()
# print(fString)

fList = []
for line in fString.split('\n'):
    fList.append(line.split(','))
#print(fList[1][0])

db = pymysql.connect("localhost","root","Nam123456","lung_images")
#prepare the cursor object using cursor method
cursor = db.cursor()

del fList[0]

rows= ''
for i in range(len(fList)-1):
    rows+= "('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fList[i][0],fList[i][1],fList[i][2],fList[i][3],fList[i][4],fList[i][5],fList[i][6],fList[i][7],fList[i][8],fList[i][9],fList[i][10])
    if i != len(fList)-2:
        rows += ','

# print(rows)
queryInsert = "INSERT INTO image_information VALUES " + rows
try:
    #excute the command
    cursor.execute(queryInsert)
    db.commit()
except ValueError as err:
    print(err)
    db.rollback()



db.close()

