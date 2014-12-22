#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""pikalang.

A brainfuck derivative based off the vocabulary of Pikachu from Pokémon.

Copyright (c) 2014 Blake Grotewold
"""

__version__ = "0.1.0"

import os
import argparse
import ply.lex as lex


class PikalangLexer:

    """Token lexer for Pikalang."""

    # List of token names
    tokens = (
        'DECREMENTPOINTER',
        'INCREMENTPOINTER',
        'OUTPUT',
        'INPUT',
        'INCREMENTBYTE',
        'DECREMENTBYTE',
        'JUMPFORWARD',
        'JUMPBACKWARD',
        'COMMENT'
    )

    # Regular expression rules for tokens
    t_DECREMENTPOINTER = r'\bpichu\b'
    t_INCREMENTPOINTER = r'\bpipi\b'
    t_OUTPUT = r'\bpikachu\b'
    t_INPUT = r'\bpikapi\b'
    t_INCREMENTBYTE = r'\bpi\b'
    t_DECREMENTBYTE = r'\bka\b'
    t_JUMPFORWARD = r'\bpika\b'
    t_JUMPBACKWARD = r'\bchu\b'
    t_COMMENT = r'[^\s]+'

    t_ignore = ' \t\n\r'

    def t_newline(self, t):
        """Token for line numbers.

        This allows us to keep track of what line number for error reporting.
        """
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        """Error handling rule."""
        print("Illegal character {}".format(t.value[0]))
        t.lexer.skip(1)

    def __init__(self, **kwargs):
        """Build the lexer."""
        self.lexer = lex.lex(module=self, **kwargs)

    def load(self, data):
        """Load data into lexer.

        Returns list of tokens.
        """
        self.lexer.input(data)


lexer = PikalangLexer()

# Next up.... Parse


def main():
    """Main entrypoint for application."""
    parser = argparse.ArgumentParser(
        prog='pikalang',
        description='a Pikalang interpreter written in Python',
        argument_default=argparse.SUPPRESS)

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {0}'.format(__version__))
    parser.add_argument('file', help='the path to the pokeball file')

    args = parser.parse_args()

    if os.path.isfile(args.file):
        if args.file.split('.')[-1] is 'pokeball':
            with open(args.file, 'r') as pikalang_file:
                pikalang_data = pikalang_file.read()
            lexer.load(pikalang_data)
        else:
            parser.print_usage()
            print('pikalang: error: file is not a pokeball')
    else:
        parser.print_usage()
        print('pikalang: error: file does not exist')


if __name__ == '__main__':
    main()
