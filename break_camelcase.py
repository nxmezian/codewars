#break up a string if it's in camel case

import re

def break_camelcase(string):
    output = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return output

print(break_camelcase("helloHelloHello"))

