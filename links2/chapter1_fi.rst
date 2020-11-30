Luku links2/chapter1
====================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nisi nisi, tincidunt sed posuere et, pulvinar at libero. Curabitur nec est non arcu ornare facilisis scelerisque eget arcu. Integer id dapibus magna. Etiam aliquet velit vel viverra ullamcorper. Phasellus vel nulla eu metus auctor iaculis et non dolor. Etiam semper malesuada lacinia. Etiam ac erat velit. Suspendisse ultricies massa non felis ornare vehicula. Sed eu volutpat elit, vitae laoreet libero. Integer suscipit risus et tortor finibus, eu vehicula turpis laoreet. Morbi condimentum bibendum risus, sit amet tristique metus fermentum a. Ut at erat eu risus euismod malesuada.

Kuva
----

Tässä on kuva.

.. image:: /images/apluslogo.png
  :alt: Aplus-logo

Tiedostot
---------

Lataa tämä :download:`esimerkkikoodi </links1/files/example.py>`.

.. literalinclude:: /links1/files/example.py
  :linenos:

Linkit
------

Doc link in the same module
   :doc:`chapter2`

Doc link in another module
   :doc:`../links1/chapter2`

Ref link in the same module
   :ref:`m02 quiz <m02-quiz>`

Ref link inside the questionnaire
   :ref:`m01 quiz image <m01-quiz-img>`

Ref link in another module
   :ref:`m01 quiz <m01-quiz>`

External link
   Open `Google search <https://www.google.com>`_.


.. _m02-quiz:

Monivalintatehtävä
------------------

.. questionnaire:: link2quiz 20
  :title: Monivalintatehtävä linkkien testaamiseen moduuli links2

  Doc link in the same module
     :doc:`chapter2`

  Doc link in another module
     :doc:`../links1/chapter1`

  Ref link in the same module
     :ref:`m02 quiz <m02-quiz>`

  Ref link in another module
     :ref:`m01 quiz <m01-quiz>`

  External link
     Open `Google search <https://www.google.com>`_.


  .. pick-one:: 5

    Mitä on 8 + 2?

    *a. 10
    b. 11
    c. 13
    d. 14

  .. _m02-quiz-img:

  .. image:: /images/apluslogo.png
    :alt: Aplus logo

  .. freetext:: 15

    Kirjoita ``test2`` tähän.

    test2

  Doc link in another module in a subdirectory
     :doc:`../links1/subdir/chapter1`

  Doc link to the parent chapter of nested chapters in another module
     :doc:`../links1/chapter3index`

  Doc link in a nested chapter in another module
     :doc:`../links1/chapter3a`

  Doc link to the parent chapter in a subdirectory in another module
     :doc:`../links1/subdir/chapter2index`

  Doc link to a nested chapter in another module in the subdirectory
     :doc:`../links1/subdir/chapter2a`

