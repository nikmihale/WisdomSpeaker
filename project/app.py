#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, Flask

class Actions:
	def __init__(self):
		self.response = 'Попробуйте передать в GET 3 полоски'

	def speakWisdom(self):	
		self.response = 'Хардбасс тусовки адидас кроссовки'

def create_app():
	app=Flask(__name__)
	@app.route('/wisdomSpeaker')
	def WisdomSpeaker():
		stripesAmount = request.args.get('poloski')
		actions = Actions()		
		if stripesAmount == '3':
			actions.speakWisdom()
		return actions.response
	return app


if __name__ == '__main__':
	app=create_app()
	app.run()
