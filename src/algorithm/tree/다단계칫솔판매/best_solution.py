"""https://school.programmers.co.kr/learn/courses/30/lessons/77486

피드백
- 이진트리를 만들 필요는 없다. 자식이 여러 명인 일반 트리이고, 돈은 자식 → 부모로만
  올라가므로 필요한 건 자식 리스트가 아니라 부모 포인터다.
- 핵심 버그는 자식이 들고 있는 이익을 합친 뒤 10%를 한 번에 뗀 것이다. 규칙은
  판매 건마다 받은 금액에 10%를 그때그때 절사하는 것이라, 1원 미만이라 안 떼야 할
  2원이 큰 합에 섞이면 mary가 957이 된다.
- seller_dict[se] = am은 같은 판매원의 이전 판매를 덮어쓴다. seller는 중복될 수
  있으므로 판매 건을 하나씩 처리하거나 += 해야 한다.
- int(x * 0.1)은 부동소수점 오차가 날 수 있다. 원 단위 절사는 money // 10이다.
- enroll마다 서브트리를 다시 내려가면 체인이 O(n²)이다. 한 건의 금액은 최대
  10,000원이고 매번 1/10이 되므로, 판매원에서 부모로 몇 칸만 올라가면 돈이 0이다.
"""

from pathlib import Path

from src.core import assert_testcases

TESTCASES = Path(__file__).parent / "testcases.txt"


def solution(
    enroll: list[str], referral: list[str], seller: list[str], amount: list[int]
) -> list[int]:
    parent = dict(zip(enroll, referral))
    profit = {name: 0 for name in enroll}

    for name, qty in zip(seller, amount):
        money = qty * 100
        cur = name
        while cur != "-" and money > 0:
            give = money // 10
            profit[cur] += money - give
            money = give
            cur = parent[cur]

    return [profit[name] for name in enroll]


def verify() -> None:
    assert_testcases(solution, TESTCASES)
    print(f"OK: {TESTCASES.parent.name} - all test cases passed")


if __name__ == "__main__":
    verify()
