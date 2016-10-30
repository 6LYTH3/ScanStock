#!/usr/bin/env python

# The Finance.py
# - Get Financial data all shared from Set.or.th
# - Store some reponse data | Assets, Liabilities, Equity, ROA, ROE,
#   per shared

import re
import requests
from bs4 import BeautifulSoup
import MongoCli

Symbol = 'PTT'

def GetData():
    url = 'http://www.set.or.th/set/companyhighlight.do?symbol=' + Symbol + '&ssoPageId=5&language=en&country=US'
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    return r.text

def GrepTag():
    html_doc = GetData()
    soup = BeautifulSoup(html_doc, "html.parser")
    # soup = BeautifulSoup(open("raw.html"), "html.parser")
    td = soup.find_all("td", style="background-color: #EAF0FE;")
    return td

def ConvertToIntBy(str):
    i = re.sub(',','',str.string.strip())
    i = re.sub('\*','',i)
    if i in ('N/A','N.A.','-',''):
        return 0
    return float(i)

def PrintData():
    fin = GrepTag()
    print '{0}'.format(Symbol)
    print 'Assets           {0}'.format(fin[1].string.strip())
    print 'Liabilities      {0}'.format(fin[2].string.strip())
    print 'Equity           {0}'.format(fin[3].string.strip())
    print 'Paid-up Capital  {0}'.format(fin[4].string.strip())
    print 'ROE(%)           {0}'.format(fin[10].string.strip())
    print 'Last Price(Bath) {0}'.format(fin[12].string.strip())

def Store():
    fin = GrepTag()
    stock = {"Symbol": Symbol, 
            "Assets": ConvertToIntBy(fin[1]),
            "Liabilities": ConvertToIntBy(fin[2]), 
            "Equity": ConvertToIntBy(fin[3]),
            "Paid-up Capital": ConvertToIntBy(fin[4]),
            "Revenue": ConvertToIntBy(fin[5]),
            "Net Profit": ConvertToIntBy(fin[6]),
            "EPS": ConvertToIntBy(fin[7]),
            "ROA": ConvertToIntBy(fin[9]),
            "ROE": ConvertToIntBy(fin[10]),
            "Margin": ConvertToIntBy(fin[11]),
            "Last Price": ConvertToIntBy(fin[12]),
            "Market Cap": ConvertToIntBy(fin[13]),
            "PE": ConvertToIntBy(fin[15]),
            "PBV": ConvertToIntBy(fin[16]),
            "Book Value": ConvertToIntBy(fin[17]),
            "Yield": ConvertToIntBy(fin[18])}
    db = MongoCli.Connect()
    MongoCli.Insert(db, stock)

