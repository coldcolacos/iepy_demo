from refo import Question, Star, Any, Plus
from iepy.extraction.rules import rule, Token, Pos

RELATION = "was born"

@rule(True)
def was_born_explicit_mention(Subject, Object):
    """
    Ex: Shamsher M. Chowdhury was born in 1950.
    """
    anything = Star(Any())
    return anything + Subject + Token("was born") + Pos("IN") + Object + anything


@rule(True)
def is_born_in(Subject, Object):
    """
    Ex: Xu is born in 1902 or 1903 in a family of farmers in Hubei ..
    """
    anything = Star(Any())
    return Subject + Token("is born in") + Object + anything


@rule(True)
def just_born(Subject, Object):
    """
    Ex: Lyle Eugene Hollister, born 6 July 1923 in Sioux Falls, South Dakota, enlisted in the Navy....
    """
    anything = Star(Any())
    return Subject + Token(", born") + Object + anything
