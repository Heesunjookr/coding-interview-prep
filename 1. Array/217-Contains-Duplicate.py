from typing import List

### set 집합 자료구조 사용
# Set (집합)**이라는 아주 특별한 주머니가 있습니다. 이 주머니의 특징은 **"똑같은 걸 두 번 넣어도 하나만 남는다(중복 허용 안 함)"**는 거예요.
# 배열을 집합으로 바꾼다. (set(nums))
# 만약 중복이 있었다면, 집합의 크기는 원래 배열보다 줄어들었을 것이다.
# 두 길이를 비교한다!

# class Solution:
#     def containsDuplicate_Set(self, nums: List[int]) -> bool:
#         # set(nums)로 중복을 제거한 크기와 원래 리스트의 크기를 비교함
#         return len(set(nums)) != len(nums)      # 크기가 다르면 중복이 있다는 뜻(True 반환)
# # 시간 복잡도: O(N)
# # 공간 복잡도: O(N)

## 해시 셋(Hash Set)을 이용한 순차 확인
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}                           # 처음엔 비어있는 기록장

        for n in nums:                          # 숫자를 하나씩 꺼내서...
            if n in hash_map:                   # 1. 기록장을 먼저 확인한다 (처음엔 당연히 없음)
                return True                     # 2. 있다면? "이미 봤던 거네!" 중복 리턴
            
            hash_map[n] = True                  # 3. 없다면? "처음 보는 거네. 기록장에 적자."
            
        return False                            # 끝까지 다 돌았는데 중복이 없으면 False
        
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)