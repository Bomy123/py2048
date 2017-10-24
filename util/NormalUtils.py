import random
class NormalUtils:

    def getintrandom(self,start:int,end:int):
        # print(start,end,"getintrandom")
        r = random.Random()
        return r.randint(start, end)

    def countzero(self,data:list):
        count = 0
        try:
            if(type(data[0]) == list):
                for line in data:
                    count = count + line.count(0)
            else:
                count = data.count(0)
        except Exception as e:
            print(e.__str__())
        return count


    def getposition(self,data: list, index):
        x = 0
        y = 0
        count =self.countzero(data)
        if index > count:
            print("data error:out of index")
            print(count)
        else:
            for line in data:
                if index > line.count(0):
                    x = x + 1
                    index = index - line.count(0)
                else:
                    i = 0
                    for y in range(0, 4):
                        if line[y] == 0:
                            i = i + 1
                        if i >= index:
                            break
                    break

        return x, y

    def printlist(self,data:list):
        print("#############################################")
        for line in range(0, 4):
            print(data[line])
        print("#############################################")