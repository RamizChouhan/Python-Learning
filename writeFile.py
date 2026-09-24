import os
file = open("data.txt","a")
file.write("MERN Stack Road Map\n")
rd = ["react","node js","express js","mongodb"]
file.writelines(rd)
print("Done")
file.close()

    

