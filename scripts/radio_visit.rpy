
label radio_visit:
    scene radio_building
    show main_character:
        xalign 0.8
    with fade

    "Олег пришел к ИРИТ РТФ и с волнением ждет своих товарищей. Ладони вспотели, живот 
    предательски бурлит, а сердце уходит в пятки." 
    "Олег никогда раньше не испытывал такого 
    волнения. Он чувствовал, что прямо здесь и сейчас решается его судьба." 
    "Олег приехал рано, 
    поэтому ему пришлось подождать своих товарищей. Стрелки часов шли предательски 
    медленно, но, к счастью Олега, все рано или поздно заканчивается." 
    "Вдруг за спиной он слышит знакомый голос."

    show denis:
        xalign 0.2
    show sergei:
        yalign 1.0
        xalign 0.5
    with moveinleft

    den "Здарова, давно здесь стоишь?"
    mc "Привет. Решил приехать пораньше, чтобы точно не опоздать."
    den "Серега, довел парня, еще станет таким как ты. Что потом с ним делать будем?"
    serg "Привет. Ничего страшного. Это ты вечно опаздываешь, поэтому у тебя и проблем не наберешься."
    den "Ладно, ладно. Что мы всё обо мне, да обо мне. Пойдем уже, а то опоздаем."
    serg "(усмехается) Когда ты об этом беспокоиться начал?"
    den "Да вот с сегодняшнего дня и начал. Тебе то что. Ты же всегда этого хотел. Вот считай, что 
    я твоя фея крестная, которая исполняет все твои желания."
    serg "Пойдем, Олег, пока эта «фея» не наколдовала чего еще."

    scene radio_enter
    with dissolve

    "Холл института просторный. Несмотря на серые стены, институт довольно светлый." 
    "Я уже 
    собрался пройти дальше, как был остановлен ультразвуковой волной, исходившей из 
    довольно немолодой женщины."

    show sergei:
        yalign 1.0
        xalign 0.6
    show main_character:
        xalign 0.3
    show denis:
        xalign 0.0
    show mother:
        xalign 0.9
    with fade

    jan "Студенческий предъявляем, молодой человек!"

    serg "Уважаемая,…гм…жен….вахт…..охр….уважаемая! Можно этот парень с нами пройдет."
    serg "Дело в том, что он поступает в наш институт и хочет лучше узнать о программах обучения"
    jan "Зубы мне не заговаривайте! Студенческий предъявляем!"
    den "*шепотом* так ее не проведешь, всякие ее тут заговорить пытались. Есть у меня идейка, 
    но нужно работать быстро."

    show sergei:
        linear 0.3 xalign 0.3
    show main_character:
        linear 0.3 xalign 0.0
    show denis:
        linear 0.3 xalign 0.6
    "Не успели Олег с Сергеем опомниться, как Ден уже приступил к своей «операции ы»"

    den "Уважаемая, я тут что-то нажал в телефоне, что-то разобрать не могу, посмотрите что 
    можно сделать"

    "В это время Ден включает фонарик и направляет в глаза охраннице" with Fade(0.1, 0.0, 0.5, color="#fff")

    call run_choose from _call_run_choose

    scene passage
    with fade
    "Олег что есть мочи начинает бежать в сторону лестницы, перепрыгивая шлагбаумы и 
    нескольких студентов." 
    "В этот субботний летний день в институте на удивление было несколько 
    студентов, благодаря которым Олегу успешно удалось скрыться от глаз всевидящей вахтерши."
    mc "А ты то что бежал? У тебя же был студенческий."
    serg "Ну как же я мог бросить товарища в беде одного. У нас в институте так не поступают."
    mc "А что с Деном будет?"
    serg "Не знаю, но я в него верю." 
    serg "Он однажды опаздывал на пару по истории, а там препод 
    за каждый пропуск 10 баллов отнимал, дак Ден так бежал, что не заметил на своем пути 
    ректора. И когда тот упал, то Ден даже не остановился." 
    serg "Несмотря на это Дена не отчислили. Он 
    там договорился, что ему и выговора никакого не выписали. Так что после этого случая, я за 
    него вообще не переживаю."
    mc "Ого. Я и не знал, что Ден так крут."
    serg "Ну про крут это спорно. Но жизнеспособен- это точно. О, а вот и Света. Привет!"

    scene corridor
    show sergei:
        yalign 1.0
        xalign 0.2
    show main_character:
        xalign 0.5
    show sveta:
        yalign 1.0
        xalign 0.8
    with fade


    svet "Привет! А это Олег, если я не ошибаюсь? Приятно познакомиться, я-Света."
    mc "Взаимно. Мне сказали, что вы мне можете подробно рассказать о направлении 
    информационной безопасности в вашем университете."
    svet "Да, конечно. Только давайте пройдем в кабинет, а то в коридоре будет неудобно."

    hide sergei
    hide main_character
    hide sveta

    "Небольшая компания направилась по лабиринтам института. Снаружи он казался гораздо 
    меньше. Олег до сих пор не верил своим глазам. Он находится в университете!"
    "Еще год назад 
    он и представить себе не мог, что он скоро он окончит школу и начнет самостоятельную 
    жизнь." 
    "Будет ходить по этим лабиринтам, но уже не как гость, а как полноценный член этого 
    общества, будет ходить на пары, общаться с однокурсниками!" 
    "Олегу это казалось чем-то 
    невероятным и недосягаемым. Но сейчас он ощущал себя гораздо ближе, чем когда-либо. 
    Совсем скоро он станет студентом. Еще один год и это случится! Осталось совсем немного."

    svet "Вот мы и пришли. Заходите."

    scene cabinet
    with fade

    "Кабинет был просторным и светлым. На противоположной стене были огромные окна. 
    Здесь, в этом кабинете, было тихо и спокойно, не ощущалось никакой суеты."

    show sergei:
        yalign 1.0
        xalign 0.2
    show main_character:
        xalign 0.5
    show sveta:
        yalign 1.0
        xalign 0.8
    with fade

    svet "Ну вот, другое дело. Тут мы сможем нормально поговорить. Можешь задавать вопросы."

    call questions from _call_questions

    svet "Надеюсь, мы смогли тебе помочь. Были рады с тобой познакомиться. Ждем тебя в 
    следующем году в нашем университете!"
    mc "Я был безумно счастлив с вами познакомиться! Спасибо, что рассказали мне все о 
    специальности 10.03.01 Информационная безопасность. Благодаря вам я теперь точно знаю, 
    куда пойду поступать! Надеюсь, что мы еще увидимся."
    serg "Конечно увидимся! Ведь мы будем твоими наставниками."
    mc "А это кто?"
    serg "Придет время, и ты все узнаешь. А пока, пойдемте вниз. Узнаем, как там Ден."

    scene radio_building
    with fade

    "Компания ребят вышла на улицу. День уже вовсю вошел в свои права. Гудели машины, по 
    своим делам шли люди и играла музыка из кафе." 
    "Но в душе Олега было спокойно. Он 
    чувствовал себя частью чего-то важного и по-настоящему ценного. Олег был счастлив, 
    несмотря на все события, которые происходили в недалеком прошлом."

    show sergei:
        yalign 1.0
        xalign 0.9
    show main_character:
        xalign 0.6
    show denis:
        xalign 0.3
    show sveta:
        yalign 1.0
        xalign 0.1
    with fade

    den "Ну наконец-то. Чего вы так долго. Я здесь чуть не запекся от солнца."
    svet "Ден, привет, а что ты внутрь не зашел?"
    den "О, Света, привет! А тебе эти двое не сказали? Я, между прочим, ценой своей жизни этих 
    двоих спас от неминуемой гибели!"
    svet "Вот как!"
    serg "Да ладно. Тебя послушать, дак тебе медаль героя дать надо. Но все равно спасибо. Без 
    тебя бы мы и вправду не прошли бы."
    den "Я не сплю? Мне кажется или меня Серега похвалил за то, что я вахтершу обманул? 
    Серега, дай я тебя обниму!"

    show main_character:
        linear 0.3 xalign 0.3
    show denis:
        linear 0.3 xalign 0.8

    serg "Сергей: Эй,эй, эй. Чего это началось. Отстань!"
    den "Ну, Серега. Ты такой милыййй"

    mc "У них всегда так?"
    svet "Не переживай. Это они любя. Они друзья с детского сада еще. Всегда были неразлей 
    вода." 
    mc "Да? Но они же такие разные. Как они могут дружить?"
    svet "Сама всегда удивляюсь. Но, несмотря на это факт остается фактом."
    mc "Да уж."

    scene black
    with fade
    
    "Конец"

    return

