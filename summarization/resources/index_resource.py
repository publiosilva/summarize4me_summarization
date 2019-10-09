from flask_restful import Resource

class IndexResource(Resource):
    def get(self):
        return {
            'ApplicationName': 'SummarizationService',
            'ApplicationVersion': '1.0',
        }