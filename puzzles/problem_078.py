"""
Problem 78: Given a DataFrame with a column of text, create a new
column containing the word count for each row.

    df = pd.DataFrame({'text': ['hello world',
                                'the quick brown fox jumps over the lazy dog',
                                'pandas is great',
                                'one']})

Expected 'word_count': [2, 9, 3, 1]
"""

import pandas as pd

df = pd.DataFrame({'text': ['hello world',
                            'the quick brown fox jumps over the lazy dog',
                            'pandas is great',
                            'one']})

df['word_count'] = df['text'].str.split().str.len()

print(df)
