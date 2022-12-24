#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports():
    import toml


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        if fdp.ConsumeBool():
            toml.loads(fdp.ConsumeRemainingString())
        else:
            toml.dumps(fuzz_helpers.build_fuzz_dict(fdp, [str, list, str]))
    except toml.TomlDecodeError:
        return -1


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
