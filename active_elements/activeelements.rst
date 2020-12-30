Active elements
===============

Test active elements.

Minimal example
---------------

This active element comprises one input and one output field.
The output simply echoes the input.

.. ae-input:: min_input
  :title: Give some input
  :width: 50%
  :height: 34px
  :class: active-element left

.. ae-output:: min_output
  :config: aelements/minimal/config.yaml
  :inputs: min_input
  :title: Output element
  :width: 50%
  :class: active-element left

Exponential distribution
------------------------

.. ae-input:: exponentlambdain
  :title: Parameter lambda for the exponential distribution
  :default: 0.4
  :class: active-element ae-input left
  :width: 20%
  :height: 34px

.. ae-output:: exponentialdist
  :config: aelements/exponentialdist/config.yaml
  :inputs: exponentlambdain
  :title: Probability density function and the cumulative distribution function of the exponential distribution
  :type: html
  :class: active-element left no-border
  :scale-size:
  :width: 70%

.. rst-class:: clear-float

Bivariate normal distribution
-----------------------------

.. ae-input:: twonormalmuin
  :title: Mean vector mu of the normal distribution
  :default: [0 0]
  :class: active-element ae-input left
  :width: 10%
  :height: 34px

.. ae-input:: twonormalsigmain
  :title: 2 * 2 covariance matrix of the normal distribution
  :default: [1 .5; .5 1]
  :class: active-element ae-input left
  :width: 10%
  :height: 34px

.. ae-output:: twodimnormaldist
  :config: aelements/twodimnormaldist/config.yaml
  :inputs: twonormalmuin twonormalsigmain
  :title: Probability density function of the bivariate normal distribution
  :type: html
  :class: active-element left no-border
  :scale-size:
  :width: 70%

