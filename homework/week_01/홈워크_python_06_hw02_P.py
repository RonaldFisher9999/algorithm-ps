# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

array = ['eatt','tea','tan','tate','nat','bat']

anagram = [[array[0]]]
print(anagram)
n = len(array)
for i in range(1, n) :
    for group in anagram :
        if sorted(array[i]) == sorted(group[0]) :
            group.append(array[i])
            break
    else :
        anagram.append([array[i]])

print(anagram)