# Use this by editing the alphabet list with the desired characters in order.
# The priority list can contain a list of characters, indicating that they are treated the same.
# Any items not in the priority list will be put at the end.

# Usage:
# alph = Alphabetizer()
#
# sorted_word_list = alph.sorted(list_of_strings)
# sorted_obj_list  = alph.sorted(list_of_objects, key=lambda obj: obj.some_id)

class Alphabetizer():
    """Alphabetizes lists according to a custom alphabetical order"""

    _priority_list = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z"
    ]

    def __init__(self):
        self._priority_map = self._generate_mapping(self._priority_list)

    def _generate_mapping(self, array):
        """Turns the priority array into a dictionary that can be queried during sort."""
        mapping = {}

        priority = 0
        for item in array:
            if isinstance(item, list):
                for subitem in item:
                    mapping[subitem] = priority
            else:
                mapping[item] = priority

            priority += 1

        return mapping

    def _get_sort_key(self, char):
        """Returns a key for sorting the given character"""

        comp_char = char.lower()
        if comp_char in self._priority_map:
            return self._priority_map[comp_char]
        else:
            return len(self._priority_list)

    def sorted(self, element_list, key=lambda element: element):
        """Returns the input list in sorted order."""

        return sorted(
            element_list,
            key=lambda element: [self._get_sort_key(char) for char in key(element)]
        )
