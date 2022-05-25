def find_anagram(l):
    group = {}
    for v in l:
        sorted_v = ''.join(sorted(v))
        if sorted_v in group.keys():
            group[sorted_v].append(v)
        else:
            group[sorted_v] = [v]
    return group    
    

def countSentences(wordSet, sentences):
    # Write your code here
    N = len(wordSet)
    group = find_anagram(wordSet)
    ans = []
    for s in sentences:
        cnt = 1
        for w in s.split():
            sorted_w = ''.join(sorted(w))
            cnt *= len(group[sorted_w])
        ans.append(cnt)    
    return ans

'''
sentencesの中の各単語をwordSet中の単語がアナグラムになる場合は入れ替え、その組み合わせの数を求める
sortでアナグラムを判定し、辞書に入れる
それを元にsentencesの中の各単語のアナグラム数を掛けたものが答え
'''