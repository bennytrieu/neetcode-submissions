class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        word = []
        for i in range(len(strs)):
            word.append(str(len(strs[i])))
            word.append("#")
            word.append(strs[i])
        return "".join(word)

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        j = 0
        num = 0
        while i < len(s):
            while s[j] != "#":
                j+=1
            num = int(s[i:j])
            i = j + 1
            j = i + num
            ans.append(s[i:j])
            i = j
        print(ans)
        return ans
