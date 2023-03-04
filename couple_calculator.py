print('Welcome to the Love Calculator!')
name1 = input('What is your name?: ').lower()
name2 = input('What is their name?: ').lower()
couple = name1 + name2

love_l = couple.count('l')
love_o = couple.count('o')
love_v = couple.count('v')
love_e = couple.count('e')
score_love = love_e + love_o + love_l + love_v

true_t = couple.count('t')
true_r = couple.count('r')
true_u = couple.count('u')
true_e = couple.count('e')
score_true = true_t + true_r + true_u + true_e

total_score = str(score_true) + str(score_love)

if int(total_score) <= 20:
    print(f'Your score is {total_score}. You guys are terrible together.')
elif 20 < int(total_score) <= 75:
    print(f'Your score is {total_score}. You guys are decent together.')
else:
    print(f'Your score is {total_score}. Match made in heaven.')




