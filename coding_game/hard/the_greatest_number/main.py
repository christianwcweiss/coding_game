class Solution:
    @staticmethod
    def solve(n: int, characters: str) -> float:
        character_list = characters.split()
        is_negative = "-" in character_list
        contains_dot = "." in character_list
        if is_negative:
            character_list.remove("-")
            character_list = sorted(character_list)
            if contains_dot:
                character_list.remove(".")
                character_list.insert(1, ".")
            character_list.insert(0, "-")

        else:
            character_list = sorted(character_list, reverse=True)
            if contains_dot:
                character_list.remove(".")
                character_list.insert(-1, ".")

        while character_list[-1] in {".", "0"} and "." in character_list:
            character_list.pop()

        return float("".join(character_list)) if "." in character_list else int("".join(character_list))
