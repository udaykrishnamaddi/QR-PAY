import pyqrcode

def generate_qrcode(contents, filename):

    qrcode = pyqrcode.create(contents)
    qrcode.png('./static/qrcodes/'+filename+'.png')

    return True