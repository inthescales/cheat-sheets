# Based on work by Jannis Mainzyk
# https://gist.github.com/jannismain/e96666ca4f059c3e5bc28abb711b5c92

# To use, change the `_encode_list` and `_encode_dict` methods as desired to
# control which lines should be condensed or expanded.

import json

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.indentation_level = 0

    def encode(self, obj):
        if isinstance(obj, list):
        	return self._encode_list(obj)
        elif isinstance(obj, dict):
            return self._encode_dict(obj)

        return json.dumps(
            obj,
            skipkeys=self.skipkeys,
            ensure_ascii=self.ensure_ascii,
            check_circular=self.check_circular,
            allow_nan=self.allow_nan,
            sort_keys=self.sort_keys,
            indent=self.indent,
            separators=(self.item_separator, self.key_separator),
            default=self.default if hasattr(self, "default") else None,
        )

    def _encode_list(self, list_in):
        """Encode a list."""

        if False:
            # Use this to keep the list on a single line
            return "[" + ", ".join([self.encode(element) for element in list_in]) + "]"
        else:
            # Use this to put each element on its own line
            self.indentation_level += 1
            output = [self.indent_str + self.encode(element) for element in list_in]
            self.indentation_level -= 1

            return "[\n" + ",\n".join(output) + "\n" + self.indent_str + "]"

    def _encode_dict(self, dict_in):
        """Encode a dict."""

        if not dict_in:
            return "{}"

        if False:
            # Use this to keep the dict on a single line
            return (
                "{ "
                + ", ".join(
                    [self.encode(key) + ": " + self.encode(val) for (key, val) in dict_in.items()]
                )
                + " }"
            )
        else:
            # Use this to put each element on its own line
            self.indentation_level += 1
            output = [self.indent_str + self.encode(key) + ": " + self.encode(val) for (key, val) in dict_in.items()]
            self.indentation_level -= 1

            return "{\n" + ",\n".join(output) + "\n" + self.indent_str + "}"

    @property
    def indent_str(self) -> str:
        """Whitespace string to be used for indentation."""

        if isinstance(self.indent, int):
            return " " * (self.indentation_level * self.indent)
        elif isinstance(self.indent, str):
            return self.indentation_level * self.indent
        else:
            raise ValueError(
                "indent must either be of type int or str (is " + str(type(self.indent)) + ")"
            )
