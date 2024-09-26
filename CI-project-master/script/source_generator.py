from math import ceil
from io import StringIO
from textwrap import dedent

def generate(signals: dict, macros: dict) -> str:
    buf_size = ceil(sum(signal["length"] for signal in signals) / 8)
    src = StringIO()
    print(dedent(f'''\
    #include <cstdint>
    #include "buffer.h"
    #include "signals.h"

    static constexpr float PRECISION = 0.1f;
    uint8_t buf[{buf_size}]{{0}};'''), file=src)

    for signal in signals:
        # setters
        print(dedent(f'''
        bool signals_set_{signal["name"]}({signal["type"]} value)
        {{
            bool status{{false}};
        '''), file=src)

        if 'range' in signal:
            print(f'    if (value >= {signal["range"][0]} && value <= {signal["range"][1]})\n    {{', file=src)
        elif 'values' in signal:
            print(f'    if (value <= {macros[signal["values"]][-1]})\n    {{', file=src)
        print(dedent(f'''\
                buffer_insert(buf, {signal["start"]}, {signal["length"]}, {'static_cast<int>(value / PRECISION)' if signal["type"] == 'float' else 'value'});
                status = true;
            }}

            return status;
        }}'''), file=src)

        # getters
        print(dedent(f'''
        {signal["type"]} signals_get_{signal["name"]}(void)
        {{'''), file=src)

        if 'range' in signal and signal['range'][0] < 0:
            print(dedent(f'''\
                auto value = buffer_extract(buf, {signal["start"]}, {signal["length"]});
                if (value & (1 << ({signal["length"]} - 1)))
                {{
                    for (int i = {signal["length"]}; i < sizeof({signal["type"]}) * 8; i++)
                    {{
                        value |= (1 << i);
                    }}
                }}
                return {"(int32_t) value * PRECISION" if signal["type"] == "float" else "value"};
            }} '''), file=src)
        else:
            print(f'    return buffer_extract(buf, {signal["start"]}, {signal["length"]}){" * PRECISION" if signal["type"] == "float" else ""};\n}}', file=src)

    return src.getvalue()

