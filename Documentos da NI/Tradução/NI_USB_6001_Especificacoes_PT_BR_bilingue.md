# NI USB-6001 | Especificações — tradução de estudo

Não oficial. Original NI, maio de 2014. Diagramas preservados na edição PDF bilíngue.

## Página 1 do original

# ESPECIFICAÇÕES
# NI USB-6001
## Dispositivo DAQ USB de baixo custo
As especificações a seguir são típicas a 25 °C, salvo indicação em contrário. Para obter mais informações sobre o NI USB-6001, consulte o Guia do usuário NI USB-6001/6002/6003, disponível em ni.com/manuals.
## Entrada analógica
| Característica | Especificação |
| Número de canais diferenciais | 4 |
| Número de canais referenciados (single-ended) | 8 |
| Resolução do ADC | 14 bits |
| Taxa máxima de amostragem (agregada) | 20 kS/s |
| Tipo de conversor | Aproximações sucessivas |
| FIFO de entrada analógica (AI) | 2.047 amostras |
| Fontes de disparo | Software, PFI 0, PFI 1 |


## Página 2 do original

## Entrada analógica (continuação)
| Característica | Especificação |
| Faixa de entrada | ±10 V |
| Tensão de trabalho | ±10 V |
| Proteção contra sobretensão, ligado | ±30 V |
| Proteção contra sobretensão, desligado | ±20 V |
| Impedância de entrada | >1 GΩ |
| Corrente de polarização de entrada | ±200 pA |
| Exatidão absoluta, típica no fundo de escala | 6 mV |
| Exatidão absoluta, máxima ao longo da faixa de temperatura, no fundo de escala | 26 mV |
| Ruído do sistema | 0,7 mV RMS |
| Não linearidade diferencial (DNL) | 14 bits, sem códigos ausentes |
| Não linearidade integral (INL) | ±0,5 LSB |
| Rejeição de modo comum (CMRR) | 56 dB (CC a 5 kHz) |
| Largura de banda | 300 kHz |
## Saída analógica
| Característica | Especificação |
| Saídas analógicas | 2 |
| Resolução do DAC | 14 bits |
| Faixa de saída | ±10 V |
| Taxa máxima de atualização | 5 kS/s simultâneos por canal, temporizados por hardware |
| FIFO de saída analógica (AO) | 2.047 amostras |
| Fontes de disparo | Software, PFI 0, PFI 1 |
| Capacidade de corrente de saída | ±5 mA |
| Corrente de curto-circuito | ±11 mA |
| Taxa de variação da saída (slew rate) | 3 V/µs |
| Impedância de saída | 0,2 Ω |


## Página 3 do original

## Saída analógica (continuação)
| Característica | Especificação |
| Exatidão absoluta sem carga, típica no fundo de escala | 9,1 mV |
| Exatidão absoluta sem carga, máxima ao longo da faixa de temperatura, no fundo de escala | 34 mV |
| DNL | 14 bits, sem códigos ausentes |
| INL | ±1 LSB |
| Estado ao ligar | 0 V |
| Transiente de inicialização (glitch) | -7 V durante 10 µs |
## Base de tempo
NOTA: As especificações a seguir se aplicam à exatidão temporal da amostragem de entrada e saída analógicas temporizadas por hardware.
| Característica | Especificação |
| Frequência da base de tempo | 80 MHz |
| Exatidão da base de tempo | ±100 ppm |
| Resolução temporal | 12,5 ns |
## Entradas e saídas digitais
São 13 linhas digitais: porta 0 com 8 linhas; porta 1 com 4 linhas; porta 2 com 1 linha.
| Linha | Função |
| P0.<0..7> | Entrada/saída digital estática |
| P1.0 | Entrada/saída digital estática |
| P1.1/PFI 1 | Entrada/saída digital estática, fonte do contador ou disparo digital |


## Página 4 do original

## Entradas e saídas digitais (continuação)
| Característica | Especificação |
| P1.<2..3> | Entrada/saída digital estática |
| P2.0/PFI 0 | Entrada/saída digital estática, fonte do contador ou disparo digital |
| Controle de direção | Cada canal programável individualmente como entrada ou saída |
| Tipo de acionamento da saída | Cada canal programável individualmente como coletor aberto ou acionamento ativo |
| Faixa de tensão máxima absoluta | -0,3 V a 5,5 V em relação a D GND |
| Resistor de pull-down | 47,5 kΩ para D GND |
| Estado ao ligar | Entrada |
## Entrada digital
| Característica | Especificação |
| Faixa de tensão de entrada, ligado | 0 a 5 V |
| Faixa de tensão de entrada, desligado | 0 a 3,3 V |
| Proteção de tensão de entrada | ±20 V em duas linhas por porta (máximo de cinco linhas no conjunto das portas) por até 24 horas |
CUIDADO: Não mantenha uma tensão superior a 3,3 V conectada a qualquer linha DIO por períodos prolongados com o dispositivo desligado. Isso pode causar problemas de confiabilidade a longo prazo.
| Característica | Especificação |
| VIH mínimo | 2,3 V |
| VIL máximo | 0,8 V |
| Corrente máxima de fuga de entrada a 3,3 V | 0,8 mA |
| Corrente máxima de fuga de entrada a 5 V | 4,5 mA |
## Saída digital (acionamento ativo)
| Característica | Especificação |
| VOL máximo a 4 mA / a 1 mA | 0,7 V / 0,2 V |
| VOH mínimo a 4 mA / a 1 mA | 2,1 V / 2,8 V |
| VOH máximo | 3,6 V |
| Corrente máxima de saída por linha | ±4 mA |


