# 내가 푼 것

from config import inputs


def make_max_sum(n_list: list, m: int, k: int):
    # 가장 큰 수와 다음으로 큰 수 찾기
    max_number = 0
    max_index = 0
    for i, n in enumerate(n_list):
        if int(n) >= max_number:
            max_number = int(n)
            max_index = i

    max_2_number = 0
    # max_2_index = 0
    tmp_list = []
    tmp_list.extend(n_list[:max_index])
    tmp_list.extend(n_list[max_index + 1 :])
    for i, n in enumerate(tmp_list):
        if int(n) >= max_2_number:
            max_2_number = int(n)
            # max_2_index = i

    # 연속 k번씩 총 m번 더하기
    total_sum = 0
    k_cnt = 1
    i = 1
    while i <= m:
        if k_cnt <= k:
            total_sum += max_number
            # print(max_number, end=" ")
            k_cnt += 1
        else:
            total_sum += max_2_number
            # print(max_2_number, end=" ")
            k_cnt = 1
        i += 1

    return total_sum


if __name__ == "__main__":
    for input in inputs:
        first_line = input["first_line"]
        N, M, K = first_line.split(" ")
        second_line = input["second_line"]
        n_list = second_line.split(" ")

        print(make_max_sum(n_list=n_list, m=int(M), k=int(K)))
