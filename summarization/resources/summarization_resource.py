from flask_restful import Resource, reqparse

from datetime import datetime

from summarization.services.summarization_service import SummaryGenerator
from summarization.util.format_key_phrases import format_key_phrases


class SummarizationResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('full_text', required = True)
        self.parser.add_argument('key_phrases', required=True)

    def post(self):
        data = self.parser.parse_args()

        try:
            full_text = data['full_text']
            key_phrases = format_key_phrases(data['key_phrases'])

            summary = SummaryGenerator(full_text, key_phrases).generate()

            return {'summary': summary}
        except Exception as e:
            print(e)
            return {'message': 'Error in summarizing'}, 400

    class FileToUpload:
        def __init__(self, file):
            self.file = file

        def save(self):
            try:
                filename = datetime.timestamp(datetime.now())
                file_path = path.join('/uploads', filename, '.txt')
                self.file.save(file_path)

                return file_path
            except:
                raise Exception('Error saving file')