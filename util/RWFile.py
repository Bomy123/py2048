
class RWFile:
    def writefile(self,path,content):
        with open(path,"a") as f:
            f.write("\n")
            f.write("##########################################################\n")
            f.write(content)
            f.write("\n")
            f.write("##########################################################\n")
    def writecachefile(self,path,content):
        with open(path,"a") as f:
            f.write("\n")
            f.write(content)
    def readfile(self,path):
        content = []
        with open(path,"r") as f:
            content = f.readlines()
        return content

    def cleanfile(self,path):
        with open(path,"w") as f:
            f.write(" ")