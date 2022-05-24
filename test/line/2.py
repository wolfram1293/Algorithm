import sys

X = int(input())
if X == 0:
    N, M, S, T = map(int, input().split())
else:
    N, M, S, T, K = map(int, input().split())

drink_list = list(input().split())
input_list = []
while True:
    try:
        s = input().split()
        if s[0] == "complete:":
            input_list.append([s[0], int(s[1])])
        else:
            input_list.append([s[0], s[1], s[2], s[3]]) 

    except EOFError:
        break

working = [[] for i in range(M)]
size = {"S": 300, "M":500, "L":700}
done = [0] * len(input_list)
i = 0
hold = -1
while True:
    if i > len(input_list) - 1:
        break
    if done[i]:
        i += 1
        continue

    s = input_list[i]
    if s[0] == "complete:":
        print("serve to:", *working[s[1]-1])
        working[s[1]-1] = []
        done[i] = 1
        if hold != -1:
            i = hold
            hold = -1
            continue

    else:
        if not s[1] in drink_list:
            print("ERROR: item named " + s[1] + " does not exist.")
            done[i] = 1
            continue
            
        if s[0] in working[0]: #dfdf
            print("ERROR: reference number duplicates.")
            done[i] = 1
            continue

        current_m = -1
        for j in range(len(working)):
            if len(working[j]) == 0:
                current_m = j
                break
        if current_m != -1:
            amount = 0
            for j in range(i, len(input_list)):
                s2 = input_list[j]
                if s2[0] != "complete:":
                    if s2[1] == s[1]:
                        if s2[0] in working[current_m]:
                            continue
                        if amount + size[s2[2]] <= S:
                            amount += size[s2[2]]
                            done[j] = 1
                            working[current_m].append(s2[0])
                else:
                    if s2[1] == current_m + 1:
                        print("make:", current_m + 1, s[1], amount)
                        break
        
        else:
            if hold == -1:
                hold = i

    i += 1
    '''drink_listは対応するドリンクの名前を格納するリスト
workingはそれぞれのマシンがどの注文番号を処理しているかを格納するリスト
doneは各入力を処理したかを格納するリスト
while文の中では基本的に注文を順番に処理し、マシンがいっぱいで処理しきれない場合のみ、スキップした注文へ戻る。
マシンが空いている場合、最初に受けた注文と同じドリンクを作れるだけ作るよう指示する。
ドリンク作成が完了した報告があった場合は、workingから注文番号を取り出して完了報告をする。
マシンがいっぱいで処理しきれなかった場合は完了報告後、スキップした注文へ戻り処理をする。'''