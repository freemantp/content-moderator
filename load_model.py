from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("KoalaAI/Text-Moderation")
tokenizer = AutoTokenizer.from_pretrained("KoalaAI/Text-Moderation")

# Run the model on your input
inputs = tokenizer("Mice are rats", return_tensors="pt")
outputs = model(**inputs)

# Get the predicted logits
logits = outputs.logits

# Apply softmax to get probabilities (scores)
probabilities = logits.softmax(dim=-1).squeeze()

# Retrieve the labels
id2label = model.config.id2label
labels = [id2label[idx] for idx in range(len(probabilities))]

# Combine labels and probabilities, then sort
label_prob_pairs = list(zip(labels, probabilities))
label_prob_pairs.sort(key=lambda item: item[1], reverse=True)  

# Print the sorted results
for label, probability in label_prob_pairs:
    if probability > 0.1:
        print(f"Label: {label} - Probability: {probability:.4f}")
