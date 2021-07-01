from LogicSign import LogicSign
from LogicMath import LogicMath
from LogicBoolOperator import LogicBoolOperator

print("Привет! Это программа тренировки, правила такие:\nВыбираешь курс, отвечаешь на вопросы (их 10 за 1 раз).\nОтвет верный +1 бал, неверный -1.\nВ начале игры 10 очков. Если очки станут равны 0 - ты проиграл.\n\tУдачи")
print()
gameOver = False
point = 10



while not gameOver:
    
    print("Выбери курс:")
    print("\t0. Математические операции;")
    print("\t1. Логические операции операции;")
    print("\t2. And, or, not;")
    print("\t3. Выход.")

    answer = input("> ")
    

    if answer == "0":
        for _ in range(0,10):  
            x = LogicMath(-(10+point),10+point)

            if x.Сheck():
                point+=1
            else:
                if point > 0:
                    point-=1
        print(f"У тебя очков {point}")
    elif answer == "1":
        for _ in range(0,10):  
            x = LogicSign(-(10+point),10+point)

            if x.Сheck():
                point+=1
            else:
                if point > 0:
                    point-=1
        print(f"У тебя очков {point}")
    elif answer == "2":
       print("Выбери сложность: 0, 1, 2 (напиши число в ответ)")
       answerCon = input("> ")
       
       if answerCon == "0" or answerCon == "1" or answerCon == "2":
            for _ in range(0,10):  
                x = LogicBoolOperator(int(answerCon))

                if x.Сheck():
                    point+=1
                else:
                    if point > 0:
                        point-=1
            print(f"У тебя очков {point}")
    else:
        print("Ошибка, выбери что нибудь другое")
        
    if point == 0:
        gameOver = True
        print("Ты проиграл(")
        break
else:
    print(f"Спасибо за игру, у тебя получилось - {point} очков")

print("Что бы закончить нажми enter..."); input()