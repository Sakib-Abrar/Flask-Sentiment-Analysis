## Flask-Sentiment-Analysis

### Instructions
1. Make sure you have these installed:
```bash
python3
python3-venv
```

2. Clone the repository && Run these commands:
```bash
git clone https://github.com/Sakib-Abrar/Flask-Sentiment-Analysis.git
cd Flask-Sentiment-Analysis
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=main.py
```
3. Run python interactive shell:
```bash
python3
```

4. Run these commands in the python shell:
```bash
import nltk
nltk.download("stopwords")
exit()
```

5. Then finally run the application:
```bash
flask run
```

## Result
6. Open the browser and go to http://127.0.0.1:5000/
![screenshot of options](https://github.com/Sakib-Abrar/Flask-Sentiment-Analysis/blob/master/screenshot/Screenshot-2020-02-02%2012-23-34.png)
