# from bs4 import BeautifulSoup
# import requests
# import urllib.request
# import shutil
# from selenium import webdriver
# from selenium.webdriver.common.by import By

import os
import kaggle

# def Craw():
#     driver= webdriver.Chrome(executable_path="F:/New/chromedriver_win32/chromedriver.exe") 
#     driver.get("file:///C:/Users/Admin/Desktop/WebCrawler-Project/main.html")
#     text = driver.find_elements_by_name("inputbox")
#     print(text)


# url = "https://radiopaedia.org/articles/chest-radiograph"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# aas = soup.find_all("a", class_='media-object centered-image')
# image_info = []

# for a in aas: 
#     image_tag = a.findChildren("img")
#     image_info.append((image_tag[0]["src"],image_tag[0]["alt"]))

# def download_image(image):
#     response = requests.get(image[0], stream=True)
#     realname = ''.join(e for e in image[1] if e.isalnum())
    
#     file = open("C://images//bs//{}.jpg".format(realname), 'wb')
    
#     response.raw.decode_content = True
#     shutil.copyfileobj(response.raw, file)
#     del response

# for i in range(0, len(image_info)):
#     download_image(image_info[i])

from flask import Flask,render_template,request,send_from_directory
from flask_paginate import Pagination,get_page_parameter


app = Flask(__name__)     # create an app instance
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=['GET', 'POST'] )   

def hello():                      # call method hello
    return render_template("main.html")
def get_form():
    if request.method == "GET":

     url_input = request.args.get('inputbox',default='*', type= str)

     print(url_input)

@app.route("/download",methods = ["GET"])

def download():
        orskl_kaggle = kaggle.KaggleApi()
        orskl_kaggle.authenticate()
        orskl_dataset_loc = "nih-chest-xrays/sample"  # link location of the dataset in kaggle

        # orskl_dataset = orskl_kaggle.dataset_view(orskl_dataset_loc)
        orskl_kaggle.dataset_download_cli(orskl_dataset_loc, None, None, "F:/", True)
        return
            
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route("/linkKaggle",methods=['POST'])
def get_link():
    
    if request.method == "POST":
        req = request.form.get('inputbox') # get the link have input
       
        return render_template("test1.html",getLink= req)    


@app.route("/gallery", methods=['GET'])
def get_gallery():
    image_names = os.listdir('./images/') #list all the image in this directory
    data = get_info()
    page = request.args.get('page',1,type = int)
    pagination = Pagination(page=page, per_page=10,record_name=image_names)
    return render_template('gallery.html', image_names = image_names,data = data, pagination= pagination)
def get_info():
    import  pymysql


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
    finally:
        connection.close()
        return data


if __name__ == "__main__":        
    app.run(debug=True)

