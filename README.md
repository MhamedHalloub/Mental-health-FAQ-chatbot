# Mental-health-FAQ-chatbot
A simple and interactive chatbot that answers frequently asked questions (FAQs) about mental health using natural language processing (NLP). This app is built with Python, Flask, and scikit-learn and uses TF-IDF vectorization to find the best matching answer from a dataset.


📂 Project Structure

faq_chatbot_web/

├── app.py                  # Flask backend

├── Mental_Health_FAQ.csv   # FAQ dataset (questions and answers)

└── templates/

    └── index.html          # Frontend UI
    
🚀 Features

💬 Ask natural language questions about mental health

⚡ Instant response from a curated FAQ dataset

🧠 NLP-powered matching using TF-IDF & cosine similarity

🌐 Lightweight and easy to run on any machine

📦 Installation

Clone the repository:


git clone https://github.com/MhamedHalloub/Mental-health-FAQ-chatbot.git

cd Mental-health-FAQ-chatbot

Install dependencies:

bash

pip install flask pandas scikit-learn

Run the app:

python app.py

Open your browser and go to: http://127.0.0.1:5000

🛠 Customize

To use your own FAQ data, replace the contents of Mental_Health_FAQ.csv.

Make sure it has two columns: Questions and Answers.

🧪 Example

Q: Can mental illness be cured?

A: Many people with mental health conditions recover completely or can manage their symptoms with treatment.

📌 Requirements

Python 3.7+

Flask

pandas

scikit-learn

📄 License

This project is licensed under the MIT License.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

