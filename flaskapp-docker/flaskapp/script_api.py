from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import re
import string

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


def extracts(raw_text):

	nlp = spacy.load('en_core_web_sm', disable = ['ner'])

	# TITLE
	title1 = ["Agreement on Managed Data Center Services","Agreement on the Provision of Regional WAN IT Services"]
	title2 = ["Master Services Agreement on the Provision of IT Services",
			"Master Services Agreement on the Provision of IT Services (“Agreement“ or “Master Services Agreement”)"]
	title3 = ["MASTER SERVICES AGREEMENT ON THE PROVISION OF MANAGED SERVICES IN PUBLIC COULDS",
			"Master Services Agreement (“Agreement“ or “Master Services Agreement”) on the provision of Managed Services in Public Clouds"]
	title4 = ["Agreement on the Provision of MANAGED PRINT Services",
			"Agreement on the Provision of MPS (Managed Print Services)"]
	title5 = ["Agreement for Security Operation Center Services"]
	title6 = ["AGREEMENT ON PROVISIONING OF IT AND COMMUNICATION SERVICES"]
	title7 = ["Agreement on Managed Data Center Services"]
	title8 = ["Master Project, Support and Maintenance Agreement"]
	title9 = ["ENTERPRISE CUSTOMER AGREEMENT","Master Project, Support and Maintenance Agreement"]
	title10 = ["AGREEMENT on the provision of managed Mobile communication Services"]
	title11 = ["MASTER SERVICE AGREEMENT","CONTRACT FOR TELECOMMUNICATION SERVICES"]
	title12 = ["Agreement for Security Operation Center Services"]
	title13 = ["Base Terms","AGREEMENT on the provision, OPERATION and maintenance of a CUSTOMER CONTACT PLATFORM",
				"Agreement on the Provision, Operation and Maintenance of a Customer Contact Platform "]
	title14 = ["AGREEMENT on the provision of hosting and support services For Macroware office 365"]


	# SUPPLIER
	suppliers1 = ["TEASYS", "Teasys", "TEASYS GLOBAL INVEST AG","Teasys International GmbH",
				"Teasys Global Invest AG", "teasys global invest ag"]
	suppliers2 = ["FTP", "FTP Deutschland GmbH", "FTP Deutschland GmbH"]
	suppliers3 = ["Wisniewski & Sohn GmbH", "FBS"]
	suppliers4 = ["Horizon Deutschland AG",
				"Horizon", "Harpe", "Harpe Deutschland GmbH"]
	suppliers5 = ["ADVENTURE SERVICES GMBH", "Adventure Services GmbH", "SWIPERO LIMITED", "Swipero Limited",
				"Swipero"]
	suppliers6 = ["Nozama Net Service", "NOZAMA NET SERVICE"]
	suppliers7 = ["Schwyz Mail Solutions GmbH","Timber Limited"]
	suppliers8 = ["Verizon Deutschland GmbH"]
	suppliers9 = ["DZX","Avanti Netz GmbH","Baden Netz GmbH","e.com ScHolstein Telekommunikation GmbH",
				"Netz AG","SCHOLSTEIN Netz AG"]


	# CLIENT
	clients = ["F.UN", "FUN", "F.UN BUSINESS SERVICES GMBH",
			"F.UN Business Services GmbH"]

	# DATE
	dates1 = ["29 September 2018", "01 January 2015", "01.07.2018",
			" August 2017", "6 December 2016", "December 2015","1 of July 2016" ]
	dates2 = ["31. July 2018", "August 30, 2017"]
	dates3 = ["period of 48 months", "36 months","concluded for five (5) years",
			"three (3) months notice prior to termination"]
	dates4 = ["31.01.2017", "31.03.2019", "1 October 2018", "September 1st, 2017"]
	dates5 = ["31.12.2018", "Apr 11th 2023", "19.01.2020", "July 31, 2017"]


	# COUNTRIES
	countries1 = ["UK", "Germany", "France", "Italy","U.S","U.S.A","United States",
				"Netherlands", "Russia", "Hungary", "India"]
	countries2 = ["Slovakia", "Czech", "Australia","Cuba","North Sudan","North Korea",
				"Vietnam", "Japan", "Philippines", "Romania"]
	countries3 = ["Sweden", "Czech Republic", "United Kingdom", "Switzerland"]

	# CLIENT_CONTRACT_MANAGER
	cli_cont_managr1 = ["Amanda Kyzwani"]

	# SUPPLIER_CONTRACT_MANAGER
	supp_cont_manar1 = ["Tim Big"]

	rulerAll = EntityRuler(nlp, overwrite_ents=True)

	# Add rulerAll to patterns

	# For Title entity

	for tit1 in title1:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit1}])

	for tit2 in title2:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit2}])

	for tit3 in title3:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit3}])

	for tit4 in title4:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit4}])

	for tit5 in title5:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit5}])

	for tit6 in title6:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit6}])

	for tit7 in title7:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit7}])

	for tit8 in title8:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit8}])

	for tit9 in title9:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit9}])

	for tit10 in title10:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit10}])

	for tit11 in title11:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit11}])

	for tit12 in title12:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit12}])

	for tit13 in title13:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit13}])

	for tit14 in title14:
		rulerAll.add_patterns([{"label": "TITLE", "pattern": tit14}])

	# for supplier

	for s1 in suppliers1:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s1}])

	for s2 in suppliers2:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

	for s3 in suppliers3:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

	for s4 in suppliers4:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

	for s5 in suppliers5:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

	for s6 in suppliers6:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s6}])

	for s7 in suppliers7:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s7}])

	for s8 in suppliers8:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s8}])
	for s9 in suppliers9:
		rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s9}])

	# for clients

	for c1 in clients:
		rulerAll.add_patterns([{"label": "CLIENT", "pattern": c1}])

	# Pattern for DATES

	for t1 in dates1:
		rulerAll.add_patterns([{"label": "Effective-DATES", "pattern": t1}])

	for t2 in dates2:
		rulerAll.add_patterns([{"label": "Signature-DATES", "pattern": t2}])

	for t3 in dates3:
		rulerAll.add_patterns([{"label": "Termination-DATES", "pattern": t3}])

	for t4 in dates4:
		rulerAll.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])

	for t5 in dates5:
		rulerAll.add_patterns([{"label": "END-DATES", "pattern": t5}])

	# for countries

	for count1 in countries1:
		rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count1}])

	for count2 in countries2:
		rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

	for count3 in countries3:
		rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count3}])

	# CLIENT_CONTRACT_MANAGER

	for c_mangr in cli_cont_managr1:
		rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": c_mangr}])

	# SUPPLIER_CONTRACT_MANAGER

	for supp_mangr in supp_cont_manar1:
		rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": supp_mangr}])

	# HOLISTIC NAME FOR RULER
	rulerAll.name = 'rulerAll'
	if 'rulerAll' not in nlp.pipe_names:
		nlp.add_pipe(rulerAll)



    # take raw text data
	docx = nlp(raw_text)
	html = displacy.render(docx,style="ent")
	html = html.replace("\n\n","\n")
	result = HTML_WRAPPER.format(html)

	return result