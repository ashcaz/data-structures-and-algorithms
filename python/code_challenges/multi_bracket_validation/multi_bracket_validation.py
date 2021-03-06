def multi_bracket_validation(str_input: str) -> bool:
    """[this method figures out whether or not the brackets in the string are balanced]

    Args:
        str_input (str): [description]

    Returns:
        bool: [outputs true or false depending on if the string is balanced]
    """
    # FIRST SOLUTION
    # brackets = {
    #     "{": 0,
    #     "[": 0,
    #     "(": 0,
    # }

    # for character in str_input:
    #     try:
    #         brackets[character] += 1
    #     except KeyError:
    #         if character == "}":
    #             brackets["{"] -= 1
    #         elif character == "]":
    #             brackets["["] -= 1
    #         elif character == ")":
    #             brackets["("] -= 1

    # print(brackets)

    # #i got the any() from stackoverflow
    # if any(value < 0 for value in brackets.values()):
    #     return False

    # elif any(value >= 1 for value in brackets.values()):
    #     return False

    # return True

    # Second Attempt
    if not len(str_input):
        raise Exception("Method can not be ran with an empty string")

    modified_stack = []
    last_index = len(modified_stack) - 1
    open_brackets = ["{", "(", "["]
    closed_brackets = ["}", ")", "]"]

    for character in str_input:
        print(character)
        if character in open_brackets:
            modified_stack.append(character)
        elif character in closed_brackets:
            if not len(modified_stack):
                return False
            if modified_stack[last_index] == "(" and character == ")":
                modified_stack.pop()
            elif modified_stack[last_index] == "{" and character == "}":
                modified_stack.pop()
            elif modified_stack[last_index] == "[" and character == "]":
                modified_stack.pop()
            else:
                return False

    if len(modified_stack) > 0:
        return False

    return True