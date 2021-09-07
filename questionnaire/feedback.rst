Questionnaire feedback
======================

.. questionnaire:: feedback-given-when-correct-and-wrong-answers-are-selected 20
  :title: Provide feedback when the correct answers and the wrong answers are selected by students
  :submissions: 5
  :show-model: true

  If students do not select the correct answers, some feedback is given to help them select the correct
  answers. Once the students have selected the correct answer, they will recieve feedback telling them that
  answers are correct.

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    +a. 9
    *b. 2
    c. 3

    %100% § The answer is correct!
    a § Not quite. Remember the cube root.
    !b § You should select option **2**.
    b § This is correct
    c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.

  .. pick-any:: 10
    :required:
    :checkbox-feedback:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    +a. 4
    *b. an integer
    *c. 3
    d. an irrational number
    e. -3
    +*f. -5
    ?g. There is more than one correct answer

    %100% § The answer is correct!
    a § Rather close. Remember that you can add or subtract the same number to both sides of the equation.
    !b § option **an integer** must be selected
    b § This is correct
    !c § option **3** must be selected.
    c § This is correct
    d § No. This equation has a nice and easy solution.
    e § Remember that :math:`x^2 = q \leftrightarrow x = \pm \sqrt{q}`
    !f § option **-5** must be selected.
    f § This is correct
    g § This is a neutral answer

.. questionnaire:: feedback-given-when-correct-answers-are-not-selected 25
  :title: Provide feedback when the correct answers are not selected by students
  :submissions: 5
  :show-model: true

  If students do not select the correct answers. Some feedback is given to help students to choose the correct
  answers. Feedback is not given if students select a checkbox with a wrong answer.

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    !b § You should select option **2**.

  .. pick-any:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    +a. 4
    *b. an integer
    *c. 3
    d. an irrational number
    e. -3
    +*f. -5
    ?g. There is more than one correct answer

    !b § option **an integer** must be selected
    !c § option **3** must be selected.

  .. freetext:: 5
    :length: 7
    :height: 4

    **Modifiers used in this question:** ``required``.

    The text-area can be larger as well. Here the correct answer is ``text-area``

    text-area
    !text-area § Hint: the answer is ``text-area``.

.. questionnaire:: general-feedback 20
  :title: The questionnaire gives feedback when the students select the wrong answer.
  :submissions: 5
  :show-model: true

  The feedback is provided if students select the wrong answer.

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    a § Not quite. Remember the cube root.
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
    ?g. There is more than one correct answer

    a § Rather close. Remember that you can add or subtract the same number to both sides of the equation.
    d § No. This equation has a nice and easy solution.
    e § Remember that :math:`x^2 = q \leftrightarrow x = \pm \sqrt{q}`
    g § This is a neutral answer


.. questionnaire:: no-feedback 20
  :title: There is no customised feedback.
  :submissions: 5
  :show-model: true

  There is no customised feedback. Students only received the default feedback.

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

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
    ?g. There is more than one correct answer
