#创建一个等于10的变量
types_of_people = 10
#创建一个字符串变量There are 10 types of people.
x = f"There are {types_of_people} types of people."
#创建binary字符串变量
binary = "binary"
#创建don't字符串变量
do_not = "don't"
#创建一个字符串变量Those who know binary and those who don't
y = f"Those who know {binary} and those who {do_not}."
#输出x和y
print(x)
print(y)
#输出I said: {x} I also said: '{y}
print(f"I said: {x}")
print(f"I also said: '{y}'")
#创建一个布尔型变量
hilarious = False
#创建一个字符串变量"Isn't that joke so funny?! {}
joke_evaluation = "Isn't that joke so funny?! {}"
#输出Isn't that joke so funny?! False
print(joke_evaluation.format(hilarious))
#创建w,e两个字符串变量
w = "This is the left side of..."
e = "a string with a right side."
#输出This is the left side of...a string with a right side.
print(w + e)
#有五处使用了string put inside string
#w+e就是把两个字符串连接在一起