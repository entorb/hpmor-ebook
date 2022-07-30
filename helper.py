import requests


def download_file(url: str, filepath: str):
    """download file from url to filepath"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0 ',
    }
    cont = requests.get(url, headers=headers, verify=True).content
    # verify=False -> skip SSL cert verification: CERTIFICATE_VERIFY_FAILED
    with open(filepath, mode='bw') as fh:
        fh.write(cont)


def get_html_start(lang: str) -> str:
    assert lang in ('en', 'de')
    if lang == 'en':
        html_start = """<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="author" content="Eliezer Yudkowsky" />
<title>Harry Potter and the Methods of Rationality</title>
</head>
<body>
"""
    elif lang == 'de':
        html_start = """<!DOCTYPE html>
<html lang="de">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="author" content="Eliezer Yudkowsky" />
<title>Harry Potter und die Methoden des rationalen Denkens</title>
</head>
<body>
"""
    return html_start
