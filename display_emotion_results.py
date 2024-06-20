import matplotlib.pyplot as plt

def display_emotion_results(results):
    emotions = list(results.keys())
    scores = list(results.values())
    plt.figure(figsize=(10, 6))
    plt.plot(emotions, scores, marker='o', linestyle='-')
    plt.title('Emotion Classification Results')
    plt.xlabel('Emotion')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
