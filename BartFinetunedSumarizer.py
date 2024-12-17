from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# using a fine-tuned version of the Bart CNN model which specializes in summarization
tokenizer = AutoTokenizer.from_pretrained("suriya7/bart-finetuned-text-summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("suriya7/bart-finetuned-text-summarization")

def generate_summary(text):
    inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_new_tokens=100, do_sample=False)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

summary = generate_summary(corrected_text)
print(summary)
