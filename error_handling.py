try:
    result = 10/10
    print(result)
except:
    print("This is not deviding to zero, try again!")


fruits = {

    "orange"  : 5,
    "apple"   : 3,
    "watermelon" : 2

}

try:
    print(fruits["cherry"])
except: KeyError
print("the key is not found")



text = "this is not a number"

try:
    text_to_int = int(text)
except Exception as e:
    print("an error is ocured",e)

try:
    result= 10/ 2
except:
    print("An error has ocurred")
else:
    print("the result is:",result)

try:
    result = 10/2
except ZeroDivisionError:
    print("can not be divided")

finally:
    print("Finally the block is divided")


























