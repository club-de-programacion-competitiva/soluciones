# Alternativa: crear un diccionrio que guarde cada resultado,
# y en cada iteración verificar si el valor ya existe, para evitar un ciclo infinito

def convert(gold):
    if (int(gold / 2) + int(gold / 3) + int(gold / 4)) <= gold:
        return gold
    elif (int(gold / 2) + int(gold / 3) + int(gold / 4)) > gold:
        return (convert((int(gold / 2)) + convert(int(gold / 3)) + convert(int(gold / 4))))
    #return max(gold, convert((int(gold / 2)) + convert(int(gold / 3)) + convert(int(gold / 4))))

nums = []
for i in range(10):
    try:
        num = int(input())
    except:
        break
    print(convert(num))