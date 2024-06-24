#!/bin/bash

# Make all Python files executable
chmod u+x *.py

black $(ls *.py | grep -v 'main')

# Run pycodestyle on all Python files, excluding those containing "main" in their names
pycodestyle $(ls *.py | grep -v 'main')
