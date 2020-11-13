Chapter links1/subdir/chapter1
==============================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nisi nisi, tincidunt sed posuere et, pulvinar at libero. Curabitur nec est non arcu ornare facilisis scelerisque eget arcu. Integer id dapibus magna. Etiam aliquet velit vel viverra ullamcorper. Phasellus vel nulla eu metus auctor iaculis et non dolor. Etiam semper malesuada lacinia. Etiam ac erat velit. Suspendisse ultricies massa non felis ornare vehicula. Sed eu volutpat elit, vitae laoreet libero. Integer suscipit risus et tortor finibus, eu vehicula turpis laoreet. Morbi condimentum bibendum risus, sit amet tristique metus fermentum a. Ut at erat eu risus euismod malesuada.

Image
-----

Here is an image.

.. image:: /images/apluslogo.png
  :alt: Aplus logo

Files
-----

Download this :download:`example code <../files/example.py>`.

.. literalinclude:: ../files/example.py
  :linenos:

Links
-----

Doc link in the same module
   :doc:`chapter2index`

Doc link in another module
   :doc:`../../links2/chapter2`

Ref link in the same module
   :ref:`m01 quiz <m01-quiz>`

Ref link inside the questionnaire
   :ref:`m01 quiz image <m01-quiz-img>`

Ref link in another module
   :ref:`m02 quiz <m02-quiz>`

External link
   Open `Google search <https://www.google.com>`_.


.. _m01-subdir-quiz:

Questionnaire
-------------

.. questionnaire:: linksubdirquiz 10
  :title: Questionnaire in a subdirectory for testing links

  Doc link in the same module
     :doc:`chapter2index`

  Doc link in another module
     :doc:`../../links2/chapter2`

  Ref link in the same module
     :ref:`m01 quiz <m01-quiz>`

  Ref link in another module
     :ref:`m02 quiz <m02-quiz>`

  External link
     Open `Google search <https://www.google.com>`_.


  .. pick-one:: 5

    What is 2 + 4?

    a. 3
    b. 4
    c. 5
    *d. 6

  .. _m01-subdir-quiz-img:

  .. image:: /images/apluslogo.png
    :alt: Aplus logo

  .. freetext:: 5

    Write ``testsub`` here.

    testsub

  Doc link in the same module in the parent directory
     :doc:`../chapter1`

  Doc link to the parent chapter of nested chapters
     :doc:`chapter2index`

  Doc link in a nested chapter
     :doc:`chapter2a`

  Doc link to the parent chapter in the parent directory
     :doc:`../chapter3index`

  Doc link in a nested chapter in the parent directory
     :doc:`../chapter3a`

