X = 10
Y: int = 20
Z: int = 30
M = 40
if X > 5 and Y < 25 and Z == 30 : #Щоб результат був True потрібно щоб виконувались всі умови
    print(True)
if X in range(20) or Y in range(15) or Z in range(100): #Щоб результат був True потрібно щоб виконувалась хоча б одна умова
    print(True)
if X == 5 or Y * 2 == 40 and Z / 3 == 10 : #Щоб результат був True: X=True АБО Y ТА Z = True
    print(True)
if X * 2 == 4 or Y // 2 == 10 and Z ** 2 == 900 or M / 4 == 10.0 :  #Щоб результат був True: X = True АБО Y ТА Z = True АБО M = True
    print(True)
if X == 234 and Y == 432 or Z == 30 and M == 40: #Щоб результат був True: X ТА Y = True АБО Z ТА M = True
    print(True)
if X == 10 and (Y == 20 or Z < 2 and M > 2): #Щоб результат був True: X =True ТА Y=True АБО Z ТА M =True
    print(True)