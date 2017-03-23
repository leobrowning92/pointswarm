DIR=$(pwd)
for i in {1..9}
do
    python ~/gitrepos/generative-art/randomburst.py $DIR $i".png"
done
montage [1-9].png -geometry 600x400 grid.png
