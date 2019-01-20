import pygame
import sqlite3


class Database:
	def __init__(self, score, time):
		self.score = score
		self.time = time
		self.create_database()

	def create_database(self):
		self.conn =sqlite3.connect('game.db')
		self.c=self.conn.cursor()

		self.conn.execute('''
			CREATE TABLE IF NOT EXISTS GAME
				(score INTEGER NOT NULL,
				second INTEGER NOT NULL)
		''')

		self.conn.execute('''INSERT INTO GAME (score, second) VALUES (?, ?)''', (self.score, self.time))

		self.conn.commit()
		self.conn.close()