## Página 5 do original

## Saída digital (coletor aberto)
| Característica | Especificação |
| VOL máximo a 4 mA | 0,8 V |
| VOL máximo a 1 mA | 0,2 V |
NOTA: O VOH mínimo depende do resistor de pull-up e da fonte de tensão fornecidos pelo usuário. O resistor de pull-up recomendado é de 1 kΩ.
Com resistor de pull-up de 1 kΩ e fonte de tensão de 5 V:
| Característica | Especificação |
| VOH mínimo | 3,5 V |
| VOH típico | 4,5 V |
| Corrente máxima de saída por linha, absorvendo corrente (sinking) | -4 mA |
| Tensão máxima de pull-up | 5 V |
| Corrente máxima de fuga a 3,3 V | 0,8 mA |
| Corrente máxima de fuga a 5 V | 4,5 mA |
## Contador
| Característica | Especificação |
| Número de contadores | 1 |
| Resolução | 32 bits |
| Medições do contador | Contagem de bordas de subida ou descida |
| Sentido da contagem | Crescente |
| Fonte do contador | PFI 0 ou PFI 1 |
| Frequência máxima de entrada | 5 MHz |
| Largura mínima do pulso em nível alto | 100 ns |
| Largura mínima do pulso em nível baixo | 100 ns |


## Página 6 do original

## Fonte de alimentação de +5 V
| Característica | Especificação |
| Tensão de saída | +5 V, ±3% |
| Corrente máxima | 150 mA |
| Proteção contra sobrecorrente | 200 mA |
| Corrente de curto-circuito | 50 mA |
| Proteção contra sobretensão | ±20 V |
## Interface de barramento
| Característica | Especificação |
| Especificação USB | USB Full Speed |
| Velocidade do barramento USB | 12 Mb/s |
## Características físicas
| Dimensões | Valor |
| Sem os conectores de borne a parafuso | 75,4 mm × 86,2 mm × 23,6 mm (2,97 pol. × 3,40 pol. × 0,93 pol.) |
| Com os conectores de borne a parafuso | 93,2 mm × 86,2 mm × 23,6 mm (3,67 pol. × 3,40 pol. × 0,93 pol.) |


## Página 7 do original

## Figura 1. Dimensões do NI USB-6001
O desenho original correspondente é reproduzido na página seguinte. Cotas: 3,67 pol. (93,2 mm); 0,93 pol. (23,6 mm); 3,40 pol. (86,2 mm); 2,97 pol. (75,4 mm). As identificações AI e AO correspondem a entrada e saída analógicas.
| Característica | Especificação |
| Massa sem os conectores de borne a parafuso | 83 g (2,93 oz) |
| Massa com os conectores de borne a parafuso | 105 g (3,70 oz) |
| Conectores de E/S | Receptáculo USB Micro-B, (1); conectores de borne a parafuso de 16 posições |
| Fiação dos bornes | 1,31 a 0,08 mm² (16 a 28 AWG) |
| Torque de aperto dos bornes | 0,22 a 0,25 N·m (2,0 a 2,2 lb·pol.) |
Se precisar limpar o módulo, passe uma toalha seca.
## Condições ambientais
Temperatura: IEC 60068-2-1 e IEC 60068-2-2. Umidade: IEC 60068-2-56.
| Condição | Operação | Armazenamento |
| Temperatura | 0 a 45 °C | -40 a 85 °C |
| Umidade relativa, sem condensação | 5 a 95% | 5 a 90% |


## Página 8 do original

## Condições ambientais (continuação)
Grau de poluição (IEC 60664): 2. Altitude máxima: 2.000 m. Uso somente em ambientes internos.
## Segurança
Este produto atende aos requisitos das seguintes normas de segurança para equipamentos elétricos de medição, controle e uso em laboratório:
- IEC 61010-1, EN 61010-1.
- UL 61010-1, CSA 61010-1.
NOTA: Para certificações UL e outras certificações de segurança, consulte a etiqueta do produto ou a seção Certificação on-line do produto.
## Compatibilidade eletromagnética
Este produto atende aos requisitos das seguintes normas de compatibilidade eletromagnética (EMC) para equipamentos elétricos sensíveis de medição, controle e uso em laboratório:
- EN 61326-1 (IEC 61326-1): emissões Classe A; imunidade básica.
- EN 55011 (CISPR 11): Grupo 1, emissões Classe A.
- EN 55022 (CISPR 22): emissões Classe A.
- EN 55024 (CISPR 24): imunidade.
- AS/NZS CISPR 11: Grupo 1, emissões Classe A.
- AS/NZS CISPR 22: emissões Classe A.
- FCC 47 CFR Parte 15B: emissões Classe A.
- ICES-001: emissões Classe A.
NOTA: Nos Estados Unidos, segundo FCC 47 CFR, equipamentos Classe A destinam-se a locais comerciais, de indústria leve e de indústria pesada. Na Europa, Canadá, Austrália e Nova Zelândia, segundo CISPR 11, equipamentos Classe A destinam-se somente a locais de indústria pesada.
NOTA: Segundo CISPR 11, equipamentos do Grupo 1 são equipamentos industriais, científicos ou médicos que não geram intencionalmente energia de radiofrequência para tratamento de materiais ou para inspeção/análise.
NOTA: Para declarações, certificações EMC e informações adicionais, consulte Certificação on-line do produto.


