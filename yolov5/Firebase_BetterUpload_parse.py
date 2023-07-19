'''
    This worked to upload data to DB
'''


import os
from time import time
from datetime import date
from datetime import datetime


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

data = data2 = "" 
count = 1
list = []
#tempArray = ['n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a']
temp = 0

i2 = 0
i3 = 0

indexTotalTracker = 0
totalObjectsUploaded = 0

arrayLen = 0
totalObjects = 0
obCounter = 0
resetCounter = 0
currentIndex = 0
attributeCounter = 0

var = 'NameOfField'

stringTemp = ''

tempDocName = ''

todayString = ''
todayInt = date.today()
todayString = str(todayInt)

hourString = ''
hourInt = datetime.now()
hourString = str(hourInt)

collectionTemp = ''


db = firestore.client()
doc_ref_level_1 = db.collection('H&M').document(todayString)
#doc_ref_level_2 = doc_ref_level_1.collection("Time").document(hourString)


for i in os.listdir():
    videoFrame = "retail_" + str(count) + ".txt"
    dir2 = './runs/detect/exp20/labels/'
    fullPath = dir2 + videoFrame
    print("Opening file path: " + fullPath)
    


    '''
    One line at a time
    '''
    with open(fullPath) as fp:
        list=[word for line in fp for word in line.split()]
        tempArray = ['n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a']
        arrayLen = len(list)
        print("The lenght of this file array is: " + str(arrayLen))
        indexTotalTracker = indexTotalTracker + arrayLen
        '''
        Here each array item should be put into a temp var.
        This temp var will be pushed into FireStore field.
        ! Cut off at 7 intervals !
        '''
        #print("The length of this array is " + str(arrayLen))
        totalObjects = arrayLen / 7
        # Reseting counter to start at the beginging of the line
        currentIndex = 0
        while currentIndex != arrayLen:
            
            for x in list:
                attributeCounter = resetCounter
                objectDocument = datetime.now()
                objectDocument2 = str(objectDocument)
                doc_ref_level_2 = doc_ref_level_1.collection("Time").document(objectDocument2)
                #doc_ref_level_3 = doc_ref_level_2.collection(objectDocument2).document("PersonObject")
                while attributeCounter < 7:  
                    temp = list[currentIndex] 
                    #print(temp)
                    #print(attributeCounter)
                    ### LINE below has index out of rane and I don't know why.
                    tempArray[attributeCounter] = temp
                    
                    #print("The temp is: " + str(temp) + "-------- Atrribute Counter is: " + str(attributeCounter) + "-------- Index position is: " + str(currentIndex))

                    currentIndex = currentIndex + 1 
                    attributeCounter = attributeCounter + 1 

                    #print("----------------- Adding --- " + str(temp) + "--- to FIELD:  " + stringTemp )
                totalObjectsUploaded = totalObjectsUploaded + 1
                '''                
                doc_ref_level_2.set({
                    'objectType' : tempArray[0],
                    'posX1' : tempArray[1],
                    'posY1' : tempArray[2],
                    'posX2' : tempArray[3],
                    'posY2' : tempArray[4],
                    'accuracy' : tempArray[5],
                    'sceneCountID' : tempArray[6],
                    })
                '''
                #print("Uploaded " + str(totalObjectsUploaded) + " object to the DB")
                if currentIndex == arrayLen:
                    #print("The currentIndex is the same lenght as Array ! Halting now with currentIndex: " + str(currentIndex))
                    #print("Total is: " + str(indexTotalTracker))
                    #print("Stopped at index: " + str(currentIndex))
                    #print("\n\n\nTotal objects uploaded is: " + str(totalObjectsUploaded))
                    #print("\n\n\n")
                    break
                #print("Finally the broken index is: " + str(currentIndex))
              

                
                
        #print(list[i2])
        count = count + 1
        #i2 = i2 + 1
        #print("Current index at: " + str(i2))
        #print("Increased count --- Current count: " + str(count) )

        #doc_ref.collection('results').add({var :list})
        
