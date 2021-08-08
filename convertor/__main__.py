import argparse
import os
from pathlib import Path
from .decode_convertor import Decoder
from .encode_convertor import Encoder

KEY_FILE = Path(os.path.dirname(__file__)) / 'key'


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('source_text',
	                    type=str,
	                    help='Returns encoded or decode text')
	return parser.parse_args().source_text


def decode():
	source_text = parse_args()
	decoder = Decoder(KEY_FILE)
	return decoder.convert_text(source_text)


def encode():
	source_text = parse_args()
	encoder = Encoder(KEY_FILE)
	return encoder.convert_text(source_text)
