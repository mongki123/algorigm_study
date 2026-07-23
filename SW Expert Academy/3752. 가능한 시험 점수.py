T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    reachable = {0}          # 빈 집합 합
    for x in arr:
        # 기존 합에 x를 더한 새로운 합들을 추가
        reachable |= {s + x for s in reachable}
    
    print(f"#{test_case} {len(reachable)}")


"""
Incremental Set DP = “집합을 점진적으로 확장하는 동적 프로그래밍”
 - 기존의 결과물을 바탕으로 더하기를 생략함.


ex) arr = {2, 3, 5}

해당 문제는 문제의 가능한 점수이기 때문에 0을 포함하여 시작. -> {0}
list가 아닌 set을 사용하는 이유는 중복제거를 위함.

1. {0 + 2} -> {2}
 - 위 set를 기존 배열에 추가.
 - {0, 2}

2. {0 + 3, 2 + 3} -> {3, 5}
 - 위 set를 기존 배열에 추가.
 - {0, 2, 3, 5}

3. {0 + 5, 2 + 5, 3 + 5, 5 + 5} -> {5, 7, 8, 10}
 - 위 set를 기존 배열에 추가.
 - {0, 2, 3, 5, 7, 8, 10}


0
ㄴ 2
|  ㄴ 5
|  |  ㄴ 10
|  ㄴ 7
ㄴ 3
|  ㄴ 8
ㄴ 5


위의 구조를 참고하면 도움이 된다. combinations(순열) 같은 경우로 계산하면 모든 열을 계산하고 다시 계산하여 복잡하겠지만,
set DP 를 사용하면 기존의 요소를 재활용하기 때문에 획기적으로 줄일 수 있다.
"""
