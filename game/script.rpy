﻿# Вы можете расположить сценарий своей игры в этом файле. 

# Объявляйте изображения здесь, используя оператор image.
# например, image eileen happy = "eileen_happy.png"
image bg computer = "Data/BG/computer.png"
image bg university = "Data/BG/university.png"

# Определение персонажей игры.
define g = Character('Greyowl', color="#404040", window_left_padding=160, show_side_image=Image("Data/Sprites/sandman.png", xalign=0.0, yalign=1.0))
define r = Character('@, the Rogue',color="#FF0000", window_left_padding=160, show_side_image=Image("Data/Sprites/rogue.png", xalign=0.0, yalign=1.0))


# Игра начинается здесь.
label start:
    scene bg computer
    "Был обычный день. Февраль, так что на улице темно. Я устало серфил по Интернету. Скоро диплом, надо готовиться, так что времени было немного. Хотя... пожалуй, диплом успеется, так что можно и развлечься инди-играми время от времени. Что я и собирался сейчас делать."
    "Как назло, в скайп тут же пришло сообщение."
    r "Привет! Чувак, как жизнь?"
    "Рога – мой друг из Сети. Он странный, но с ним бывает интересно."
    "Впрочем, сейчас он некстати. Будет звать в ролевку (я – ее мастер, так что без меня они сыграть не смогут), а я хотел немного поиграть в одиночку, возможно, допройти наконец Psychonauts."
    "Что ж, надо ему ответить."
    g "Привет, чувак. Живу помаленьку. Как сам?"
    r "Я тут... Чувааак, мне в голову пришла отличная идея!"
    g "Какая же?"
    r "Ну смотри, ты рисуешь, так? А я... программирую немного. И мы оба любим авторские поделки."
    g "Да, а к чему ты клонишь?"
    r "Мы ведь созданы, чтобы делать визуальные новеллы!"
    "..."
    "..."
    "По-моему, он окончательно поехал..."
    g "Ты думаешь, это хорошая идея? Знаешь, у меня диплом на носу."
    g "Да и я не профессиональный художник, а ты не профессиональный программист."
    r "Все с чего-то начинали. Да и, кстати, мы крутимся в авторской среде. Всегда найдем помощь или совет. Ну что?"
    menu:
        "Это плохая идея.":
            jump diplome
        "Концепты есть?":
            jump concepts

label concepts:
    r "Отлично, ты готов выслушать. В общем, у меня есть три концепта. Рассказывать?"
    g "Давай."
    r "Первый – один из самых очевидных. Можно сделать новеллу про Гамин или Коленку, про ее обитателей и жизнь."
    r "Вторая – я, кажется о ней рассказывал. Про метания чувака-пограничника, как ты их называешь. Этакая психологическая мега-идея."
    r "Третье – можно сделать что-то шаблонное. Мне не нравится этот подход, но для первой игры... нам же надо опробовать свои силы?"
    r "Наконец, можешь предложить свои идеи :)"
    r "Ну что, рассказать о чем-то поподробнее?"
    menu:
        "Первый концепт":
            jump first_concept
        "Второй концепт":
            jump second_concept
        "Третий концепт":
            jump third_concept
        "Своя идея":
            jump idea

label first_concept:
    g "Рассказывай про Гаминопроект."
    r "Ну, тут все понятно из названия. Человек – обычный человек, никак не связанный с Гамином или Коленкой, впервые там регистрируется."
    r "Почти сразу же он понимает, что попал в совершенно другой мир, полный странных чуваков, которые ненавидят слово \"инди\", начинают день с кода и вообще, зачастую живут по ту сторону экрана."
    r "Что насчет геймплея, то игрок может оставлять какие-то (естественно, написанные заранее) комментарии, заводить друзей на сайте, а может, даже присоединиться к Пикачику или Андергамину."
    r "Ну что, рассказать еще о чем-то?"
    menu:
        "Второй концепт":
            jump second_concept
        "Третий концепт":
            jump third_concept
        "Своя идея":
            jump idea
        "Решение":
            jump decision

label second_concept:
    g "Что за мега-идея? Давай подробнее."
    r "Вначале игрок выбирает (может, с помощью теста), какой тип личности ему соответствует. Затем начинается сюжет."
    r "Главный герой попадает в психбольницу/психдиспансер и начинается вроде типичная визуальная новелла..."
    r "Но здесь герои надо также бороться с проявлениями собственного характера."
    r "О других идеях рассказать?"
    menu:
        "Первый концепт":
            jump first_concept
        "Третий концепт":
            jump third_concept
        "Своя идея":
            jump idea
        "Решение":
            jump decision

label third_concept:
    g "Можно начать с чего-то простого."
    r "Ну, здесь все просто. Взять какой-то сеттинг и сделать все по шаблону.{p}Для тренировки перед чем-то большим, конечно."
    r "Еще?"
    menu:
        "Первый концепт":
            jump first_concept
        "Второй концепт":
            jump second_concept
        "Своя идея":
            jump idea
        "Решение":
            jump decision

label idea:
    g "Чувак, знаешь, у меня самого есть замечательная идея."
    "Я озвучил ему ту идею, что давно сидела в моей голове. К моей радости, Роге она понравилась."
    r "Что ж, тогда будем реализовывать именно ее. С тебя тогда заготовка для сценария, и концепт-арты. Я же буду дальше пилить Ren\'Py."
    jump idea_ending
    

label decision:
    g "Я понял концепты, спасибо. Я думаю..."
    menu:
         "Первый подходит":
            jump first_ending
         "Второй подходит":
            jump second_ending
         "Третий подходит":
            jump third_ending
         "Своя идея":
            jump idea
         "Ни один":
            jump junction

label junction:
         g "Ничего из этого. Не до новелл сейчас."
         "На этом разговор закончился, и сколько бы меня не уговаривали, я твердо стоял на своем."
         jump bad_ending

label diplome:
    g "Идея интересная, но дилом важнее. Извини, но я сосредоточусь на нем."
    r "Но... как же.."
    "Но я уже не слушал его. Я сделал свой выбор."
    jump bad_ending

label first_ending:
    g "Мне нравится вариант про Гамин. С чего-то знакомого начинать интереснее, да и люди оценят."
    r "Отлично, когда приступаем?"
    "Так мы и начали делать свою первую визуальную новеллу."
    return

label second_ending:
    g "Вторая идея хороша, да и близка мне. Начнем с нее."
    r "Отлично, когда приступаем?"
    "Так мы и начали делать свою первую визуальную новеллу."
    return

label third_ending:
    g "Начнем с чего-то простого."
    r "Отлично, когда приступаем?"
    "Так мы и начали делать свою первую визуальную новеллу."
    return

label idea_ending:
    "Спустя несколько дней сценарий был готов. Мы начали делать новеллу."
    "Так что – еще увидимся!"
    return

label bad_ending:
    scene bg university
    "Спустя несколько месяцев я успешно защитил диплом. Пора приступать к работе. Что же насчет авторских игр... возможно, когда-нибудь я вернусь к этой идее."
    return