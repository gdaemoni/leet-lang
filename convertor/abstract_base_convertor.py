import os
from abc import ABC
from typing import Dict
import glob


class AbstractFileConvertor(ABC):
    """Abstract base - interface for 1337 encoder / decoder
    """
    def __init__(self, key_file: [str, ...] = None, **_):
        assert key_file is None or os.path.isfile(key_file)
        self._latter_mapper = self._create_map(key_file)

    @staticmethod
    def _file_to_dict(file: str) -> dict[str, str]:
        latter_mapper = {}

        with open(file, "r") as f:
            for line in f.readlines():
                latter_mapper[line[0].lower()] = line[2:-1].replace(' ', '').split(',')[0]

        return latter_mapper

    def _create_map(self, file: [str, ...], **kwargs) -> Dict[str, str]:
        """A method for generating map (dict) for encode/decode text
        :param file: the optional path to a file with text
        :return: encode/decode dict, return empty dict if file is None
        """
        raise NotImplementedError

    def convert_text(self, input_text: str) -> str:
        raise NotImplementedError

    def _convert_text(self, input_text: str) -> str:
        """A method for the convert the text
        (encode -> decode | decode -> encode)
        :param input_text: the text to convert
        :return: converted text
        """
        for original, replace in self._latter_mapper.items():
            input_text = input_text.replace(original, replace, -1)
        return input_text

    @staticmethod
    def output_name_generator(input_file_name: str, input_prefix: str,
                              output_prefix: str, output_dir: str):
        """A method for getting output file name based on input one and prefix
        :return: output name
        """
        _, name = os.path.split(input_file_name)
        name, ext = os.path.splitext(name)
        common_suffix = name.removeprefix(input_prefix)
        return os.path.join(output_dir, f'{output_prefix}{common_suffix}{ext}')

    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str):
        """A method for converting all files
        :param input_dir: the path to an input dir
        :param input_mask: the input file pattern name
        :param output_dir: the path to an output dir
        :param input_prefix: the input prefix for _output_name_generator
        :param output_prefix: the output prefix for _output_name_generator
        :return: the list of converted strings
        """
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
