import random


#library for the hangman
movi = ["baaghi","ddlj","raazi","parmanu","newton"]
actor = ["hritik","varun","sidharth","arjun","karan"]
profession = ["student","teacher","enterpreneur","farmer","pilote"]
fastfood = ["choumin","springroll","sandwich","noodles","burgers"]
list_of_list = [movi,actor,profession,fastfood]


#some functions for the hangman
def shuffel_and_choose(list1):
    random.shuffle(list1)
    return list1[0]
def find_random_list_name(w):
    if w == movi:
        list_name = "movie"
    elif w == actor:
        list_name = "actor"
    elif w == profession:
        list_name = "profession"
    else:
        list_name = "fast-food"
    return list_name
def replace(search_word):
    under_score_subtracted = 0
    for i in range(len(random_word)):
        if random_word[i] == search_word:
            under_score_list[i] = search_word
            under_score_subtracted += 1
    return under_score_subtracted


#some preparation and global variables :)
random_list = shuffel_and_choose(list_of_list)
random_list_name = find_random_list_name(random_list)
random_word = list(shuffel_and_choose(random_list))
under_score_list = []
for x in random_word:
    under_score_list.append("_")
under_score_number = len(random_word)
user_try=0

#welcome screen(root-window)
print("*"*40)
print("*"*40)
print("*"*16,"HANGMAN","*"*16)
print("*"*40)
print("*"*40)




# some default starting lines
user_name=input("enter your name :")
d=input("select difficulty by entering choice number(int type) :\n1.>easy\n2.>hard\n")
if d.isdigit():
    difficulty=int(d)
else:
    print("you have entered wrong choice ")
    exit(1)




#application code

print("guess the name of %s"%(random_list_name))
if difficulty==2:
#hard level
    print("  ".join(under_score_list))
    while under_score_number>0:
        word = input("guess the letter\t")
        number_of_places = replace(word.lower())
        under_score_number = under_score_number - number_of_places
        print("  ".join(under_score_list))
        user_try += 1
        if user_try > 10:
            print("sorry %s" % (user_name))
            print("better luck next time")
            print("%s name was " % (random_list_name), end="")
            print(" ".join(random_word))
            break
        if under_score_number == 0:
            print("congratulations %s"%(user_name))
            print("hurrey ..,you win...,in %d try.." % (user_try))

elif difficulty == 1:
#easy_level
    index_list = []
    for i in range(len(random_word)):
        index_list.append(i)
    index_no=shuffel_and_choose(index_list)
    word=random_word[index_no]
    number_of_places = replace(word.lower())
    under_score_number = under_score_number - number_of_places
    print("  ".join(under_score_list))
    while under_score_number>0:
        word = input("guess the letter\t")
        number_of_places = replace(word.lower())
        under_score_number = under_score_number - number_of_places
        print("  ".join(under_score_list))
        user_try += 1
        if user_try > 15:
            print("sorry %s" % (user_name))
            print("better luck next time")
            print("%s name was "%(random_list_name),end="")
            print(" ".join(random_word))
            break
    if under_score_number==0:
        print("congratulations %s" % (user_name))
        print("hurrey.. ,you win...,in %d try.."%(user_try))
else:
    print("enter correct choice ")