if __name__ == '__main__':
    listed = [ 
            "2S","A","AAV","ABC","ACAP","ACC","ADAM","AEC","AF","AFC","AGE","AH","AHC","AI","AIE","AIRA","AIT","AJ","AJD","AKP","AKR","ALT","AMC","ANAN","AOT","AP","APCO","APCS","APX","AQ","AQUA","ARIP","AS","ASIA","ASK","ASN","ASP","AUCT","AYUD","BA","BAFS","BAY","BBL","BCH","BCP","BCPG","BDMS","BEC","BEM","BFIT","BGT","BH","BIG","BIGC","BIZ","BJC","BKD","BKI","BLA","BM","BOL","BPP","BR","BRC","BRR","BSBM","BSM","BTC","BTNC","BTS","BTW","BUI","BWG","CBG","CCET","CCN","CCP","CEN","CGD","CGH","CHG","CHO","CHOW","CHUO","CI","CIG","CITY","CK","CKP","CM","CMO","CMR","CNS","CNT","COL","COM7","CPF","CPH","CPI","CPL","CPN","CPR","CSC","CSL","CSP","CSR","CSS","CTW","CWT","DAII","DCC","DCON","DIF","DNA","DRT","DSGT","DTAC","DTC","DTCI","EA","ECF","ECL","EE","EGCO","EIC","EKH","EMC","EPCO","EPG","ERW","ESSO","EVER","FC","FE","FER","FIRE","FMT","FNS","FPI","FSS","FVC","GBX","GC","GCAP","GEL","GFPT","GIFT","GJS","GL","GLOW","GOLD","GPSC","GTB","GYT","HANA","HFT","HPF","HPT","HTC","ICC","ICHI","IEC","IFEC","IFS","IHL","INET","INOX","IRC","IRCP","IRPC","IT","ITD","ITEL","IVL","J","JAS","JCP","JCT","JMT","JSP","JTS","JWD","K","KBS","KC","KCAR","KCE","KCM","KDH","KGI","KIAT","KKC","KKP","KOOL","KSL","KTB","KTC","KTIS","KWC","KWG","KYE","LDC","LEE","LH","LHK","LHPF","LHSC","LIT","LPH","LPN","LRH","LST","LTX","LUXF","LVT","M","MACO","MATI","MAX","MBAX","MBK","MC","MCOT","MCS","MDX","MEGA","MFC","MFEC","MIDA","M-II","MILL","MINT","MIPF","MIT","MJD","MJLF","MK","ML","MNIT","MNRF","MONO","MPG","MPIC","MSC","MTI","MTLS","NBC","NC","NCH","NCL","NDR","NEP","NEW","NEWS","NFC","NINE","NKI","NMG","NNCL","NOK","NPK","NPP","NSI","NTV","NUSA","NWR","NYT","OCC","OGC","OHTL","ORI","OTO","PACE","PAE","PAF","PAP","PATO","PB","PCA","PDG","PDI","PE","PERM","PF","PG","PHOL","PICO","PIMO","PJW","PK","PL","PLAT","PLE","PM","PMTA","POPF","POST","PPF","PPM","PPP","PPS","PR","PREB","PRG","PRIN","PRO","PS","PSL","PSTC","PT","PTG","PTL","PTT","QH","QHHR","QHOP","QHPF","QLT","QTC","RAM","RCI","RCL","RICH","RJH","RML","ROCK","ROH","RP","RPC","RS","RWI","S","S11","SAM","SAT","SBPF","SC","SCB","SCC","SCCC","SCG","SCI","SCN","SCP","SENA","SF","SFP","SGF","SGP","SIAM","SIM","SIRI","SIS","SKR","SLP","SMIT","SMK","SMM","SMPC","SMT","SNC","SNP","SPA","SPC","SPCG","SPF","SPG","SPI","SPPT","SPRC","SPVI","SQ","SR","SSC","SSF","SSI","SSPF","SSSC","SST","STA","STAR","STEC","STPI","SUC","SVH","SVI","SVOA","SWC","SYMC","T","TACC","TAE","TBSP","TC","TCAP","TCB","TCC","TCCC","TCIF","TCJ","TCMC","TEAM","TF","TFD","TFG","TFI","TGCI","TH","THAI","THE","THIF","THIP","THL","THRE","TIC","TIF1","TIP","TIW","TK","TKN","TKS","TKT","TLGF","TM","TMB","TMC","TMD","TMI","TMT","TMW","TNDT","TNH","TNL","TNP","TNPC","TNPF","TOG","TOP","TOPP","TPA","TPAC","TPBI","TPC","TPCH","TPP","TR","TRC","TRIF","TRT","TRU","TRUE","TSC","TSE","TSF","TSI","TSR","TSTE","TSTH","TTA","TTCL","TTI","TTL","TTTM","TTW","TU","TUCC","TVD","TVI","TVO","TVT","TWP","TWPC","TWZ","TYCN","U","UAC","UBIS","UEC","UKEM","UMI","UMS","UNIQ","UP","UPA","UPF","UT","UTP","UV","UVAN","UWC","VARO","VGI","VI","VIH","VNG","VNT","VPO","VTE","WAVE","WG","WHA","WICE","WIIK","WIN","WORK","WP","WR","XO","YCI","YNP"]

    for stock in listed:
        Symbol = stock
        print "[+] Getting {0}".format(Symbol)
        Store()

