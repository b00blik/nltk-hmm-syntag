## Synopsis
Repo contains training NLTK Hidden Markov Model by Russian National Corpus (SyntagRus) and parsing this corpus.
There are not texts of corpus due to license. Example of corpus text structure: 

<body>
<S ID="99">
<W DOM="_root" FEAT="PR" ID="1" LEMMA="ПО">По</W> 
<W DOM="1" FEAT="S МН ЖЕН ДАТ НЕОД" ID="2" LEMMA="СТРАНИЦА" LINK="предл">страницам</W> 
<W DOM="4" FEAT="A ЕД ЖЕН РОД" ID="3" LEMMA="ВСЕМИРНЫЙ" LINK="опред">Всемирной</W> 
<W DOM="2" FEAT="S ЕД ЖЕН РОД НЕОД" ID="4" LEMMA="ИСТОРИЯ" LINK="квазиагент">истории</W> 
</S>
</body>

HMM_Tags_Only.py contains training with only parts of speech (NOUN, ADJ, etc).
HMM_ext_tags.py contains training with full string of FEAT field.