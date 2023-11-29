label cafe_trip:
    scene black
    with fade

    "День стоит теплый. На площадке играют дети, бегают собаки, голуби дерутся с воробьями 
    за кусок засохшей булки. В общем, всё как всегда."

    "Однако Олег чувствует, как устал, хотя 
    ничего сегодня не делал. Случай с картой выбил его из сил."

    "Олег настолько погрузился в 
    свои мысли, что не заметил, как на улице стемнело и загорелись фонари." 
    
    play music cafe_music volume 0.1 fadein 2
    scene cafe with fade
    "Тут он услышал 
    музыку и, повернув голову на звук, увидел кафе «У Нюры»."

    "Недолго думая он решил зайти 
    перекусить, так как аромат стоял просто восхитительный."

    scene cafe_inside with dissolve
    "Внутри было очень уютно. 
    Ротанговые стулья с зелеными подушками , круглые деревянные столики, гирлянды и 
    растения на подоконниках придавали этому место что-то невероятно притягательное."

    show main_character:
        xalign 0.1
    with moveinleft
    show main_character:
        linear 0.1 yalign -0.3
    "Олег 
    сел за столик, его ноги гудели от долгой прогулки и он был не прочь перекусить"

    show denis:
        xalign 0.7
        xzoom -1.0
    show sergei:
        xalign 0.9
        xzoom -1.0
        yalign 1.0
    with fade
    "В это время за соседним столиком сидела компания молодых людей. Они то и дело 
    привлекали внимание Олега своей оживленной беседой."

    den "Да я вообще не понимаю, как они пишут эти антивирусные программы, если они 
    даже от простейших вирусов защитить не могут!"

    serg "Понимаю. Вот у меня друг недавно попал в неприятную ситуацию из-за этих 
    антивирусов дурацких. Еле как потом его данные в модеусе восстановил..."
    serg "Хотя все равно 
    после этого модеус лег, так что зря старались."

    show main_character:
        linear 0.1 yalign 0.0

    "После слов о взломах, Олег уже не могу усидеть на месте и решил подойти к их столику."

    show main_character:
        linear 0.5 xalign 0.3

    mc "Привет, ребята."
    mc "Я слышал, что вы говорили про антивирусные программы. Мне стало очень интересно, 
    так как недавно во время игры в World of Cars у меня взломали счет и украли все деньги."

    show denis:
        xzoom 1.0

    den "Ооо. Капец. Жаль конечно, что так произошло. С этой игрой часто так происходит. 
    Разрабы не могут нормальную защиту сделать, а люди страдают."

    $ den_name = "Денис"
    den "Меня кстати Ден зовут."

    mc "Олег, приятно познакомится."

    show sergei:
        xzoom 1.0

    serg "Да это часто так происходит и не только в этой игре. Нигде нормальную программу 
    сделать не могут. Я поэтому и пошел на Информационную безопасность, чтобы таких проблем 
    больше не было."

    $ serg_name = "Сергей"
    serg "Мое имя Сергей, приятно познакомится."

    mc "Ого. Впервые слышу о такой специальности. А можете рассказать поподробнее? Я как 
    раз думаю, на кого поступать."

    den "Случайности не случайны. Тебе повезло встретить нас, путник. Мы откроем тебе 
    загадочный мир вычислительной техники и компьютерного волшебства."
    den "Присоединяйся в 
    наши ряды и мы даруем тебе вечную безопасность от мошенников. Да будет так!"

    den "АХАХАХА." with vpunch

    serg "Да хватит тебе. Совсем сума сошёл что-ли? Человека только пугаешь."
    serg "Не обращай на него внимание, он не всегда такой."

    den "Да ладно тебе. Пошутить уже и нельзя чтоли?"
    den "А вообще, если хочешь узнать поподробнее 
    о нашем направлении, то можешь поговорить со Светой, она у нас главная по всем этим 
    делам."

    mc "Правда? Это было бы здорово!"

    serg "Приходи к ИРИТ РТФ к 10.00. Только не опаздывай, а то у нас потом пары."

    show denis:
        linear 0.4 xpos 0.65
    den "*шепотом* Этот заучка никогда ничего не прогуливает. Так что внемли голосу 
    пророка и будет тебе счастье!"

    serg "Ден! Этот заучка может и перестать давать тебе списывать."

    show denis:
        linear 0.2 xpos 0.7
    with hpunch
    den "Нет, нет, только не это! Ты же человек в конце концов, ты не опустишься до такого!"

    serg "Ладно, нам пора, а то у нас коменданша-женщина серьезная. Может и не пустить 
    поздно. Так что до завтра."

    jump next_morning