from itertools import *

#Кубики и слово. На детских кубиках с шести сторон изображены буквы. Дан список
#слов, образующий словарь. Необходимо подсчитать сколько слов из словаря можно
#выложить их кубиков. Подсказка: Для каждого размещения кубиков сгенерировать
#размещения с повторениями.
#а) используя все кубики
#б) используя не все кубики

def find_word(cubes, word):
    def backtracking(cube, i): #рекурсивно проверяет соответствие букв на кубиках слову
        if i == len(word):
            return True #успешное совпадение букв
        if cube > 3:
            return False
        for k in range(6):
            if combination[cube][k] == word[i]: #куб == слово
                if backtracking(cube+1, i+1):
                    return True #Если i становится равным длине word, функция возвращает True

    for combination in permutations(cubes): #Размещение с повторениями
        if backtracking(0, 0): #Для каждой перестановки проверяется возможность составить слово
            return True
    return False


if __name__=='__main__':
    cube1 = ['a', 'b', 'c', 'd', 'e', 'f']
    cube2 = ['g', 'h', 'i', 'j', 'k', 'l']
    cube3 = ['m', 'n', 'o', 'p', 'r', 's']
    cube4 = ['t', 'u', 'v', 'w', 'x', 'y']
    cubes = [cube1, cube2, cube3, cube4]

    words = ['bug', 'home', 'word', 'key', 'door']
    for word in words:
        if find_word(cubes, word):
            print(f'Слово {word} можно сложить из кубиков.')
        else:
            print(f'Слово {word} нельзя сложить из кубиков.')