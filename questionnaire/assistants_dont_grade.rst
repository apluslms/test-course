Course Assistant do not grade the assignments
=============================================

.. questionnaire:: assistant-cannot-grade A
  :title: This questionnaire cannot be graded by the course assistant
  :submissions: 4
  :points-to-pass: 30
  :no-override:

  This is a questionnaire that gives a maximum of 70 points, but students can pass if they get at least 30 points.
  The difficulty is considered A. Students can make at most 4 submissions.

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

  (Hints can be included or omitted in any question.)

  .. pick-one:: 10
    :dropdown:

    **Modifiers used in this question:** ``dropdown``.

    What is 1+2?

    +0. 0
    1. 1
    2. 2
    *3. 3

  .. pick-any:: 10
    :partial-points:

    **Modifiers used in this question:** ``partial-points``.

    Pick the options ``this is the first`` and ``this is the second``.

    +*a. this is the **first**
    *b. this is the **second**
    c. this is the **third**
    d. this is the **fourth**
    ?e. choosing this does not affect the granted points

  .. freetext:: 30 string-ignorews-ignorequotes-requirecase

    **Modifiers used in this question:** None.

    The correct answer for this question is ``test``. Surrounding quotes are ignored as well as whitespaces.

    test
    !test § Follow the instruction.
    regexp:Test|TEST § Use the lower case!

  .. freetext:: 10 regexp

    **Modifiers used in this question:** None.

    This question accepts either ``red`` or ``blue`` as the correct answer.
    The model solution is a regular expression.

    red|blue
