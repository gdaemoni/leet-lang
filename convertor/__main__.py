import argparse
import re
import string
from .decode_convertor import Decoder
from .encode_convertor import Encoder

KEY_FILE = '/home/wepos/Desktop/leet-lang/convertor/key'


def prepare_text_source(text: str):
	return re.sub(f"[{re.escape(string.punctuation)}]", '', text.lower())


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('source_text',
	                    type=str,
	                    help='Returns encoded or decode text')
	return parser.parse_args()


def decode():
	source_text = parse_args().source_text
	# source_text = prepare_text_source(source_text)
	decoder = Decoder(KEY_FILE)
	print(decoder.convert_text(source_text))


def encode():
	source_text = parse_args().source_text
	# source_text = prepare_text_source(source_text)
	encoder = Encoder(KEY_FILE)
	print(encoder.convert_text(source_text))
