def format_Name(f_Name, l_Name):
    if f_Name == "" or l_Name == "":
        return "You didn't provide valid inputs."

    formatted_f_name = f_Name.title()
    formatted_l_name = l_Name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_Name(input("What is your first name? ")))

