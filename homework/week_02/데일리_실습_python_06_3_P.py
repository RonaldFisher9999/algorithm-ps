def count_vowels(string) :
    vowels = 'aeiou'
    string = string.lower()
    answer = 0
    for s in string :
        if s in vowels :
            answer += 1
    return answer

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3