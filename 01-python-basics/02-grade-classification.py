score = float (input("Enter your score: "))

if score < 0 or score > 10:
    print("Invalid score")
elif score >= 9 :
    print("Classification: Excellent")
elif score >= 8:
    print("Classification: Very good")
elif score >= 6.5:
    print("Classification: Good" )
elif score >= 5:
    print("Classification: Average")
else:
    print("Classification: Fail")