sudo tc qdisc del dev $1 root
sudo tc qdisc add dev $1 root handle 1: htb default 10
sudo tc class add dev $1 parent 1: classid 1:10 htb rate 1000Mbit
sudo tc qdisc add dev $1 parent 1:10 handle 20: netem delay 1ms limit $2

