#coding utf-8

from rede import Subestacao, Alimentador, Setor, Chave
from rede import Trecho, NoDeCarga, Gerador, Transformador, Condutor
from rede import Fasor
from protecao import IED, GrupoAjuste


# grupos de ajustes

"""
OBSERVACOES:

ied de fronteira so possui UM grupo de ajustes

calculei os grupo de ajuste:

     1 = situacao normal da rede com gd
     2 = situacao normal da rede sem gd (2, 7, 19, 11, 12, 16, 20)

"""

# grupos de ajustes do ied1 2500
ied1_g1 = GrupoAjuste(ipk51p=600, ipk50p=3000, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=256, curvan='MI', dialn=0.42)
#ied1_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied1_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied2
ied2_g1 = GrupoAjuste(ipk51p=110, ipk50p=2200, curvap='MI', dialp=1.7, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
ied2_g2 = GrupoAjuste(ipk51p=156, ipk50p=1660, curvap='MI', dialp=1.36, ipk51n=24, ipk50n=206, curvan='MI', dialn=0.66)
# ied2_g3 = GrupoAjuste(ipk51p=245, ipk50p=1006, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)

# grupos de ajustes do ied3
ied3_g1 = GrupoAjuste(ipk51p=348, ipk50p=940, curvap='MI', dialp=0.14, ipk51n=24, ipk50n=256, curvan='MI', dialn=0.83)
ied3_g2 = GrupoAjuste(ipk51p=245, ipk50p=1202, curvap='MI', dialp=0.14, ipk51n=24, ipk50n=256, curvan='MI', dialn=0.83)
# ied3_g3 = GrupoAjuste(ipk51p=365, ipk50p=1202, curvap='MI', dialp=0.14, ipk51n=24, ipk50n=256, curvan='MI', dialn=0.83)

# grupos de ajustes do ied4
ied4_g1 = GrupoAjuste(ipk51p=500, ipk50p=4000, curvap='MI', dialp=0.3, ipk51n=24, ipk50n=2084, curvan='MI', dialn=1.04)
#ied4_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied4_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied5
ied5_g1 = GrupoAjuste(ipk51p=59, ipk50p=540, curvap='MI', dialp=0.14, ipk51n=24, ipk50n=156, curvan='MI', dialn=0.54)
ied5_g2 = GrupoAjuste(ipk51p=59, ipk50p=802, curvap='MI', dialp=0.03, ipk51n=24, ipk50n=156, curvan='MI', dialn=0.54)
#ied5_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied6
ied6_g1 = GrupoAjuste(ipk51p=600, ipk50p=3000, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=256, curvan='MI', dialn=0.42)
#ied6_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied6_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied7
ied7_g1 = GrupoAjuste(ipk51p=200, ipk50p=2166, curvap='MI', dialp=0.89, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
ied7_g2 = GrupoAjuste(ipk51p=200, ipk50p=1680, curvap='MI', dialp=1.05, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
#ied7_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied8
ied8_g1 = GrupoAjuste(ipk51p=270, ipk50p=899, curvap='MI', dialp=0.23, ipk51n=24, ipk50n=256, curvan='MI', dialn=0.21)
#ied8_g2 = GrupoAjuste(ipk51p=270, ipk50p=670, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
#ied8_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied9
ied9_g1 = GrupoAjuste(ipk51p=552, ipk50p=4500, curvap='MI', dialp=0.23, ipk51n=24, ipk50n=1000.8, curvan='MI', dialn=0.42)
#ied9_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied9_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied10
ied10_g1 = GrupoAjuste(ipk51p=600, ipk50p=5000, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=256, curvan='MI', dialn=0.42)
#ied10_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied10_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied11
ied11_g1 = GrupoAjuste(ipk51p=173, ipk50p=2660, curvap='MI', dialp=0.87, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
ied11_g2 = GrupoAjuste(ipk51p=173, ipk50p=2160, curvap='MI', dialp=1.0, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
#ied11_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied12
ied12_g1 = GrupoAjuste(ipk51p=143, ipk50p=1625, curvap='MI', dialp=0.85, ipk51n=25.6, ipk50n=156, curvan='MI', dialn=0.26)
ied12_g2 = GrupoAjuste(ipk51p=143, ipk50p=1156, curvap='MI', dialp=1.08, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
#ied12_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied13
ied13_g1 = GrupoAjuste(ipk51p=143, ipk50p=528, curvap='MI', dialp=0.2, ipk51n=24, ipk50n=256, curvan='MI', dialn=0.21)
#ied13_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied13_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied14
ied14_g1 = GrupoAjuste(ipk51p=30, ipk50p=1088, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
ied14_g2 = GrupoAjuste(ipk51p=30, ipk50p=874, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
#ied14_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied15
ied15_g1 = GrupoAjuste(ipk51p=600, ipk50p=3000, curvap='MI', dialp=0.29, ipk51n=25.6, ipk50n=256, curvan='MI', dialn=0.42)
#ied15_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied15_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied16
ied16_g1 = GrupoAjuste(ipk51p=257, ipk50p=1960, curvap='MI', dialp=0.70, ipk51n=25.6, ipk50n=206, curvan='MI', dialn=0.26)
ied16_g2 = GrupoAjuste(ipk51p=257, ipk50p=1470, curvap='MI', dialp=0.85, ipk51n=10, ipk50n=206, curvan='MI', dialn=0.1)
#ied16_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied17
ied17_g1 = GrupoAjuste(ipk51p=75, ipk50p=807, curvap='MI', dialp=0.20, ipk51n=24, ipk50n=256, curvan='MI', dialn=0.21)
#ied17_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied17_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied18
ied18_g1 = GrupoAjuste(ipk51p=640, ipk50p=1200, curvap='MI', dialp=0.20, ipk51n=24, ipk50n=1000, curvan='MI', dialn=0.42)
#ied18_g2 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)
#ied18_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

ied19_g1 = GrupoAjuste(ipk51p=100, ipk50p=1912, curvap='MI', dialp=1.47, ipk51n=24, ipk50n=1000, curvan='MI', dialn=0.42)
ied19_g2 = GrupoAjuste(ipk51p=100, ipk50p=1425, curvap='MI', dialp=1.9, ipk51n=10, ipk50n=206, curvan='MI', dialn=0.1)
#ied19_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

ied20_g1 = GrupoAjuste(ipk51p=130, ipk50p=1857, curvap='MI', dialp=1.20, ipk51n=24, ipk50n=1000, curvan='MI', dialn=0.42)
ied20_g2 = GrupoAjuste(ipk51p=130, ipk50p=1370, curvap='MI', dialp=1.65, ipk51n=10, ipk50n=206, curvan='MI', dialn=0.1)
#ied20_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied21
ied21_g1 = GrupoAjuste(ipk51p=153, ipk50p=2400, curvap='MI', dialp=0.21, ipk51n=24, ipk50n=2084, curvan='MI', dialn=1.04)
ied21_g2 = GrupoAjuste(ipk51p=153, ipk50p=2400, curvap='MI', dialp=0.21, ipk51n=24, ipk50n=2084, curvan='MI', dialn=1.04)
# ied21_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# grupos de ajustes do ied22
ied22_g1 = GrupoAjuste(ipk51p=210, ipk50p=4300, curvap='MI', dialp=0.25, ipk51n=24, ipk50n=1000.8, curvan='MI', dialn=0.42)
ied22_g2 = GrupoAjuste(ipk51p=210, ipk50p=4300, curvap='MI', dialp=0.4, ipk51n=24, ipk50n=1000.8, curvan='MI', dialn=0.42)
#ied22_g3 = GrupoAjuste(ipk51p=10, ipk50p=20, curvap='MI', dialp=0.1, ipk51n=10, ipk50n=20, curvan='MI', dialn=0.1)

# ied

ied1 = IED(nome='IED1',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied1.grupos['1'] = ied1_g1
#ied1.grupos['2'] = ied1_g2
#ied1.grupos['3'] = ied1_g3

ied2 = IED(nome='IED2',nmax=2,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied2.grupos['1'] = ied2_g1
ied2.grupos['2'] = ied2_g2
# ied2.grupos['3'] = ied2_g3 

ied3 = IED(nome='IED3',nmax=2,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied3.grupos['1'] = ied3_g1
ied3.grupos['2'] = ied3_g2
# ied3.grupos['3'] = ied3_g3

ied4 = IED(nome='IED4',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied4.grupos['1'] = ied4_g1
#ied4.grupos['2'] = ied4_g2
#ied4.grupos['3'] = ied4_g3

ied5 = IED(nome='IED5',nmax=2,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied5.grupos['1'] = ied5_g1
ied5.grupos['2'] = ied5_g2
#ied5.grupos['3'] = ied5_g3

ied6 = IED(nome='IED6',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied6.grupos['1'] = ied6_g1
#ied6.grupos['2'] = ied6_g2
#ied6.grupos['3'] = ied6_g3

ied7 = IED(nome='IED7',nmax=2,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied7.grupos['1'] = ied7_g1
ied7.grupos['2'] = ied7_g2
#ied7.grupos['3'] = ied7_g3

ied8 = IED(nome='IED8',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied8.grupos['1'] = ied8_g1
#ied8.grupos['2'] = ied8_g2
#ied8.grupos['3'] = ied8_g3

ied9 = IED(nome='IED9',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied9.grupos['1'] = ied9_g1
#ied9.grupos['2'] = ied9_g2
#ied9.grupos['3'] = ied9_g3

ied10 = IED(nome='IED10',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied10.grupos['1'] = ied10_g1
#ied10.grupos['2'] = ied10_g2
#ied10.grupos['3'] = ied10_g3

ied11 = IED(nome='IED11',nmax=2,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied11.grupos['1'] = ied11_g1
ied11.grupos['2'] = ied11_g2
#ied11.grupos['3'] = ied11_g3

ied12 = IED(nome='IED12',nmax=2,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied12.grupos['1'] = ied12_g1
ied12.grupos['2'] = ied12_g2
#ied12.grupos['3'] = ied12_g3 

ied13 = IED(nome='IED13',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied13.grupos['1'] = ied13_g1
#ied13.grupos['2'] = ied13_g2
#ied13.grupos['3'] = ied13_g3

ied14 = IED(nome='IED14',nmax=2,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied14.grupos['1'] = ied14_g1
ied14.grupos['2'] = ied14_g2
#ied14.grupos['3'] = ied14_g3

ied15 = IED(nome='IED15',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied15.grupos['1'] = ied15_g1
#ied15.grupos['2'] = ied15_g2
#ied15.grupos['3'] = ied15_g3

ied16 = IED(nome='IED16',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied16.grupos['1'] = ied16_g1
ied16.grupos['2'] = ied16_g2
#ied16.grupos['3'] = ied16_g3 

ied17 = IED(nome='IED17',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False)
ied17.grupos['1'] = ied17_g1
#ied17.grupos['2'] = ied17_g2
#ied17.grupos['3'] = ied17_g3 

ied18 = IED(nome='IED18',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied18.grupos['1'] = ied18_g1
#ied18.grupos['2'] = ied18_g2
#ied18.grupos['3'] = ied18_g3

ied19 = IED(nome='IED19',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied19.grupos['1'] = ied19_g1
ied19.grupos['2'] = ied19_g2
#ied18.grupos['3'] = ied18_g3

ied20 = IED(nome='IED20',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied20.grupos['1'] = ied20_g1
ied20.grupos['2'] = ied20_g2
#ied20.grupos['3'] = ied20_g3

ied21 = IED(nome='IED21',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied21.grupos['1'] = ied21_g1
# ied21.grupos['2'] = ied21_g2
#ied21.grupos['3'] = ied21_g3

ied22 = IED(nome='IED22',nmax=1,grupoAtivo='1',funcoes={'51P': True,'50P':True,'51N': True,'50N':True},BRKF=False) # << chave de referencia
ied22.grupos['1'] = ied22_g1
# ied22.grupos['2'] = ied22_g2
#ied22.grupos['3'] = ied22_g3


# chaves

ch1 = Chave(nome='1', estado=1,ied=ied1)
ch2 = Chave(nome='2', estado=1,ied=ied2)
ch3 = Chave(nome='3', estado=0,ied=ied3)
ch4 = Chave(nome='4', estado=1,ied=ied4)
ch5 = Chave(nome='5', estado=0,ied=ied5)
ch6 = Chave(nome='6', estado=1,ied=ied6)
ch7 = Chave(nome='7', estado=1,ied=ied7)
ch8 = Chave(nome='8', estado=0,ied=ied8)
ch9 = Chave(nome='9', estado=1,ied=ied9)
ch10 = Chave(nome='10', estado=1,ied=ied10)
ch11 = Chave(nome='11', estado=1,ied=ied11)
ch12 = Chave(nome='12', estado=1,ied=ied12)
ch13 = Chave(nome='13', estado=0,ied=ied13)
ch14 = Chave(nome='14', estado=0,ied=ied14)
ch15 = Chave(nome='15', estado=1,ied=ied15)
ch16 = Chave(nome='16', estado=1,ied=ied16)
ch17 = Chave(nome='17', estado=0,ied=ied17)
ch18 = Chave(nome='18', estado=1,ied=ied18)
ch19 = Chave(nome='19', estado=1,ied=ied19)
ch20 = Chave(nome='20', estado=1,ied=ied20)
ch21 = Chave(nome='21', estado=1,ied=ied21)
ch22 = Chave(nome='22', estado=1,ied=ied22)


# nos de carga

ns1 = NoDeCarga(nome='S1',
               vizinhos=['A1','D1','G1','J1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['1','6','10','15'])

ns2 = NoDeCarga(nome='S2',
               vizinhos=['C1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['4'])

ns3 = NoDeCarga(nome='S3',
               vizinhos=['F1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['9'])

ns4 = NoDeCarga(nome='S4',
               vizinhos=['L2'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['18'])

a1 = NoDeCarga(nome='A1',
               vizinhos=['S1','A2'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=326e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['1'])

a2 = NoDeCarga(nome='A2',
               vizinhos=['A1','B1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=1.6e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['2'])

b1 = NoDeCarga(nome='B1',
               vizinhos=['A2','O1','GD1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=1.6e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['2','3'])

c1 = NoDeCarga(nome='C1',
               vizinhos=['S2','O1','E1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=1.6e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['21','4','5'])

o1 = NoDeCarga(nome='O1',
               vizinhos=['C1','B1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=1.6e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['3','21'])

d1 = NoDeCarga(nome='D1',
               vizinhos=['S1','D2'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=310e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['6'])

d2 = NoDeCarga(nome='D2',
               vizinhos=['D1','E1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=1.5e6*3/3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['7'])

e1 = NoDeCarga(nome='E1',
               vizinhos=['D2','C1','M1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=1.5e6*3/3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['7','19','5'])

m1 = NoDeCarga(nome='M1',
               vizinhos=['E1','P1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=1.5e6*3/3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['19','8'])

f1 = NoDeCarga(nome='F1',
               vizinhos=['S3','P1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=2.2e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['22','9'])

p1 = NoDeCarga(nome='P1',
               vizinhos=['F1','M1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=2.2e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['8','22'])

g1 = NoDeCarga(nome='G1',
               vizinhos=['S1','H1','GD2'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=500e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['10','11'])

h1 = NoDeCarga(nome='H1',
               vizinhos=['G1','H2','K1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['11','14'])

h2 = NoDeCarga(nome='H2',
               vizinhos=['H1','I1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=160e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['12'])

i1 = NoDeCarga(nome='I1',
               vizinhos=['H2','L1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=757e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['12','13'])

l1 = NoDeCarga(nome='L1',
               vizinhos=['I1','L2','N1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=2.1e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['13','17'])

l2 = NoDeCarga(nome='L2',
               vizinhos=['S4','L1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=2.1e6*3/2, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['18'])


j1 = NoDeCarga(nome='J1',
               vizinhos=['S1','K1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=650e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['15','16'])

k1 = NoDeCarga(nome='K1',
               vizinhos=['J1','N1','H1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=650e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['14','16','20'])

n1 = NoDeCarga(nome='N1',
               vizinhos=['K1','L1'],
               #conexao='estrela',
               modelo='PQ',
               potencia_fase_a=Fasor(real=650e3*3, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_b=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               potencia_fase_c=Fasor(real=0.0, imag=0.0, tipo=Fasor.Potencia),
               chaves=['20','17'])

# geradores

gd1 = Gerador(nome='GD1',
		   ativo=True,
             vizinhos=['B1'],
             dvtol=150,
             potencia_nominal=Fasor(real=1e6, imag=850e3, tipo=Fasor.Potencia),
             chaves=[''],
             x0 = 0.4574,
             x2 = 0.1114,
             xsobrer = 4.106,
             xsubt = 0.15,
             interface_rede='SINCRONO',
             #maquina='',
             modelo='PV',
             conexao='estrela',
             qmin=-250e3,
             qmax=900e3,
             tensaogerador=13800)

gd2 = Gerador(nome='GD2',
		   	 ativo=True,
             vizinhos=['G1'],
             dvtol=150,
             potencia_nominal=Fasor(real=1e6, imag=700e3, tipo=Fasor.Potencia),
             chaves=[''],
             x0 = 1.7197,
             x2 = 0.4545,
             xsobrer = 4.106,
             xsubt = 0.15,
             interface_rede='SINCRONO',
             #maquina='',
             modelo='PV',
             conexao='estrela',
             qmin=-400e3,
             qmax=750e3,
             tensaogerador=13800)

# condutor

cond1 = Condutor(nome='CAA 266R',
                #tamanho='',
                #d_ext=0,
                #raio_m_g=0,
                #d_iso=0,
                #d_tela=0,
                rp=0.2391,
                xp=0.3790,
                rz=0.4169,
                xz=1.5559,
                ampacidade=475)

cond2 = Condutor(nome='1/0',
                #tamanho='',
                #d_ext=0,
                #raio_m_g=0,
                #d_iso=0,
                #d_tela=0,
                rp=0.6955,
                xp=0.4984,
                rz=0.8733,
                xz=2.0219,
                ampacidade=242)

cond3 = Condutor(nome='95mm2',
                #tamanho='',
                #d_ext=0,
                #raio_m_g=0,
                #d_iso=0,
                #d_tela=0,
                rp=0.2231,
                xp=0.4040,
                rz=0.3991,
                xz=1.9282,
                ampacidade=438)

# trechos

# s1_al1

s1ch1 = Trecho(nome='S1CH1', n1=ns1, n2=ch1, condutor=cond1, comprimento=0.001)
ch1a1 = Trecho(nome='CH1A1', n1=ch1, n2=a1, condutor=cond1, comprimento=2.246)
a1a2 = Trecho(nome='A1A2', n1=a1, n2=a2, condutor=cond1, comprimento=2.246)
a2ch2 = Trecho(nome='A2CH2', n1=a2, n2=ch2, condutor=cond1, comprimento=0.01)
ch2b1 = Trecho(nome='CH2B1', n1=ch2, n2=b1, condutor=cond1, comprimento=1.6585)
b1gd1 = Trecho(nome='B1GD1', n1=b1, n2=gd1, condutor=cond1, comprimento=0.1)
b1ch3 = Trecho(nome='B1CH3', n1=b1, n2=ch3, condutor=cond1, comprimento=1.6585)

# s2_al1

s2ch4 = Trecho(nome='S2CH4', n1=ns2, n2=ch4, condutor=cond1, comprimento=0.001)
ch4c1 = Trecho(nome='CH4C1', n1=ch4, n2=c1, condutor=cond1, comprimento=5.071/4)
c1ch5 = Trecho(nome='C1CH5', n1=c1, n2=ch5, condutor=cond1, comprimento=1.0)
c1ch21 = Trecho(nome='C1CH21', n1=c1, n2=ch21, condutor=cond1, comprimento=5.071/4)
ch21o1 = Trecho(nome='CH21O1', n1=ch21, n2=o1, condutor=cond1, comprimento=5.071/4)
o1ch3 = Trecho(nome='O1CH3', n1=o1, n2=ch3, condutor=cond1, comprimento=5.071/4)

# s1_al2

s1ch6 = Trecho(nome='S1CH6', n1=ns1, n2=ch6, condutor=cond1, comprimento=0.001)
ch6d1 = Trecho(nome='CH6D1', n1=ch6, n2=d1, condutor=cond1, comprimento=2.6485)
d1d2 = Trecho(nome='D1D2', n1=d1, n2=d2, condutor=cond1, comprimento=2.6485)
d2ch7 = Trecho(nome='D2CH7', n1=d2, n2=ch7, condutor=cond1, comprimento=0.01)
ch7e1 = Trecho(nome='CH7E1', n1=ch7, n2=e1, condutor=cond1, comprimento=3.0185/4)
e1ch19 = Trecho(nome='E1CH19', n1=e1, n2=ch19, condutor=cond1, comprimento=3.0185/4)
ch19m1 = Trecho(nome='CH19M1', n1=ch19, n2=m1, condutor=cond1, comprimento=3.0185/4)
m1ch8 = Trecho(nome='M1CH8', n1=m1, n2=ch8, condutor=cond1, comprimento=3.0185/4)
e1ch5 = Trecho(nome='E1CH5', n1=e1, n2=ch5, condutor=cond1, comprimento=1.0)

# s3_al1

s3ch9 = Trecho(nome='S3CH9', n1=ns3, n2=ch9, condutor=cond1, comprimento=0.001)
ch9f1 = Trecho(nome='CH9F1', n1=ch9, n2=f1, condutor=cond1, comprimento=1.9465/4)
f1ch22 = Trecho(nome='F1CH22', n1=f1, n2=ch22, condutor=cond1, comprimento=1.9465/4)
ch22p1 = Trecho(nome='CH22P1', n1=ch22, n2=p1, condutor=cond1, comprimento=1.9465/4)
p1ch8 = Trecho(nome='P1CH8', n1=p1, n2=ch8, condutor=cond1, comprimento=1.9465/4)

# s1_al3

s1ch10 = Trecho(nome='S1CH10', n1=ns1, n2=ch10, condutor=cond1, comprimento=0.001)
ch10g1 = Trecho(nome='CH10G1', n1=ch10, n2=g1, condutor=cond1, comprimento=0.8915)
g1gd2 = Trecho(nome='G1GD2', n1=g1, n2=gd2, condutor=cond1, comprimento=0.1)
g1ch11 = Trecho(nome='G1CH11', n1=g1, n2=ch11, condutor=cond1, comprimento=0.8915)
ch11h1 = Trecho(nome='CH11H1', n1=ch11, n2=h1, condutor=cond1, comprimento=0.01)
h1ch14 = Trecho(nome='H1CH14', n1=h1, n2=ch14, condutor=cond1, comprimento=0.01)
h1h2 = Trecho(nome='H1H2', n1=h1, n2=h2, condutor=cond1, comprimento=2.3525)
h2ch12 = Trecho(nome='H2CH12', n1=h2, n2=ch12, condutor=cond1, comprimento=2.3525)
ch12i1 = Trecho(nome='CH12I1', n1=ch12, n2=i1, condutor=cond1, comprimento=3.405)
i1ch13 = Trecho(nome='I1CH13', n1=i1, n2=ch13, condutor=cond1, comprimento=3.405)

# s1_al4

s1ch15 = Trecho(nome='S1CH15', n1=ns1, n2=ch15, condutor=cond1, comprimento=0.001)
ch15j1 = Trecho(nome='CH15J1', n1=ch15, n2=j1, condutor=cond1, comprimento=3.4685)
j1ch16 = Trecho(nome='J1CH16', n1=j1, n2=ch16, condutor=cond1, comprimento=3.4685)
k1ch14 = Trecho(nome='K1CH14', n1=k1, n2=ch14, condutor=cond1, comprimento=0.01)
ch16k1 = Trecho(nome='CH16K1', n1=ch16, n2=k1, condutor=cond1, comprimento=1.3645/4)
k1ch20 = Trecho(nome='K1CH20', n1=k1, n2=ch20, condutor=cond1, comprimento=1.3645/4)
ch20n1 = Trecho(nome='CH20N1', n1=ch20, n2=n1, condutor=cond1, comprimento=1.3645/4)
n1ch17 = Trecho(nome='N1CH17', n1=n1, n2=ch17, condutor=cond1, comprimento=1.3645/4)

# s4_al1

s4ch18 = Trecho(nome='S4CH18', n1=ns4, n2=ch18, condutor=cond1, comprimento=0.001)
ch18l2 = Trecho(nome='CH18L2', n1=ch18, n2=l2, condutor=cond1, comprimento=3.0)
l2l1 = Trecho(nome='L2L1', n1=l2, n2=l1, condutor=cond1, comprimento=3.0)
l1ch13 = Trecho(nome='L1CH13', n1=l1, n2=ch13, condutor=cond1, comprimento=0.01)
l1ch17 = Trecho(nome='L1CH17', n1=l1, n2=ch17, condutor=cond1, comprimento=0.01)


# setores

st1 = Setor(nome='S1',
            vizinhos=['A','D','G','J'],
            nos_de_carga=[ns1])

stA = Setor(nome='A',
            vizinhos=['S1','B'],
            nos_de_carga=[a1, a2])

stB = Setor(nome='B',
            vizinhos=['A','O'],
            nos_de_carga=[b1, gd1])
	
stC = Setor(nome='C',
            vizinhos=['O','S2','E'],
            nos_de_carga=[c1])

stO = Setor(nome='O',
            vizinhos=['B','C'],
            nos_de_carga=[o1])

st2 = Setor(nome='S2',
            vizinhos=['C'],
            nos_de_carga=[ns2])

stD = Setor(nome='D',
            vizinhos=['S1','E'],
            nos_de_carga=[d1, d2])

stE = Setor(nome='E',
            vizinhos=['D','M','C'],
            nos_de_carga=[e1])

stM = Setor(nome='M',
            vizinhos=['E','P','A'],
            nos_de_carga=[m1])

stP = Setor(nome='P',
            vizinhos=['M','F'],
            nos_de_carga=[p1])

stF = Setor(nome='F',
            vizinhos=['P','S3'],
            nos_de_carga=[f1])

st3 = Setor(nome='S3',
            vizinhos=['F'],
            nos_de_carga=[ns3])

stG = Setor(nome='G',
			vizinhos=['S1','D','H'],
			nos_de_carga=[g1,gd2])

stH = Setor(nome='H',
            vizinhos=['G','K','I'],
            nos_de_carga=[h1, h2])

stI = Setor(nome='I',
            vizinhos=['H','L'],
            nos_de_carga=[i1])

stJ = Setor(nome='J',
            vizinhos=['S1','K'],
            nos_de_carga=[j1])

stK = Setor(nome='K',
            vizinhos=['J','N','H'],
            nos_de_carga=[k1])

stN = Setor(nome='N',
            vizinhos=['K','L'],
            nos_de_carga=[n1])

stL = Setor(nome='L',
            vizinhos=['N','I','S4'],
            nos_de_carga=[l1, l2])

st4 = Setor(nome='S4',
            vizinhos=['L'],
            nos_de_carga=[ns4])

# ligacao das chaves

ch1.n1 = st1
ch1.n2 = stA

ch2.n1 = stA
ch2.n2 = stB

ch3.n1 = stB
ch3.n2 = stO

ch4.n1 = st2
ch4.n2 = stC

ch21.n1 = stC
ch21.n2 = stO

ch5.n1 = stC
ch5.n2 = stE

ch6.n1 = st1
ch6.n2 = stD

ch7.n1 = stD
ch7.n2 = stE

ch19.n1 = stE
ch19.n2 = stM

ch8.n1 = stM
ch8.n2 = stP

ch9.n1 = st3
ch9.n2 = stF

ch22.n1 = stF
ch22.n2 = stP

ch10.n1 = st1
ch10.n2 = stG

ch11.n1 = stG
ch11.n2 = stH

ch12.n1 = stH
ch12.n2 = stI

ch13.n1 = stI
ch13.n2 = stL

ch14.n1 = stH
ch14.n2 = stK

ch15.n1 = st1
ch15.n2 = stJ

ch16.n1 = stJ
ch16.n2 = stK

ch20.n1 = stK
ch20.n2 = stN

ch17.n1 = stN
ch17.n2 = stL

ch18.n1 = st4
ch18.n2 = stL


# alimentadores

s1_al1 = Alimentador(nome='S1_AL1',
                         setores=[st1, stA, stB],
                         trechos=[s1ch1,ch1a1,a1a2, a2ch2,ch2b1,b1gd1,b1ch3],
                         chaves=[ch1, ch2, ch3])

s1_al2 = Alimentador(nome='S1_AL2',
                         setores=[st1, stD, stE, stM],
                         trechos=[s1ch6,ch6d1,d1d2,d2ch7,ch7e1,e1ch19,ch19m1,m1ch8,e1ch5],
                         chaves=[ch6,ch5,ch7,ch8,ch19])

s1_al3 = Alimentador(nome='S1_AL3',
                         setores=[st1, stG, stH, stI],
                         trechos=[s1ch10,ch10g1,g1gd2,g1ch11,ch11h1,h1ch14,h1h2,h2ch12,ch12i1,i1ch13],
                         chaves=[ch10,ch11,ch12,ch13,ch14])

s1_al4 = Alimentador(nome='S1_AL4',
                         setores=[st1, stJ, stK, stN],
                         trechos=[s1ch15,ch15j1,j1ch16,ch16k1,k1ch14,k1ch20,ch20n1,n1ch17],
                         chaves=[ch15, ch16, ch17, ch14, ch20])

s2_al1 = Alimentador(nome='S2_AL1',
                         setores=[st2, stC,stO],
                         trechos=[s2ch4,ch4c1,c1ch21,ch21o1,o1ch3,c1ch5],
                         chaves=[ch4,ch3,ch5,ch21])

s3_al1 = Alimentador(nome='S3_AL1',
                         setores=[st3, stF, stP],
                         trechos=[s3ch9, ch9f1, f1ch22, ch22p1, p1ch8],
                         chaves=[ch9,ch8,ch22])

s4_al1 = Alimentador(nome='S4_AL1',
                         setores=[st4, stL],
                         trechos=[s4ch18,ch18l2,l2l1,l1ch13,l1ch17],
                         chaves=[ch18,ch17,ch13])

s1_t1 = Transformador(nome='S1_T1',
                   alimentadores=[s1_al1,s1_al2,s1_al3,s1_al4],
                   ligacao_primario='delta',
                   ligacao_secundario='estrela_aterrado',
                   tensao_primario=Fasor(mod=69e3, ang=0.0, tipo=Fasor.Tensao),
                   tensao_secundario=Fasor(mod=13.8e3, ang=0.0, tipo=Fasor.Tensao),
                   potencia=Fasor(mod=15e6, ang=0.0, tipo=Fasor.Potencia),
                   z1=0.0001,
                   xsobrer=1)

s1_t2 = Transformador(nome='S1_T2',
                   alimentadores=[s1_al1,s1_al2,s1_al3,s1_al4],
                   ligacao_primario='delta',
                   ligacao_secundario='estrela_aterrado',
                   tensao_primario=Fasor(mod=69e3, ang=0.0, tipo=Fasor.Tensao),
                   tensao_secundario=Fasor(mod=13.8e3, ang=0.0, tipo=Fasor.Tensao),
                   potencia=Fasor(mod=15e6, ang=0.0, tipo=Fasor.Potencia),
                   z1=0.0001,
                   xsobrer=1)

s2_t1 = Transformador(nome='S2_T1',
                   alimentadores=[s2_al1],
                   ligacao_primario='delta',
                   ligacao_secundario='estrela_aterrado',
                   tensao_primario=Fasor(mod=69e3, ang=0.0, tipo=Fasor.Tensao),
                   tensao_secundario=Fasor(mod=13.8e3, ang=0.0, tipo=Fasor.Tensao),
                   potencia=Fasor(mod=10e6, ang=0.0, tipo=Fasor.Potencia),
                   z1=0.0001,
                   xsobrer=1)

s3_t1 = Transformador(nome='S3_T1',
                   alimentadores=[s3_al1],
                   ligacao_primario='delta',
                   ligacao_secundario='estrela_aterrado',
                   tensao_primario=Fasor(mod=69e3, ang=0.0, tipo=Fasor.Tensao),
                   tensao_secundario=Fasor(mod=13.8e3, ang=0.0, tipo=Fasor.Tensao),
                   potencia=Fasor(mod=10e6, ang=0.0, tipo=Fasor.Potencia),
                   z1=0.0001,
                   xsobrer=1)

s4_t1 = Transformador(nome='S4_T1',
                   alimentadores=[s4_al1],
                   ligacao_primario='delta',
                   ligacao_secundario='estrela_aterrado',
                   tensao_primario=Fasor(mod=69e3, ang=0.0, tipo=Fasor.Tensao),
                   tensao_secundario=Fasor(mod=13.8e3, ang=0.0, tipo=Fasor.Tensao),
                   potencia=Fasor(mod=10e6, ang=0.0, tipo=Fasor.Potencia),
                   z1=0.0001,
                   xsobrer=1)

# subestacoes

s1 = Subestacao(nome='S1',
                alimentadores=[s1_al1,s1_al2,s1_al3,s1_al4],
                transformadores=[s1_t1,s2_t1],
                sbase=100e6,
                tensaoentrada=69e3,
                tensaosaida=13.8e3,
                impedancia_equivalente_positiva=(0.1021 + 1.0j * 0.5904),
                impedancia_equivalente_zero=(0.0 + 1.0j * 0.3453))

s2 = Subestacao(nome='S2',
                alimentadores=[s2_al1],
                transformadores=[s2_t1],
                sbase=100e6,
                tensaoentrada=69e3,
                tensaosaida=13.8e3,
                impedancia_equivalente_positiva=(0.0283 + 1.0j * 0.4418),
                impedancia_equivalente_zero=(0.0 + 1.0j * 0.3549))

s3 = Subestacao(nome='S3',
                alimentadores=[s3_al1],
                transformadores=[s3_t1],
                sbase=100e6,
                tensaoentrada=69e3,
                tensaosaida=13.8e3,
                impedancia_equivalente_positiva=(0.0163 + 1.0j * 0.4521),
                impedancia_equivalente_zero=(0.0 + 1.0j * 0.3647))

s4 = Subestacao(nome='S4',
                alimentadores=[s4_al1],
                transformadores=[s4_t1],
                sbase=100e6,
                tensaoentrada=69e3,
                tensaosaida=13.8e3,
                impedancia_equivalente_positiva=(0.0088 + 1.0j * 0.4245),
                impedancia_equivalente_zero=(0.0 + 1.0j * 0.3647))

# ordenar

s1_al1.ordenar(raiz='S1')
s1_al2.ordenar(raiz='S1')
s1_al3.ordenar(raiz='S1')
s1_al4.ordenar(raiz='S1')

s2_al1.ordenar(raiz='S2')

s3_al1.ordenar(raiz='S3')

s4_al1.ordenar(raiz='S4')

# gerar arvore de nos de carga

s1_al1.gerar_arvore_nos_de_carga()
s1_al2.gerar_arvore_nos_de_carga()
s1_al3.gerar_arvore_nos_de_carga()
s1_al4.gerar_arvore_nos_de_carga()
s2_al1.gerar_arvore_nos_de_carga()
s3_al1.gerar_arvore_nos_de_carga()
s4_al1.gerar_arvore_nos_de_carga()


def carregar_subestacao(subestacao):

     """
          Metodo temporario para testes. Utilizado para carregar a topologia da subestacao. 
          Substitui o carregamento da rede via arquivo xml
     """

     if subestacao == 'S1':

          sub = s1

     elif subestacao == 'S2':

          sub  = s2

     if subestacao == 'S3':

          sub = s3

     elif subestacao == 'S4':

          sub  = s4

     return sub

