from typing import list

## Hashmap 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}                         # 이전에 본 숫자와 인덱스를 저장할 딕셔너리

        for i, n in enumerate(nums):         # 인덱스(i)와 값(n)을 동시에 꺼내어 반복
            diff = target - n                # 현재 숫자 n의 짝꿍(diff)을 계산
            
            if diff in prevMap:              # 만약 짝꿍이 이미 딕셔너리에 들어있다면?
                return [prevMap[diff], i]    # 짝꿍의 인덱스와 현재 인덱스를 리턴
            
            prevMap[n] = i                   # 짝꿍이 없으면 나중에 쓰이도록 현재 정보를 저장

# Test
if __name__ == "__main__":
    sol = Solution()                         # 1. 기계(객체) 생성
    print(sol.twoSum([2, 7, 11, 15], 9))     # 2. 기계를 사용해서 실제 문제 풀기