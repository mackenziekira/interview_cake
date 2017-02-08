#!/bin/bash

touch $1

echo "if __name__ == '__main__':" > $1
echo "    import doctest" >> $1
echo "    doctest.testmod()" >> $1

subl $1