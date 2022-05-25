def find_anagram(l):
    group = {} # 辞書
    for v in l:
        sorted_v = ''.join(sorted(v)) # アルファベット順に並び替え
        if sorted_v in group.keys(): # それをキーにして辞書を作る
            group[sorted_v].append(v)
        else:
            group[sorted_v] = [v]
    return group 
