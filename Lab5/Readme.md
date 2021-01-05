# Praca z tekstem - spaCy

## Wczytywanie polskiego języka
```
!python -m spacy download pl_core_news_sm
import pl_core_news_sm
nlp = pl_core_news_sm.load()
```
## String read
```
about_text = ('Tutorial spacy do laboratrium, który jest dość długi, żeby sprawdzić inforacje')
about_doc = nlp(about_text)
print([token.text for token in about_doc])
```
## Text file read
```
file_name = 'Notatnik.txt'
file_text = open(file_name).read()
file_doc = nlp(file_text)

print([token.text for token in file_doc])
```

## Wielokropek przenosi do nowej lini
Poniższa funkcja sprawia, że w momencie wczytanie '...' przenosi tekst do nowej lini. <br>

```
def kropki(doc):
  for token in doc[:-1]:
    if token.text == '...':
      doc[token.i+1].is_sent_start = True
  return doc

text_kropki = ('To jest tekst ... zaweierajacy'
              'duza ilosc ... kropek.')
custom_nlp = pl_core_news_sm.load() 
custom_nlp.add_pipe(kropki, before='parser') 
custom_ell_doc = custom_nlp(text_kropki) 
custom_ell_sent = list(custom_ell_doc.sents) 
for sentences in custom_ell_sent:
  print(sentences)
```
## Tokenization
```
for token in about_doc:
  print (token, token.idx, token.text_with_ws,
        token.is_alpha, token.is_punct, token.is_space,
         #is_alpha - sprawdza czy znaki są z alfabetu
         #is_punct - sprawdza znaki interpunkcyjne
         #is_space szuka spacji
         #shape - kształt słowa, rozmiar liter
         #is_stop-  sprawdza czy to stop word czy nie
        token.shape_, token.is_stop)
```
## Tworzenie własnego tokenu
```
prefix_re = spacy.util.compile_prefix_regex(nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')
def customize_tokenizer(nlp):
    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,suffix_search=suffix_re.search,infix_finditer=infix_re.finditer,token_match=None)
custom_token_text = 'To-jest-mój-tokenizer'
nlp.tokenizer = customize_tokenizer(nlp)
custom_tokenizer_doc = nlp(custom_token_text)
print([token.text for token in custom_tokenizer_doc])
```
## Stop words
```
spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
  print(stop_word)

#usuwanie stop wordow
for token in about_doc:
  if not token.is_stop:
    print (token)
```

## Mierzenie częstotliwości występowania słów
```
from collections import Counter
complete_text=(about_text)
complete_doc = nlp(about_text)

words = [token.text for token in complete_doc
         if not token.is_stop and not token.is_punct]
word_freq = Counter(words)

#Najczęstsze słowa
common_words = word_freq.most_common(5)
print (common_words)

#Słowa unikatowe
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print (unique_words)

#Ropoznanie części mowy
for token in complete_doc:
  print(token, token.tag_, token.pos_, spacy.explain(token.tag_),sep=', ')
```
## Kategoryzacja
Możemy sprawdzić ile w naszym tekście występuje, rzeczowników, przymitoników itd.
```
nouns = []
adjectives = []
for token in about_doc:
    if token.pos_ == 'NOUN':
        nouns.append(token)
    if token.pos_ == 'ADJ':
        adjectives.append(token)

print(f'Rzeczowniki: {nouns}')
print(f'Przymiotniki: {adjectives}')
```
Wykrywanie czasowników
```
import textacy
about_talk_text=('Grupa kolegów chodziła całą noc, po osiedlu i rzucali kamieniami w okna.')
pattern = [{"POS": "VERB", "OP": "*"},{"POS": "ADV", "OP": "*"},{"POS": "VERB", "OP": "+"},{"POS": "PART", "OP": "*"}]
about_talk_doc = textacy.make_spacy_doc(about_talk_text, nlp)
verb_phrases = textacy.extract.matches(about_talk_doc, pattern)
for chunk in verb_phrases:
    print(chunk.text)

for chunk in about_talk_doc.noun_chunks:
    print (chunk)
```
## Wizualizacja
```
from spacy import displacy
about_displaCy_text = ('Laborka robiona na ostatnia chwile')
about_displaCy_doc = nlp(about_displaCy_text)
displacy.render(about_displaCy_doc, style='dep', jupyter=True)
```
## Wyciąnie konkretnych słów z tekstu
 W tym przypadku jest to imię i nazwisko
 
 ```
 from spacy.matcher import Matcher
def extract_full_name(nlp_doc):
    pattern = [{'POS': 'PROPN '}, {'POS': 'PROPN'}]
    matcher.add('FULL_NAME', None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text

new_text_extract="Patryk Tkaczyk jedzenie to jest test Test"
new_text_extract_doc=nlp(new_text_extract)
matcher = Matcher(nlp.vocab)
print(extract_full_name(new_text_extract_doc))

new_text_extract_eg="Gus Proto"
new_text_extract_doc_eg=nlp(new_text_extract_eg)
matcher = Matcher(nlp.vocab)
print(extract_full_name(new_text_extract_doc_eg))
 ```
Wyciąganie numeru telefonu z tekstu
```
phone_number=("To mój numer: 666 668 152")

def extract_phone_number(nlp_doc):
	pattern = [{"SHAPE": "ddd"}, {"SHAPE": "ddd"},{"SHAPE": "ddd"}]
	matcher.add('PHONE_NUMBER', None, pattern)
	matches = matcher(nlp_doc)
	for match_id, start, end in matches:
		span = nlp_doc[start:end]
		return span.text

conference_org_doc = nlp(phone_number)
extract_phone_number(conference_org_doc)
```
## Wykorzystanie NER
Wyszukiwanie konkretnych słów i ukrywanie ich
```
survey_text =('Jan Nowak nie wie co się dzieje natomiast Anna Dymna doskonale zdaje sobie sprawę, że Tomasz Kos zjadł jej czekoaldki')
def replace_person_names(token):
    if token.ent_iob != 0 and token.ent_type_ == 'persName':
        return '[Zgadnij] '
    return token.string

def redact_names(nlp_doc):
    for ent in nlp_doc.ents:
        ent.merge()
    tokens = map(replace_person_names, nlp_doc)
    return ''.join(tokens)

survey_doc = nlp(survey_text)
print(redact_names(survey_doc))
print(survey_text)
```
