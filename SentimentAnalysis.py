import speech_recognition as sr
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')

# Define the function to perform sentiment analysis
def sentiment_analysis(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove the stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    # Compute the sentiment scores
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(' '.join(filtered_tokens))
    # Determine the sentiment label
    if scores['compound'] >= 0.05:
        label = 'positive'
    elif scores['compound'] <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'
    return label

# Define the function to analyze the sentiment of speech input
def analyze_voice_sentiment():
    """Analyze the sentiment of speech input and return a sentiment label."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
    try:
        # Recognize speech using the Google Speech Recognition API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        # Analyze the sentiment of the recognized text
        label = sentiment_analysis(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        label = 'unknown'
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        label = 'unknown'
    return label

# Test the sentiment analysis function with voice input
sentiment_label = analyze_voice_sentiment()
print("The sentiment of the audio file is:", sentiment_label)
