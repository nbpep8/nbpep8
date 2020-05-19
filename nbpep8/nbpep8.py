def pep8():
    """ Display PEP8 analysis for a notebook cell
    Usage:
        - pep8() at the end of the notebook code cell
    Returns:
        - PEP8 analysis
    """
    global _ih
    text_file = open("cell_content.py", "w")
    n = text_file.write(_ih[-1][:] + '\n')
    text_file.close()
    s = subprocess.run(["pycodestyle", "cell_content.py"], capture_output=True)
    print(s.stdout.decode('utf8'))
    subprocess.run(["rm", "cell_content.py"], capture_output=False)
