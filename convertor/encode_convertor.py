import os
from typing import Dict
from convertor.abstract_base_convertor import AbstractFileConvertor
import glob


class Encoder(AbstractFileConvertor):
	@staticmethod
	def _file_to_dict(filename):
		latter_mapper = {}

		with open(filename, "r") as f:
			for line in f.readlines():
				latter_mapper[line[0].lower()] = line[2:-1].replace(' ', '').split(',')[0]
		return latter_mapper

	def convert_text(self, input_text: str) -> str:
		lower_text = input_text.lower()
		for original, replace in self._latter_mapper.items():
			lower_text = lower_text.replace(original, replace, -1)
		return lower_text

	def _create_map(self, file: str, **kwargs) -> Dict[str, str]:
		assert file
		return self._file_to_dict(file)

	def convert_files(self, *, input_dir: str, input_mask: str,
	                  output_dir: str, input_prefix: str,
	                  output_prefix: str):
		os.makedirs(output_dir, exist_ok=True)
		for file_name in glob.glob(os.path.join(input_dir, input_mask)):
			output_name = self.output_name_generator(
				file_name,
				input_prefix,
				output_prefix,
				output_dir
			)
			with open(file_name) as file:
				with open(output_name, "w") as outfile:
					convert_text = self.convert_text(file.read())
					outfile.write(convert_text)
