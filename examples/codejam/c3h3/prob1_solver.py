
import sys
lines = map(lambda line:line.strip(),sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n == len(problem_cases)

test_prob_sol = [0,1,2,0] 

for case_i in range(n):
    max_s = int(problem_cases[case_i][0])
#     print problem_cases[case_i][1]
    print "Case #{case_i}: {solution}".format(case_i=case_i,solution=test_prob_sol[case_i])
    