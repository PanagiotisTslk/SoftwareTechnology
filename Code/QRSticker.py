#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class QRSticker '''

# Libraries
import qrcode


# Class for QR-Stickers
class QRSticker:

  # Constructor
  def __init__(self, code, room):
    self.code = code
    self.room = room

  def ReadQR(self):
    pass


# Creating QR-code stickers
def CreateQR(num):

  rooms = ('ΒΑ', 'Β', 'Δ1', 'Δ2', 'Β4')
  capacity = (350, 100, 60, 60, 150)
  codes = ('001', '010', '011', '100', '101')

  try:
    # Creating an instance of qrcode
    for x in range(num):

      sticker = {
        'Αίθουσα': rooms[x],
        'Χωρητικότητα': capacity[x],
        'Κωδικός Αίθουσας': codes[x]
      }

      qr = qrcode.QRCode(version=1, box_size=10, border=5)
      qr.add_data(sticker)
      qr.make(fit=True)
      img = qr.make_image(fill='black', back_color='white')
      img.save(f'icons/QR-Stickers/qrcode{rooms[x]}.png')
      print('QR stickers created successfully!\n')

      # Connecting with database
      dbname = get_database()
      # Choosing collection
      col = dbname["QRStickers"]

      col.insert_one(sticker)
      print("QR stickers inserted to database successfully!\n")

  except:
    print('Error!\nQR stickers not created!')

# Connection with database
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://tslk:Tslkgtx950pt@cluster0.jnvsh.mongodb.net/StudentUp"

    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client["StudentUp"]


# CreateQR(5)