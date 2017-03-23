DIR=$(pwd)
for i in {1..9}
do
    python ~/gitrepos/generative-art/randomburst.py $DIR $i"_"$1".png"
done
montage [1-9]_$1.png -geometry 600x400 "grid_"$1.png
