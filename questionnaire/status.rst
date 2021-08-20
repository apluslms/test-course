Questionnaires with different Status
====================================

Status: ready
-------------
.. questionnaire:: status_ready
  :title: Question with a ``ready`` status. The questionnaire is listed in the table of content.
  :submissions: 4
  :category: Status
  :status: ready

  .. freetext:: 10 regexp

    **Modifiers used in this question:** None.

    This question accepts either ``red`` or ``blue`` as the correct answer.
    The model solution is a regular expression.

    red|blue

Status: hidden
--------------
.. questionnaire:: status_hidden
  :title: Question with a ``hidden`` status. The questionnaire is hidden from non course staff.
  :submissions: 4
  :category: Status
  :status: hidden

  .. pick-one:: 10
    :required:
    :dropdown:

    **Modifiers used in this question:** None.

    What is 1+2?

    +0. 0
    1. 1
    2. 2
    *3. 3

Status: enrollment
------------------
.. questionnaire:: status_enrollment
  :title: Question with a ``enrollment`` status. Internal students use this to enrol in the course.
  :submissions: 4
  :category: Status
  :status: enrollment

  .. freetext:: 10 string-ignorews-ignorequotes-requirecase

    **Modifiers used in this question:** ``ignorequotes`` and ``ignorews``.

    The correct answer for this question is ``test``. Surrounding quotes are ignored as well as whitespaces.

    test
    !test § Follow the instruction.
    regexp:Test|TEST § Use the lower case!

Status: enrollment_ext
----------------------
.. questionnaire:: status_enrollment_ext
  :title: Question with a ``enrollment_ext`` status. External students use this to enrol in the course.
  :submissions: 4
  :category: Status
  :status: enrollment_ext

  .. pick-any:: 10
    :partial-points:

    **Modifiers used in this question:** ``partial-point``

    Pick the options ``this is the first`` and ``this is the second``.

    +*a. this is the **first**
    *b. this is the **second**
    c. this is the **third**
    d. this is the **fourth**
    ?e. choosing this does not affect the granted points

Status: maintenance
-------------------
.. questionnaire:: status_maintenance
  :title: Question with a ``maintenance`` status. The questionnaire is hidden along with the previous submissions.
  :submissions: 4
  :category: Status
  :status: maintenance

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
