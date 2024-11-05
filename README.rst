README
######

Local dev setup and testing
***************************
.. code-block:: bash
   :linenos:
   
   python ./bb.py # Will build web server in ./build 
   python -m http.server 8080 -d source/ # will host web server at localhost:8000 until ctrl-c
