"""Entry point of CLI application."""

import click


@click.command('analyze')
@click.argument('words')
def analyze_word(words: str):
    """Count total characters and words in input.
    
    Arguments:
     words: str - Input sentence to analyze.

    Returns:
     None - Prints to stdout the number of characters and words.
    """
    if not words:
        print('No input words')
        raise SystemExit(1)

    char_count = len(words)
    word_count = len(words.strip().split())
    print('Total characters:', char_count)
    print('Total words:', word_count)
