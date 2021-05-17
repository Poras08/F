import random
import re
import string
import urllib.parse


class ExpansionError(Exception):
    pass


START_SYMBOL = "<start>"
RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')

test_string = list(string.printable)
final = []
for i in test_string:
    final.append(urllib.parse.quote(i))

CHARACTERS_WITHOUT_QUOTE = (string.digits
                            + string.ascii_letters
                            + string.punctuation.replace('"', '').replace('\\', '')
                            + ' ')


def nonterminals(expansion):
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return re.findall(RE_NONTERMINAL, expansion)


def simple_grammar_fuzzer(grammar, start_symbol=START_SYMBOL,
                          max_nonterminals=10, max_expansion_trials=100,
                          log=False):
    term = start_symbol
    expansion_trials = 0
    while len(nonterminals(term)) > 0:
        symbol_to_expand = random.choice(nonterminals(term))
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        new_term = term.replace(symbol_to_expand, expansion, 1)

        if len(nonterminals(new_term)) < max_nonterminals:
            term = new_term
            if log:
                print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                raise ExpansionError("Cannot expand " + repr(term))

    while "RANDOM_GRAMMAR_STRING" in term:
        term = term.replace("RANDOM_GRAMMAR_STRING", random_generator(final), 1)
    while "RANDOM_INT" in term:
        term = term.replace("RANDOM_INT", str(random.randint(1, 1165418181)), 1)

    return term


def random_generator(entry):
    return ''.join(random.choice(entry) for _ in range(random.randint(1, 20)))
