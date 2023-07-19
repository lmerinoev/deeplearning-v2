''' 
    This script connects to Firebase.
        - Acquires pointer to collection for retail space
        - Generates document for a day (or hour) of inference data
'''


import os
from time import time


# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

print("Successfuly got credentials")


data = data2 = ""
newdata = ""
count = 1
count2 = 1

list = []


fN = "Field Test Name"

data93 = {
    'number' : 3.14,
    'string' : 'Hello world',
}


dir = './runs/detect/exp21/labels/'
db = firestore.client()
doc_ref = db.collection('Retail1').document('Hour')

'''
    Accessing Retail inference result file.
    Will append to a var and push to db.
'''
var = 'NameOfField'
for i in os.listdir():
    newFn = fN +str(count)
    videoFrame = "retail_" + str(count) + ".txt"
    #print(videoFrame)

    dir2 = './runs/detect/exp21/labels/'
    fullPath = dir2 + videoFrame
    
    '''
        !! Need to create a way to extract each file into a JSON !!
        https://www.geeksforgeeks.org/convert-text-file-to-json-in-python/

    '''


    '''
        This is a file reader that reads and inputs an entire
        text file into a variable
    '''
    #with open (fullPath) as fp:
        #data = fp.read()
        #print(data)

    with open(fullPath) as fp:
        list=[word for line in fp for word in line.split()]
        doc_ref.collection('results').add(list)
        print("Added data to DB")   
    print(list)
    '''
        Add data to collection inside of document
    '''
    #db.collection('Retail1').document_id().collection_id('resultField').add({var :data})
    #doc_ref = db.collection('Retail1').document('Hour')
    #doc_ref.collection('results').add(list)
    

    '''
        Line below creats a document with one field containing all data
    '''
   #db.collection('Retail1').add({var :data})
    #db.collection('Retail1').add({var :data})
    print("Added data to DB")   
    count = count + 1

'''
    Pushing data to db
'''
#db = firestore.client()
#db.collection('Retail1').add({'name':'NFM Furniture', 'id': 1})
#print("Added data to DB")

