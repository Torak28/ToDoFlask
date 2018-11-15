# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):

	def get(self):
		"""Simple static get"""
		return {'hello': 'world'}, 201

if __name__ == '__main__':
	app.run(debug=True, port=5000)
