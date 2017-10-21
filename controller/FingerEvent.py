from controller import CalNewData, RotateData
from util import NormalUtils

def fingerup(data):
    resdata = CalNewData.cal(data)
    return CalNewData.insertdata(resdata)


def fingerdown(data):
    resdata = RotateData.roatedown(data)
    resdata = CalNewData.cal(resdata)
    resdata = RotateData.roateup(resdata)
    resdata = CalNewData.insertdata(resdata)
    return resdata


def fingerleft(data):
    resdata = RotateData.roateright(data)
    resdata = CalNewData.cal(resdata)
    resdata = RotateData.roateleft(resdata)
    resdata = CalNewData.insertdata(resdata)
    return resdata


def fingerright(data):
    resdata = RotateData.roateleft(data)
    NormalUtils.printlist(resdata)
    resdata = CalNewData.cal(resdata)
    NormalUtils.printlist(resdata)
    resdata = RotateData.roateright(resdata)
    NormalUtils.printlist(resdata)
    resdata = CalNewData.insertdata(resdata)
    return resdata


data = [[1, 2, 0, 0],
        [1, 6, 0, 2],
        [0, 0, 8, 0],
        [0, 0, 0, 8]]
NormalUtils.printlist(fingerright(data))
