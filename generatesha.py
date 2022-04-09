import hashlib
import glob

paths = []
wrongpath = []
with open('folderspath.txt', 'r') as file:
    for line in file.readlines():
        if line.strip().endswith("\\") == True:
            paths.append(line.strip())
        elif line.strip().endswith("\\") == False:
            wrongpath.append(line.strip())
            
for path in paths:
    for file in glob.glob(path+"*.*"):
        with open(file, 'rb') as readfile: # Open the file to read it's bytes
            BLOCK_SIZE = 65536 # The size of each read from the file
            file_hash = hashlib.sha512()
            fb = readfile.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = readfile.read(BLOCK_SIZE) # Read the next block from the file
        if file.endswith("sha") == False:
            with open(file+".sha", 'w') as writefile:
                writefile.write(file_hash.hexdigest())

if len(wrongpath) > 0:
    print("These Below Folder Paths Are Invalid")
    for i in wrongpath:
        print(i)

if len(paths) > 0:
    print("\n**********************************")
    print("SHA File Successfully Generated")
    print("**********************************")