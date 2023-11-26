screen choose: 
    imagebutton: 
        at left
        focus_mask True 
        idle "images/objects/car.jpg" 
        hover "images/objects/car_hover.png"
        padding (0.23, 0.3)
        action Return()
    imagebutton: 
        at center
        focus_mask True 
        idle "images/objects/car.jpg" 
        hover "images/objects/car_hover.png"
        padding (0.23, 0.3)
        action Return()
    imagebutton: 
        at right
        focus_mask True 
        idle "images/objects/car.jpg" 
        hover "images/objects/car_hover.png"
        padding (0.23, 0.3)
        action Return()

label card_accident:
    scene mc_room 
    show main_character:
        xalign 0.2
        xzoom -1.0
        yalign 0.3
    with fade

    "Был теплый июньский день. Олег сосредоточенно сидел за игрой World of Cars и донатил на 
    очередное дополнение для своей новой машины."

    play sound door_open volume 0.5 fadein 1.0
    show main_character:
        xzoom 1.0
    "Вдруг, дверь неожиданно распахнулась."

    show mother with moveinright:
        xzoom -1.0
        xalign 0.8

    mum "Опять ты в своих игрульках сидишь. Лучше бы погулять сходил."

    mc "Ну, мам. Это не просто игрульки, а серьезное занятие. Некоторые на этом даже большие
    деньги зарабатывают. И вообще…"

    mum "Ладно, ладно. Я вообще по другому вопросу пришла. Ты подумал уже над тем, какие 
    экзамены будешь сдавать и вообще куда поступать собираешься."

    menu:
        "Как ответить?"
        "Нагрубить":
            mc "Что ты ко мне с этим пристала. Сказал же тебе, что подумаю. И вообще я занят."

            mum "А что это ты голос поднимать на мать начал. Что я тебе сказала такого. Будешь так
            разговаривать, то вообще компьютер заберу. А пока остаешься без карманных расходов." 

            show mother:
                xzoom 1.0
                linear 0.2 xalign 1.5
            with hpunch
            play sound door_slam

            "..."

        "Ответить вежливо":
            mc "Да думал. Но все равно не знаю куда поступать. С друзьями это обсуждал, они 
            тоже не знают ничего. Всю голову только сломал."

            mum "Но ты не затягивай с этим делом. Уже надо думать, а то 11 класс не за горами."
            mum "И кстати, у тети Лены сын…."

            play sound "<from 1 to 3>audio/sounds/phone_ring.mp3" volume 0.1 fadeout 1.0
            "Тут Олегу повезло и у мамы зазвонил телефон и она убежала разговаривать."

            show mother:
                xzoom 1.0
                linear 0.5 xalign 1.5

    mc "Опять она с этим университетом пристала. Откуда я знаю, кем я хочу быть?"

    show main_character:
        xzoom -1.0

    mc "Лучше поиграю, а то совсем забыл про турнир, 
    а он уже в 4 начинается. Надо скорее прокачать мою машину."

    call money_theft from _call_money_theft

    scene mc_room 
    show main_character:
        xalign 0.2
        xzoom -1.0
        yalign 0.3
    with fade

    play sound notification
    "..."

    "\"С вашей карты были списаны все деньги\""

    mc "Адалваоиватпл." with vpunch

    show main_character:
        xzoom 1.0
        linear 0.3 yalign 0.5
    mc "Я же недавно антивирус устанавливал. Да пошло оно всё…."

    show main_character:
        linear 1 xalign 1.5
    "..."

    jump cafe_trip


label money_theft:
    scene computer_screen
    show game_launcher
    call screen choose
    with fade

    show credit_card_info:
        yalign 0.7
        xalign 0.5

    mc "Класс. Осталось только оплатить."

    "Введите данные карты"
    call screen input_id

    show layer master at glitch
    play sound glitch_sound volume 0.5

    mc "..."

    scene black
    mc "Какого…."

screen input_id():
    input:
        pos (650, 615)
        length 16
        allow "1234567890"
        color "#000"
