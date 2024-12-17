from transformers import pipeline
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# model 
model_name = "google/pegasus-xsum"
# Loading pretrained tokenizer for the model as given by google
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)


pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)
# here, tokenization happensss
tokens = pegasus_tokenizer(example_text, truncation=True, padding="longest", return_tensors="pt")

#summary will be encoded here using pegasus model on the basis of provided tokens as per input
encoded_summary = pegasus_model.generate(**tokens)

# encoded summary encoded above using decode function of the tokenized input
decoded_summary = pegasus_tokenizer.decode(encoded_summary[0], skip_special_tokens=True)

print('Decoded Summary is :--',decoded_summary)

summarizer = pipeline(
    "summarization", 
    model=model_name, 
    tokenizer=pegasus_tokenizer, 
    framework="pt"
)
# summarizer function takes in the text mainly in the pipeline for summarization as mentioned, given to the model specified and tokenized as mentioned.
summary = summarizer(text, min_length=30, max_length=150)
summary[0]["summary_text"]
