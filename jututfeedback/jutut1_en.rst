Jutut
=====

Test MOOC-Jutut feedback questionnaires.

.. questionnaire:: math 10
  :title: Normal questionnaire in the Jutut chapter
  :submissions: 10

  .. pick-one:: 10

    What is 1+3?

    a. 2
    b. 3
    *c. 4
    d. 5


.. questionnaire::
  :feedback:
  :title: MOOC-Jutut test feedback questionnaire
  :category: jututfeedback

  .. freetext:: 0 int
    :required:
    :key: timespent
    :height: 1
    :length: 20
    :class: time-usage-question
    :extra: minimum=6;validationMessage=Please enter the time in minutes.

    **Time spent:**

    Please estimate the total number of minutes you spent on this chapter (reading, assignments,
    etc.). You don’t have to be exact, but if you can produce an estimate to within 15 minutes or
    half an hour, that would be great.

  .. pick-one::
    :required:
    :key: understood

    **“I feel that I have understood the most important things in this chapter.”**

    a. fully agree
    b. somewhat agree
    c. somewhat disagree
    d. fully disagree
    e. I’m unable to answer or don’t want to comment.

  .. freetext::
    :main-feedback:
    :required:
    :key: mainfeedback
    :length: 100
    :height: 8

    Give feedback on the chapter.
