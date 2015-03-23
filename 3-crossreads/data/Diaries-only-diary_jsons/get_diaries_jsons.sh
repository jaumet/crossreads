#!/bin/bash



for i in $(cat diariesURLs.txt); do
    wget $i
done
