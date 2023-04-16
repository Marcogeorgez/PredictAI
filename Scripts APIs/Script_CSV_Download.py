import webbrowser

# insert companies name in the yahoo finance URL and download the historical data for the companies from it

from datetime import date
d0 = date(1970, 1, 1)
d1 = date.today()

delta = d1 - d0
End = (delta.days * 24 * 60 * 60)
Start = End - 31536000  *4

# Start=int(datetime.strptime('1970-01-01', "%Y-%m-%d").replace(tzinfo = timezone.utc).timestamp())
# End = int(datetime.strptime(date.today().strftime('%Y-%m-%d'), "%Y-%m-%d").replace(tzinfo = timezone.utc).timestamp())

for Ticker in "AAPL   ABNB   ADBE   ADI   ADSK   AMAT   AMD   AMX   AMZN   ASML AVGO   CAJ   CRM   CSCO   \
  DELL   GOOG   GOOGL   HPE   IBM   INFY   INTC   INTU   LOGI   LRCX   META   MRVL   MSFT   MU   NDAQ   \
  NET   NOW   NVDA ORCL   PANW   PYPL   QCOM RELX   SAP   SNPS   SONY   T   TMUS TSLA TSM TXN U UBER VMW \
  VZ ZM  A   AAC   AAL   AAP   AAT   AB   ABBV   ABC   ABG   ABM   ABMD   ABR   ACC   ACGL   ACH   ACN   \
  ACRE   ADM   ADP   ADPT   AEE   AEL   AEM   AEO   AEP   AER   AFB   AFSI   AG   AGI   AGM   AGO   AGRO  \
  AHH   AHL   AHT AI   AIG   AINV   AIT   AIV   AIZ   AJG   AKR   ALB   ALEX   ALGN   ALK   ALL   ALLE   \
  ALLY   ALSN   ALTR   AMC AME   AMG   AMP   AMT   AMTD   ANET   ANF ANTM   AOS   APAM   APH   AR   ARC   \
  ARCC   ARCO   ARDC   ARE   ARHVF   ARI   ARW   ASA   ASB   ASC   ASGN   ASPN   ASR   ASX   ATEN   ATI   \
  ATO   ATW   AU   AVB   AVD   AVG   AVY   AWH   AWK   AXL   AXP   AXTA   AZN   AZO   BA   BAC   BAH   BAK   \
  BAM   BAP   BAX   BBVA   BBY   BCC   BCS   BDN   BDX   BEN   BEP   BERY   BFAM   BG   BGC   BH   BHE   BHI   \
  BHLB   BHP   BIIB   BIO   BIP   BK   BKD   BLH   BLK BLX   BMO   BMRA   BMS   BMY   BNK   BOH   BOOT   BPK   \
  BR   BRFS   BRK-A   BRO   BRP   BRX   BSAC   BSHI   BSX   BTSGY BTU   BURL   BWA BWMG   BWP   BXC   BXMT   BXP   \
  BZH   C   CAG   CAH   CB   CBL   CBU   CCI   CCK   CCS   CCU   CCZ   CDE   CDNS   CDR   CEA   CEO   CEQP   \
  CF   CFG   CFR   CGA   CHD   CHH   CHMI   CHRW   CHS   CHT   CHTR   CIB   CIM   CINF   CIO   CIR   CIVI   \
  CL   CLB   CLH   CLR   CLW   CLX   CM   CMC   CMCSA   CME   CMG   CMI   CMP   CMS   CNC   CNHI   CNI   CNO   \
  CNP   CNQ   CNS   CNWT   CNX   COF   COL   COO   COP   CORR   COST   COTY   COWN   CP   CPB   CPE   CPF   \
  CPG   CPK   CPRT   CPT   CRL   CRS   CS   CSC   CSL   CSTM   CSV   CTAS   CTSH   CTT   CTXS   CUDA   CUK   \
  CUPUF   CUZ   CVE   CWT   CYD   CYH   CYS   D   DAL   DAR   DCI   DCO   DCT   DD   DDS   DE   DECK   DEI   \
  DFS   DG   DGX   DHI   DHT   DIS   DK   DKS   DLB   DLNG   DLR   DLTR   DNB   DO   DOOR DPSGY   DRE   DRI   \
  DSL   DST   DSU   DSX   DTE   DV   DVA   DVN   DXCM   EA   EAT   EBAY   EBS   ECL   ED   EE   EFX   EGL   EGO   \
  EGP   EIG   EIX   EL   ELP   ELY   EME   EMN   EMO   EMR   ENS   ENVA   EOS   EPAM   EPD   EPR-PC   EPR-PE   \
  EPR   EQIX   EQR   EQS   ES   ESI   ESS   ETN   ETP   EVC   EVER   EVT   EW   EXC   EXR   F   FANG   FAST   \
  FBC   FBHS   FBP   FBR   FCF   FCN   FCX   FDP   FDS   FDX   FE   FET   FF   FFIV   FGL   FHN   FIG   FIS   FISV   \
  FITB   FIX   FL   FLO   FLS   FLT   FMBM   FMC   FMN   FMS   FMX   FMY   FN   FNF   FOR   FPLPF   FPRUF   \
  FR FRC   FRT   FSM   FSS   FTI   FTK   FUL   FUN   G   GAM   GBX   GD   GE   GEL   GGG   GHC   GILD   GIM   GIS   \
  GLOB   GLW   GM   GMED   GNE GNRC   GNW   GOLD   GPC   GPI   GPK   GPN   GPT   GRMN   GS-PJ   GSK   GVA   GWRE   \
  GWW   HAL   HAS   HASI   HBAN   HBI   HCA   HD   HDB   HE   HES   HIG   HII   HIL   HIO   HIVE   HIW   HL   HLF  \
  HLT   HLX   HMC   HMN   HMY   HNP   HOLX   HOT   HP   HPP   HPQ   HR   HRB   HRL   HRTG   HSBC   HSIC   HST   \
  HTA   HTLF   HTZ   HUM   HVT   HYT   IBA   IBN   ICD   ICE   IDE   IDXX   IEX   IFF   IGA   IGT   ILMN   INGR   \
  INN   INT   IP   IPG   IPGP   IPI   IR   IRM   IRS   ISRG   IT   ITW   IVR   IVZ   JBHT   JBT   JCI   JE   JKHY   \
  JLL   JNJ   JNPR   JOB   JPM   K   KAR   KB   KED   KEP   KEY   KEYS   KFS   KFY   KHC   KIM   KMB   KMG   KMX   \
  KND   KNX   KO   KODK   KOF   KOS   KR   KRC   KRG   KS   KSS   KST   KWR   LADR   LBTYA   LC   LDOS   LEE   \
  LEG   LEN-B   LEU   LFC   LGI   LH   LII   LKQ   LL   LLY   LMT   LNC   LNT   LOW   LPG   LPI   LTC   LUV   \
  LVS   LXP   LXU   LYB   LYV   MA   MAA   MAIN   MAN   MAR   MCD   MCHP   MCK   MCO   MCY   MDC   MDLZ   \
  MDT   MEG   MEI   MET   MFC   MFG   MG   MGA   MGM   MHD   MHK   MIG   MKC   MKTX   MLI   MLM   MLR   \
  MMC   MMI   MMM   MMP   MN   MNP   MNST   MO   MOD   MOH   MOS   MOV   MPC   MPW   MRCR   MRIN   MRK   \
  MRO   MSA   MSCI   MSI   MSM   MTDR   MTG   MTN   MTR   MTRN   MTX   MUSA   MXCHF   MYE   NBR   NC   \
  NCLH   NCTKF   NCZ NE   NEE   NEOG   NEU   NFLX   NFX   NGVC   NI   NIO   NL   NLSN   NLY   NM   NMHLY   \
  NOC NOK   NORNQ   NOV   NOXL   NP   NPK   NPO   NPTN   NR   NRG   NRP   NRZ   NS   NSC   NSM   NTAP   \
  NTRA   NTRR   NTRS   NTZ   NUS   NVO   NVR   NVRO   NWL   NWN   NX   O   OAS   OB   OCN ODFL   OFC   \
  OHI   OII   OIS   OKE   OLP   OMC   OMI   ORAN   ORI   ORLY   OXM   OXY   P   PAA   PAI   PAM   PAR   \
  PAY   PAYC   PAYX PB   PBA   PBH   PBI   PBR   PCAR   PCN   PDM   PDS   PEB   PEG   PEP   PFE   PFG   \
  PFS   PFSI   PG   PGEM   PH   PHG   PHM   PII   PKG   PKI   PLD   PLOW   PM   PMF   PMT   PNC   PNK   \
  PNNT   PNR   PNW   PNWRF   POR   PPG   PRGO   PRLB   PRO   PRU   PSEC   PSF   PSX   PT   PTR PWR   PXD   \
  PZE   QRVO   QSR QTWO   R   RBA   RCI   RCL   RCS   RDY   RE   REG   REGN   REX   REXR   RF   RFIL   RFP   \
  RGA   RGC   RGR   RHI   RJF   RL   RLI   RM   RMD   ROK   ROL   ROP   RPM   RQI   RRC   RRTS   RS   RSG   \
  RSNHF   RVT   RWT   RXMD   RY   RYAM   RYI   SAH   SAN   SAR   SBS   SBUX   SCCO   SCHW   SCI   SE   SEAS   \
  SEE   SEGXF   SEM   SF   SFE   SFL   SHG   SHI   SHW   SIG   SIGI   SIVB   SIX   SJR   SKM   SKT   SKX   \
  SLB   SLCA   SLF   SM   SMG   SMP   SNI   SNOW   SNP   SNV   SO   SON   SONC   SPB   SPG   SPH   SPLP   \
  SPR   SQM   SRE   SSD   SSTK   ST   STAG   STC   STM   STOR   STT   STWD   STX   STZ-B   SU   SUI   SUP   \
  SWK   SWKS   SWN   SWZ   SXT   SYF   SYK   TA   TAC   TAP   TCI   TCYSF   TDG   TDS   TDY   TEL   TEO   \
  TEVA   TGH   TGI   THG   THLEF   THR   THS   TIME   TJX   TKC   TLK   TMHC   TMO   TMST   TNC   TNH   \
  TNP   TPL   TPPPF   TPVG   TPX   TR   TRAUF   TRC   TRI   TRN   TRNO   TROW   TSCO   TSE   TSI   \
  TSLX   TSN   TSQ   TTM   TTWO   TUP   TV   TVPT   TW   TWI TWO   TWTR   TXT TYL   UA   UAL   UBA   \
  UEEC   UL   ULTA   UMC   UNH   UNM   UNP   UPS   URI   USB   USM   USNA   USPH   UTF   UTI   V   \
  VAC   VET   VFC VG   VGR   VIV   VLY   VMC   VMI   VOYA   VR   VRSK   VRSN   VSH   VTR   VVR   \
  WAB   WAT   WBA   WBS   WCC   WCN   WDC   WEC   WFC   WGO   WHR   WIT   WLK   WLL   WMB   WMK   \
  WNC   WNS   WOR   WPC   WPZ   WRB   WRE   WRK   WSPOF   WSR   WST   WTI   WTM   WTS   WTW   WU   \
  WWE   WWW   WY   X   XEL   XHR   XIN   XOM   XPO   XYL   YPF   YUM   ZBH   ZDPY   ZION   ZNH  ZTS".split():

    # period1-period2 = the amount of seconds in 1 year. 3.154e^7
    # Remember to Update Period1 & Period2.
    # how it works:
    # for every second that passes , the period1,period2 counter is increased by 1.
    # period 2 = date from 1.1.1980 till today in seconds. ( x )
    # period 1 = date from period2 - 3.154e^7 ( y )
    # period 2 - period 1 == get me all DATA from the latest year.

    webbrowser.open(
        f"https://query1.finance.yahoo.com/v7/finance/download/{Ticker}?period1={Start}&period2={End}&interval=1d&events=history&includeAdjustedClose=true", autoraise=True)
