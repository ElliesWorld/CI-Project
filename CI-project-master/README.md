[![.github/workflows/signals.yml](https://github.com/albfor/CI-project/actions/workflows/signals.yml/badge.svg?event=push)](https://github.com/albfor/CI-project/actions/workflows/signals.yml)

# CI Project

In this teamwork project you are supposed to develop python scripts to automatically generate a maintainable C++ module to get and set signal values based on a structured signals in data.json accroding to the requirements below:

1. Make a private repository for the project and invite your teammates as collaborators
2. Follow the Scrum framework and Github Project to organize the project
3. Follow the Github Flow strategy
4. The python scripts shall automatically generated
  * A C++ module named signals in directory lib/signals
      * There shall be a header file(signals.h) and a source file(signals.cpp).
      * The module shall have getters and setters to get and set signal values
          * To set and get the value of a signal the buffer module shall be used. In signals.cpp you need to define a buffer(an array of uint8_t) whose size is calculated according to the signals in data.json
      * A function name is made of two parts; signals_get_/signals_set_ and name of the signal. For example:
          * bool signals_set_temperature(float value);
          * float signals_get_temperature(void);
      * Precision of float values shall be 0.1f. To insert a float value into the buffer, divide the float value by the precision and convert the result to an integer and then insert the integer value into the buffer. To extract a float value from the buffer, extract the integer value and then multiply it by the precision.
      * In the header file of the module, macros for the defines in data.json based on the indices of elements in the arrays shall be created, and in the implementation file, the macros shall be used. E.g. OFF is 0 and ON is 1.
      * Describe the function declarations  in the header file using the doxygen format.
  List of signals as a text file (signals.txt) lib/signals 
  test.cpp in directory test to test the c++ module using googletest. All the functions in the signals module shall be tested. For setter functions the following cases shall be tested:
        * The boundaries specified in the signal range/values
        * An invalid value greater than the upper boundary
        * If  possible, an invalid value lesser than the lower boundary
  * The python scripts shall be able to handle changes in data.json. E.g. If we add a new signal to the signals list there shall be no need to change the python scripts.
      * To get VG, the generated module shall suport setting and getting negative values for the signals.
5. To build and run the generated test a cmake file shall be used
  * There shall be a custom target to run the python program
6. Use a Github Actions workflow which is triggered on push to any branch, but not main and pull request to main in order to build and run the test.
  * Create a status badge in the README.md file the repository
7. Use modular programming to develop the python program. For example; a module to generate the test, a module to generate the signals list and etc.
  * In generate.py use the modules to make the program.
