Jutut
=====

Testaa MOOC-Jutut-palautekyselyä.

.. questionnaire:: math 10
  :title: Normaali monivalintatehtävä Jutut-luvussa
  :submissions: 10

  .. pick-one:: 10

    Mitä on 1+3?

    a. 2
    b. 3
    *c. 4
    d. 5


.. questionnaire::
  :feedback:
  :title: MOOC-Jutut-testipalautekysely
  :category: jututfeedback

  .. freetext:: 0 int
    :required:
    :key: timespent
    :height: 1
    :length: 20
    :class: time-usage-question
    :extra: minimum=6;validationMessage=Anna aika minuutteina.

    **Ajankäyttö:**

    Kirjoita alle, kuinka monta minuuttia olet käyttänyt kokonaisuudessaan oppimateriaalin
    tähän lukuun (materiaalin lukeminen, tehtävien tekeminen jne.). Viidentoista minuutin
    tai puolen tunnin tarkkuus riittää hyvin.

  .. pick-one::
    :required:
    :key: understood

    **"Minusta tuntuu, että olen tajunnut oleellisimmat asiat tästä luvusta."**

    a. täysin samaa mieltä
    b. jokseenkin samaa mieltä
    c. jokseenkin eri mieltä
    d. täysin eri mieltä
    e. en osaa sanoa / en kommentoi

  .. freetext::
    :main-feedback:
    :required:
    :key: mainfeedback
    :length: 100
    :height: 8

    Anna palautetta luvusta.
