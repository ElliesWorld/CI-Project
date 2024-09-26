def generate_signals_header(signals, macros):
    file = ""

    # Add #ifndef directive
    file += "#ifndef SIGNALS_H\n"
    file += "#define SIGNALS_H\n\n"

    # Add #define directives for macros
    file += "// Macro Deffinitions\n"
    for key, values in macros.items():
        for index, item in enumerate(values):
            file += f"#define {item} {index}\n"

    # Include <cstdint>
    file += "\n#include <cstdint>\n\n"

    # Write function declarations to signals.h
    for signal in signals:
        name = signal["name"]
        type = signal["type"]
        comment = signal["comment"]
        
        # Write the doxygen comments
        file += f"""
/**
 * @brief This function is used to set {comment}.
 *
 * @param value: The value to get ({type})
 * @return The return value is: {type}.
 */
"""
        # Write the get functions
        file += f"{type} signals_get_{name}(void);\n"
        file += f"""
/**
 * @brief This function is used to get {comment}.
 * 
 * @param value: The value to set ({type})
 * @return bool: True or flase
 */
"""
        # Write the set functions
        file += f"bool signals_set_{name}({type} value);\n"

    # Add #endif directive
    file += "#endif // SIGNALS_H\n"

    return file
