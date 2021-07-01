import random, Log

class LogicMath:
    def __init__(self, minNum,maxNum):
        self.operator = random.choice(["+","-","/","*"])
        self.a = random.randint(minNum,maxNum)
        self.b = random.randint(minNum,maxNum)
        
        if self.operator == "-" and self.b < 0:
            self.b = abs(self.b)
            
        if self.operator == "+" and self.b < 0:
            self.operator = "-"
            self.b = abs(self.b)
        
        if self.operator == "/" and self.b == 0:
            self.b = 2
            
        if self.operator == "/" and self.a % self.b != 0:
            self.a = self.a * self.b
            


    def Сheck(self):
        print(f"Какой ответ получится в результате вычисления {self.a} {self.operator} {self.b} = ?")
        value = input("> ")

        globalDict = {"answerComp": 0}
        
        try:

            exec(f"answerComp = {self.a} {self.operator} {self.b}",globalDict)

            if int(value) == globalDict["answerComp"]:
                print("Отлично, твое решение подходит!")
                return True
            else:
                raise NameError()
        except:
            print("Ошибка, попробуй подумать!")
            Log.Logger(f"ERROR = {self.a} {self.operator} {self.b} = {value}, correct = {globalDict['answerComp']}", "Log.txt")
            return False
        