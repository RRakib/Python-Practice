############### Importing Modules
# from pathlib import Path

############### Create Folders and Open File to Perform Read Or Write Operation
# path = Path()
# newPath = Path("test")
# print(newPath.mkdir())
# print(newPath.rmdir())
# print(path.exists())
# for file in path.glob("*"):
#     print(file)
text = open('test.txt', 'r+')
# text.close()
print(text)
print('Check to see the file name: ', text.name)
print('Wring file:', text.write('Overwritten text'))
print('Reading the file after writing:', text.read())
print('Check to see the mode used in the file: ', text.mode)
print('Check to see if the file is closed or not: ', text.closed)
