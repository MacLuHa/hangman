word=str(input("Enter word: "))
def hangman(word):
    wrong=0 #отвечает за число неверных предположений
    stages=[" ",
            "____     ",         
            "|   |    ",        
            "|   |    ",
            "|   o    ",
            "|  /|\   ",
            "|  / \   ",
            "|        "
            ]
    rletters=list(word) #Список всех символов,содержащихся в загаданном слове
                        #Также отслеживает,какие буквы осталось отгадать

    board=["_"]*len(word) #Список строк,используется для отображения подсказок
    win=False      #Отслеживает,победил ли игрок        

    print("Welcome to execution!!!\nComputer chose the word\nLet's try quess it")
    while wrong<len(stages)-1:   #Если число неудачных попыток станет больше,чем
                                 #кол-во символов в слове,игра закончится
                                 #-1,because нужно уравновесить:счёт в списке stages
                                 #начинается с 0,а wrong-с 1

        print("\n")              #?????
        char=str(input("Player,enter your letter: "))
                     #Передаем загаданной букве переменную
        if char in rletters:    #Проверяем её наличие в списке
            yep=rletters.index(char) #index получает первый индекс отгаданной буквы
            board[yep]=char          #и заменяет нижнее подчёркивание в board на
            rletters[yep]="$"        # индекс отгаданной буквы
        else:
            wrong+=1
        print((" ".join(board)))       #в случае ошибки board ничего не получает
        e=wrong+1
        print("\n".join(stages[:e]))    #Выводит виселицу,каждую строчку по отдельности
                                       #Срез берём [0:wrong+1],+1,because
                                       #при выполнение среза конец не включается
        if "_" not in board:
            print("You have won!!!Word was: ")   #Если "_" не осталось в board
                                                     #,то все буквы отгаданы
            print(" ".join(board))           #??????????
            win=True
            break
    if not win:
        print("\n".join(stages[:wrong]))     #?????????
        print("You have lost.Word was: {}".format(word))

hangman(word)
                                
    
