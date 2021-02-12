Course Assistants can grade these exercises
===========================================


.. questionnaire:: assistant_grade_ex_1 10
  :title: Questionnaire using regular expressions
  :submissions: 1
  :allow-assistant-viewing: False
  :reveal-model-at-max-submissions: True

  Regular expressions are useful when there are multiple solutions or when
  one wants to have some tolerance in numeric questions, like accept real
  numbers beginning with 0.014, 0.015, or 0.016.

  .. freetext:: 10 regexp
    :required:
    :length: 7

    **Modifiers used in this question:** ``required`` and ``length``.

    Type either ``cat`` or ``dog``.

    ^(cat|dog)$

.. questionnaire:: assistant_grade_ex_2 10
  :title: Questionnaire using regular expressions
  :submissions: 1
  :allow-assistant-grading: True
  :reveal-model-at-max-submissions: True

  .. freetext:: 10 regexp
    :length: 7

    **Modifiers used in this question:** ``length``.

    What is the value of :math:`\pi` with four most significant digits?
    This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
    ``3.141`` and zero or more digits after that.

    ^3\.141\d*$
