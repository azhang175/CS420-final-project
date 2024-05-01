import re

# QuestCode language Tokens
# This file contains the tokens that are used in the QuestCode language.

TOKENS = {
    "INT_TYPE": r"\btreasure\b",
    "STRING_TYPE": r"\bmessage\b",
    "IF": r"\bchallenge\b",
    "ELSEIF": r"\borChallenge\b",
    "ELSE": r"\bdefaultQuest\b",    
    "FOR_LOOP": r"\brepeatQuest\b",
    "WHILE_LOOP": r"\bcontinueQuest\b",
    "PRINT": r'\bdisplay\b',

    "IDENTIFIER": r'[a-zA-Z_][a-zA-Z0-9_]*',
    "NUMBER": r"\d+",
    "STRING": r'\"([^\\\"]|\\.)*\"',
    
    # Operators
    "PLUS": r"\+",
    "MINUS": r"\-",
    "MULTIPLY": r"\*",
    "DIVIDE": r"\/",
    "MOD": r"\%",
    "ASSIGN": r"\=",
    "NOT_EQUAL": r"!=",
    "EQUAL": r"==",
    "GREATER": r">",
    "GREATER_EQUAL": r">=",
    "LESS": r"<",
    "LESS_EQUAL": r"<=",
    "SEMICOLON": r";",
    "WHITESPACE": r"\s+",
    "LEFT_PAREN": r"\(",
    "RIGHT_PAREN": r"\)",
    "LEFT_BRACE": r"{",
    "RIGHT_BRACE": r"}",
}


