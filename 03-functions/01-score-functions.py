scores = [7.5, 8.0, 4.5, 9.0, 6.5, 3.5, 8.5]

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def count_passed(scores):
    passed_count = 0

    for score in scores:
        if score >= 5:
            passed_count += 1

    return passed_count

def count_failed(scores):
    failed_count = 0

    for score in scores:
        if score < 5:
            failed_count += 1

    return failed_count

def classify_score(score):
    if score >= 8.5:
        return "Excellent"
    elif score >= 7:
        return "Good"
    elif score >= 5:
        return "Average"
    else:
        return "Failed"

average_score = calculate_average(scores)
passed_students = count_passed(scores)
failed_students = count_failed(scores)

print(f"Average score: {average_score: .2f}")
print(f"Passed: {passed_students}")
print(f"Failed: {failed_students}")

print("\nScore classifications:")

for score in scores:
    classification = classify_score(score)
    print(f"{score}: {classification}")