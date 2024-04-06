from transformers import AutoModelForSequenceClassification, AutoTokenizer
from models import OffensivenessCategoryPrediction, CategoryDescription
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

class ModerationService:

    MODEL_NAME = "KoalaAI/Text-Moderation"

    def __init__(self) -> None:
        logger.info(f'Loading Model {self.MODEL_NAME}')
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL_NAME)
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_NAME)
        logger.info(f'Model {self.MODEL_NAME}successfully loaded')

    def classify(self, input_text: str) -> OffensivenessCategoryPrediction:
        """Takes an input text and classifies it according to different offensiveness categories.

        Args:
            input_text(str): An input text to classify

        Returns:
            get_classifcation: an offensiveness category prediction containing the categories and its probabilities
        """

        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model(**inputs)

        # Apply softmax to get probabilities
        probabilities = outputs.logits.softmax(dim=-1).squeeze()

        # Retrieve labels from ids
        labels = [self.model.config.id2label[idx] for idx in range(len(probabilities))]

        return OffensivenessCategoryPrediction(
            predictions={key: value for key, value in zip(labels, probabilities)}
        )

    def get_category_descriptions(self) -> CategoryDescription:
        return CategoryDescription(
            descriptions={
                "S": "sexual",
                "H": "hate",
                "V": "violence",
                "HR": "harassment",
                "SH": "self-harm",
                "S3": "sexual/minors",
                "H2": "hate/threatening",
                "V2": "violence/graphic",
                "OK": "OK",
            }
        )
