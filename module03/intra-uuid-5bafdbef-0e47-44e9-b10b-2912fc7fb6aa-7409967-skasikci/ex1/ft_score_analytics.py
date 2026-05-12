import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print(
        "No scores provided! Usage: python3 "
        "ft_score_analytics.py <score1> <score2> ..."
    )
else:
    scores = []

    i = 1
    while i < len(sys.argv):
        try:
            score = int(sys.argv[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1

    if len(scores) == 0:
        print(
            "No scores provided! Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print("Scores processed:", scores)

        total = sum(scores)
        high = max(scores)
        low = min(scores)
        average = total / len(scores)
        score_range = high - low

        print("Total players:", len(scores))
        print("Total score:", total)
        print("Average score:", average)
        print("High score:", high)
        print("Low score:", low)
        print("Score range:", score_range)
