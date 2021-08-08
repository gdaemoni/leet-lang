import unittest
import os
from encode_convertor import Encoder
from decode_convertor import Decoder
from pathlib import Path

KEY_FILE = Path(os.path.dirname(__file__)) / 'key'
examples = {
	'a': '4',
	'b': '8',
	'c': '<',
	'd': '|)',
	'e': '3',
	'f': '|=',
	'g': '[',
	'h': '#',
	'i': '!',
	'j': '_|',
	'k': '|<',
	'l': '1',
	'm': '|\/|',
	'n': '|\|',
	'o': '0',
	'p': '|o',
	'q': 'O_',
	'r': '|2',
	's': '5',
	't': '7',
	'u': '|_|',
	'v': '\/',
	'w': '\^/',
	'x': '><',
	'y': '¥',
	'z': '2',
	'Test': '7357',
	'test': '7357',
	'QWERTYUIOP{} ASDFGHJKL: ZXCVBNM<>? qwertyuiop[] asdfghjkl; zxcvbnm,./': "O_\^/3|27¥|_|!0|o 45|)|=[#_||<1 2><<\/8|\||\/| O_\^/3|27¥|_|!0|o 45|)|=[#_||<1 2><<\/8|\||\/|",
	'qwertyuiop asdfghjkl zxcvbnm qwertyuiop asdfghjkl zxcvbnm': "O_\^/3|27¥|_|!0|o 45|)|=[#_||<1 2><<\/8|\||\/| O_\^/3|27¥|_|!0|o 45|)|=[#_||<1 2><<\/8|\||\/|",
}


class TestConvertor(unittest.TestCase):
	def setUp(self):
		self.encoder = Encoder(KEY_FILE)
		self.decoder = Decoder(KEY_FILE)

	def test_encoder(self):
		for key, value in examples.items():
			rez = self.encoder.convert_text(key)
			self.assertEqual(rez, value)

	def test_decoder(self):
		for key, value in examples.items():
			rez = self.decoder.convert_text(value)
			self.assertEqual(examples[rez], value)


if __name__ == '__main__':
	unittest.main()
