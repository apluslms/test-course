Kapitlet links1/subdir/chapter1
===============================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nisi nisi, tincidunt sed posuere et, pulvinar at libero. Curabitur nec est non arcu ornare facilisis scelerisque eget arcu. Integer id dapibus magna. Etiam aliquet velit vel viverra ullamcorper. Phasellus vel nulla eu metus auctor iaculis et non dolor. Etiam semper malesuada lacinia. Etiam ac erat velit. Suspendisse ultricies massa non felis ornare vehicula. Sed eu volutpat elit, vitae laoreet libero. Integer suscipit risus et tortor finibus, eu vehicula turpis laoreet. Morbi condimentum bibendum risus, sit amet tristique metus fermentum a. Ut at erat eu risus euismod malesuada.

Bild
----

Here is an image.

.. image:: /images/apluslogo.png
  :alt: Aplus logotyp

Filar
-----

Download this :download:`example code <../files/example.py>`.

.. literalinclude:: ../files/example.py
  :linenos:

Länkar
------

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

Manually written link to a model solution
   `Model solution of links1/chapter2 quiz <../../links1/chapter2/links1_chapter2_linkquiz/info/model/>`_

Manually written link to a model solution
   `Model solution of links1/chapter1 Python exercise <../../links1/chapter1/links1_chapter1_examplepython1/info/model/>`_

Manually written link to an exercise template file
   `Template file of links1/chapter1 Python exercise <../../links1/chapter1/links1_chapter1_examplepython1/info/template/>`_

Manually written link to the model solution of the subdirectory chapter
   `Model solution of links1/subdir/chapter1 quiz <../../links1/subdir_chapter1/links1_subdir_chapter1_linksubdirquiz/info/model/>`_


.. _m01-subdir-quiz:

Frågeformulär
-------------

.. questionnaire:: linksubdirquiz 10
  :title: Frågeformulär in en underkatalog för att test länkar

  **Svensk uppgift**

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
    :alt: Aplus logotyp

  Download this :download:`example code <../files/example.py>`.

  .. literalinclude:: ../files/example.py
    :linenos:

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

  Manually written link to a model solution
     `Model solution of links1/chapter2 quiz <../../links1/chapter2/links1_chapter2_linkquiz/info/model/>`_

  Manually written link to a model solution
     `Model solution of links1/chapter1 Python exercise <../../links1/chapter1/links1_chapter1_examplepython1/info/model/>`_

  Manually written link to an exercise template file
     `Template file of links1/chapter1 Python exercise <../../links1/chapter1/links1_chapter1_examplepython1/info/template/>`_

  Manually written link to the model solution of the subdirectory chapter
     `Model solution of links1/subdir/chapter1 quiz <../../links1/subdir_chapter1/links1_subdir_chapter1_linksubdirquiz/info/model/>`_

