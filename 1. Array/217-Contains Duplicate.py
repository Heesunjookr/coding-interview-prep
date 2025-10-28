from typing import List

# class Solution:
#     def containsDuplicate_BruteForce(self, nums: List[int]) -> bool:
#         n = len(nums)
        
#         for i in range(n): # O(N^2) 시간 복잡도: 이중 반복문
#             for j in range(i + 1, n): # 모든 쌍을 비교
#                 if nums[i] == nums[j]:
#                     return True # 중복 발견 시 즉시 True 반환
                    
#         return False # 루프 종료 시 중복 없음
        
# # 시간 복잡도: O(N^2)
# # 공간 복잡도: O(1)



# class Solution:
#     def containsDuplicate_Sorting(self, nums: List[int]) -> bool:
#         nums.sort() # O(N log N) 시간 복잡도: 배열 정렬
#         n = len(nums)
        
#         for i in range(n - 1): # O(N) 시간 복잡도: 정렬된 배열을 한 번 순회
#             if nums[i] == nums[i + 1]: # 인접한 두 요소 비교
#                 return True            # 중복 발견 시 True 반환
            
#         return False # 루프 종료 시 중복 없음

# # 시간 복잡도: O(N log N)
# # 공간 복잡도: O(1) 또는 O(N) (정렬 방식에 따름)



# class Solution:
#     def containsDuplicate_HashSet(self, nums: List[int]) -> bool:
#         seen = set() # O(N) 공간 복잡도: 본 요소를 저장할 집합 생성
        
#         for num in nums: # O(N) 시간 복잡도: 배열을 한 번 순회
#             if num in seen: # 집합 검색은 평균 O(1)
#                 return True # 중복 발견 시 즉시 True 반환
#             seen.add(num)   # 중복이 아니면 집합에 추가 (평균 O(1))
            
#         return False # 루프 종료 시 중복 없음
        
# # 시간 복잡도: O(N)
# # 공간 복잡도: O(N)


class Solution:
    def containsDuplicate_HashMap(self, nums: List[int]) -> bool:
        #4. Hash Map
        d = {}
        for num in nums:
            if num in d and d[num] >= 1:
                return True
            d[num] = d.get(num, 0) + 1
        return False
        
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)