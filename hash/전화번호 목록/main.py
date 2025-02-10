from config import test_cases


# 내가 짠 코드
# def solution(phone_book: list) -> bool:
#     # 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
#     # 1 <= len(phone_book) <= 1000000
#     # 1 <= len(phone) <= 20
#     # 중복 x
#     def is_prefix(phone_1: str, phone_2: str) -> bool:
#         len_phone_1 = len(phone_1)
#         len_phone_2 = len(phone_2)

#         if len_phone_1 <= len_phone_2:
#             result = phone_2[:len_phone_1] == phone_1
#         else:
#             result = phone_1[:len_phone_2] == phone_2

#         return result

#     for i in range(len(phone_book)):
#         # 이 번호가 나머지 번호의 접두어인 경우가 있는가?
#         phone = phone_book[i]

#         rest_phone_book = []
#         rest_phone_book.extend(phone_book[:i])
#         rest_phone_book.extend(phone_book[i + 1 :])

#         for rest_phone in rest_phone_book:
#             result = is_prefix(phone, rest_phone)

#             if result is True:
#                 return False

#     return True


# gpt 답변
def solution(phone_book):
    phone_book.sort()  # 사전순 정렬

    for i in range(len(phone_book) - 1):
        # 앞 번호가 뒷 번호의 접두사인지 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


if __name__ == "__main__":
    for test_case in test_cases:
        phone_book = test_case["phone_book"]
        expected_return = test_case["return"]
        predicted_return = solution(phone_book)

        print(f"phone book : {phone_book}")
        print(f"expected return : {expected_return}")
        print(f"predicted return : {predicted_return}")
        print(f"is success : {expected_return == predicted_return}")
        print("-" * 50)
