import util.NormalUtils


def cal(data):
    #print("cal",data.__str__())
    resdata = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    resdata[0] = data[0]
    for idx in range(0, 4, 1):

        i = 0
        j = 1
        while i < 4 and j < 4:
            #print(j,idx)
            if data[j][idx] == 0:
                j = j + 1
            elif data[i][idx] == 0:
                resdata[i][idx] = data[j][idx]
                data[j][idx] = 0
                j = j + 1
            elif data[i][idx] == data[j][idx]:
                resdata[i][idx] = data[i][idx] + data[j][idx]
                data[j][idx] = 0
                i = i + 1
                j = j + 1
            else:
                resdata[i][idx] = data[i][idx]
                resdata[i + 1][idx] = data[j][idx]
                data[j][idx] = 0
                i = i + 2
                j = j + 1
    # print(resdata.__str__())
    return resdata


def insertdata(data:list):
    candidatenum = [2, 4, 8]
    zeronum = util.NormalUtils.countzero(data)
    candidatenumidx = util.NormalUtils.getintrandom(0, 2)
    newidx = util.NormalUtils.getintrandom(1, zeronum)
    posx, posy = util.NormalUtils.getposition(data, newidx)
    print(posx, posy, candidatenum[candidatenumidx], zeronum, newidx)
    data[posx][posy] = candidatenum[candidatenumidx]
    return data


if __name__ == '__main__':
    data = [[1, 2, 0, 0],
            [1, 6, 0, 2],
            [0, 0, 8, 0],
            [0, 0, 0, 8]]

    newdata = cal(data)
    print(newdata.__str__())