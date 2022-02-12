# Brazilian Private Health Care System Viewer

The main goal of this project is to centralize in a unique system the essential information about private health care providers in Brazil regarding what cities, states of the country they operate. Also what plans they offer to costumers and with which hospitals and medical clinic these plans cover. As the point of view of someone who needs information about plans in a location, the system will find hospitals based on location and, subsequently, all health care plans covering that hospital.

## The parser

The main goal of this parser is to parse all information from some .csv databases to .json files. These .csv files have all information about the hospitals, cities and some information about plans and providers. This .csv was obtained in the "Portal Brasileiro de Dados Abertos"(Brazilian Open Data Portal) by the following links:

* Article(Portuguese): https://dados.gov.br/dataset/operadoras-e-prestadores-nao-hospitalares
* .csv(zipped): http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=http://ftp.dadosabertos.ans.gov.br/FTP/PDA/operadoras_e_prestadores_nao_hospitalares/operadoras_e_prestadores_nao_hospitalares.zip
* Documentation(.pdf): http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=http://ftp.dadosabertos.ans.gov.br/FTP/PDA/operadoras_e_prestadores_nao_hospitalares/dicionario_operadoras_prestadores_nao_hospitalares.pdf