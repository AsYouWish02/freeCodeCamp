full_dot = '●'
empty_dot = '○'

def create_character(name_character, strength, intelligence,charisma):
        #name_character check
    if not isinstance(name_character, str):
        return 'The character name should be a string'
    elif not name_character:
        return 'The character should have a name'  
    elif len(name_character) > 10:
        return 'The character name is too long'
    elif ' ' in name_character:
        return 'The character name should not contain spaces'

        #strength, intelligence, charisma check
    if any(not isinstance(stat, int) for stat in [strength, intelligence, charisma]):
    #if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
    #if any(type(stat) is not int for stat in [strength, intelligence, charisma]):
    #if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return 'All stats should be integers'
    #elif any(stat < 1 for stat in [strength, intelligence, charisma]):
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    #elif any(stat > 4 for stat in [strength, intelligence, charisma]):
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
    #elif sum([strength + intelligence + charisma]) != 7:
        return 'The character should start with 7 points'

    #Note: While str and int are common abbreviations for the stats, Python also uses those names for its string and integer types, so it's best if you avoid using them as variable names.

    strength_bar = strength * full_dot + (empty_dot * (10 - strength))
    intelligence_bar = intelligence * full_dot + (empty_dot * (10 - intelligence))
    charisma_bar = charisma * full_dot + (empty_dot * (10 - charisma))

    return f'{name_character}\nSTR {strength_bar}\nINT {intelligence_bar}\nCHA {charisma_bar}'
    
    #else:
        #return f'{name_character}\nSTR {strength * full_dot + (empty_dot * (10 - strength))}\nINT {intelligence * full_dot + (empty_dot * (10 - intelligence))}\nCHA {charisma * full_dot + (empty_dot * (10 - charisma))}'


create_character('ren', 4, 2, 1)
