
def BMIcalcu(height, weight):
    if not isinstance(height, (int, float)):
        raise TypeError('bad operand type')
    return weight/(height*height)

def prinf_shenti(bmi):
    if(bmi < 18.5):
        print("体重过轻")
    elif(bmi < 25):
        print("正常")
    elif(bmi < 28):
        print("体重过重")
    elif(bmi < 32):
        print("肥胖")
    else:
        print("严重肥胖")

height = input("height: ")
weight = input("weight: ")
bmi = BMIcalcu(float(height), float(weight))
print("BMI: ", bmi)
prinf_shenti(bmi)