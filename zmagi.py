def zmagi(_word):

    def checkword(this_word):

        # Чай
        if this_word == "чай":  # Им., В.
            outpt = "джёй"

        elif this_word == "чая":  # Р.
            outpt = "джёя"
        elif this_word == "чаев" or this_word == "чаёв":
            outpt = "джёев"

        elif this_word == "чаю":  # Д.
            outpt = "джёю"
        elif this_word == "чаям":
            outpt = "джёям"

        elif this_word == "чаем":  # Тв.
            outpt = "джёем"
        elif this_word == "чаями":
            outpt = "джёями"

        elif this_word == "чае":  # Пр.
            outpt = "джёе"
        elif this_word == "чаях":
            outpt = "джёях"

        # Дача
        elif this_word == "дача":   # Им., В.
            outpt = "тоджо"
        elif this_word == "дачи":   # Им. мн., Р. ед., В. мн.
            outpt = "тоджы"

        elif this_word == "дач":    # Р. мн.
            outpt = "тодж"

        elif this_word == "даче":   # Д.
            outpt = "тодже"
        elif this_word == "дачам":
            outpt = "тоджам"

        elif this_word == "дачей":  # Тв.
            outpt = "тоджей"
        elif this_word == "дачами":
            outpt = "тоджами"

        elif this_word == "даче":   # Пр.
            outpt = "тодже"
        elif this_word == "дачах":
            outpt = "тоджах"

        # Трамвай
        elif this_word == "трамвай":    # Им., В.
            outpt = "драмфое"
        elif this_word == "трамваи":
            outpt = "драмфои"

        elif this_word == "трамвая":    # Р.
            outpt = "драмфоя"
        elif this_word == "трамваев":
            outpt = "драмфоев"

        elif this_word == "трамваю":    # Д.
            outpt = "драмфою"
        elif this_word == "трамваям":
            outpt = "драмфоям"

        elif this_word == "трамваем":   # Тв.
            outpt = "драмфоем"
        elif this_word == "трамваями":
            outpt = "драмфоями"

        elif this_word == "трамве":    # Пр.
            outpt = "драмфое"
        elif this_word == "трамваях":
            outpt = "драмфоях"

        # День
        elif this_word == "день":   # Им., В.
            outpt = "вонд"
        elif this_word == "дни":
            outpt = "вонды"

        elif this_word == "дня":    # Р.
            outpt = "вонда"
        elif this_word == "дней":
            outpt = "вондов"

        elif this_word == "дню":    # Д.
            outpt = "вонду"
        elif this_word == "дням":
            outpt = "вондам"

        elif this_word == "днем" or this_word == "днём":   # Тв.
            outpt = "вондом"
        elif this_word == "дней":
            outpt = "вондами"

        elif this_word == "дне":    # Пр.
            outpt = "вонде"
        elif this_word == "днях":
            outpt = "вондах"

        # Древнезмагийский
        elif this_word == "зфчшбч":
            outpt = "чай"

        else:
            outpt = this_word

        return outpt

    def relit(lit):

        # Согласные
        if lit == "с":
            altlit = "з"
        elif lit == "з":
            altlit = "с"

        elif lit == "д":
            altlit = "т"
        elif lit == "т":
            altlit = "д"

        elif lit == "ж":
            altlit = "ш"
        elif lit == "ш":
            altlit = "ж"

        elif lit == "щ":
            altlit = "җ"    # расш. кир.
        elif lit == "җ":
            altlit = "щ"

        elif lit == "б":
            altlit = "п"
        elif lit == "п":
            altlit = "б"

        elif lit == "в":
            altlit = "ф"
        elif lit == "ф":
            altlit = "в"

        elif lit == "г":
            altlit = "к"
        elif lit == "к":
            altlit = "г"

        elif lit == "ч":
            altlit = "дж"    # кир.

        elif lit == "й":
            altlit = "e"
        elif lit == "e":
            altlit = "й"

        # Гласные
        elif lit == "о":
            altlit = "а"
        elif lit == "а":
            altlit = "о"

        elif lit == "е":
            altlit = "и"
        elif lit == "и":
            altlit = "е"

        elif lit == "э":
            altlit = "ͷ"    # греч.
        elif lit == "ͷ":
            altlit = "э"

        # elif lit == "у":
        #     altlit = "ю"
        # elif lit == "ю":
        #     altlit = "у"

        # elif lit == "я":
        #    altlit = "a"    # лат.
        # elif lit == "a":
        #    altlit = "я"

        else:
            altlit = lit
        return altlit

    zmagi_word = ""
    t_word = checkword(_word)

    if t_word == _word:
        for i in range(len(_word)):
            zmagi_word += relit(_word[i])
    else:
        zmagi_word += t_word

    return zmagi_word

