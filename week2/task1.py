# We have example messages from 6 persons in JSON format. 
# There are at least 3 persons who are older than 17.
# Using a loop to find out those who are most probably older than 17 years old based on example messages.
# Print their names in the console.



def find_and_print(messages):
    # 迴圈、字串判斷、對字串做處理
    # write down your judgment rules in comments
    # 判斷準則:字串中是否有以下條件"18","college student","vote for Donald Trump"，若有包含這些文字，則印出來名字
    # your code here, based on your own rules
    nameover17=[]
    for name,description in messages.items():
        if check_age(description):
            nameover17.append(name)
    print(nameover17)

#
def check_age(description):
    keywords=["18","college","legal","vote"] #比對數字大於17，轉出來
    for word in description.split():
        for keyword in keywords:
            if keyword in word:
                return True
    return False

find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.", 
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})

