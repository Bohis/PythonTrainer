import random, Log

class LogicSign:
    def __init__(self, minNum,maxNum):
        self.a = random.randint(minNum,maxNum)
        self.b = random.randint(minNum,maxNum)
        self.value = bool(random.randint(0,1))

    def Сheck(self):
        print(f"Какой знак сравнения нужно поставить между {self.a} и {self.b}, что бы получилось {self.value}?")
        value = input("> ")

        try:
            globalDict = {"answer": False}

            exec(f"answer = {self.a} {value} {self.b}",globalDict)

            if self.value == globalDict["answer"]:
                print("Отлично, твое решение подходит!")
                return True
            else:
                raise NameError()
        except:
            print("Ошибка, попробуй другой знак!")
            Log.Logger(f"ERROR = {self.a} {value} {self.b}, need = {self.value}", "Log.txt")
            return False



