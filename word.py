words = input('Word:')
while True:
    try:
        number = input('Enter number:')
        text = words.split()
        a = ""
        number = int(number)
        for i in text:
            a = a + str(i[number]).upper()

        print(a)
    except IndexError:
        print('index out of range')
    except ValueError:
        print('Plase Enter number')


#'SGilhd AinI TtSn r_tk Ahaei Pugd 1brid 8_mn_f'
# 0-Satrap18
# 1-git_hub_
# 2-instagram
# 3-LINKEDIN
