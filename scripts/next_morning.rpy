label next_morning:
    scene black
    with fade

    "Следующее утро..."

    play sound bird_sing volume 0.5
    "Солнце просвечивает сквозь тонкую щель между шторами, пуская по стене полосу 
    солнца. За окном птицы сутра пораньше ведут важные переговоры, не давая снова 
    провалиться в сон." 

    play sound "<from 0 to 2>audio/sounds/alarm.mp3" 
    "..."

    menu:
        "Продлить будильник на 5 минут":
            "Олег, который уже месяц встает не раньше 12 часов не находит в себе силы встать с первым 
            будильником и решает продлить сон." 
            play sound "<from 49 to 55>audio/sounds/meladze_song.mp3" volume 0.01 fadeout 1.0
            scene mc_room
            show main_character
            with fade

            "Просыпается Олег от Меладзе, который поет на их кухне 
            каждую субботу для мамы. Правда пока только на ее телефоне." 
            "Но маму это не останавлевает 
            от этой еженедельной пытки для ушей Олега, который с удовольствием бы «тысячу раз 
            оборвал провода», лишь бы эта традиция навсегда ушла из его жизни." 
            "Однако сегодня 
            Меладзе помог не опоздать на встречу, так как будильник предательски подвел Олега."

            mc "О нет! Уже 9.30. Я не успею!"
            show main_character:
                linear 0.5 xalign 1.5
            "Олег наспех одевается и выбегает из комнаты"

            scene kitchen
            show main_character at left
            show mother at right
            with dissolve

            mum "С добрым утром! Ты чего так рано встал….."
            mc "Я опаздываю на встречу, нет времени объяснять. Пока!"
            show main_character:
                linear 0.8 xalign 1.5
            mum "На встречу? Я тебя не узнаю, то из дома не выгонишь, а тут…."
            "Но Олегу не суждено было услышать конец фразы, так как он уже бежал в ИРИТ РТФ."

        "Проснуться вместе с будильником":
            scene mc_room
            show main_character
            with fade
            "Олег встает вместе с будильником." 

            show main_character:
                linear 1 xalign 1.5
            "Еле как открыв глаза Олег идет на кухню откуда 
            доносится запах свежесваренного кофе и ароматных блинчиков." 

            scene kitchen
            show main_character at left
            show mother at right
            with dissolve

            mum "С добрым утром! Ты чего так рано встал?"
            mc "Мне нужно сегодня на встречу к 10."
            mum "Встреча? Интересно… Будешь блинчик?"
            mc "Возможно сегодня я определюсь с тем, на кого пойду учиться. От блинчика не откажусь."
            mum "Ну наконец-то. А то я уже себе место не нахожу. Ну не буду тебя отвлекать, ешь уже, а
            то совсем исхудал уже."
            mc "Маааам."
            mum "Ну всё, молчу молчу."

            show main_character:
                linear 1.4 xalign 1.5
            mc "Ладно, я побежал!"

    play sound "<from 0 to 4>audio/sounds/bus_ambiance.mp3" volume 0.1 fadein 1.0
    scene black
    with fade
    mc "«И куда эти бабушки ездят в субботу в 9 утра. Ответ на этот вопрос я никогда не узнаю .»"

    jump radio_visit
