echo 'hello world'
git clone https://github.com/PixarAnimationStudios/USD.git
apt-get update
apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev
pip3 install PySide2
pip3 install PyOpenGL
python USD/build_scripts/build_usd.py ../local/USD