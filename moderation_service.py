from transformers import AutoModelForSequenceClassification, AutoTokenizer
from models import CategoryPrediction
from itertools import starmap


class ModerationService:

    MODEL_NAME = "KoalaAI/Text-Moderation"

    def __init__(self) -> None:
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL_NAME)
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_NAME)

    def cleanup(self):
        pass

    def classify_text(self, input_text: str) -> CategoryPrediction:
        """The moderation service is a service to classify t"""

        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model(**inputs)

        # Apply softmax to get probabilities (scores)
        probabilities = outputs.logits.softmax(dim=-1).squeeze()

        # Retrieve the labels
        labels = [self.model.config.id2label[idx] for idx in range(len(probabilities))]

        return CategoryPrediction(
            predictions={key: value for key, value in zip(labels, probabilities)}
        )
