# 1475. Final Prices With a Special Discount in a Shop

## 문제 설명

정수 배열 `prices`가 주어지며, `prices[i]`는 가게의 i번째 상품 가격이다.

가게에는 특별 할인이 있다. i번째 상품을 구매하면, `j > i`이면서 `prices[j] <= prices[i]`를 만족하는 가장 작은 인덱스 `j`에 대해 `prices[j]`만큼 할인을 받는다. 그런 `j`가 없으면 할인을 받지 않는다.

i번째 상품의 최종 결제 금액(할인 반영)을 `answer[i]`에 담은 정수 배열을 반환하는 `solution` 함수를 구현하라.

## 제한 조건

- `1 <= prices.length <= 500`
- `1 <= prices[i] <= 1000`

## 입출력 예

| prices | result |
| --- | --- |
| `[8, 4, 6, 2, 3]` | `[4, 2, 4, 2, 3]` |
| `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` |
| `[10, 1, 1, 6]` | `[9, 0, 1, 6]` |

## 입출력 예 설명

### 입출력 예 #1

- 상품 0: `prices[0]=8`, `prices[1]=4`로 할인, 최종 가격은 `8 - 4 = 4`
- 상품 1: `prices[1]=4`, `prices[3]=2`로 할인, 최종 가격은 `4 - 2 = 2`
- 상품 2: `prices[2]=6`, `prices[3]=2`로 할인, 최종 가격은 `6 - 2 = 4`
- 상품 3, 4: 할인이 없다.

### 입출력 예 #2

모든 상품에 대해 할인 조건을 만족하는 이후 상품이 없으므로 가격이 그대로다.

### 입출력 예 #3

- 상품 0: `prices[1]=1`로 할인, `10 - 1 = 9`
- 상품 1: `prices[2]=1`로 할인, `1 - 1 = 0`
- 상품 2, 3: 할인이 없다.

## 풀이

- 테스트 케이스: [`testcases.txt`](testcases.txt)

## 참고

- [LeetCode 1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)
