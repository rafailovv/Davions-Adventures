from classes.npc import NPC

class TavernRagnarsTail():
    """ Класс для локации Таверна "Хвост Рагнара" """

    def __init__(self, game):
        """ Инициализируем класс уровня Таверна "Хвост Рагнара" """
        self.game = game
        self.settings = game.settings
        self.davion = game.davion

        # Инициализируем стартовые параметры уровня
        self.level_name = 'Таверна "Хвост Рагнара"'
        self.start_text = """Первым место, куда забрел Дэвион стала таверна "Хвост Рагнара"."""
        self.is_drunken_robbers_in_tavern = True

        # Инициализиурем настройки NPC
        self.rigvarl = NPC(self, self.settings.rigvarl_name, ["Чего тебе, путник?",
                                                              "С чего это мне тебе рассказывать, как тут дела? И без любопытствующих хорошо.",
                                                              "Не видишь что-ли? Пьют! Достали уже, вот бы прогнал их кто-нибудь..."])
                                                              
        self.drunken_robbers = NPC(self, self.settings.drunken_robbers_name, ["У тебя какие-то проблемы, мальчишка?",
                                                                              "Проваливай отсюда, придурок!",
                                                                              "Мы с тобой еще разберемся..."])

    def start_level(self):
        """ Запускает уровень """

        # Выводит название локации и стартовый текст
        print(self.level_name)
        print()
        print(self.start_text)
        print(self.davion.say("Надо бы осмотреться здесь. Может кто-нибудь из здешних расскажет мне что-нибудь интересное?"))
        self._kick_drunken_robbers_quest()
    
    def _kick_drunken_robbers_quest(self): # TODO Рефакторинг кода
        """ Запускает квест - выгнать Пьяных разбойников из таверны и поговорить с Ригварлом """
        
        # Запускаем цикл квеста
        while True:
            available_actions = ["Поговорить с Ригварлом"]
            if self.is_drunken_robbers_in_tavern:
                available_actions.append("Поговорить с Пьяными разбойниками")
            self._actions(available_actions)

            # Ждем выбора действий от пользователя
            selected_action_index = int(input()) - 1 # TODO Сделать метод для проверки ввода

            # Идем к Ригварлу
            if selected_action_index == 0:
                if self.is_drunken_robbers_in_tavern:
                    print(self.davion.say("Здравствуй, дружище!"))
                    print(f"{self.rigvarl.name}: {self.rigvarl.phrases[0]}")

                    possible_answers, selected_answer_index = [], float("-inf")

                    while len(possible_answers) - 1 != selected_answer_index:
                        possible_answers = ["Расскажи-ка мне, как дела обстоят вообще здесь?", "Что эти разбойники здесь забыли", "*Отойти*"] # TODO Добавить дерево диалогов
                        selected_answer_index = self._dialog_variants(self.davion.name, possible_answers)
                    
                        # Проверка на выход из диалога 
                        if selected_answer_index == len(possible_answers) - 1:
                            break
                        else:
                            print(f"{self.rigvarl.name}: {self.rigvarl.phrases[1 + selected_answer_index]}")
                else:
                    print(self.davion.say("Здравствуй, дружище!"))
                    print(f"{self.rigvarl.name}: {self.rigvarl.phrases[0]}")

                    possible_answers, selected_answer_index = [], float("-inf")

                    possible_answers = ["Расскажи-ка мне, как дела обстоят вообще здесь?", "*Отойти*"] # TODO Добавить дерево диалогов
                    selected_answer_index = self._dialog_variants(self.davion.name, possible_answers)
                        
                    # Проверка на выход из диалога 
                    if selected_answer_index == len(possible_answers) - 1:
                        continue
                    else:
                        print(f"{self.rigvarl.name}: {self.rigvarl.phrases[1 + selected_answer_index]}")
                        break
            # Идем к разбойникам
            elif selected_action_index == 1:
                print(self.davion.say("Как отдыхается, воины?"))
                print(f"{self.drunken_robbers.name}: {self.drunken_robbers.phrases[0]}")
                print(self.davion.say("Да нет, хотел узнать, нет ли у вас проблем?"))
                print(f"{self.drunken_robbers.name}: {self.drunken_robbers.phrases[1]}")
                print(self.davion.say("Видимо, придется преподать вам урок!"))
                print("Fight")
                print(f"{self.drunken_robbers.name}: {self.drunken_robbers.phrases[2]}")
                self.is_drunken_robbers_in_tavern = False
                self.rigvarl.phrases.pop()
                self.rigvarl.phrases.pop()
                self.rigvarl.phrases.append("Ого, ты прогнал этих разбойников. Видимо, ты не такой уже и сопливый. Ладно, слушай...")

        print("История продолжается") # TODO Доделать историю

    def _actions(self, actions: list):
        """ Метод, выводящий последовательность возможных действий на экран """
        if actions:
            for i in range(len(actions)):
                print(f"{i + 1}. {actions[i]}")
    
    def _dialog_variants(self, name, variants: list):
        """ Выводит список возможных фраз и действий для персонажа, выводит выбранную опцию и возвращает индекс выбранной им опции """
        if variants:
            print(f"{name}:")
            for i in range(len(variants)):
                print(f"{i + 1}. {variants[i]}")
            
            selected_variant_index = int(input()) - 1 # TODO Сделать метод для проверки ввода
            print(f"{name}: {variants[selected_variant_index]}")
            return selected_variant_index