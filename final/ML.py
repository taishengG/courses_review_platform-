import argparse
import sys

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six


class Ml:

# [START def_sentiment_text]
    def sentiment_text(text):
        """Detects sentiment in the text."""
        client = language.LanguageServiceClient()

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        # Instantiates a plain text document.
        # [START migration_document_text]
        # [START migration_analyze_sentiment]
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)
        # [END migration_document_text]

        # Detects sentiment in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        sentiment = client.analyze_sentiment(document).document_sentiment

        print('Score: {}'.format(sentiment.score))
        print('Magnitude: {}'.format(sentiment.magnitude))
        # [END migration_analyze_sentiment]
# [END def_sentiment_text]
