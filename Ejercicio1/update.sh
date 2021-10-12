#!/bin/bash

rm mensaje.txt
cp original_message.txt mensaje.txt
python3 code_decrypt.py
cat mensaje.txt
