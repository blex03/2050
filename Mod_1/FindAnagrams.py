from WordCompare import word_compare

def find_anagrams(word_lst):

    final_str = ""

    for i in word_lst: #Each word will iterate through the whole list of words to find anagrams
        new_lst = []

        if word_lst.index(i) != 0:
            final_str += "\n"

        final_str += i + ": "

        for j in word_lst:
            if word_compare(i, j) == "Anagram" and i != j:
                new_lst.append(j)

        final_str += str(new_lst)

    return final_str


words = ["listen", "silent", "triangle", "integral", "race", "care", "doctor", "stone", "fire", "force", "sorcery", "fight"]
expected_result = "listen: ['silent']\nsilent: ['listen']\ntriangle: ['integral']\nintegral: ['triangle']\nrace: ['care']\ncare: ['race']\ndoctor: []\nstone: []\nfire: []\nforce: []\nsorcery: []\nfight: []"
assert find_anagrams(words) == expected_result


