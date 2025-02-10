from config import test_cases

# 내 풀이
# def solution(participant: list, completion: list) -> str:
#     # len(participant) - len(completion) = 1

#     # 완주하지 못한 사람 text로 알려주기

#     # 동명이인 어떻게 처리할 것인가
#     # uncompletion = set(participant) - set(completion)
#     # uncompletion_str = ",".join(uncompletion)
#     # answer = f"{uncompletion_str}는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다."

#     # dictionary로 처리할까?
#     participant_dict = {}
#     for name in participant:
#         cnt = participant_dict.get(name, 0)
#         cnt += 1
#         participant_dict[name] = cnt

#     completion_dict = {}
#     for name in completion:
#         cnt = completion_dict.get(name, 0)
#         cnt += 1
#         completion_dict[name] = cnt

#     for name, cnt in participant_dict.items():
#         completion_cnt = completion_dict.get(name, 0)

#         count_different = cnt - completion_cnt
#         if count_different == 0:
#             continue
#         else:
#             return name


# gpt 풀이

# from collections import Counter


# def solution(participant: list, completion: list) -> str:
#     participant_count = Counter(participant)
#     completion_count = Counter(completion)

#     for name in participant_count:
#         if participant_count[name] != completion_count[name]:  # 완주하지 못한 사람이 있으면 반환
#             return name


def solution(participant: list, completion: list) -> str:
    result = 0  # 모든 이름의 해시 값을 저장할 변수

    # 참가자의 해시 값을 모두 더함
    for name in participant:
        result += hash(name)

    # 완주한 사람들의 해시 값을 뺌
    for name in completion:
        result -= hash(name)

    # 남은 해시 값과 일치하는 이름 찾기
    for name in participant:
        if hash(name) == result:  # 남은 해시 값과 같은 이름 찾기
            return name


if __name__ == "__main__":
    for test_case in test_cases:
        participant = test_case["participant"]
        completion = test_case["completion"]
        correct_return = test_case["result"]
        predicted_return = solution(participant, completion)

        print(f"participant: {participant}")
        print(f"completion : {completion}")
        print(f"correct result : {correct_return}")
        print(f"result of solution : {predicted_return}")
        print(f"Is Success : {correct_return == predicted_return}")
        print("-" * 30)
