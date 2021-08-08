from convertor.abstract_base_convertor import AbstractFileConvertor


class Decoder(AbstractFileConvertor):

	def _create_map(self, file: str, **kwargs) -> dict[str, str]:
		assert file
		latter_mapper = self._file_to_dict(file)
		sorted_latter_mapper = {}

		for i in sorted(latter_mapper.items(), key=lambda x: len(x[1]), reverse=True):
			sorted_latter_mapper[i[1]] = i[0]
		return sorted_latter_mapper

	def convert_text(self, input_text: str) -> str:
		return self._convert_text(input_text)
