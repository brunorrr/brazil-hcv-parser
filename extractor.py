import os
import zipfile
import urllib.request

print('Starting CSVs downloading and extraction.')

if not os.path.isdir('temp'):
    os.mkdir('temp')
    print('Dir "temp" added.')
if not os.path.isdir('temp/zip'):
    os.mkdir('temp/zip')
    print('Dir "temp/zip" added.')
if not os.path.isdir('temp/csv'):
    os.mkdir('temp/csv')
    print('Dir "temp/csv" added.')

if os.path.isfile('temp/zip/download.zip'):
    os.remove('temp/zip/download.zip')
    print('Dir "temp/zip/download.zip" removed before the download.')

for fileName in os.scandir('temp/csv'):
    try:
        os.remove(os.path.join(fileName))
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (os.path.join(fileName), e))
print('Temp files removed, if there are any')

print('Downloading the zipped CSVs')
(path,response) = urllib.request.urlretrieve('http://ftp.dadosabertos.ans.gov.br/FTP/PDA/operadoras_e_prestadores_nao_hospitalares/operadoras_e_prestadores_nao_hospitalares.zip', 'temp/zip/download.zip')
print('.zip downloaded to the path %s, it weights %sKBs' % (path, response.get('Content-Length')))

print('Extracting the CSVs to temp/csv')
zip = zipfile.ZipFile(path)
zip.extractall('temp/csv')
zip.close()
print('CSVs extracted to temp/csv')
print('Done!')