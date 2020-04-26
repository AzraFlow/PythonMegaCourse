#! python3


def getInput():
    i = 0
    text_entry = []
    while True:
        raw_string = input('Say something (\\end to quit): ')
        if raw_string == '\\end':
            break
        else:
            text_entry.append(raw_string)
            i += 1
            continue
    return text_entry


def processRawList(rawList):
    finished_output = ''
    for phrase in rawList:
        words = phrase.split(' ')
        if words[-1].endswith(('.', '!', '?')):
            punct = '  '
        elif words[-1] == '':
            punct = ''
        # could use the startswith method here
        elif check_question(words[0]):
            punct = '?  '
        else:
            punct = '.  '
        finished_output += phrase.capitalize() + punct
    return finished_output


def check_question(first_word):
    question_words = ('when', 'where', 'what', 'why', 'who', 'which',
                      'how', 'is', "what's", "how's", "whose", "who's")
    for i in range(len(question_words)):
        if first_word.lower() == question_words[i]:
            return True


print(processRawList(getInput()))
