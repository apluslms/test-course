Chapter links1/chapter1
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

Doc link in the same module
   :doc:`chapter2`

Doc link in another module
   :doc:`chapter1 in links2 <../links2/chapter1>`

Ref link in the same module
   :ref:`m01 quiz <m01-quiz>`

Ref link inside the questionnaire
   :ref:`m01 quiz image <m01-quiz-img>`

Ref link in another module
   :ref:`m02 quiz <m02-quiz>`

Absolute external link
   Open `Google search <https://www.google.com>`_.

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

Ref link to the questionnaire in the subdirectory chapter
   :ref:`m01 subdir quiz <m01-subdir-quiz>`

Ref link to the image in the questionnaire in the subdirectory chapter
   :ref:`m01 subdir quiz image <m01-subdir-quiz-img>`

Manually written link to a model solution
   `Model solution of links1/chapter2 quiz <../links1/chapter2/links1_chapter2_linkquiz/info/model/>`_

Manually written link to a model solution
   `Model solution of links1/chapter1 Python exercise <../links1/chapter1/links1_chapter1_examplepython1/info/model/>`_

Manually written link to an exercise template file
   `Template file of links1/chapter1 Python exercise <../links1/chapter1/links1_chapter1_examplepython1/info/template/>`_

Manually written link to the model solution of the subdirectory chapter
   `Model solution of links1/subdir/chapter1 quiz <../links1/subdir_chapter1/links1_subdir_chapter1_linksubdirquiz/info/model/>`_


.. _m01-python:

Python exercise
---------------

Simple Python programming exercise.

.. submit:: examplepython1 100
  :title: Python Example
  :submissions: 99
  :points-to-pass: 50
  :config: exercises/example_python/config.yaml

  In this exercise, you must implement a function ``greeting`` that takes **one parameter** and
  **returns** the string :literal:`Hello, \ ` appended with the parameter value and ``!``.

  **Here is an image.**

  .. _m01-python-img:

  .. image:: /images/apluslogo.png
    :alt: Aplus logo

  Download this :download:`example code <files/example.py>`.

  .. literalinclude:: files/example.py
    :linenos:

  **Links**

  Doc link in the same module
     :doc:`chapter2`

  Doc link in another module, different format
     :doc:`chapter1 in links2 <../links2/chapter1>`

  Ref link in the same module
     :ref:`m01 quiz <m01-quiz>`

  Ref link inside the questionnaire
     :ref:`m01 quiz image <m01-quiz-img>`

  Ref link in another module
     :ref:`m02 quiz <m02-quiz>`

  Absolute external link
     Open `Google search <https://www.google.com>`_.

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

  Ref link to the questionnaire in the subdirectory chapter
     :ref:`m01 subdir quiz <m01-subdir-quiz>`

  Ref link to the image in the questionnaire in the subdirectory chapter
     :ref:`m01 subdir quiz image <m01-subdir-quiz-img>`

  Manually written link to a model solution
     `Model solution of links1/chapter2 quiz <../links1/chapter2/links1_chapter2_linkquiz/info/model/>`_

  Manually written link to a model solution
     `Model solution of links1/chapter1 Python exercise <../links1/chapter1/links1_chapter1_examplepython1/info/model/>`_

  Manually written link to an exercise template file
     `Template file of links1/chapter1 Python exercise <../links1/chapter1/links1_chapter1_examplepython1/info/template/>`_

  Manually written link to the model solution of the subdirectory chapter
     `Model solution of links1/subdir/chapter1 quiz <../links1/subdir_chapter1/links1_subdir_chapter1_linksubdirquiz/info/model/>`_


Small quiz
----------

.. questionnaire:: verysmallquiz 8
  :title: Very small quiz
  :submissions: 3

  .. pick-one:: 8

    Pick ``1``.

    *a. 1
    b. 2
    c. 3
