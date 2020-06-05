fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def count_fruit(name):
    count = 0
    for fruit in fruits:
        if (fruit == name):
            count += 1
    return count

result = count_fruit('배')
print(result)