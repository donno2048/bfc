#!/bin/bash
set -e
bfc tests/0.bf 0
bfc tests/hello_world.bf hello
bfc tests/reverse.bf reverse
bfc tests/sort.bf sort
if [[ $(./0) != "0" ]]; then
    echo "test 1 failed"
    exit 1
fi
if [[ $(./hello) != "Hello, World!" ]]; then
    echo "test 2 failed"
    exit 1
fi
if [[ $(printf "test" | ./reverse) != "tset" ]]; then
    echo "test 3 failed"
    exit 1
fi
if [[ $(printf "test" | ./sort) != "estt" ]]; then
    echo "test 4 failed"
    exit 1
fi
echo "success"
