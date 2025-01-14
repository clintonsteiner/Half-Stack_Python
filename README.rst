README
######

Local dev setup and testing
***************************
.. code-block:: bash
   :linenos:

   uv sync
   uv run pre-commit install

   # Building html
   make html
   uv run python -m http.server --directory build/html/
