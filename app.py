import csv
import os
from flask import Flask, render_template, request, url_for, session, send_file
from src import qrcode_generator as qr
from src import prepare_qrcode_data as pqrd

# create flask app
app = Flask(__name__)

app.secret_key="1234"

@app.route('/', methods=['GET'])
def homePage():

    return render_template('home.html')


@app.route('/getStalls', methods=['GET'])
def stallsPage():

    stalls = os.listdir('./static/data/')
    stalls_names = []

    for stall in stalls:
        stalls_names.append(stall.split('.')[0])

    return render_template('stalls.html', stalls_names=stalls_names)


@app.route('/orderFood/<stall_name>', methods=['GET', 'POST'])
def orderFood(stall_name):

    file = open('./static/data/'+stall_name+'.csv')
    file_reader = csv.reader(file)

    food_items = []

    for row in file_reader:

        food_items.append(row)

    file.close()

    no_of_food_items = len(food_items)

    return render_template('orderFood.html', stall_name=stall_name, no_of_food_items=no_of_food_items, food_items=food_items)


@app.route('/generateQRCode/<stall_name>', methods=['GET', 'POST'])
def generateQRCode(stall_name):

    data=dict(request.form)

    data=pqrd.structure_data(stall_name, data)

    filename=data["userData"]["username"]+'_qrcode'

    status = qr.generate_qrcode(str(data), filename)

    session[filename]=filename+'.png'

    return render_template('serveQRCode.html', filename=filename+'.png')


@app.route('/downloadQRCode/<filename>', methods=['GET'])
def downloadQRCode(filename):

    return send_file('./static/qrcodes/'+filename, as_attachment=True)


@app.route('/clearSession', methods=['GET'])
def clearSession():

    for filename in session.keys():

        try:
            os.remove('./static/qrcodes/'+filename+'.png')

        except:
            continue

    return render_template('home.html')
            

if __name__ == '__main__':
    app.run(debug=True)