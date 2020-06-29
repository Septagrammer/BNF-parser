with open("data.txt", "r") as myfile:
    data = myfile.readlines()

servTokens = ['::=', '+', '|']


def makeRulesFromSet(set):
    rules = []
    rule = ''
    leftToken = set[0]
    for index, token in enumerate(set):
        if token == '|':
            rules.append(rule)
            rule = leftToken + ' ::= '
            continue

        rule = rule + ' ' + token + ' '
    rules.append(rule)

    return rules


def stripTokens(tokens):
    rules = []
    rule = []
    for index, token in enumerate(tokens):
        if index + 2 >= tokens.__len__():
            rule.append(token)
            rule.append(tokens[index + 1])
            rules.append(rule)
            break

        if tokens[index + 2] == '::=':
            rule.append(token)
            rules.append(rule)
            rule = []
        else:
            rule.append(token)

    return rules


def getTokens(data):
    tokens = []
    for line in data:
        if line.startswith('--'):
            pass
        token = None
        for index, char in enumerate(line):
            if char.isspace():
                if token == None:
                    pass
                else:
                    tokens.append(token)
                    token = None
                pass
            else:
                if token == None:
                    token = char
                else:
                    token = token + str(char)
            if index + 1 == len(line):
                tokens.append(token)
                token = None

    return tokens


def preprocessTokens(tokens):
    for index, token in enumerate(tokens):
        if token == None or token == '<space>':
            del tokens[index]

    return tokens


def __main__():
    tokens = preprocessTokens(getTokens(data))
    strippedTokens = stripTokens(tokens)
    rules = []
    for set in strippedTokens:
        rules += makeRulesFromSet(set)
    file = open("d.txt", "a")
    file.truncate(0)
    for index, rule in enumerate(rules):
        file.write(str(index) + '  ' + rule + '\n')
    file.close()



__main__()
