import urllib

# Definição do SQ
setor = 299
quadra = 47

# Requerimento ao endereço da prodam
url_prodam = 'http://sf9402.app.prodam/intranet/frmConsultaCroquiPDF.aspx?pstrSetor={0:0>3}&pstrQuadra={1:0>3}'.format(setor, quadra)
url_pub = 'http://geosampa.prefeitura.sp.gov.br/PaginasPublicas/DownloadCroqui.aspx?setor={0:0>3}&quadra={1:0>3}.format(setor, quadra)
fileobj = urllib.request.urlopen (url_pub)

# Cria um novo arquivo e salva o conteúdo
file = open(r'path\to\folder\{0:0>3}_{1:0>3}.pdf'.format(setor, quadra), 'bw')
file.write(fileobj.read())
file.close()

print(url)
