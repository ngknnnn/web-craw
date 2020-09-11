# from bs4 import BeautifulSoup
# import requests
# import urllib.request
# import shutil
# from selenium import webdriver
# from selenium.webdriver.common.by import By

import os

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

from flask import Flask, render_template, request, send_from_directory
import kaggle
# import flask
app = Flask(__name__)  # create an app instance
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/", methods=['GET', 'POST'])
def hello():  # call method hello
    return render_template("main.html")
def display_crawler_image(url):
    return "C:/Users/Admin/PycharmProjects/app/images/crawler.png"





@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route("/linkKaggle", methods=['POST'])
def get_link():
    if request.method == "POST":
        req = request.form.get('inputbox')  # get the link have input

        return render_template("test1.html", getLink=req)


@app.route("/gallery", methods=['GET'])
def get_gallery():
    image_names = os.listdir('./images')  # list all the image in this directory

    return render_template('gallery.html', image_names=image_names)


# url_db = db.getAll()
# if new_url in url_db
# link ="abc.com" 


if __name__ == "__main__":
    app.run(debug=True)

    # which returns "hello world"
# @app.route("/upload", methods=["POST"])
# def upload():
#     target = os.path.join(APP_ROOT, 'images/')
#     print(target)
#     if not os.path.isdir(target):
#             os.mkdir(target)
#     else:
#         print("Couldn't create upload directory: {}".format(target))
#     print(request.files.getlist("file"))
#     for upload in request.files.getlist("file"):
#         print(upload)
#         print("{} is the file name".format(upload.filename))
#         filename = upload.filename
#         destination = "/".join([target, filename])
#         print ("Accept incoming file:", filename)
#         print ("Save it to:", destination)
#         upload.save(destination)

#     # return send_from_directory("images", filename, as_attachment=True)
#     return render_template("complete.html", image_name=filename)
