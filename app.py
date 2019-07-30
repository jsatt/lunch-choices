from datetime import datetime
from random import choice
from textwrap import dedent

from flask import Flask

app = Flask(__name__)

@app.route('/')
def choose_lunch():
    random_choice = get_random_lunch()

    output = dedent(f'''
    Random Choice:
    {random_choice}

    Today's Specials:
    ''')

    specials = get_todays_specials()
    if specials:
        output += '\n'.join(specials)
    else:
        output += 'No specials today'

    return f'<pre>{output}</pre>'


def get_random_lunch():
    with open('lunch_choices.txt') as f:
        opts = f.readlines()
    return choice(opts)


def get_todays_specials():
    day = datetime.now().strftime('%A')
    specials = []
    with open('lunch_specials.txt') as f:
        reading = False
        for line in f.readlines():
            line = line.strip()
            if reading:
                if line == '##':
                    break
                specials.append(line)
            elif line == f'#{day}':
                reading = True
    return specials


if __name__ == '__main__':
    app.run()
