def tempo_clima(tipo):
	siglas_tempo = {	'ec': 'Encoberto com Chuvas Isoladas', 'ci': 'Chuvas Isoladas', 'c': 'Chuva',
						'in': 'Instável', 'pp': 'Poss. de Pancadas de Chuva', 'cm':	'Chuva pela Manhã',
						'cn': 'Chuva a Noite', 'pt': 'Pancadas de Chuva a Tarde', 'pm':	'Pancadas de Chuva pela Manhã',
						'np': 'Nublado e Pancadas de Chuva', 'pc': 'Pancadas de Chuva', 'pn': 'Parcialmente Nublado',
						'cv': 'Chuvisco', 'ch': 'Chuvoso', 't':	'Tempestade', 'ps': 'Predomínio de Sol',
						'e': 'Encoberto', 'n': 'Nublado', 'cl':	'Céu Claro', 'nv': 'Nevoeiro', 'g':	'Geada',
						'ne': 'Neve', 'nd':	'Não Definido', 'pnt': 'Pancadas de Chuva a Noite',
						'psc': 'Possibilidade de Chuva', 'pcm':	'Possibilidade de Chuva pela Manhã',
						'pct': 'Possibilidade de Chuva a Tarde', 'pcn':	'Possibilidade de Chuva a Noite',
						'npt': 'Nublado com Pancadas a Tarde', 'npn': 'Nublado com Pancadas a Noite',
						'ncn': 'Nublado com Poss. de Chuva a Noite', 'nct':	'Nublado com Poss. de Chuva a Tarde',
						'ncm': 'Nubl. c/ Poss. de Chuva pela Manhã', 'npm':	'Nublado com Pancadas pela Manhã',
						'npp': 'Nublado com Possibilidade de Chuva', 'vn': 'Variação de Nebulosidade',
						'ct': 'Chuva a Tarde', 'ppn': 'Poss. de Panc. de Chuva a Noite',
						'ppt': 'Poss. de Panc. de Chuva a Tarde', 'ppm': 'Poss. de Panc. de Chuva pela Manhã'
					}
	return siglas_tempo[tipo]

