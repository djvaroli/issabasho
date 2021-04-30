import os
from typing import *
import simplejson as json

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer, tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences


def get_haiku_tokenizer(
        tokenizer_json_fp: str = "app/utilities/tokenizers/haiku_tokenizer_april-28-2021.json"
):
    # at the moment we will store the tokenizer configuration
    # TODO: figure out a way to store tokenizer configuration in a in-memory database (i.e. Redis)
    # TODO: or some other more scalable approach
    with open(tokenizer_json_fp) as f:
        tokenizer_string = json.load(f)

    tokenizer = tokenizer_from_json(tokenizer_string)
    return tokenizer


def tokenize_for_haiku_model(
        user_input: str,
        sequence_length: int = 14,
        tokenizer_json_fp: Optional[str] = None,
        *args,
        **kwargs
):
    tokenizer = get_haiku_tokenizer()
    if tokenizer_json_fp is not None:
        tokenizer = get_haiku_tokenizer(tokenizer_json_fp)

    w1, w2 = user_input.split(" ")
    w1_ix, w2_ix = tokenizer.word_index[w1], tokenizer.word_index[w2]
    sequence = [[w1_ix, w2_ix]]
    sequence = pad_sequences(sequence, maxlen=sequence_length)

    return sequence


