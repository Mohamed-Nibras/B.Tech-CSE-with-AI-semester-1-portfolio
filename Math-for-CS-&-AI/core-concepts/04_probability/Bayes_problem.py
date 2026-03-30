"""
| Variable                | Meaning        |
| ----------------------- | -------------- |
| `p_event`               | Prior          |
| `p_pos_given_event`     | True positive  |
| `p_pos_given_not_event` | False positive |

"""


def bayes_problem(p_event, p_positive_given_event, p_positive_given_not_event):
    p_not_event = 1 - p_event

    numerator = p_positive_given_event * p_event
    denominator = numerator + (p_positive_given_not_event * p_not_event)

    return round(numerator/denominator, 3)

print(bayes_problem(0.01, 0.99, 0.05))  # rare event
print(bayes_problem(0.2, 0.99, 0.05))   # less rare
print(bayes_problem(0.01, 0.99, 0.3))   # high false positive
print(bayes_problem(0.01, 1.0, 0.0))    # perfect test