from goto import with_goto

class Brain():
    buffer = []
    for i in range(30000):
        buffer.append(0)
    index = [0]
    minValue = 0
    maxValue = 255
    colvo = [0]
    code = []
    output = []
    whil = []
    ifWhil = [False]
    input = ""

    def __init__(self):
        pass


    def nextIndex(self):
        if self.index[0] < 30000:
            self.index[0] += 1
            if self.ifWhil[0] == False:
                self.code.append('>')
            else:
                if self.colvo[0] == 1:
                    self.whil.append(">")

    def prevIndex(self):
        if self.index[0] > 0:
            self.index[0] -= 1
            if self.ifWhil[0] == False:
                self.code.append('<')
            else:
                if self.colvo[0] == 1:
                    self.whil.append("<")

    def add(self):
        if self.buffer[self.index[0]] < self.maxValue:
            self.buffer[self.index[0]] += 1
        else:
            self.buffer[self.index[0]] = 0
        if self.ifWhil[0] == False:
                self.code.append('+')
        else:
            if self.colvo[0] == 1:
                self.whil.append("+")

    def remove(self):
        if self.buffer[self.index[0]] > self.minValue:
            self.buffer[self.index[0]] -= 1
        else:
            self.buffer[self.index[0]] = 255
        if self.ifWhil[0] == False:
                self.code.append('-')
        else:
            if self.colvo[0] == 1:
                self.whil.append("-")

    def read(self):
        self.input = input()
        self.buffer[self.index[0]] = ord(str(self.input[0]))
        if self.ifWhil[0] == False:
                self.code.append(',')
        else:
            if self.colvo[0] == 1:
                self.whil.append(",")

    def print(self):
        self.output.append(chr(self.buffer[self.index[0]]))
        print(''.join(self.output))
        if self.ifWhil[0] == False:
                self.code.append('.')
        else:
            if self.colvo[0] == 1:
                self.whil.append(".")

    def setValue(self, value):
        if value >= self.minValue and value <= self.maxValue:
            while self.buffer[self.index[0]] != value:
                if value > self.buffer[self.index[0]]:
                    Brain().add()
                elif value < self.buffer[self.index[0]]:
                    Brain().remove()

    @with_goto
    def whiled(self, type):
        def start(self):
            self.code.append('[')
            label .begin
    
        def end(self):
            self.code.append(']')
            if self.buffer[self.index[0]] == 0:
                goto .end
            label .end

        if type == "start":
            start()
        elif type == "end":
            end()




    def getCode(self):
        print(''.join(self.code))
