from flask import Flask, request, jsonify
import watson_nlp

app = Flask(__name__)

# Загружаем модель Watson NLP для анализа эмоций
emotion_model = watson_nlp.load('emotion_aggregated-workflow_lang_en_stock')

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    """
    Получает текст через JSON и возвращает эмоцию
    Пример запроса:
    { "text": "I am so happy today" }
    """
    data = request.get_json()
    text = data.get("text", "")
    result = emotion_model.run(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
