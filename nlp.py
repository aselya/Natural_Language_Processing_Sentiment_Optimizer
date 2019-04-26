

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# [END language_sentiment_tutorial_imports]
print("imports successfull")

# [START language_sentiment_tutorial_print_result]
def print_result_and_return_fitness_score(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    fitness_score = score * magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    print("fittness_score =" + str(fitness_score))
    return fitness_score
# [END language_sentiment_tutorial_print_result]


# [START language_sentiment_tutorial_analyze_sentiment]
def analyze(insult):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()


    content = insult

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    fitness_score = print_result_and_return_fitness_score(annotations)
    return fitness_score
# [END language_sentiment_tutorial_analyze_sentiment]


# [START language_sentiment_tutorial_run_application]


#analyze("you suck google")
# [END language_sentiment_tutorial_run_application]
# [END language_sentiment_tutorial]
