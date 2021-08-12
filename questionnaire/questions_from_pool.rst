Questions taken from a pool of questions
========================================
The following **two** questionnaires cannot include a general description. Therefore, you must use the
description inside each question type (pick-one, pick-any, freetext)

.. questionnaire:: pick_randomly_1
  :title: Pick question randomly from a pool of questions
  :submissions: 4
  :points-to-pass: 10
  :pick_randomly: 1
  :category: Pool

  .. include:: pool_of_questions.rst


.. questionnaire:: pick_randomly_2
  :title: Pick question randomly from a pool of questions
  :submissions: 4
  :points-to-pass: 10
  :pick_randomly: 1
  :preserve-questions-between-attempts:
  :category: Pool

  .. freetext:: 10 subdiff

    **Modifiers used in this question:** None.

    This question accepts either ``red`` or ``blue`` as the correct answer.
    The model solution is a regular expression.

    red|blue

  .. pick-one:: 10
    :dropdown:

    **Modifiers used in this question:** ``dropdown``.

    What is 1+2?

    +0. 0
    1. 1
    2. 2
    *3. 3

  .. freetext:: 10 string-ignorews-ignorequotes-requirecase
    :length: 10

    **Modifiers used in this question:** ``length``.

    The correct answer for this question is ``test``. Surrounding quotes are ignored as well as whitespaces.

    test
    !test § Follow the instruction.
    regexp:Test|TEST § Use the lower case!

  .. pick-any:: 10
    :partial-points:

    **Modifiers used in this question:** ``partial-points``.

    Pick the options ``this is the first`` and ``this is the second``.

    +*a. this is the **first**
    *b. this is the **second**
    c. this is the **third**
    d. this is the **fourth**
    ?e. choosing this does not affect the granted points

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    What is 1+1?

    a. 1
    *b. 2
    c. 3

    !b § Count again!
    b § That is correct!
    c § Too much
