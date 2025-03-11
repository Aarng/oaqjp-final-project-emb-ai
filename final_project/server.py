"""
Flask server para análisis de emociones usando Watson NLP
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Renderiza la página principal"""
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint para análisis de emociones.
    Procesa texto enviado como parámetro 'text' y retorna análisis formateado.
    Maneja errores para entradas inválidas o vacías.
    """
    text = request.args.get('text')
    if not text:
        return "Invalid text! Please try again!"

    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotions = ", ".join(
        [f"'{k}': {v:.2f}" for k, v in result.items() if k != 'dominant_emotion']
    )
    return (
        f"For the given statement, the system response is {emotions}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    