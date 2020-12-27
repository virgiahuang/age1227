driving = input ('Have you ever driven ?')
if driving != 'Yes' and driving != 'No':
    print ('Please answer Yes or No')
    raise SystemExit
#多種做法：
#其中一種是raise SystemExit --> 啟動程式終止///程式就不會繼續跑下去

age = input ('How old are you ?')
age = int(age)
if driving == 'yes':
    if age >= 18: #第二個相關問題的if必須要低一層（前面有空格）
        print ('You have passed')
    else :
        print ('That is odd, how come?')
elif driving == 'No':
    if age >= 18:
        print ('You are eligible to get driver''s license')
    else :
        print ('Very good. You will be able to get your license when you turn 18')

    