from rest_framework import serializers
from lessons.models import (Subject, QuestionBase, Lesson, VocabMCQuestion, SentenceMCQuestion, WriteSentenceQuestion, TranslatePickWordsQuestion,
    PairsQuestion)


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="subject-detail")

    class Meta:
        model = Subject
        fields = ['url', 'name']

class QuestionBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionBase
        fields = ['url', 'id', 'subjects']

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(
        many=True, view_name='questionbase-detail', queryset=QuestionBase.objects.all())

    class Meta:
        model = Lesson
        fields = ['url', 'id', 'lesson_name', 'subjects', 'questions']

class VocabMCQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VocabMCQuestion
        fields = ['url', 'id', 'subjects', 'vocab_word', 'correct_answer', 'incorrect_answer_options']
        # extra_kwargs = {'incorrect_answer_options': {'binary': True}}

class SentenceMCQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=SentenceMCQuestion
        fields = ['url', 'id', 'subjects', 'native_language_sentence', 'correct_answer', 'incorrect_answer_options']

class WriteSentenceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=WriteSentenceQuestion
        fields = ['url', 'id', 'subjects', 'native_language_sentence', 'correct_answer']

class TranslatePickWordsQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TranslatePickWordsQuestion
        fields = ['url', 'id', 'subjects', 'native_language_sentence', 'correct_answer', 'incorrect_words']

class PairsQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=PairsQuestion
        fields = ['url', 'id', 'subjects', 'mixed', 'word_pairs']