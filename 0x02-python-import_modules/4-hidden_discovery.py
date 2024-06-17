#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4  # type: ignore
    attrs = dir(hidden_4)
    for attr in attrs:
        if attr[:2] != "__":
            print("{:s}".format(attr))
