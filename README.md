# Multi-Agent-Translator
## Running the Application

Start the FastAPI server using:

```bash
python run.py
```

Once the server is running, the API will be available at:

```text
http://127.0.0.1:8080
```

### API Documentation

Swagger UI:

```text
http://127.0.0.1:8080/docs
```

ReDoc:

```text
http://127.0.0.1:8080/redoc
```

### Health Check

```bash
curl http://127.0.0.1:8080/
```

Expected response:

```json
{
  "message": "Multi-Agent Translator Running"
}
```

## Example Request

Send a POST request to the `/translate` endpoint with the following JSON payload:

```json
{
  "text": "Jag älskar ML. Var du komma från?",
  "source_lang": "swe_Latn",
  "target_lang": "eng_Latn"
}
```

### Request Parameters

| Parameter     | Type     | Description                        |
| ------------- | -------- | ---------------------------------- |
| `text`        | `string` | Input text to be translated        |
| `source_lang` | `string` | Source language code (NLLB format) |
| `target_lang` | `string` | Target language code (NLLB format) |

### Example cURL

```bash
curl -X POST "http://localhost:8000/translate" \
-H "Content-Type: application/json" \
-d '{
  "text": "Jag älskar ML. Var du komma från?",
  "source_lang": "swe_Latn",
  "target_lang": "eng_Latn"
}'
```

## Example Response

```json
{
  "input_text": "Jag älskar ML.Var du komma från?",
  "source_language": "swe_Latn",
  "target_language": "eng_Latn",
  "translated_text": "I love ML. Where were you from?",
  "sentiment": {
    "label": "NEGATIVE",
    "score": 0.9969
  },
  "safety": {
    "toxicity": 0.0065,
    "insult": 0.0004,
    "threat": 0.0001,
    "identity_attack": 0.0002
  }
}
```

### Response Fields

| Field                    | Description                              |
| ------------------------ | ---------------------------------------- |
| `input_text`             | Original text submitted by the user      |
| `source_language`        | Source language code                     |
| `target_language`        | Target language code                     |
| `translated_text`        | Generated translation                    |
| `sentiment.label`        | Predicted sentiment label                |
| `sentiment.score`        | Confidence score of sentiment prediction |
| `safety.toxicity`        | Toxicity probability score               |
| `safety.insult`          | Insult detection score                   |
| `safety.threat`          | Threat detection score                   |
| `safety.identity_attack` | Identity attack detection score          |

### Response Summary

| Analysis             | Result                            |
| -------------------- | --------------------------------- |
| Translation          | *I love ML. Where were you from?* |
| Sentiment            | NEGATIVE                          |
| Sentiment Confidence | 99.69%                            |
| Toxicity Level       | Very Low                          |
| Safety Status        | Safe Content                      |

> The API not only translates text but also performs sentiment analysis and safety evaluation, making it suitable for multilingual conversational AI, customer support systems, content moderation pipelines, and intelligent language services.





