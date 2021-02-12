Questionnaires with a custom category
=====================================

Questionnaire with a category named - Aplus questionnaire
---------------------------------------------------------

.. questionnaire:: category-ex1
  :title: Questionnaire with category "Aplus questionnaire"
  :category: Aplus questionnaire

  .. pick-one:: 10

    **Modifiers used in this question:** None.

    Is Aplus considered a Learning Management System (LMS)?.

    a. No
    *b. Yes
    ?c. Don't know

    a § A learning management system (LMS) is a software application for the administration, documentation, tracking, reporting, automation and delivery of educational courses, training programs, or learning and development programs [1]_.
    b § Yes, Aplus is considered a LMS.
    c § Visit `the Aplus website <https://apluslms.github.io/>`_

.. questionnaire:: category-ex2
  :title: Questionnaire with category "Aplus questionnaire"
  :category: Aplus questionnaire

  .. pick-any:: 10

    **Modifiers used in this question:** None.

    Which services/systems/tools can be integrated with Aplus?

    a. `CodeGrade <https://www.codegrade.com/>`_.
    *b. `Acos <https://acos.cs.aalto.fi/>`_.
    *c. `Rubyric <https://rubyric.cs.hut.fi/>`_.
    d. `Github classroom <https://classroom.github.com/>`_.
    *e. `Lab Queue <https://tilkkutakki.cs.aalto.fi/neuvontajono/queue>`_.
    f. `Google classroom <https://classroom.google.com>`_.
    ?g. Services that allow LMS integration

    a § Aplus does not connect with CodeGrade.
    !b § Acos is part of the main Aplus services.
    b § Acos can be used in Aplus by adding the ``acos-submit`` directive.
    !c § Rubyric is part of the main Aplus services.
    c § Rubyric can be used in Aplus by adding the ``submit`` directive
    d § No. we do not support Github Classroom.
    !e § Lab Queue or neuvontajono is part of the main Aplus services.
    e § Lab Queue can be used in Aplus.
    d § No. we do not support Google Classroom.
    g § Any service that support LMS integration can be integrated with Aplus.

----

References
..........

.. [1] Ellis, Ryann K. (2009), Field Guide to Learning Management, ASTD Learning Circuits, archived from the
   original on 24 August 2014, retrieved 5 July 2012

