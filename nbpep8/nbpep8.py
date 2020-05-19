def pep8():
    """ Display PEP8 analysis for a notebook cell
    Usage:
        - pep8() at the end of the notebook code cell
    Returns:
        - PEP8 analysis
    """
    text_file = open("cell_content.py", "w")
    n = text_file.write(_ih[-1][:] + '\n')
    text_file.close()
    !pycodestyle cell_content.py
    !rm cell_content.py 
