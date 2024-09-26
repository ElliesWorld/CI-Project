# Generate C++ test cases for the given signals. 
def generate_tests(signals: dict, defines: dict) -> str: 
    tests = '#include <gtest/gtest.h>\n#include "signals.h"\n\n'
    # Generates test cases to check setting and getting values within and outside the range.
    for signal in signals:
        if "range" in signal:  
            lower_bound, upper_bound = signal["range"]
            increment = 0.1 if signal["type"] == "float" else 1
            tests += f'''
TEST(signal_test, {signal["name"]})
{{
    {signal["type"]} value;

    value = {lower_bound};
    EXPECT_TRUE(signals_set_{signal["name"]}(value));
    EXPECT_EQ(value, signals_get_{signal["name"]}());

    value = {upper_bound};
    EXPECT_TRUE(signals_set_{signal["name"]}(value));
    EXPECT_EQ(value, signals_get_{signal["name"]}());

    value = {upper_bound} + {increment};
    EXPECT_FALSE(signals_set_{signal["name"]}(value));

    value = {lower_bound} - {increment};
    EXPECT_FALSE(signals_set_{signal["name"]}(value));
}}
'''
        elif 'values' in signal:
            invalid_state = len(defines[signal["values"]]) 
            state_test_cases = "\n".join([
                f'''
    EXPECT_TRUE(signals_set_{signal["name"]}({state}));
    EXPECT_EQ({state}, signals_get_{signal["name"]}());\n''' for state in defines[signal["values"]]
            ])
            
            # For invalid case
            state_test_cases += f'''
    EXPECT_FALSE(signals_set_{signal["name"]}({invalid_state}));'''

            tests += f'''
TEST(signal_state_test, {signal["name"]})
{{
    uint8_t value;\n\n{state_test_cases}
}}
'''
    return tests

