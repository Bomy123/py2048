from controller import CalNewData, RotateData
class FingerEvent:
    def __init__(self):
        self.calnewdata = CalNewData.CalNewData()
        self.rotatedata = RotateData.RotateData()

    def fingerup(self,data):
        resdata = self.calnewdata.cal(data)
        return self.calnewdata.insertdata(resdata)


    def fingerdown(self,data):
        resdata = self.rotatedata.roatedown(data)
        resdata = self.calnewdata.cal(resdata)
        resdata = self.rotatedata.roateup(resdata)
        resdata = self.calnewdata.insertdata(resdata)
        return resdata


    def fingerleft(self,data):
        resdata = self.rotatedata.roateright(data)
        resdata = self.calnewdata.cal(resdata)
        resdata = self.rotatedata.roateleft(resdata)
        resdata = self.calnewdata.insertdata(resdata)
        return resdata


    def fingerright(self,data):
        resdata = self.rotatedata.roateleft(data)
        # NormalUtils.printlist(resdata)
        resdata = self.calnewdata.cal(resdata)
        # NormalUtils.printlist(resdata)
        resdata = self.rotatedata.roateright(resdata)
        # NormalUtils.printlist(resdata)
        resdata = self.calnewdata.insertdata(resdata)
        return resdata


# data = [[1, 2, 0, 0],
#         [1, 6, 0, 2],
#         [0, 0, 8, 0],
#         [0, 0, 0, 8]]
# NormalUtils.printlist(fingerright(data))
