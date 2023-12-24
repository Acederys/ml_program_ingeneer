from transformers import pipeline
from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,

    Doc, AddrExtractor, MoneyExtractor, DatesExtractor
)
classifier = pipeline('translation','Helsinki-NLP/opus-mt-en-ru')
with open('test_text.txt', 'r', encoding='utf-8') as file:
    string = file.read()
Values_list = classifier(string)[0]
Values = Values_list['translation_text']



# работа с бибоиотекой Наташа
segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)

# предаем переведенное предложение в переменную для работы с бибоиотекой
doc = Doc(Values)

doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)
doc.tag_ner(ner_tagger)
doc.segment(segmenter)
# показывает токены в тексте
print(f'Данный текст содержит токены: {doc.tokens[1:]}')

# показывает разбивку по предложениям
print(f'Данный текст разбит на предложения: {doc.sents[:5]}')

# показывает разбивку на слово - часть речи
print(f'Данный текст содержит части речи:')
doc.tag_morph(morph_tagger)
doc.sents[0].morph.print()
# показывает модель
print(f'Данный текст содержит синтаксическую модель:')
doc.parse_syntax(syntax_parser)
doc.sents[0].syntax.print()

#Разбив на сущности
print(f'Данный текст содержит сущности:')
doc.tag_ner(ner_tagger)
doc.ner.print()

# приводит сущности к начальному виду
for span in doc.spans:
    span.normalize(morph_vocab)
print(f'Сущности приведены кначальному виду:{doc.spans[:5]}')
{_.text: _.normal for _ in doc.spans if _.text != _.normal}


