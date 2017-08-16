from xml.etree.ElementTree import XML

def parse_log(log):
    card_nos = []
    for line in log.split('\n'):
        if line.strip() != '':
            card_nos.append(line.split(' ')[1])
    return card_nos


def parse_card_title(cards):
    titles = []
    for card in cards:
        titles.append(XML(card.content).find("name").text)
    return titles
