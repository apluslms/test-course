Jutut på svenska
================

Testa MOOC-Jutut feedback frågeformulär.

Test MOOC-Jutut feedback questionnaires.

.. questionnaire:: math 10
  :title: Normalt frågeformulär i det Jutut kapitlet
  :submissions: 10

  .. pick-one:: 10

    Vad är 1+3?

    a. 2
    b. 3
    *c. 4
    d. 5


.. questionnaire::
  :feedback:
  :title: MOOC-Jutut test feedback frågeformulär
  :category: jututfeedback

  .. freetext:: 0 int
    :required:
    :key: timespent
    :height: 1
    :length: 20
    :class: time-usage-question
    :extra: minimum=6;validationMessage=Ange tid i minuter.

    **Spenderad tid:**

    Beräkna det totala antalet minuter du har tillbringat på detta kapitel (läsning, uppgifter,
    osv.). Du behöver inte vara exakt, men om du kan göra en uppskattning inom 15 minuter eller
    en halvtimme, det skulle vara jättebra.

  .. pick-one::
    :required:
    :key: understood

    **"Jag känner att jag har förstått de viktigaste sakerna i detta kapitel."**

    a. instämmer helt
    b. instämmer delvis
    c. instämmer inte
    d. instämmer inte alls
    e. Jag kan inte svara eller vill inte kommentera.

  .. freetext::
    :main-feedback:
    :required:
    :key: mainfeedback
    :length: 100
    :height: 8

    Ge feedback om detta kapitel.
