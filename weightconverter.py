#author codesntech
pounds = 2.20462
weightinput = float(input("Please enter your weight: "))
unit = input("What is the unit of the weight you input? (kgs or lbs) ")
choice = int(input("Enter 1 for kgs and 2 for lbs to convert your weight: "))

if unit == "kgs" and choice == 2:
    convertweight = weightinput * pounds
    print("Your weight in pounds is {:.2f} lbs".format(convertweight))
elif unit == "lbs" and choice == 1:
    convertweight =  weightinput / pounds
    print("Your weight in kilograms is {:.2f} kg".format(convertweight))
else:
    print("You have entered the same weight units!".format(weightinput))


    
    
    
    




            
