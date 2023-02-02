import sys
sys.stdin = open("input.txt")

def counts(arr) :
    cnt_arr = [0] * 10
    for num in arr :
        cnt_arr[num] += 1
    return cnt_arr

for t in range(1, int(input())+1) :
    cnt_arr = counts(map(int, list(input())))
    check = 2
    run_trip = 0
    while check > 0 :
        for i in range(10) :
            if cnt_arr[i] == 3 :
                cnt_arr[i] -= 3
                check -= 1
                run_trip += 1
                break
            if cnt_arr[i] and cnt_arr[i+1] and cnt_arr[i+2] :
                cnt_arr[i] -= 1
                cnt_arr[i+1] -= 1
                cnt_arr[i+2] -= 1
                check -= 1
                run_trip += 1
                break
        else :
            check -= 1
        answer = 0
        if run_trip == 2 :
            answer = 1
    print(f"#{t} {answer}")