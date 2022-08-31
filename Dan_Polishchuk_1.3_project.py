import math

print("Завдання 1.")
print("Введіть ваше число :")
number = int(input())
def func(number):
    print((number*2)+4)
print("Ваш результат = ")
func(number)
print("Завдання 2.")
print("Введіть ваше слово :")
word = input()
def func(word):
    print(word + "!")
func(word)
print("Завдання 3.")
print("Введіть ваше число :")
number = input()
def func(number):
    print("Дякую!")
    return number
func(number)
print("Завдання 4.")
while True:
    enteredSymbol = input("Знак операції(+, -, *, /, **) :")
    if enteredSymbol == "exit" :
        break
    print("Введіть перше число")
    number1 = int(input())
    print("Введіть друге число ")
    number2 = int(input())
    if enteredSymbol == "+":
        print(number1 + number2)
    elif enteredSymbol == "-":
        print(number1 - number2)
    elif enteredSymbol == "*":
        print(number1 * number2)
    elif enteredSymbol == "/":
        print(number1 / number2)
    elif enteredSymbol == "**":
        print(number1 ** number2)
print("Завдання 5.")
print("Привіт світ !\n\tПривіт знову!\n\t\tМені подобається це друкувати.\n\t\t\tYpa!\n\t\t\t\t Я друкую!\n\t\t\t\t\tЦе весело!\n\t\t\t\t\t\tЦе заняття як 'диво' .\n\t\t\t\t\t\t\t" 'Я б "сказав", що це круто!' )
print("Завдання 6.")
print("Варіант 3)")
while True:
    procedure = input("Оберіть операцію (+, -, *, /, **,Exp, tan, Mod, n! ) :")
    if procedure == "exit" :
        break
    print("Введіть число")
    number1 = int(input())
    if procedure == "Exp" :
        print(math.exp(number1))
    elif procedure == "tan" :
        print(math.tan(number1))
    elif procedure == "Mod" :
        print(math.modf(number1))
    elif procedure == "n!" :
        print(math.factorial(number1))
    elif procedure == "+":
        print("Введіть друге число ")
        number2 = int(input())
        print(number1 + number2)
    elif procedure == "-":
        print(number1 - number2)
    elif procedure == "*":
        print("Введіть друге число ")
        number2 = int(input())
        print(number1 * number2)
    elif procedure == "/":
        print("Введіть друге число ")
        number2 = int(input())
        print(number1 / number2)
    elif procedure == "**":
        print("Введіть друге число ")
        number2 = int(input())
        print(number1 ** number2)
