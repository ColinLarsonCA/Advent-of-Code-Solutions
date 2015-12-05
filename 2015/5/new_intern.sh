#!/bin/bash

cat input |  grep "\(..\).*\1" | grep "\(.\).\1" | wc -l
