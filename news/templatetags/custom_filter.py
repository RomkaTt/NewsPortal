from django import template

register = template.Library()

words = {
    'китайский': True,
    'февраля': True,
    'Южной': True,
    'VR': True,
    'оборудование': True,
    'систем': True
}


@register.filter()
def censor(value: str) -> str:
    try:
        if not isinstance(value, str):
            raise Exception('Error')
        a = value
        for word in list(words.keys()):
            if word in a:
                a = a.replace(word[1:], '*' * len(word[1:]))
        return a
    except Exception as e:
        print(e)
