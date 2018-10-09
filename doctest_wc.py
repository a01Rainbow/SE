 # Everything is in a docstring!
"""
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/test1.txt testinputs/test2.txt', shell=True)
b'\\t10\\t10\\t20\\ttestinputs/test1.txt\\n\\t4\\t5\\t18\\ttestinputs/test2.txt\\n\\t14\\t15\\t38\\ttotal\\n'

>>> subprocess.check_output('python3 wc.py -l testinputs/test1.txt', shell=True)
b'\\t10\\ttestinputs/test1.txt\\n'

>>> subprocess.check_output('python3 wc.py -w testinputs/test1.txt', shell=True)
b'\\t10\\ttestinputs/test1.txt\\n'

>>> subprocess.check_output('python3 wc.py -c testinputs/test1.txt', shell=True)
b'\\t20\\ttestinputs/test1.txt\\n'

"""

 # We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()
