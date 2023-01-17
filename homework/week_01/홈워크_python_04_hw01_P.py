words = ["round" , "dream", "magnet" , "tweet", "tweet", "trick", "kiwi"]

n = len(words)
for i in range(n) :
    if words[i] == "done" :
        print("Game finished")
        break
    if i >= 1 :
        if words[i] in words[:i] :
            print(f"Player {i + 1} lost")
            break
        if words[i][0] != words[i - 1][-1] :
            print(f"Player {i + 1} lost")
            break
else :
    print("Success")