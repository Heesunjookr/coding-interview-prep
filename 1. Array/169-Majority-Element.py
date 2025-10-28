from typing import List

class Solution:
	def majorityElement_sorting(self, nums: List[int]) -> int:
		n = len(nums)
		nums.sort() #시간 복잡도: n*logn
		return nums[n//2] #정렬된 배열의 중앙 인덱스에 접근 = 나눗셈 결과의 소수점을 버리고 몫만 취합
											#다수결 요소 = 항상 중앙에 위치
# 시간 복잡도: O(n log n)
# 공간 복잡도: O(1) (파이썬의 Timsort는 보통 O(n) 공간을 사용하지만,

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counts = {}
#         n = len(nums)
#         threshold = n // 2
        
#         for num in nums:  # O(n) 시간 복잡도
#             counts[num] = counts.get(num, 0) + 1 # 딕셔너리 삽입/접근은 평균 O(1)
            
#         for num, count in counts.items(): # O(n) 시간 복잡도
#             if count > threshold:
#                 return num
                
#         return -1

# # 시간 복잡도: O(n)
# # 공간 복잡도: O(n) (딕셔너리 저장을 위한 추가 공간)

# class Solution:
#     def majorityElement_BoyerMoore(self, nums: List[int]) -> int:
#         candidate = 0  # 다수결 요소 후보
#         count = 0      # 후보의 득표수

#         for num in nums:  # O(n) 시간 복잡도
#             if count == 0:  # Count가 0이면, 새로운 후보 지정
#                 candidate = num
#                 count = 1
            
#             elif num == candidate: # 후보와 같으면 Count 증가 (투표)
#                 count += 1
                
#             else:  # 후보와 다르면 Count 감소 (상쇄)
#                 count -= 1
        
#         return candidate  # 최종 후보가 정답
        
# # 시간 복잡도: O(n)
# # 공간 복잡도: O(1) (상수 개수의 변수만 사용)