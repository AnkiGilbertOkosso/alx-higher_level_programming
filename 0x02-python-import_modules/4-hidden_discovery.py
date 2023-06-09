#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    my_name = dir(hidden_4)
    for name in my_name:
        if name[:2] != "__":
            print(name)
