import util.NormalUtils

class CalNewData:
    def __init__(self):
        self.normalutils = util.NormalUtils.NormalUtils()

    def cal(self,data):
        #print("cal",data.__str__())
        for idx in range(0, 4, 1):

            i = 0
            j = 1
            while i < 4 and j < 4:
                #print(j,idx)
                if data[j][idx] == 0:
                    j = j + 1
                elif data[i][idx] == 0:
                    data[i][idx] = data[j][idx]
                    data[j][idx] = 0
                    j = j + 1
                elif data[i][idx] == data[j][idx]:
                    data[i][idx] = data[i][idx] + data[j][idx]
                    data[j][idx] = 0
                    i = i + 1
                    j = j + 1
                else:
                    if j == i + 1:
                        i = j
                        j = j + 1
                    else:
                        i = i+1
                        data[i][idx] = data[j][idx]
                        data[j][idx] = 0
                        j = j + 1
                print("i:",i,"j:",j)
        # print(resdata.__str__())
        return data


    def insertdata(self,data:list):
        candidatenum = [2, 4, 8]
        zeronum = self.normalutils.countzero(data)
        candidatenumidx = self.normalutils.getintrandom(0, 2)
        if zeronum == 0:
            return data
        newidx = self.normalutils.getintrandom(1, zeronum)
        posx, posy = self.normalutils.getposition(data, newidx)
        print(posx, posy, candidatenum[candidatenumidx], zeronum, newidx)
        data[posx][posy] = candidatenum[candidatenumidx]
        return data


if __name__ == '__main__':
    data = [[1, 2, 0, 0],
            [1, 6, 0, 2],
            [0, 0, 8, 0],
            [0, 0, 0, 8]]
    c = CalNewData()
    newdata = c.cal(data)
    print(newdata.__str__())