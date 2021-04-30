from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

from app.utilities import nlp_utils
from app.utilities import model_serving


def generate_haiku(
        user_input: str,
        sequence_length: int = 14,
        *args,
        **kwargs
):
    tokenizer = nlp_utils.get_haiku_tokenizer()
    model_uri = "localhost:8500"
    model_name = "haiku"

    generated_haiku = f"{user_input}"
    while len(generated_haiku.split()) < sequence_length:
        encoded_input = tokenizer.texts_to_sequences([generated_haiku])
        encoded_input_padded = pad_sequences(encoded_input, maxlen=sequence_length)
        predicted_scores = model_serving.get_haiku_scores(encoded_input_padded, model_uri, model_name)[0]
        best_word_ix = predicted_scores.argmax()
        if best_word_ix == 0:
            best_word_ix = np.random.choice(np.arange(0, predicted_scores.shape[0]))
        next_predicted_word = tokenizer.index_word[best_word_ix]
        generated_haiku += f" {next_predicted_word}"

    return generated_haiku
