
from transformers import pipeline
from flask import Flask, request, render_template
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'




from transformers import pipeline
# Initialize the text generation pipeline
generator = pipeline("text-generation", model="xfoxxe/AraCLLv1")

# Initialize the text classification pipeline
classifier = pipeline("text-classification", model="xfoxxe/Classify_Kalimat")




app = Flask(__name__)

# Route for main page
@app.route('/')
def main_page():
    return render_template('index.html')

# Route for text generation page
@app.route('/text_generation', methods=['GET', 'POST'])
def text_generation():
    if request.method == 'POST':
        # Check if 'prompt' exists in form
        if 'prompt' in request.form:
            prompt = request.form['prompt']
            out = generator(prompt)
            generated_text = out[0]["generated_text"]
            print(generated_text)
            return render_template('text_generation.html', generated_text=generated_text, prompt=prompt)
        else:
            # Handle missing prompt
            return render_template('text_generation.html', error="No prompt provided. Please enter a prompt.")
    return render_template('text_generation.html')



# Route for text class page
@app.route('/text_classification', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'input_text' in request.form:  # Check if the input_text field exists
            input_text = request.form['input_text']
            out = classifier(input_text)
            prediction = out[0]["label"]
            print(prediction)
            return render_template('text_classification.html', prediction=prediction, input_text=input_text)
        else:
            # Handle missing prompt
            return render_template('text_classification.html', error="No prompt provided. Please enter a prompt.")
    return render_template('text_classification.html')

if __name__ == "__main__":
    app.run(debug=True)
