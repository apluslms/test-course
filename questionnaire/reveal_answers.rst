Reveal Answers
==============

.. questionnaire:: reveal-model-answer-at-max-submission 40
  :title: Questionnaire reveals answers after Max. submissions.
  :submissions: 1
  :reveal-model-at-max-submissions: True

  The following questionnaire reveals the model answers after students have run out of attempts.

  .. danger::

    The model answers disappear after the page is reloaded.

  .. freetext:: 10 regexp
    :required:
    :length: 7

    **Modifiers used in this question:** ``required`` and ``length``.

    Type either ``cat`` or ``dog``.

    ^(cat|dog)$

  .. freetext:: 10 regexp
    :length: 7

    **Modifiers used in this question:** ``length``.

    What is the value of :math:`\pi` with four most significant digits?
    This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
    ``3.141`` and zero or more digits after that.

    ^3\.141\d*$

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    a § Not quite. Remember the cube root.
    b § This is correct!
    c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.


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

    a § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.
    b § This is correct!
    c § This is correct!
    d § No. This equation has a nice and easy solution.
    e § Remember that :math:`x^2 = q \leftrightarrow x = \pm \sqrt{q}`
    f § This is correct!

.. questionnaire:: reveal-answer-after-deadline 40
  :title: Questionnaire reveals answers after the deadline has passed.
  :submissions: 1
  :show-model: True

  The following questionnaire reveals the model answers only after the deadline has passed. This is the default
  behavior.

  .. freetext:: 10 regexp
    :required:
    :length: 7

    **Modifiers used in this question:** ``required`` and ``length``.

    Type either ``cat`` or ``dog``.

    ^(cat|dog)$

  .. freetext:: 10 regexp
    :length: 7

    **Modifiers used in this question:** ``length``.

    What is the value of :math:`\pi` with four most significant digits?
    This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
    ``3.141`` and zero or more digits after that.

    ^3\.141\d*$

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    a § Not quite. Remember the cube root.
    b § This is correct!
    c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.


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

    a § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.
    b § This is correct!
    c § This is correct!
    d § No. This equation has a nice and easy solution.
    e § Remember that :math:`x^2 = q \leftrightarrow x = \pm \sqrt{q}`
    f § This is correct!

.. questionnaire:: override-settings 40
  :title: Questionnaire with both options. (``:show-model:`` & ``:reveal-model-at-max-submissions:``)
  :submissions: 1
  :show-model: True
  :reveal-model-at-max-submissions: True

  This questionnaire includes the ``:show-model:`` & ``:reveal-model-at-max-submissions:``.

  .. freetext:: 10 regexp
    :required:
    :length: 7

    **Modifiers used in this question:** ``required`` and ``length``.

    Type either ``cat`` or ``dog``.

    ^(cat|dog)$

  .. freetext:: 10 regexp
    :length: 7

    **Modifiers used in this question:** ``length``.

    What is the value of :math:`\pi` with four most significant digits?
    This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
    ``3.141`` and zero or more digits after that.

    ^3\.141\d*$

  .. pick-one:: 10
    :required:

    **Modifiers used in this question:** ``required``.

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    a § Not quite. Remember the cube root.
    b § This is correct!
    c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.


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

    a § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.
    b § This is correct!
    c § This is correct!
    d § No. This equation has a nice and easy solution.
    e § Remember that :math:`x^2 = q \leftrightarrow x = \pm \sqrt{q}`
    f § This is correct!

