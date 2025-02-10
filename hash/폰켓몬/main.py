from config import test_cases


# 내가 짠거
# in을 사용하니까 O(N^2)의 성능이 될 가능성이 있음
# def solution(nums):
#     pokemon_ids = []
#     for num in nums:
#         if num not in pokemon_ids and len(pokemon_ids) < len(nums) / 2:
#             pokemon_ids.append(num)

#     return len(pokemon_ids)


# gpt 답변
# O(N)
def solution(nums):
    return min(len(set(nums)), len(nums) // 2)


if __name__ == "__main__":
    for test_case in test_cases:
        nums = test_case["nums"]
        result = test_case["result"]
        print(f"nums : {nums}")
        print(f"result of solution : {solution(nums)}")
        print(f"result : {result}")
