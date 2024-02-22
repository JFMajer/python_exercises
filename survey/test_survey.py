import pytest

from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    question = "What language did you learn to speak first?"
    survey = AnonymousSurvey(question)
    return survey


def test_store_single_response(language_survey):
    language_survey.store_response("English")

    assert "English" in language_survey.responses


def test_store_three_responses(language_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for res in responses:
        assert res in language_survey.responses
