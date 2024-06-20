from transformers import pipeline

def emotion_detection(text):
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

    def emotion_sentiment(text):
        results = classifier(text, padding='max_length', max_length=512)
        return {label['label']: label['score'] for label in results[0]}
    result = emotion_sentiment(text)
    return result
