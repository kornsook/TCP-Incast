#!\bin\bash

if [ $1 -eq 1 ]
then
sudo tc qdisc del dev $1 root
fi
sudo tc qdisc add dev $2 root handle 1: htb default 10
sudo tc class add dev $2 parent 1: classid 1:10 htb rate $3Mbit
sudo tc qdisc add dev $2 parent 1:10 handle 20: netem delay 1ms limit $4

