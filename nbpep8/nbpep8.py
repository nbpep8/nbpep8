def pep8(content: str = _ih) -> None:
    """ Display PEP8 analysis for a notebook cell
    Usage:
        - pep8(content: str) at the end of the notebook code cell
    Returns:
        - PEP8 analysis
    """
    import subprocess
    from subprocess import PIPE
    
    text_file = open("cell_content.py", "w")
    n = text_file.write(content[-1][:] + '\n')
    text_file.close()
    s = subprocess.run(["pycodestyle", "cell_content.py"], stdout=PIPE, stderr=PIPE)
    print(s.stdout.decode('utf8'))
    subprocess.run(["rm", "cell_content.py"],  stdout=PIPE, stderr=PIPE)
