import copy
from controller import CalNewData, RotateData
class FingerEvent:
    def __init__(self):
        self.calnewdata = CalNewData.CalNewData()
        self.rotatedata = RotateData.RotateData()
        self.data = []

    def fingerup(self,data):
        self.data = copy.deepcopy(data)
        self.data = self.calnewdata.cal(self.data)
        return self.calnewdata.insertdata(self.data)


    def fingerdown(self,data):
        self.data = copy.deepcopy(data)
        self.data = self.rotatedata.roatedown(self.data)
        self.data = self.calnewdata.cal(self.data)
        self.data = self.rotatedata.roateup(self.data)
        self.data = self.calnewdata.insertdata(self.data)
        return self.data


    def fingerleft(self,data):
        self.data = copy.deepcopy(data)
        self.data = self.rotatedata.roateright(self.data)
        self.data = self.calnewdata.cal(self.data)
        self.data = self.rotatedata.roateleft(self.data)
        self.data = self.calnewdata.insertdata(self.data)
        return self.data


    def fingerright(self,data):
        self.data = copy.deepcopy(data)
        self.data = self.rotatedata.roateleft(self.data)
        # NormalUtils.printlist(resdata)
        self.data = self.calnewdata.cal(self.data)
        # NormalUtils.printlist(resdata)
        self.data = self.rotatedata.roateright(self.data)
        # NormalUtils.printlist(resdata)
        self.data = self.calnewdata.insertdata(self.data)
        return self.data


# data = [[1, 2, 0, 0],
#         [1, 6, 0, 2],
#         [0, 0, 8, 0],
#         [0, 0, 0, 8]]
# NormalUtils.printlist(fingerright(data))
