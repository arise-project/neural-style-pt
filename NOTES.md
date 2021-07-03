1) it is work for my mb with only cudnn:

USE_NNPACK=0 python neural_style.py -style_image ~/Pictures/1/starship1.jpeg -content_image ~/Pictures/1/station.jpg -output_image profile.png -gpu 1  -num_iterations 1000 -image_size 550 -backend cudnn

2) workswith two gpu

python neural_style.py -style_image ~/Pictures/1/first_symbols.jpg -content_image ~/Pictures/1/rabbit.jpg -output_image profile.png -gpu 0,1 -multidevice_strategy 9  -num_iterations 1000 -image_size 950 -optimizer adam -backend cudnn



python neural_style.py -style_image /home/eugene/Pictures/grid/norm/s/11.jpg -content_image /home/eugene/Pictures/grid/norm/c/13.jpg -output_image profile.png -gpu 0,1 -multidevice_strategy 6  -num_iterations 10000 -image_size 1250 -optimizer adam -backend cudnn



python neural_style.py -style_image /home/eugene/Projects/neural-style-pt/P4.png -content_image /home/eugene/Projects/neural-style-pt/p3.png -output_image profile.png -gpu 0,1 -multidevice_strategy 6  -num_iterations 10000 -image_size 1050 -optimizer adam -backend cudnn -style_weight 1250

