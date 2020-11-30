Chapter links1/chapter2
=======================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nisi nisi, tincidunt sed posuere et, pulvinar at libero. Curabitur nec est non arcu ornare facilisis scelerisque eget arcu. Integer id dapibus magna. Etiam aliquet velit vel viverra ullamcorper. Phasellus vel nulla eu metus auctor iaculis et non dolor. Etiam semper malesuada lacinia. Etiam ac erat velit. Suspendisse ultricies massa non felis ornare vehicula. Sed eu volutpat elit, vitae laoreet libero. Integer suscipit risus et tortor finibus, eu vehicula turpis laoreet. Morbi condimentum bibendum risus, sit amet tristique metus fermentum a. Ut at erat eu risus euismod malesuada.

Image
-----

Here is an image.

.. image:: /images/apluslogo.png
  :alt: Aplus logo

Files
-----

Download this :download:`example code <files/example.py>`.

.. literalinclude:: files/example.py
  :linenos:

Links
-----

Doc link in the same module (with language suffix)
   :doc:`chapter1_en`

Doc link in another module
   :doc:`../links2/chapter2`

Ref link in the same module
   :ref:`m01 quiz <m01-quiz>`

Ref link inside the questionnaire
   :ref:`m01 quiz image <m01-quiz-img>`

Ref link in another module
   :ref:`m02 quiz <m02-quiz>`

External link
   Open `Google search <https://www.google.com>`_.


.. _m01-quiz:

Questionnaire
-------------

.. questionnaire:: linkquiz 10
  :title: Questionnaire for testing links

  Doc link in the same module
     :doc:`chapter1`

  Doc link in another module
     :doc:`../links2/chapter2`

  Ref link in the same module
     :ref:`m01 quiz <m01-quiz>`

  Ref link in another module
     :ref:`m02 quiz <m02-quiz>`

  External link
     Open `Google search <https://www.google.com>`_.


  .. pick-one:: 5

    What is 1 + 2?

    a. 1
    b. 2
    *c. 3
    d. 4

  .. _m01-quiz-img:

  .. image:: /images/apluslogo.png
    :alt: Aplus logo

  .. freetext:: 5

    Write ``test`` here.

    test

  Doc link in the same module in a subdirectory
     :doc:`subdir/chapter1`

  Doc link to the parent chapter of nested chapters
     :doc:`chapter3index`

  Doc link in a nested chapter
     :doc:`chapter3a`

  Doc link to the parent chapter in a subdirectory
     :doc:`subdir/chapter2index`

  Doc link in a nested chapter
     :doc:`subdir/chapter2a`

