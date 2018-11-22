import glob, os

current_dir = os.path.dirname(os.path.abspath(__file__))

percentage_test = 10

file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir + '/Images/001', "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1