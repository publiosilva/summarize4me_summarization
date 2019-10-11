from nltk.tokenize import sent_tokenize


class SummaryGenerator:
    def __init__(self, full_text, key_phrases):
        self.full_text = full_text
        self.key_phrases = key_phrases
        self.ponderated_sentences = SummaryGenerator.__ponderate_sentences(full_text, key_phrases)

    def __average_weight_of_sentences(self):
        total_weight = 0
        for ps in self.ponderated_sentences:
            total_weight += ps['Weight']

        return total_weight / len(self.ponderated_sentences)

    def generate(self, minimum_weight_by_sentence = None):
        if not minimum_weight_by_sentence:
            minimum_weight_by_sentence = self.__average_weight_of_sentences()

        summary = []

        for ps in self.ponderated_sentences:
            if ps['Weight'] >= minimum_weight_by_sentence:
                summary.append({ 'text': ps['Text'], 'weight': ps['Weight'] })

        return summary

    @staticmethod
    def __ponderate_sentences(full_text, key_phrases):
        sentences = sent_tokenize(full_text)
        ponderated_sentences = []

        for key_phrase in key_phrases:
            for index, sentence in enumerate(sentences):
                if index >= len(ponderated_sentences):
                    line_number, begin_offset, end_offset = SummaryGenerator.__find_sentence_in_text(sentence, full_text)
                    ponderated_sentences.append({
                        'BeginOffset': begin_offset,
                        'EndOffset': end_offset,
                        'Weight': 0,
                        'Text': sentence,
                        'Line': line_number
                    })
                
                if key_phrase['Line'] == ponderated_sentences[index]['Line'] and key_phrase['BeginOffset'] >= ponderated_sentences[index]['BeginOffset'] and key_phrase['EndOffset'] >= ponderated_sentences[index]['EndOffset']:
                    ponderated_sentences[index]['Weight'] += key_phrase['Score']

        return ponderated_sentences

    @staticmethod
    def __find_sentence_in_text(sentence, text):
        text_lines = text.split('\n')
        
        for index, line in enumerate(text_lines):
            begin_offset = line.find(sentence)

            if begin_offset > -1:
                return index, begin_offset, begin_offset + len(sentence)

        return -1, -1, -1
