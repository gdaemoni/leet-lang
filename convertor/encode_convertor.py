from typing import Dict
from convertor.abstract_base_convertor import AbstractFileConvertor
import re
import string


class Encoder(AbstractFileConvertor):

	def _create_map(self, file: str, **kwargs) -> Dict[str, str]:
		assert file
		return self._file_to_dict(file)

	def convert_text(self, input_text: str) -> str:
		input_text = self._prepare_text_source(input_text)
		return self._convert_text(input_text.lower())

	@staticmethod
	def _prepare_text_source(text: str):
		return re.sub(f"[{re.escape(string.punctuation)}]", '', text.lower())