default menuset = set()
default done = False
label questions:
    if len(menuset) == 7:
        return
    else:
        menu:
            set menuset
            den "Что ты хочешь узнать?"
            "1(какие предметы ЕГЭ нужно сдавать, чтобы поступить на это направление?)":
                jump subjects
            "2(Какие проходные баллы?)":
                jump scores
            "3(Кем я смогу работать, отучившись на информационной безопасности?)":
                jump professions
            "4(Чем конкретно занимается Аналитик информационной безопасности?)":
                jump description
            "5(Сколько лет учиться?)":
                jump years
            "6(Есть ли внеурочная деятельность?)":
                jump life
            "7( Кто может попасть в общежитие и как?)":
                jump dormitory


label subjects:
    "Света: на данный момент нужно сдавать Профильную математику, Русский язык и 
    Физику/Информатику. Если появятся какие-то изменения, то ты сможешь их отследит на сайте 
    УрФУ"
    jump questions

label scores:
    svet "Информация про проходные баллы"
    jump questions

label professions:
    svet "Рассказывает перечень профессий"
    jump questions

label description:
    svet "Описание профессиии детальнее"
    jump questions

label years:
    serg "отвечает"
    jump questions

label life:
    svet "Рассказывает про внеурочные занятия и ярмарку возможностей"
    jump questions

label dormitory:
    svet "Рассказывает"
    jump questions


label run_choose:
    menu:
        "Бежать":
            return
        "Быть честным и продолжать стоять":
            jump think

label think:
    menu:
        "Подумать лучше":
            jump run_choose