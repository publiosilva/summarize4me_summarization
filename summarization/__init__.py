from flask import Flask
from flask_restful import Api
from flask_script import Manager

from summarization.resources import index_resource, summarization_resource

app = Flask(__name__)
app.config.from_object('instance.config.DevelopmentConfig')

api = Api(app)

manager = Manager(app)

api.add_resource(index_resource.IndexResource, '/')
api.add_resource(summarization_resource.SummarizationResource, '/summarize')