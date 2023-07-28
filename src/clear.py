import os

path = "data"

#rm all files w/in specified path
def clearFolder(path):
    for file in os.listdir(path):
        filename = os.path.join(path,file)
        if os.path.isfile(filename):
            os.remove(filename)
    print("Completed")

if __name__ == "__main__":
    # print(os.getcwd())
    clearFolder(path)
