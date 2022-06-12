# sortでアナグラムを判定し、辞書に入れる

def group_anagrams(l):
    group = {}
    for v in l:
        sorted_v = ''.join(sorted(v))
        if sorted_v in group.keys():
            group[sorted_v].append(v)
        else:
            group[sorted_v] = [v]
    return group
