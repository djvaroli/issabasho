

def tokenize_for_haiku_model(
        user_input: str
):
    w1, w2 = user_input.split(" ")



test_input = "The wild goose"
max_length = 14

while len(test_input.split()) < max_length:
    encoded_input = tokenizer.texts_to_sequences([test_input])
    encoded_input = pad_sequences(encoded_input, maxlen=max_length)
    model_output = model.predict(encoded_input)[0][-1]
    index = model_output.argmax()
    if index == 0:
        break
    next_predicted_word = tokenizer.index_word[index]
    test_input += f" {next_predicted_word}"