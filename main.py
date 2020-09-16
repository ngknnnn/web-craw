
import os
import kaggle
from flask import Flask, render_template, request, send_from_directory
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)  # create an app instance
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/", methods=['GET', 'POST'])
def hello():  # call method hello
    return render_template("main.html")


# @app.route("/download",methods = ["GET"])
# def download():
#         orskl_kaggle = kaggle.KaggleApi()
#         orskl_kaggle.authenticate()
#         orskl_dataset_loc = "nih-chest-xrays/sample"  # link location of the dataset in kaggle
#
#         # orskl_dataset = orskl_kaggle.dataset_view(orskl_dataset_loc)
#         orskl_kaggle.dataset_download_cli(orskl_dataset_loc, None, None, "F:/", True)
#

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
    image_names = os.listdir('./images/')  # list all the image in this directory
    data = get_info()
    page = request.args.get('page', 1, type=int)
    pagination = Pagination(page=page, per_page=10, record_name=image_names)
    return render_template('gallery.html', image_names=image_names, data=data, pagination=pagination)


def get_info():
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
    finally:
        connection.close()
        return data


if __name__ == "__main__":
    app.run(debug=True)

