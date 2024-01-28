from classes.player import Player
from locations.prologue import Prologue
from locations.tavern_Ragnars_Tail import TavernRagnarsTail

davion = Player("Дэвион", 100, 1, 0, [], [], [], [])

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
print(davion.say("Надо бы осмотреться здесь. Может кто-нибудь из здешних расскажет мне что-нибудь интересное?"))
choice_number = level_2.actions(["Поговорить с трактирщиком", "Поговорить с пьяными разбойниками"], [davion.say("Здравствуй, дружище."), davion.say("Как отдыхается, воины?")])