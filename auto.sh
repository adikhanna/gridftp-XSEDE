#!/bin/bash
# javac Automator_Supermic.java
# java Automator_Supermic
# echo "Supermic to Bridges done"
javac Automator_Stampede.java
for ((i=1; i <= 5; i++))
do
  java Automator_Stampede
  echo "Stampede to Comet done"
done
