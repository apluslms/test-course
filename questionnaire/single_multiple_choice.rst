Single and Multiple-choice questionnaire
========================================

Partial points
--------------

.. questionnaire:: pick-any-with-partial-points 10
  :title: Pick-any with partial points
  :submissions: 5
  :show-model: true

  This questionnaire gives partial points to students. It means that students can get points even if they do not
  mark all the choices correctly. But they can get some points deducted if they mark the wrong answers.
  This configuration **applies only** to ``pick-any`` questionnaires.

  In this question, the grading goes as follows:

  1. One correct answer= 3 points are given

  2. Two correct answers = 6 points are given

  3. Three correct answers = 10 points are given

  And for the wrong answers:

  1. One wrong option is chosen = 3 points are deducted

  2. Two wrong options are chosen = 6 points are deducted

  3. Three wrong options are chosen = 10 points are deducted

  .. pick-any:: 10
    :partial-points:

    **Modifiers used in this question:** ``partial-points``.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    a. 4
    *b. an integer
    *c. 3
    d. an irrational number
    e. -3
    *f. -5

Answers are required and 100% feedback
--------------------------------------

.. questionnaire:: required-answers-and-show-model 30
  :title: Questionnaire with 100% feedback, answers required and show-model setting enabled.
  :submissions: 5
  :show-model: true

  This questionnaire required students to answer to the questions. If students answer the single-choice and
  the multiple-choices question correctly, the application will display a hint indicating that the answer is
  100% correct. We can show this type of feedback by prepending the ``%100%`` character to the hints, e.g.,
  ``%100% § The answer is 100% correct``

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    %100% § The answer is 100% correct
    a § Not quite. Remember the cube root.
    b § This is correct!
    c § Rather close. Remember that you can add or subtract the same number to both sides of the equation.

  .. pick-any:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    a. 4
    *b. an integer
    *c. 3
    d. an irrational number
    e. -3
    *f. -5

    %100% § The answers are 100% correct

  .. freetext:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    Type the word ``mandatory`` in the following text box.

    mandatory

Randomized answers for a multiple-choice questionnaire
-----------------------------------------------------------

.. questionnaire:: questionnaire-randomized 30
  :title: Use the randomized settings
  :submissions: 3
  :points-to-pass: 20

  The following questionnaire swaps the possible choices after each of students' attempt.

  * The first question changes the possible choices after each student attempt.
  * The second question will keep the same choices for all student attempts.
  * The third question will change the choices after every student attempt, but we also provide students
    with hints.

  .. pick-any:: 10
    :randomized: 4
    :correct-count: 1

    **Modifiers used in this question:** ``randomized`` and ``correct-count``.

    :math:`10` is the result of the following arithmetic operation.

    *a. :math:`5 \times 2`
    *b. :math:`50 \div 5`
    *c. :math:`2+2+2+2+2`
    d. :math:`50 \div 4`
    e. :math:`3+2+4+2`
    *f. :math:`3 \times 2+4`
    g. :math:`2 \times 2+3`
    h. :math:`3+3+3+3`
    *i. :math:`2 \times (2+3)`

  .. pick-any:: 10
    :randomized: 4
    :preserve-questions-between-attempts:
    :correct-count: 1

    **Modifiers used in this question:** ``randomized``, ``preserve-questions-between-attempts`` and ``correct-count``.

    :math:`20` is the result of the following arithmetic operation.

    *a. :math:`5 \times 4`
    *b. :math:`40 \div 2`
    *c. :math:`(2+2+2+2+2) \times 2`
    d. :math:`50 \div 4`
    e. :math:`6+4+8+4`
    *f. :math:`6 \times 2+2`
    g. :math:`2 \times 8+3`
    h. :math:`6+3+6+6`
    *i. :math:`4 \times (2+3)`

  .. pick-any:: 10
    :randomized: 4
    :correct-count: 1

    **Modifiers used in this question:** ``randomized`` and ``correct-count``.

    :math:`20` is the result of the following arithmetic operation.

    *a. :math:`5 \times 4`
    *b. :math:`40 \div 2`
    *c. :math:`(2+2+2+2+2) \times 2`
    d. :math:`50 \div 4`
    e. :math:`6+4+8+4`
    *f. :math:`6 \times 2+2`
    g. :math:`2 \times 8+3`
    h. :math:`6+3+6+6`
    *i. :math:`4 \times (2+3)`

    !a § This is correct. Multiplication.
    !b § This is correct. Division.
    !c § This is correct. Sum and Multiplication.
    d § Incorrect answer. The solution of this operation is not equal to 20.
    e § Incorrect answer. Please try again.
    !f § This is correct. Multiplication and Sum with operator precedence.
    g § Incorrect. Remember the operator precedence.
    h § Incorrect. Verify your results.
    !i § This is correct. Sum and multiplication with grouping symbols.

Pass without full points
------------------------

.. questionnaire:: questionnaire_points_to_pass 20
  :title: Pass with 12 points and dropdown question
  :submissions: 3
  :points-to-pass: 12

  The following questionnaire allows students to pass with 12 points or more. The questionnaire also includes
  a dropdown question.

  .. pick-any:: 10
    :partial-points:

    **Modifiers used in this question:** ``partial-points``.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    a. 4
    *b. an integer
    *c. 3
    d. an irrational number
    e. -3
    *f. -5

  .. pick-one:: 10
    :dropdown:

    **Modifiers used in this question:** ``dropdown``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3



