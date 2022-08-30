class OS:
    def __init__(self,size,method):
        self.size=size
        self.method=method
        self.fullArray=[]
        self.emptyArray=[[0,self.size]]
    def fit(self,programSize,programName):
        if(programSize > self.size):
            print("Program Size is larger than OS..")
            return
        for i in self.fullArray:
            if(i[1]==programName):
                print("There is a collision in the name please choose a different name...")
                return
        check =self.calculateAndPlaceLocation(programSize,programName)
        self.fullArray.sort()
    def deleteProgram(self,programName):
        available=False
        for i in self.fullArray:
            if(i[1]==programName):
                
                startingLocation=i[0]
                programSize=i[2]
                endingLocation=startingLocation + i[2]
                self.fullArray.remove(i)
                hit=False
                for j in self.emptyArray:
                    startingEdge=j[0]
                    endingEdge=startingEdge+j[1]
                    if(startingLocation==endingEdge):
                        j[1]=j[1]+programSize
                        hit=True
                    if(endingLocation==startingEdge and hit!=True):
                        j[0]=j[0]-programSize
                        j[1]=j[1]+programSize
                        hit=True
                if(hit==False):
                    self.emptyArray.append([startingLocation,programSize])
                    self.emptyArray.sort()
                
                if(hit==True):
                    #self.printArrays()
                    self.checkCollision()
                available=True
                break
        if(available==False):
            print(f"There is no program named as {programName}.")
            return
        
        return
    def checkCollision(self):
        tempArray=self.emptyArray
        for i in range(len(tempArray)-1):
            if(tempArray[i][0]+tempArray[i][1]==tempArray[i+1][0]):
                self.emptyArray[i+1][0]=tempArray[i][0]
                self.emptyArray[i+1][1]=tempArray[i][1]+tempArray[i+1][1]
                self.emptyArray.remove(tempArray[i])
    def compaction(self):
        tempArray=self.fullArray.copy()
        for i in tempArray:
            programSize=i[2]
            programName=i[1]
            self.deleteProgram(programName)
            self.calculateAndPlaceLocation(programSize,programName)
        self.fullArray.sort()
        return
    def calculateAndPlaceLocation(self,programSize,programName):
        emptyLocations=list()
        worstLocation=None
        worstEmptySize=None
        bestLocation=None
        bestEmptySize=None
        firstLocation=None
        location=None
        available=False
        for i in range(len(self.emptyArray)):
            if(self.emptyArray[i][1]>= programSize):
                emptyLocations.append([i,self.emptyArray[i][1]])#[0,20] [25,10]
                available=True        

        if(available==False):
            print("There is no possible location. Please do compaction..")
            return False
        if(self.method == "F"):
            firstLocation=emptyLocations[0][0]
            location = firstLocation
        if(self.method == "B"):
            bestLocation=emptyLocations[0][0]
            bestEmptySize=emptyLocations[0][1]
            for i in emptyLocations:
                if(bestEmptySize>i[1]):
                    bestEmptySize=i[1]
                    bestLocation=i[0]
            location = bestLocation
        if(self.method == "W"):
            worstLocation=emptyLocations[0][0]
            worstEmptySize=emptyLocations[0][1]
            for i in emptyLocations:
                if(worstEmptySize<i[1]):
                    worstEmptySize=i[1]
                    worstLocation=i[0]
            location = worstLocation
        self.fullArray.append([self.emptyArray[location][0],programName,programSize])
        self.emptyArray[location][0]=self.emptyArray[location][0]+programSize
        self.emptyArray[location][1]=self.emptyArray[location][1]-programSize
        tempArray=self.emptyArray.copy()
        if(self.emptyArray[location][1]==0):
            for i in range(len(self.emptyArray)):
                print(i)
                if(self.emptyArray[i][1]==0):
                    tempArray.remove(self.emptyArray[i])
        self.emptyArray=tempArray
        return True
    def printArrays(self):
        indexEmpty=0
        indexProgram=0
        tempArray=self.emptyArray + self.fullArray
        tempArray.sort()
        for i in tempArray:
            if(len(i)==3):
                print("{:>3}-{:>3} : {}".format(i[0],i[0]+i[2],i[1]))
            else:
                print("{:>3}-{:>3} : Empty".format(i[0],i[0]+i[1]))