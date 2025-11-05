# Document Classification and Text Generation in Arabic

A Natural Language Processing (NLP) project focused on **Arabic text classification** and **text generation** using **transformer-based models** such as **BERT** and **GPT-2**.  
The project leverages the **Kalimat Arabic Corpus** and provides a **Flask web interface** for real-time user interaction.

---

## Overview

This project combines the power of **transformer architectures** with the complexity of the **Arabic language**, addressing challenges like morphology, diacritics, and right-to-left script.  
It includes two main components:

1. **Text Classification** – Classifies Arabic text into predefined categories using a fine-tuned **BERT** model.  
2. **Text Generation** – Generates coherent Arabic text using **AraGPT-2**, fine-tuned on the Kalimat dataset.

---

## Features

- **Arabic Text Classification** using BERT fine-tuned on Kalimat corpus  
- **Text Generation** using fine-tuned AraGPT-2 model  
- **Evaluation Metrics** – Accuracy, F1-score, Precision, Recall, and Perplexity  
- **Flask Web App** for real-time interaction  
- **Visualizations** – Confusion matrix, accuracy/loss plots, and generated text samples  

---

## Models Used

| Task                | Model                      | Accuracy / Metric |
|---------------------|----------------------------|-------------------|
| Text Classification | Random Forest (Baseline)   | 93% Accuracy      |
| Text Classification | BERT (Arabic)              | 95% Accuracy      |
| Text Generation     | AraGPT-2                   | Perplexity: 59.44 |

- BERT outperformed traditional models in text classification.  
- AraGPT-2 generated semantically consistent and grammatically correct Arabic sentences.

---

## Dataset

**Dataset:** [Kalimat Arabic Corpus](https://sourceforge.net/projects/kalimat/)  
- Contains thousands of Arabic documents labeled into 6 categories.  
- Preprocessing steps included:
  - Removing diacritics  
  - Tokenization using `Arabic-Transformers` tokenizer  
  - Text normalization  

---

🛠️ Technologies Used

- Python  
- Hugging Face Transformers  
- PyTorch  
- Flask  
- Pandas / Scikit-learn  
- HTML / CSS

---
## Preview
[1](<img width="875" height="399" alt="image" src="https://github.com/user-attachments/assets/93a32f6b-8be2-453e-8265-1609e7cc9c4f" />)
[2](<img width="910" height="458" alt="image" src="https://github.com/user-attachments/assets/fa736bf8-596f-44cc-be0c-a09fb203d5a9" />)
[3](<img width="890" height="416" alt="image" src="https://github.com/user-attachments/assets/b2c64a7f-3e95-4bf8-b1e5-975d6bccd938" />)



