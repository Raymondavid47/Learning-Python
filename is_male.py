is_male = input("Are you a male? ")
is_tall = input("Are you tall? ")

if is_male == ("Yes") and is_tall == ("Yes"):
    print ("you are a male and You are tall")
elif is_male == ("No") and is_tall == ("Yes"):
    print ("You are not a male but you are tall")
elif is_male == ("Yes") and is_tall == ("No"):
    print ("You are a male but You are not tall")
else: 
    print ("You are not a male and You are not tall")

