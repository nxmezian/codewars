def to_camel_case(text):
    if text == "":
         return text
    if "_" in text:
        text = text.split("_")
    elif "-" in text:
         text = text.split("-")
    new_text =""
    new_text += text[0]
    for i in text[1:]:
            new_text += i.capitalize()

    return new_text


print(to_camel_case("APippi-was-hungry"))