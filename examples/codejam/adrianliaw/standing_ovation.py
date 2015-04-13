import sys

def transform_data(stdin):
    stdin.readline()
    for line in stdin:
        S_max, Si = line.strip().split()
        yield int(S_max), [int(n) for n in Si]

def solution(inputs):
    S_max, Si = inputs
    total_inviting = stood_up_already = 0
    while True:
        if not Si: return total_inviting
        if stood_up_already >= S_max - len(Si) + 1:
            stood_up_already += Si[0]
            Si = Si[1:]
        else:
            inviting = S_max - len(Si) + 1 - stood_up_already
            total_inviting += inviting
            stood_up_already += inviting + Si[0]
            Si = Si[1:]

def solve(stdin):
    return map(solution, transform_data(stdin))

for i, result in enumerate(solve(sys.stdin), 1):
    print("Case #{i}: {result}".format(i=i, result=result))
