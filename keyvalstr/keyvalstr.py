class KeyValStr(object):
    """A simple key value format string."""

    def __init__(self, parser, default_value=None):
        """To initialize the parser.

        @param parser: The string contain the key value
        @type  param: str

        @param default_value: A default value if the key as not value
        @type  param: str

        @raise ValueError: The parser must be a string and not empty
        """
        if not parser or not isinstance(parser, str):
            raise ValueError('The parser must be a string and not empty')

        self.parser = parser
        self.default_value = default_value

    @staticmethod
    def _get_value(index, obj):
        result = [item.strip() for item in obj[index].split(':')]
        return result[1]

    def _index(self, string, obj=None):
        if not obj:
            obj = self.parser

        result = None

        for index, value in enumerate(obj):
            split_value = value.split(':')

            if string in value and split_value[0] == string:
                result = index
                break

        return result

    def get_value(self, key):
        """Return the value associate to the key. If the key is not found
        or has no value None is return.

        @param key: The key
        @type key: str

        @return: The key
        @rtype : str
        """
        parser_split = [item.strip() for item in self.parser.split(',')]

        try:
            index = parser_split.index(key)
        except ValueError:
            index = self._index(key, obj=parser_split)

            if index is None:
                return index

            return self._get_value(index, parser_split)

        index = self._index('default', obj=parser_split)

        if index is None:
            return self.default_value if self.default_value else None

        return self._get_value(index, parser_split)
