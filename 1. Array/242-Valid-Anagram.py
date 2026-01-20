### Dictionary을 이용한 풀이
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):                     # 길이가 다르면 아나그램 아님
			return False
		
		countS, countT = {}, {}                  # 빈 해시맵 생성
		for i in range(len(s)):
			countS[s[i]] = 1 + countS.get(s[i], 0) # 해시맵에 각 글자의 개수 저장
			countT[t[i]] = 1 + countT.get(t[i], 0) # 해시맵에 각 글자의 개수 저장
		return countS == countT                  # 두 해시맵이 같은지 비교
		

# ## Counter Object를 이용한 풀이
# from collections import Counter              # 카운터 도구 가져오기

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)      # 두 단어의 글자 구성(해시맵)이 같은지 비교

# ## Sorting을 이용한 풀이
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)        # "abc" == "abc" 인지 확인