import os
data = data2 = ""
newdata = ""

dir = './runs/detect/exp21/labels/'
# read data from file 1
count = 1
count2 = 1
for i in os.listdir(dir):

    videoFrame = "retail_" + str(count) + ".txt"
    #print(videoFrame)

    dir2 = './runs/detect/exp21/labels/'
    fullPath = dir2 + videoFrame
    
    with open (fullPath) as fp:
        data = fp.read()
    
    # Write content of file 1 in Append mode
    with open ('./runs/detect/exp21/labels/retail_final.txt', 'a') as fp:
        fp.write(data)

    # Add break line to seperate each written file
    breakLine = "\n"
    with open ('./runs/detect/exp21/labels/retail_final.txt', 'a') as fp:
        fp.write(breakLine)

    count = count + 1
    #videoFrame2 = "retail_" + str(count) + ".txt"
    #fullPath2 = dir2 + "retail_" + str(count2) + ".txt"

    #print(fullPath)

    #newData = "data" + str(count2)
    #print(fullPath2)

    # read data from file 2
   # with open (fullPath2) as fp:
        #data2 = fp.read()

    # Merge
    #data += "\n"
    #data += data2

    # Write to new file
   # with open ('./runs/detect/exp21/labels/retail_final.txt', 'a') as fp:
       # fp.write(data)


