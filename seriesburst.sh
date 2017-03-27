DIR=$(pwd)
for i in {1..9}
do
    for back in {0,0.1,1}
    do
        for n in {100,1000}
        do
            python ~/gitrepos/generative-art/randomburst.py $DIR $back"back"_$n"part"_$i"_"$1".png" $back $n
        done
    done
done
