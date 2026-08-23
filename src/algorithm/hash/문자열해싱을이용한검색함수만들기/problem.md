# 문자열 해싱을 이용한 검색 함수 만들기

## 문제 설명

문자열 리스트 `string_list`와 쿼리 리스트 `query_list`가 주어진다. `query_list`의 각 문자열이 `string_list`에 있는지 확인하라. 있으면 `True`, 없으면 `False`이다.

각 쿼리에 대한 존재 여부를 리스트로 반환하는 `solution` 함수를 구현하라.

아래 문자열 해싱 방법으로 해시 함수를 구현해서 풀어야 한다. 식에서 `p`는 31, `m`은 1,000,000,007이다.

\[
\text{hash}(s) = (s[0] + s[1] \cdot p + s[2] \cdot p^2 + \cdots + s[n-1] \cdot p^{n-1}) \bmod m
\]

## 제한 조건

- 입력 문자열은 영어 소문자로만 이루어져 있다.
- 문자열의 최대 길이는 \(10^6\)이다.
- 해시 충돌은 없다.

## 입출력 예

| string_list | query_list | return |
| --- | --- | --- |
| `["apple", "banna", "cherry"]` | `["banna", "kiwi", "melon", "apple"]` | `[true, false, false, true]` |

## 입출력 예 설명

### 입출력 예 #1

`"banna"`와 `"apple"`은 `string_list`에 있으므로 `true`, `"kiwi"`와 `"melon"`은 없으므로 `false`.

## 풀이

- 테스트 케이스: [`testcases.txt`](testcases.txt)
