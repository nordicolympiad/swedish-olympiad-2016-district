GROUP_SCORES = [7, 11, 12, 20]
GROUP_CASES = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
import sys

def is_int(arg):
    try:
        int(arg)
        return True
    except:
        return False


def main():
    if "ignore" in sys.argv:
        print "AC 0"
    elif "groups" in sys.argv:
        scores = []
        for line in sys.stdin.readlines():
            verdict, score = line.split()
            if verdict != "AC":
                scores.append(0)
            else:
                scores.append(score)
        score = 0
        for group in range(len(GROUP_SCORES)):
            group_score = GROUP_SCORES[group]
            for case in GROUP_CASES[group]:
                if scores[case] == 0:
                    group_score = 0
            score += group_score
        print "AC %s" % score
    else:
        for line in sys.stdin.readlines():
            print line

main()

