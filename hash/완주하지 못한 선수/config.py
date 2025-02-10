# 동명이인이 있을 수 있음

test_cases = [
    {
        "participant": ["leo", "kiki", "eden"],
        "completion": ["eden", "kiki"],
        "result": "leo",
    },
    {
        "participant": ["marina", "josipa", "nikola", "vinko", "filipa"],
        "completion": ["josipa", "filipa", "marina", "nikola"],
        "result": "vinko",
    },
    {
        "participant": ["mislav", "stanko", "mislav", "ana"],
        "completion": ["stanko", "ana", "mislav"],
        "result": "mislav",
    },
]

# 입출력 예 설명
# 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
