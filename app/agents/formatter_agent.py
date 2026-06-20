class FormatterAgent:

    def execute(
        self,
        text,
        source_lang,
        target_lang,
        translation,
        sentiment,
        safety
    ):

        return {
            "input_text": text,
            "source_language": source_lang,
            "target_language": target_lang,
            "translated_text": translation,
            "sentiment": sentiment,
            "safety": safety
        }