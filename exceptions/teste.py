def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('entre com um numero diferente de 0')
    except TypeError:
        print('Somente numeros')
    finally:
        print('Acabou a divisão')

print(div(4, 'a'))
