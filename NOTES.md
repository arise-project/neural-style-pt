1) it is work for my mb with only cudnn:

USE_NNPACK=0 python neural_style.py -style_image ~/Pictures/1/starship1.jpeg -content_image ~/Pictures/1/station.jpg -output_image profile.png -gpu 1  -num_iterations 1000 -image_size 550 -backend cudnn

2) workswith two gpu

python neural_style.py -style_image ~/Pictures/1/first_symbols.jpg -content_image ~/Pictures/1/rabbit.jpg -output_image profile.png -gpu 0,1 -multidevice_strategy 9  -num_iterations 1000 -image_size 950 -optimizer adam -backend cudnn

