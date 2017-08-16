def parse(log):
    card_nos = []
    for line in log.split('\n'):
        if line.strip() != '':
            card_nos.append(line.split(' ')[1])
    return card_nos
