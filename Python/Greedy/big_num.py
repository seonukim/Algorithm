## 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 초과 제한 K가 주어질 때
## 큰 수의 법칙에 따른 결과를 출력하시오.

n, m, k = map(int, input().split())
N = list(map(int, input().split()))

N.sort()
first = N[-1]
second = N[-2]

# print(first)
# print(second)

res = 0

while True:
    for i in range(k):
        if m == 0:
            break
        res += first
        m -= 1
    if m == 0:
        break
    res += second
    m -= 1

print(res)
