from classes.player import Player
from classes.npc import npc
from locations.prologue import Prologue
from locations.tavern_Ragnars_Tail import TavernRagnarsTail

davion = Player("Дэвион", 100, 1, 0, [], [], [], [])

rigvarl = npc("Ригварл")
drunken_robbers = npc("Пьяные разбойники")

print("Игра началась!\n")

level_1 = Prologue(davion, "Пролог")
text = f"""Однажды, задолго до времени, Вечная темнота поглащала весь мир.
Тогда, принцесса Селемине в поисках уничтожения необратимого попала в лапы великого и ужасного дракона Рагнара.
Придворный маг дракона - Эредар, обманом заманил принцессу в ловушку и наложил оцепеняющее заклятие.
Перед тем как пасть, Селемине успела воззвать к своему верному рыцарю {davion.name}у.
Рыцарь услышал свою повелительнцу и пошел к ней на помощь..."""

level_1.start(text)

# Prologue ends

level_2 = TavernRagnarsTail(davion, 'Таверна "Хвост Рагнара"')
text = f"""Первым место, куда забрел {davion.name} стала {level_2.location_name}."""

level_2.start(text)

# Set level triggers
drunken_robbers_in_tavern = True

print(davion.say("Надо бы осмотреться здесь. Может кто-нибудь из здешних расскажет мне что-нибудь интересное?"))

while True:
    if drunken_robbers_in_tavern:
        choice_number = level_2.actions(["Поговорить с трактирщиком", "Поговорить с пьяными разбойниками"], [davion.say("Здравствуй, дружище."), davion.say("Как отдыхается, воины?")])
    else:
        choice_number = level_2.actions(["Поговорить с трактирщиком"], [davion.say("Здравствуй, дружище.")])

    if choice_number == 1:
        print(rigvarl.say("Чего тебе, путник?"))
        if drunken_robbers_in_tavern:
            while True:
                variants = [davion.say("Расскажи-ка мне, как дела обстоят вообще здесь?"), davion.say("Что эти разбойники здесь забыли?"), "Отойти"]
                choice_number = level_2.dialog(variants)
                if choice_number == 1:
                    print(rigvarl.say("С чего это мне тебе рассказывать, как тут дела? И без любопытствующих хорошо"))
                elif choice_number == 2:
                    print(rigvarl.say("Не видишь что-ли? Пьют! Достали уже, вот бы прогнал их кто-нибудь..."))
                elif choice_number == 3:
                    break
            if choice_number == 3:
                continue
        else:
            while True:
                variants = [davion.say("Расскажи-ка мне, как дела обстоят вообще здесь?"), "Отойти"]
                choice_number = level_2.dialog(variants)
                if choice_number == 1:
                    print(rigvarl.say("Ого, ты прогнал их, видимо не такой уж ты и сопливый. Ну слушай..."))
                    break
                elif choice_number == 2:
                    break
            if choice_number == 1:
                break
            elif choice_number == 2:
                continue
    elif choice_number == 2:
        print(drunken_robbers.say("У тебя какие-то проблемы, мальчишка?"))
        print(davion.say("Да нет, хотел узнать, нет ли у вас проблем?"))
        print(drunken_robbers.say("Проваливай отсюда, придурок!"))
        print(davion.say("Видимо, придется преподать вам урок!"))
        
        # Fight
        print("Fight")

        print(davion.say("Думаю, вы найдете другое место отдохнуть, да?"))
        print(drunken_robbers.say("Мы с тобой еще разберемся..."))
        print("Разбойники уходят из таверны")
        drunken_robbers_in_tavern = False

print("История продолжается")