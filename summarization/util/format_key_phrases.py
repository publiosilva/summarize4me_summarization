import os
import tempfile
import json

from datetime import datetime

def format_key_phrases(key_phrases_string):
    temp_file = os.path.join(tempfile.gettempdir(), str(datetime.timestamp(datetime.now())))

    with open(temp_file, 'w') as file:
        file.write(key_phrases_string)

    key_phrases = []

    with open(temp_file, 'r', encoding='utf-8') as file:
        for line in file:
            key_phrases_line = json.loads(line)

            for key_phrase in key_phrases_line['KeyPhrases']:
                key_phrase['Line'] = key_phrases_line['Line']

            key_phrases += key_phrases_line['KeyPhrases']

    return key_phrases