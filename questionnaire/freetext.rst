Free text questionnaire
=======================

FreeText questionnaires
-----------------------

.. questionnaire:: questionnaire-freetext-examples 30
  :title: Questionnaire full of freetext questions
  :submissions: 3

  This questionnaire contains different types of questions with various modifiers.

  .. danger::

    The model answers disappear after the page is reloaded.

  .. freetext:: 5
    :length: 5

    **Modifiers used in this question:** ``length``.

    This is the most basic free text questionnaire. The correct answer is
    ``test``. You can write at most 5 characters into the box. This question provides hints to students.

    test
    !test § Hint: follow the instructions.

  .. freetext:: 5
    :height: 2

    **Modifiers used in this question:** ``height``.

    This is the basic free text questionnaire, with the **height set at 2**, so the input is transformed into a
    textbox. The correct answer is ``textbox``. This question does not provide students with a hint.

    textbox

  .. freetext:: 5
    :length: 10
    :required:

    **Modifiers used in this question:** ``length`` and ``required``.

    This specific question is **mandatory**. Therefore, the questionnaire submission is not accepted if the
    question remains unanswered. The correct answer here is ``mandatory``.

    mandatory

  .. freetext:: 5 int
    :length: 7

    **Modifiers used in this question:** ``length``.

    The answer should be an **integer**. What is :math:`3 + 8`?.

    11
    !11 § Hint to be shown when the student's answer is not 11.

  .. freetext:: 5 float
    :length: 7

    **Modifiers used in this question:** ``length``.

    The answer should be a **decimal number** (floating point number).
    What is :math:`3 / 8` in decimal? (When the question uses the float type,
    the grader also accepts answers that slightly differ from the model solution.)

    0.378
    !0.378 § Hint: the answer is between 0 and 1. Use the decimal point and write three first decimals, for example, ``0.375``.

  .. freetext:: 5 subdiff

    **Modifiers used in this question:** None.

    This question accepts either ``red`` or ``blue`` as the correct answer. But you can try answers as ``led``
    or ``clue``. You will see some interesting feedback.

    red|blue

Regex Questionnaire
-------------------

.. questionnaire:: questionnaire_regexp 30
  :title: Questionnaire using regular expressions
  :submissions: 5

  Regular expressions are useful when there are multiple solutions or when
  you want to have some tolerance in numerical questions, such as accepting real
  numbers beginning with 0.014, 0.015, or 0.016.

  .. freetext:: 10 regexp

    **Modifiers used in this question:** None.

    Type either ``cat`` or ``dog``.

    ^(cat|dog)$

  .. freetext:: 10 regexp

    **Modifiers used in this question:** None.

    What is the value of :math:`\pi` with four most significant digits?
    This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
    ``3.141`` and zero or more digits after that.

    ^3\.141\d*$

  .. freetext:: 10 regexp

    **Modifiers used in this question:** None.

    Type either ``cat`` or ``dog``. But also try with ``Dog``, ``DOG``, ``Cat`` or ``CAT``, you will get
    additional feedback.

    ^(cat|dog)$
    !cat § What about cat;
    regexp:Cat|CAT § Use the lower case!
    !dog § What about dog.
    regexp:Dog|DOG § Use the lower case!

FreeText questionnaire and modifiers
------------------------------------

.. questionnaire:: questionnaire-with-modifiers
  :title: Free text questionnaire with modifiers

  The following questions use the following modifiers.

  * ``ignorews``: ignore white space (applies to regexp too)
  * ``ignorequotes``: iqnore "quotes" around
  * ``requirecase``: require identical lower and upper cases (only with the string and subdiff types)
  * ``ignorerepl``: ignore REPL prefixes
  * ``ignoreparenthesis``: ignore parenthesis "( )"

  .. freetext:: 5 string-ignorews-ignorequotes
    :length: 10

    **Modifiers used in this question:** ``ignorequotes`` and ``ignorews``.

    Here the correct answer is either ``anothertest``, ``"anothertest"`` or ``another test``. Surrounding
    quotes are ignored in the solution as well as whitespace.

    anothertest
    !anothertest § Check the correct answer given in the description

  .. freetext:: 5 unsortedchars-ignorews
    :length: 7

    **Modifiers used in this question:** ``unsortedchars`` and ``ignorews``.

    What are the unique vowels in the word "cacophonic"? Correct answers are: ``aio``, ``aoi``, ``iao``, ``ioa``,
    ``oai``, ``oia``, and also the versions with two o's, e.g., ``aioo``, ``aooi`` and so on,  because
    *unsortedchars* always compares unique characters.

    aio

  .. freetext:: 5 string-ignorews
    :length: 7

    **Modifiers used in this question:** ``ignorews``.

    The answer can contain white spaces or not. Try answering with one of the following strings: ``Whitespaces``
    or ``White spaces``.

    White spaces

  .. freetext:: 5 string-requirecase
    :length: 7

    **Modifiers used in this question:** ``requirecase``.

    The answer should have the right case. Try answering with one of the following strings: ``White Spaces``
    or ``White spaces``. But, the correct answer is ``White spaces``.

    White spaces

  .. freetext:: 5 string-ignorews-requirecase
    :length: 7

    **Modifiers used in this question:** ``requirecase`` and ``ignorews``.

    The answer can contain white spaces or not. The answer also should use the right capitalization.
    Try answering with one of the following strings: ``White Spaces`` or ``WhiteSpaces``.
    However, the correct answer can be either ``White spaces`` or ``Whitespaces``.

    White spaces

  .. freetext:: 5 string-ignorerepl
    :height: 2

    **Modifiers used in this question:** ``ignorerepl``.

    The following question ignores REPL prefixes. If you are using the Scala REPL, what is the output of the
    following operation:

    .. code-block:: scala

      scala> val z = res0 + res1

    You can copy and paste the following snippet in the answer box below. But, you can also type the number
    five ``5`` in the answer box

    .. code-block:: scala

      z: Int = 5

    5
