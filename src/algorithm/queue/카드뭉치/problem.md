# 카드 뭉치

## 문제 설명

영어 단어가 적힌 카드 뭉치 두 개가 주어진다. 각 뭉치에서 카드를 사용해 원하는 순서의 단어 배열을 만들 수 있는지 판별하라.

규칙은 다음과 같다.

- 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용한다.
- 한 번 사용한 카드는 다시 사용할 수 없다.
- 카드를 사용하지 않고 다음 카드로 넘어갈 수 없다.
- 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없다.

문자열 배열 `cards1`, `cards2`와 원하는 단어 배열 `goal`이 주어질 때, `cards1`과 `cards2`의 단어로 `goal`을 만들 수 있으면 `"Yes"`를, 만들 수 없으면 `"No"`를 반환하는 `solution` 함수를 구현하라.

## 제한 조건

- `1 <= cards1의 길이, cards2의 길이 <= 10`
- `1 <= cards1[i]의 길이, cards2[i]의 길이 <= 10`
- `cards1`과 `cards2`에는 서로 다른 단어만 존재한다.
- `2 <= goal의 길이 <= cards1의 길이 + cards2의 길이`
- `1 <= goal[i]의 길이 <= 10`
- `goal`의 원소는 `cards1`과 `cards2`의 원소들로만 이루어져 있다.
- `cards1`, `cards2`, `goal`의 문자열은 모두 알파벳 소문자로만 이루어져 있다.

## 입출력 예

| cards1 | cards2 | goal | result |
| --- | --- | --- | --- |
| `["i", "drink", "water"]` | `["want", "to"]` | `["i", "want", "to", "drink", "water"]` | `"Yes"` |
| `["i", "water", "drink"]` | `["want", "to"]` | `["i", "want", "to", "drink", "water"]` | `"No"` |

## 입출력 예 설명

### 입출력 예 #1

첫 번째 뭉치에서 `"i"`를 사용한 뒤, 두 번째 뭉치에서 `"want"`, `"to"`를 사용하고, 다시 첫 번째 뭉치에서 `"drink"`, `"water"`를 사용하면 원하는 순서를 만들 수 있다.

### 입출력 예 #2

`"i want to"`까지는 만들 수 있지만, `"water"`가 `"drink"`보다 먼저 사용되어야 하므로 문장을 완성할 수 없다.

## 풀이

- 테스트 케이스: [`testcases.txt`](testcases.txt)

## 참고

- [프로그래머스 - 카드 뭉치](https://school.programmers.co.kr/learn/courses/30/lessons/159994)
