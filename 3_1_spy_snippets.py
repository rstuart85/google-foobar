# Copyright (c) 2012-2014 Kapiche Limited
# Author: Ryan Stuart <ryan@kapiche.com>
"""
Spy snippets
============

You've been recruited by the team building Spy4Rabbits, a highly advanced search engine used to help fellow agents
discover files and intel needed to continue the operations against Dr. Boolean's evil experiments. The team is known for
recruiting only the brightest rabbit engineers, so there's no surprise they brought you on board. While you're elbow
deep in some important encryption algorithm, a high-ranking rabbit official requests a nice aesthetic feature for the
tool called "Snippet Search."  While you really wanted to tell him how such a feature is a waste of time in this
intense, fast-paced spy organization, you also wouldn't mind  getting kudos from a leader. How hard could it be, anyway?

When someone makes a search, Spy4Rabbits shows the title of the page. Your commander would also like it to show a short
snippet of the page containing the terms that were searched for.

Write a function called answer(document, searchTerms) which returns the shortest snippet of the document, containing all
of the given search terms. The search terms can appear in any order.

The length of a snippet is the number of words in the snippet. For example, the length of the snippet "round fluffy
rabbit tails" is 4. (Hey, don't judge your colleagues for what they search in their spare time).

The document will be a string consisting only of lower-case letters [a-z] and spaces. Words in the string will be
separated by a single  space. A word could appear multiple times in the document. searchTerms will be a list of words,
each word comprised only of lower-case letters [a-z]. All the search terms will be distinct.

Search terms must match words exactly, so "hop" does not match "hopping".

Return the first sub-string if multiple sub-strings are shortest. For example, if the document is "world there hello
hello where world" and the search terms are ["hello", "world"], you must return "world there hello".

The document will be guaranteed to contain all the search terms.

The number of words in the document will be at least one, will not exceed 500, and each word will be 1 to 10 letters
long. Repeat words in  the document are considered distinct for counting purposes.

The number of words in searchTerms will be at least one, will not exceed 100, and each word will not be more than 10
letters long.
"""
import math
import sys


def answer(document, search_terms):
    """Index the position of all search_terms then find the min "score" for a search."""
    index = {k: [] for k in search_terms}
    tokens = document.split()
    for i, token in enumerate(tokens, start=1):
        if token in search_terms:
            index[token].append(i)
    min_score = sys.maxint
    winning_slice = None
    for term in index.keys():  # ignore duplicate terms
        for position in index[term]:
            positions = [position]
            for other_term in index.keys():
                distances = [int(math.fabs(position - x)) for x in index[other_term]]
                positions.append(index[other_term][distances.index(min(distances))])
            score = max(positions) - min(positions) + 1
            if score < min_score:
                winning_slice = (min(positions) - 1, max(positions),)
                min_score = score
    return " ".join(tokens[slice(*winning_slice)])

if __name__ == '__main__':
    print answer(
        """
        many google employees can program can google employees because google is a technology company that writes
        programs
        """,
        ["google", "program", "can"]
    )
    print answer(
        "a b d a c a c c d a",
        ["a", "c", "d"]
    )
