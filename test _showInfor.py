import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Nam123456',
                             db='lung_images',
                             )
try:


    with connection.cursor() as cursor:
        sql = "SELECT * FROM image_information WHERE ImageIndex ='00000017_001.png'"
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data)
        for row in data:

            print(row)


        # # Read a single record
        # sql = "SELECT * FROM image_information WHERE ImageIndex =%s"
        # cursor.execute(sql)
        # result = cursor.fetchone()
        # print(result)
        #
finally:
    connection.close()

# def displayImageInformation():
#     with connection.cursor() as cursor:
#
#         sql = "SELECT * FROM image_information WHERE ImageIndex = '0.jpg '"
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         print(result)
#     return;