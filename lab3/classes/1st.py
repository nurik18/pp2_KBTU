class IOStream:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = str(input("Enter a string: "))

    def printString(self):
        print(self.text.upper())

obj = IOStream()

obj.getString()
obj.printString()