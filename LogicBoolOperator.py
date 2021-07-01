import random, Log

class LogicBoolOperator:
    def __init__(self, complexity):
        self.condition = ""
        
        if complexity == 0:
            self.condition = self.GenerateSimpleCondition()
        elif complexity == 1:
            self.condition = self.GenerateHardCondition()
        elif complexity == 2:
            self.condition = self.GenerateVeryHardCondition()
    
    def GenerateVeryHardCondition(self):
            ch = random.randint(0,2)
            
            if ch == 0:
                return f"not ({self.GenerateHardCondition()})"
            elif ch == 1:
                return f"({self.GenerateHardCondition()}) and ({self.GenerateHardCondition()})"
            elif ch == 2:
                return f"({self.GenerateHardCondition()}) or ({self.GenerateHardCondition()})"
        
    def GenerateHardCondition(self):
            ch = random.randint(0,2)
            
            if ch == 0:
                return f"not ({self.GenerateSimpleCondition()})"
            elif ch == 1:
                return f"({self.GenerateSimpleCondition()}) and ({self.GenerateSimpleCondition()})"
            elif ch == 2:
                return f"({self.GenerateSimpleCondition()}) or ({self.GenerateSimpleCondition()})"
                
    def GenerateSimpleCondition(self):
            ch = random.randint(0,2)
            
            if ch == 0:
                return f"not ({self.GenerateCondition()})"
            elif ch == 1:
                return f"({self.GenerateCondition()}) and ({self.GenerateCondition()})"
            elif ch == 2:
                return f"({self.GenerateCondition()}) or ({self.GenerateCondition()})"     
                
    def GenerateCondition(self):
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        value = random.choice(["<",">","!=","==",">=","<="])
        
        return f"{a}{value}{b}"

    def Сheck(self):
        print(f"Какой ответ получится в результате вычисления {self.condition} = ? (True или False)")
        value = input("> ")

        globalDict = {"answerComp": 0}
        
        try:

            exec(f"answerComp = {self.condition}",globalDict)
            
            if value == "False":
                value = False
            elif value == "True":
                value = True
            else:
                raise NameError()
                

            if bool(value) == globalDict["answerComp"]:
                print("Отлично, твое решение подходит!")
                return True
            else:
                raise NameError()
        except:
            print("Ошибка, попробуй подумать!")
            Log.Logger(f"ERROR = {self.condition} = {value}, correct = {globalDict['answerComp']}", "Log.txt")
            return False