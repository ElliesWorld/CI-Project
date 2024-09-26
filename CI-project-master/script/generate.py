#!/usr/bin/env python3

import os
import json
from pathlib import Path
import source_generator as src
import text_generator as text
import test_generator as test
import header_generator as head

ROOT = Path(__file__).parent.parent

SIGNALS_DIR = f"{ROOT}/lib/signals/"
TEST_DIR = f"{ROOT}/test/"
JSON_DIR = f"{ROOT}/script/data.json"

# check if directories exist and create them if they don't
os.makedirs(SIGNALS_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

# copying the contents of the json file into a variable called data
with open(JSON_DIR, 'r') as file:
    data = json.load(file)

# separating the contents of the json file into the signals and macros
signals = data['signals']
macros = data['defines']
del data

# function to write a string to a file in a chosen directory
def write_file(directory: str, filename: str, content: str):

    file_path = os.path.join(directory, filename)

    with open(file_path, "w") as file:
        file.write(content)

# Commented functions are the real ones to be used later on

write_file(SIGNALS_DIR, "signals.cpp", src.generate(signals, macros))
write_file(SIGNALS_DIR, "signals.h", head.generate_signals_header(signals, macros))
write_file(SIGNALS_DIR, "signals.txt", text.generate_text_file(signals, macros))
write_file(TEST_DIR, "test.cpp", test.generate_tests(signals, macros))