## Página 9 do original

## Conformidade CE
Este produto atende aos requisitos essenciais das diretivas europeias aplicáveis:
- 2006/95/EC: Diretiva de Baixa Tensão (segurança).
- 2004/108/EC: Diretiva de Compatibilidade Eletromagnética (EMC).
## Certificação on-line do produto
Para obter as certificações e a Declaração de Conformidade (DoC) deste produto, acesse ni.com/certification, pesquise pelo número do modelo ou pela linha de produtos e clique no link correspondente na coluna Certification.
## Gestão ambiental
A NI tem o compromisso de projetar e fabricar produtos de maneira ambientalmente responsável. A NI reconhece que eliminar determinadas substâncias perigosas de seus produtos beneficia o meio ambiente e seus clientes.
Para mais informações ambientais, consulte a página Minimize Our Environmental Impact em ni.com/environment. Ela contém os regulamentos e as diretivas ambientais atendidos pela NI, além de informações ambientais não incluídas neste documento.
## Resíduos de equipamentos elétricos e eletrônicos (WEEE)
Clientes da União Europeia: este símbolo indica que os produtos descartados devem ser separados dos resíduos domésticos municipais, de acordo com a Diretiva WEEE 2002/96/EC do Parlamento Europeu e do Conselho. Todos os produtos no fim de sua vida útil devem ser enviados a um centro de coleta e reciclagem WEEE. O descarte adequado reduz o impacto ambiental e o risco à saúde humana decorrente de substâncias potencialmente perigosas empregadas nesses equipamentos. Sua cooperação contribui para o uso eficiente dos recursos naturais. Para informações sobre coleta e reciclagem em cada país, acesse ni.com/environment/weee.
## Controle da poluição de produtos eletrônicos de informação (RoHS da China)
Clientes da China: a National Instruments atende à diretiva chinesa de restrição de determinadas substâncias perigosas em produtos eletrônicos de informação (RoHS). Para informações sobre conformidade RoHS da China, acesse ni.com/environment/rohs_china.


## Página 10 do original

## Pinagem do dispositivo
O desenho da página original seguinte preserva a orientação física dos terminais. LEFT VIEW = vista esquerda; RIGHT VIEW = vista direita. Identificadores de terminais são mantidos sem tradução.
| Vista esquerda, de cima para baixo no desenho | Vista direita, de cima para baixo no desenho |
| AI GND | P0.0 |
| AI 0 | P0.1 |
| AI 4 | P0.2 |
| AI GND | P0.3 |
| AI 1 | P0.4 |
| AI 5 | P0.5 |
| AI GND | P0.6 |
| AI 2 | P0.7 |
| AI 6 | P1.0 |
| AI GND | P1.1/PFI 1 |
| AI 3 | P1.2 |
| AI 7 | P1.3 |
| AI GND | P2.0/PFI 0 |
| AO 0 | D GND |
| AO 1 | +5 V |
| AO GND | D GND |
## Avisos legais
Consulte NI Trademarks and Logo Guidelines em ni.com/trademarks para informações sobre marcas da National Instruments. Outros nomes de produtos e empresas são marcas ou nomes comerciais de seus respectivos titulares. Para patentes referentes a produtos/tecnologias NI, consulte Help > Patents no software, o arquivo patents.txt na mídia ou National Instruments Patent Notice em ni.com/patents. Informações sobre contratos de licença de usuário final (EULAs) e avisos legais de terceiros estão no arquivo readme do produto NI. Consulte Export Compliance Information em ni.com/legal/export-compliance para a política global de conformidade comercial e para obter códigos HTS, ECCN e outros dados de importação/exportação.
A NI NÃO OFERECE GARANTIAS EXPRESSAS OU IMPLÍCITAS QUANTO À EXATIDÃO DAS INFORMAÇÕES AQUI CONTIDAS E NÃO SE RESPONSABILIZA POR ERROS. Clientes do governo dos EUA: os dados deste manual foram desenvolvidos com recursos privados e estão sujeitos aos direitos limitados e restritos aplicáveis estabelecidos em FAR 52.227-14, DFAR 252.227-7014 e DFAR 252.227-7015.
© 2014 National Instruments. Todos os direitos reservados. 374369A-01, maio de 2014.
