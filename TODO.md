----------
DONE
(base) eugene@eugene-All-Series:~/Projects/neural-style-pt$ python neural_style.py -style_image ~/Pictures/1/starship1.jpeg -content_image ~/Pictures/1/station.jpg -output_image profile.png -gpu 1  -num_iterations 1000 -image_size 550 -backend cudnn
Traceback (most recent call last):
  File "neural_style.py", line 10, in <module>
    from koila import LazyTensor, lazy
ModuleNotFoundError: No module named 'koila'

sudo pip install koila
pip install koila
----------
DONE
pip search koila
 <Fault -32500: "RuntimeError: PyPI's XMLRPC API is currently disabled due to unmanageable load and will be deprecated in the near future. See https://status.python.org/ for more information.">

pip install pip_search
pip_search koila

-----------