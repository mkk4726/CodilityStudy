Codility 테스트를 준비 중이라면, Hash에 대한 개념을 정확히 이해하는 것이 중요합니다.

1. Hash란?

Hash(해시)는 데이터를 고정된 크기의 값으로 변환하는 함수 또는 데이터 구조를 의미합니다. 보통 **해시 함수(hash function)**와 **해시 테이블(hash table)**을 함께 사용하여 빠른 데이터 검색과 저장이 가능하게 합니다.

2. 해시 함수 (Hash Function)

해시 함수는 입력값을 고정된 길이의 해시 값으로 변환하는 함수입니다. 예를 들어, hash("Codility")라는 해시 함수를 적용하면 특정한 정수 값이 생성됩니다.

좋은 해시 함수는 다음과 같은 특징을 가집니다:
	•	고유성(Uniqueness): 서로 다른 입력값은 가능한 한 다른 해시 값을 가져야 합니다.
	•	빠른 계산(Fast Computation): 해시 값은 빠르게 계산될 수 있어야 합니다.
	•	균등 분포(Uniform Distribution): 해시 값이 가능한 한 고르게 분포되어야 충돌(collision)이 적습니다.

3. 해시 테이블 (Hash Table)

해시 테이블은 키-값(Key-Value) 쌍을 저장하는 자료구조로, 키를 해시 함수로 변환하여 값을 저장하거나 검색할 수 있습니다.
대표적인 구현 방법은 딕셔너리(Dictionary) 또는 **셋(Set)**을 사용하는 것입니다.

해시 테이블의 장점
	•	빠른 검색(O(1)): 리스트(배열)에서 원하는 데이터를 찾으려면 O(n), 정렬된 배열에서 이진 탐색을 하면 O(log n)이지만, 해시 테이블을 사용하면 O(1)의 시간 복잡도로 검색이 가능합니다.
	•	중복 확인이 용이함: set()을 이용하면 간단하게 중복을 제거할 수 있습니다.

해시 테이블의 예시 (Python)

# Dictionary (Key-Value 저장)
hash_table = {}
hash_table["apple"] = 3
hash_table["banana"] = 5

print(hash_table["apple"])  # 3

# Set (중복 없는 자료 저장)
hash_set = set()
hash_set.add("apple")
hash_set.add("banana")
hash_set.add("apple")  # 중복 추가 시 무시됨

print(hash_set)  # {'apple', 'banana'}

4. 해시 충돌 (Hash Collision)

같은 해시 값을 가지는 두 개 이상의 키가 존재하는 경우를 “해시 충돌”이라고 합니다.
이를 해결하는 대표적인 방법:
	1.	체이닝(Chaining) - 같은 해시 값을 가지는 데이터를 연결 리스트로 저장
	2.	개방 주소법(Open Addressing) - 빈 슬롯을 찾아 데이터를 저장

5. Codility에서 해시를 활용한 문제 예시

Codility에서는 해시 테이블을 활용하여 중복 제거, 빈도수 계산, 빠른 검색 등의 문제를 해결해야 하는 경우가 많습니다.

예제 1: 배열에서 중복 없는 값 찾기

	문제: 주어진 배열에서 한 번만 등장하는 요소를 찾으세요.
(단, O(n) 시간 복잡도로 해결해야 합니다.)

def find_unique(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1  # 등장 횟수 카운팅

    for num in arr:
        if count[num] == 1:
            return num  # 한 번만 등장한 요소 반환

    return -1  # 없으면 -1 반환

print(find_unique([4, 3, 2, 4, 2, 5, 3]))  # 5

예제 2: 두 배열 간 공통 요소 찾기

	문제: 두 개의 배열 A와 B가 주어졌을 때, 공통으로 포함된 숫자를 리스트로 반환하세요.

def find_common(A, B):
    set_a = set(A)  # 첫 번째 배열을 해시셋으로 변환
    return list(set_a.intersection(B))  # 교집합 찾기

print(find_common([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]

6. Codility 해시 관련 문제 유형

Codility에서 자주 나오는 해시 관련 문제 유형은 다음과 같습니다:
✅ 중복 확인 → set()을 활용
✅ 유일한 요소 찾기 → dict()로 등장 횟수 체크
✅ 페어(pair) 찾기 → dict 또는 set 활용
✅ 배열에서 특정 합을 이루는 두 숫자 찾기 → set 활용

Codility 문제를 풀 때, 해시 테이블을 활용하면 시간 복잡도를 낮추고 효율적으로 해결할 수 있습니다. 🚀

추가로 더 궁금한 점 있으면 알려주세요! 💡