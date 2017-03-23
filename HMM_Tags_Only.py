import xml.etree.ElementTree as ET
from nltk.tag import hmm
import os

def parseXMLToList(pathtodir):
    filenames = os.listdir(pathtodir)
    tagged_sentences = []
    words_total = 0
    for filename in filenames:
        filename = pathtodir + "/" + filename
        e = ET.parse(filename).getroot()
        body = e.find('body')
        sentencesList = list(body.iter("S"))
        #print(len(sentencesList))

        for sentence in sentencesList:
            wordsInSentence = list(sentence.iter("W"))
            sentenceaslist = []
            for word in wordsInSentence:
                feat = word.attrib["FEAT"]
                feat_list = feat.split()
                word_tagged = (word.text, feat_list[0])
                #print(word_tagged)
                words_total+=1
                sentenceaslist.append(word_tagged)
            sentenceaslist.append((['.', '.']))
            tagged_sentences.append(sentenceaslist)

    return (tagged_sentences, words_total)


parseresult = parseXMLToList("./corpora")
sentences = parseresult[0]
words_num = str(parseresult[1])
print("Read " + str(len(sentences)) + " sentences including " + words_num + " words")

# Going to train Tagger
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train(sentences)

print(tagger.tag("он крикнул в окружение дико захохотав .".split()))
print(tagger.tag("еще ребенком я любил смотреть на звёзды .".split()))
print(tagger.tag("Лидер Жириновский крикнул в окружение дико захохотав .".split()))
print(tagger.tag("вторая мировая война началась стабильным уютным разрушением .".split()))
print(tagger.tag("кто сидел на моем стуле и сломал его .".split()))
print(tagger.tag("кто из нас ровесники кто герой кто чмо .".split()))
print(tagger.tag("капитан колесников пишет нам письмо .".split()))
print(tagger.tag("пластмассовый мир победил ликует картонный набат .".split()))