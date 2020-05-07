#!  /usr/bin/bash

echo "This is a password generator"
echo "Enter the length of the password"
read len
for p in $(seq 1 5);
do
openssl rand -base64 48 | cut -c1-$len
done