################################
lemmas folder
################################
Tool: Snowball Stemmer 
File extension: .lemma




################################
NER folder
Named Entity Tagging
################################

Tool: opennlp 1.5.3 > namefind
Entity types: date, location, money, organization, percentage, person, time

Each entity type is writing in a different file. 
The extension of the file is the Entity Type, e.g., 111019.dates
We also save the entity spans (start and end index of the entity in the sentence) with an type+Spans extension e.g., 111019.datesSpans