#
#
# # Estações de Superfície dos Aeroportos
# # Sigla	Aeroporto	Estado
# # Total 117 cidades
#
# def clima_aeroportos(sigla):
# 	aeroportos = {	'AC':{'SBTK': 'Tarauacá', 'SBRB': 'Presidente Médici', 'SBCZ': 'Internacional'},
# 					'AL':{'SBMO': 'Zumbi dos Palmares'},
# 					'AM':{'SBEG': 'Eduardo Gomes', 'SBMN': 'Ponta Pelada', 'SBMY': 'Manicoré',
# 						  'SBTT': 'Tabatinga', 'SBYA': 'Iuaretê', 'SBUA': 'São Gabriel da Cachoeira', 'SBTF': 'Tefé'},
# 					'AP':{'SBAM': 'Amapá', 'SBMQ': 'Internacional', 'SBOI': 'Oiapoque'},
# 					'BA':{'SBLP': 'Bom Jesus da Lapa', 'SBCV': 'Caravelas', 'SBIL':	'Jorge Amado',
# 						  'SBLE': 'Chapada Diamantina', 'SBUF': 'Paulo Afonso', 'SBPS': 'Porto Seguro',
# 						  'SBSV': 'Dep. Luís Eduardo Magalhães', 'SBQV': 'Vitória da Conquista'},
# 					'CE': {'SBFZ': 'Pinto Martins', 'SBJU': 'Cariri'},
# 					'DF':{'SBBR': 'Juscelino Kubitschek'},
# 					'ES':{'SBVT': 'Eurico Aguiar Salles'},
# 					'GO':{'SBAN': 'Anápolis', 'SBGO': 'Santa Genoveva'},
# 					'MA':{'SBCI': 'Carolina', 'SBIZ': 'Imperatriz', 'SBSL': 'Mar. Cunha Machado'},
# 					'MG':{'SBAX': 'Araxá', 'SBPR': 'Carlos Prates', 'SBBQ': 'Barbacena', 'SBBH': 'Pampulha',
# 						  'SBCF': 'Tancredo Neves', 'SBPC':	'Poços de Caldas', 'SBUR': 'Uberaba',
# 						  'SBUL': 'Uberlândia', 'SBIP': 'Ipatinga', 'SBJF':	'Francisco de Assis',
# 						  'SBMK': 'Montes Claros', 'SBVG': 'Varginha', 'SBGV': 'Gov. Valadares'},
# 					'MS':{'SBCG': 'Internacional', 'SBCR': 'Corumbá', 'SBPP': 'Internacional'},
# 					'MT':{'SBAT': 'Alta Floresta', 'SBBW': 'Barra do Garças', 'SBCY': 'Marechal Rondon'},
# 					'PA':{'SBHT': 'Altamira', 'SBBE': 'Val-de-Cans', 'SBIH': 'Itaituba', 'SBEK': 'Jacareacanga',
# 						  'SBMA': 'Marabá', 'SBCC': 'Cachimbó', 'SBTB': 'Trombetas', 'SBCJ': 'Carajás',
# 						  'SBSN': 'Santarém', 'SBTU': 'Tucuruí', 'SBAA': 'Conceição do Araguaia'},
# 					'PB':{'SBKG': 'Pres. João Suassuna', 'SBJP': 'Pres. Castro Pinto'},
# 					'PE':{'SBFN': 'Fernando de Noronha', 'SBRF': 'Guararapes', 'SBPL': 'Sen. Nilo Coelho'},
# 					'PI':{'SBPB': 'Dr. João Silva Filho', 'SBTE': 'Sen. Petrônio Portella'},
# 					'PR':{'SBLO': 'Londrina', 'SBFI': 'Cataratas', 'SBBI': 'Bacacheri', 'SBCT': 'Afonso Pena',
# 						  'SBMG': 'Silvio Name Junior'},
# 					'RJ':{'SBCB': 'Cabo Frio', 'SBAF': 'Afonsos', 'SBGL': 'Galeão', 'SBJR': 'Jacarepaguá',
# 						  'SBRJ': 'Santos Dumont', 'SBSC': 'Santa Cruz', 'SBME': 'Macaé',
# 						  'SBES':'S. Pedro da Aldeia', 'SBCP': 'Bartolomeu Lysandro'},
# 					'RN':{'SBMS': 'Dix-Sept Rosado', 'SBNT': 'Augusto Severo'},
# 					'RO':{'SBGM': 'Guajará Mirim', 'SBVH': 'Brigadeiro Camarão',
# 						  'SBPV': 'Gov. Jorge Teixeira de Oliveira'},
# 					'RR':{'SBBV': 'Boa Vista'},
# 					'RS':{'SBBG': 'Bagé', 'SBSM': 'Santa Maria', 'SBPA': 'Salgado Filho', 'SBPK': 'Pelotas',
# 						  'SBCO': 'Canoas', 'SBUG':	'Rubem Berta'},
# 					'SC':{'SBCH': 'Chapecó', 'SBCM': 'Forquilinha', 'SBFL': 'Hercílio Luz',
# 						  'SBJV': 'Lauro Carneiro de Loyola', 'SBNF': 'Min. Victor Konder'},
# 					'SE':{'SBAR': 'Santa Maria'},
# 					'SP':{'SBAU': 'Araçatuba', 'SBBU': 'Bauru', 'SBKP': 'Viracopos', 'SBDN': 'Pres. Prudente',
# 						  'SBRP': 'Leite Lopes', 'SBSR': 'S. J. do Rio Preto', 'SBYS': 'Fontenelle',
# 						  'SBST': 'Base Aérea', 'SBGP': 'Gavião Peixoto', 'SBGW': 'Guaratinguetá',
# 						  'SBGR': 'Guarulhos', 'SBSJ': 'São J. dos Campos', 'SBMT': 'Campo de Marte',
# 						  'SBSP': 'Congonhas', 'SBTA': 'Taubaté'},
# 					'TO':{'SBPJ': 'Palmas', 'SBPN': 'Porto Nacional'}
# 	}
# 	for i in aeroportos.keys():
# 		if aeroportos[i].get(sigla):
# 			return aeroportos[i].get(sigla)
#
#
# # Estados e suas siglas
#
# def estados(sigla):
# 	estados = {	'AC': 'Acre', 'AL': 'Alagoas', 'AM': 'Amazonas', 'AP': 'Amapá', 'BA': 'Bahia', 'CE': 'Ceará',
# 				'DF': 'Distrito Federal', 'ES': 'Espírito Santo', 'GO': 'Goiás', 'MA': 'Maranhão',
# 				'MG': 'Minas Gerais', 'MS': 'Mato Grosso do Sul', 'MT': 'Mato Grosso', 'PA': 'Pará',
# 				'PB': 'Paraíba', 'PE': 'Pernambuco', 'PI': 'Piauí', 'PR': 'Paraná', 'RJ': 'Rio de Janeiro',
# 				'RN': 'Rio Grande do Norte', 'RO': 'Rondônia', 'RR': 'Roraima', 'RS': 'Rio Grande do Sul',
# 				'SC': 'Santa Catarina', 'SE': 'Sergipe', 'SP': 'São Paulo', 'TO': 'Tocantins'}
#
# 	return estados[sigla]
#
#
# def siglas_estados():
# 	siglas = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE',
# 		 	  'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
# 	return siglas
