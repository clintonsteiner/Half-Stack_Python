Example using bazel-remote-cache to host packages
#################################################

Install and run bazel-remote build cache
****************************************
.. code-block:: bash
   :linenos:

   /opt/homebrew/bin/bazel-remote --max_size 1000 \
   --dir /Users/cs/bazel_cache --profile_host 127.0.0.1 \
   --profile_port 8000 --enable_endpoint_metrics

As before our tarball will be essentially blank consisting of one
file in a .tar.gz zip

***************
Confirm working
.. code-block:: bash

   curl http://localhost:8080/status

Upload tarball
**************
.. code-block:: bash

   curl -o ./generic.tar.gz http://localhost:8080/cache/cas/739ac58f6dc82cf2e62df56e07eda32213aa7e3148e1ff4a71b0be329c6f27d2

Download generic tarball
************************
.. code-block:: bash
   
   curl -o ./generic.tar.gz http://localhost:8080/cache/cas/739ac58f6dc82cf2e62df56e07eda32213aa7e3148e1ff4a71b0be329c6f27d2


   
