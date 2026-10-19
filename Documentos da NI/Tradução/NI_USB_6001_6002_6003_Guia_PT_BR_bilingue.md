# NI USB-6001/6002/6003 | Guia do usuário — tradução de estudo

Não oficial. Original NI, maio de 2014. Diagramas preservados na edição PDF bilíngue.

## Página 1 do original

# GUIA DO USUÁRIO
# NI USB-6001/6002/6003
## Dispositivo DAQ USB de baixo custo
Este guia descreve como usar os dispositivos de aquisição de dados (DAQ) National Instruments USB-6001/6002/6003. Para obter as especificações, acesse ni.com/manuals e pesquise pelo nome do dispositivo.
O NI USB-6001/6002/6003 é um dispositivo USB Full Speed com oito canais de entrada analógica (AI) referenciados (single-ended), que também podem ser configurados como quatro canais diferenciais. Inclui ainda dois canais de saída analógica (AO), 13 canais de entrada/saída digital (DIO) e um contador de 32 bits.
## Tabela 1. Diferenças entre os modelos
| Característica | USB-6001 | USB-6002 | USB-6003 |
| Entrada: resolução do ADC | 14 bits | 16 bits | 16 bits |
| Entrada: taxa máxima de amostragem agregada | 20 kS/s | 50 kS/s | 100 kS/s |
| Saída: resolução do DAC | 14 bits | 16 bits | 16 bits |
| Saída: exatidão absoluta típica no fundo de escala | 9,1 mV | 8,6 mV | 8,6 mV |
Outras versões de idioma indicadas no original: alemão e francês, em ni.com/manuals.


## Página 2 do original

## Figura 1. Vistas superior e lateral do NI USB-6001/6002/6003
Legenda do desenho original: 1 - conector de borne a parafuso; 2 - indicador LED; 3 - conector USB Micro-B.
## Orientações de segurança
Opere o dispositivo NI DAQ somente conforme descrito neste documento.
CUIDADO: Consulte o documento NI USB-6001/6002/6003 Safety, Environmental, and Regulatory Information, incluído no kit, para informações importantes de segurança e compatibilidade eletromagnética. Para obter uma cópia on-line, acesse ni.com/manuals e pesquise pelo título.
CUIDADO: Não opere o dispositivo de modo não especificado neste documento. O uso indevido pode criar riscos. A proteção de segurança incorporada pode ser comprometida se o dispositivo estiver danificado de qualquer forma. Nesse caso, entre em contato com a National Instruments para reparo.
CUIDADO: Não substitua peças nem modifique o dispositivo, exceto conforme descrito neste documento. Use-o somente com o chassi, módulos, acessórios e cabos especificados nas instruções de instalação.
CUIDADO: Não opere o dispositivo em atmosfera explosiva ou onde possa haver gases ou vapores inflamáveis. Se for necessário operá-lo nesse ambiente, ele deverá estar em um invólucro com classificação adequada.
CUIDADO: Todas as tampas e painéis de fechamento devem estar instalados durante a operação. Não opere o dispositivo sem verificar se a tampa está corretamente fixada e se o dispositivo está completamente fechado.


## Página 3 do original

## Orientações de compatibilidade eletromagnética
Este produto foi testado e atende aos requisitos e limites regulatórios de compatibilidade eletromagnética (EMC) indicados nas especificações. Esses requisitos e limites oferecem proteção razoável contra interferência prejudicial quando o produto é operado no ambiente eletromagnético operacional previsto.
O produto destina-se a locais industriais. Entretanto, pode ocorrer interferência prejudicial em algumas instalações, quando conectado a um periférico ou objeto de teste, ou quando usado em áreas residenciais ou comerciais. Para minimizar a interferência na recepção de rádio e televisão e evitar degradação inaceitável de desempenho, instale e utilize o produto rigorosamente conforme a documentação.
Além disso, modificações não expressamente aprovadas pela National Instruments podem anular sua autorização para operar o produto segundo as regras regulatórias locais.
CUIDADO: Para garantir o desempenho EMC especificado, qualquer fio ou cabo conectado ao conector de borne a parafuso deve ter comprimento máximo de 0,5 m (20 pol.).
## Desembalagem
O dispositivo NI DAQ é fornecido em embalagem antiestática para evitar descarga eletrostática (ESD). A ESD pode danificar diversos componentes.
CUIDADO: Nunca toque nos pinos expostos dos conectores.
Para evitar danos por ESD durante o manuseio:
- Aterre-se usando uma pulseira de aterramento ou tocando um objeto aterrado.
- Encoste a embalagem antiestática em uma parte metálica do gabinete do computador antes de retirar o dispositivo.
Retire o dispositivo e verifique se há componentes soltos ou outros sinais de danos. Notifique a NI se houver qualquer dano aparente. Não instale um dispositivo danificado no computador. Guarde o dispositivo na embalagem antiestática quando não estiver em uso.
## Conteúdo da embalagem
- NI USB-6001/6002/6003.
- Dois conectores de borne a parafuso.
- Cabo Micro USB Hi-Speed.
- DVD do NI-DAQmx.
- Documento NI USB-6001/6002/6003 Quick Start.
- Documento NI USB-6001/6002/6003 Safety, Environmental, and Regulatory Information.


## Página 4 do original

## Configuração do NI USB-6001/6002/6003
Execute as etapas abaixo para começar a usar o dispositivo.
## Instalação do software
1. Instale o software de aplicação, quando aplicável, conforme as instruções que o acompanham.
2. Instale o NI-DAQmx. Os dispositivos NI USB-6001/6002/6003 são compatíveis com NI-DAQmx 9.9 e versões posteriores.
NOTA: O NI-DAQmx está incluído no disco do kit e disponível em ni.com/support. Após a instalação, sua documentação fica em Start > All Programs > National Instruments > NI-DAQmx. Outros documentos NI estão em ni.com/manuals.
3. Registre os produtos quando aparecer o NI Product Registration Wizard.
## Preparação do hardware
1. Insira os conectores de borne a parafuso nos receptáculos do dispositivo. Consulte a Figura 2.
2. O cabo Micro USB Hi-Speed possui dois conectores diferentes. Conecte o menor ao dispositivo e o maior à porta USB do computador em que o NI-DAQmx está instalado.
## Figura 2. Montagem do hardware
Legenda: 1 - conectores de borne a parafuso; 2 - cabo Micro USB Hi-Speed.


## Página 5 do original

## Verificação da instalação
1. Abra o NI Measurement & Automation Explorer (NI MAX): no Windows 7/Vista, dê duplo clique no ícone NI MAX da área de trabalho; no Windows 8, clique em NI Measurement & Automation Explorer no NI Launcher.
2. Expanda My System > Devices and Interfaces e verifique se o NI USB-6001/6002/6003 aparece. Caso não apareça, pressione F5 para atualizar a visualização. Se continuar sem reconhecimento, consulte ni.com/support/daqmx para solução de problemas.
3. Para executar o autoteste no NI MAX, clique com o botão direito no dispositivo e selecione Self-Test. O autoteste faz uma verificação breve da instalação. Ao terminar, uma mensagem indica se a verificação foi bem-sucedida. Em caso de erro, consulte ni.com/support/daqmx.
CUIDADO: Para garantir o desempenho EMC especificado, opere este produto somente com cabos e acessórios blindados.
4. Conecte os fios de um cabo multicondutor blindado, com seção de 0,08 a 1,31 mm² (28 a 16 AWG), aos bornes. Remova 6 mm (0,25 pol.) da isolação, insira os fios desencapados e aperte os parafusos com chave de fenda, aplicando torque de 0,22 a 0,25 N·m (2,0 a 2,2 lb·pol.). Consulte a pinagem na Figura 4. Se usar cabo blindado, conecte a blindagem a um terminal GND próximo.
5. Abra um painel de teste no NI MAX clicando com o botão direito no dispositivo e selecionando Test Panels. Clique em Start para testar as funções ou Help para instruções. Se ocorrer erro, consulte ni.com/support/daqmx. Clique em Close para sair.
## Uso do dispositivo em uma aplicação: programas de exemplo
O driver NI-DAQmx inclui exemplos para começar a programar com o dispositivo. Você pode modificar e salvar o código em uma aplicação, usá-lo para desenvolver uma nova aplicação ou adicioná-lo a uma aplicação existente.
Para localizar exemplos NI, acesse ni.com/info e informe o código daqmxexp. Para executar exemplos sem o dispositivo instalado, use um dispositivo simulado NI-DAQmx. No NI MAX, selecione Help > Help Topics > NI-DAQmx > MAX Help for NI-DAQmx e pesquise simulated devices.


## Página 6 do original

## NI-DAQ Assistant
O NI-DAQ Assistant pode ser usado em diversos programas NI para configurar canais virtuais e de medição. A Tabela 2 indica onde encontrar tutoriais.
## Tabela 2. Localização dos tutoriais
| Aplicação | Caminho do tutorial, mantido como na interface original |
| LabVIEW | Start > All Programs > National Instruments > NI-DAQmx > NI-DAQmx Help > Getting Started |
| LabWindows/CVI | Help > Contents > Using LabWindows/CVI > Data Acquisition > Taking an NI-DAQmx Measurement in LabWindows/CVI |
| Measurement Studio | NI Measurement Studio Help > Getting Started with the Measurement Studio Class Libraries > Measurement Studio Walkthroughs > Walkthrough: Creating a Measurement Studio NI-DAQmx Application |
| SignalExpress | Help > Taking an NI-DAQmx Measurement in SignalExpress |
## ANSI C sem software de aplicação NI
A NI-DAQmx Help apresenta a API e conceitos gerais de medição. Selecione Start > All Programs > National Instruments > NI-DAQmx > NI-DAQmx Help. A NI-DAQmx C Reference Help descreve as funções da biblioteca. Acesse Start > All Programs > National Instruments > NI-DAQmx > Text-Based Code Support > NI-DAQmx C Reference Help.
## Linguagens .NET sem software de aplicação NI
Com Microsoft .NET Framework 2.0 ou posterior, é possível criar aplicações NI-DAQmx em Visual C# e Visual Basic .NET sem Measurement Studio. Para instalar a documentação da API, é necessário Microsoft Visual Studio .NET 2005 ou posterior.
A documentação instalada apresenta a API, tarefas e conceitos de medição e referência de funções. Acesse Start > All Programs > National Instruments > NI-DAQmx > Text-Based Code Support. Para funções, consulte NationalInstruments.DAQmx Namespace e NationalInstruments.DAQmx.ComponentModel Namespace. Para conceitos, consulte Using the Measurement Studio NI-DAQmx .NET Library e Developing with Measurement Studio NI-DAQmx.
No Visual Studio 2005 ou 2008, acesse Help > Contents e selecione Measurement Studio em Filtered By. No Visual Studio 2010, acesse Help > View Help e selecione NI Measurement Studio Help em Related Links.


## Página 7 do original

## Recursos: diagrama de blocos
A Figura 3 apresenta os principais componentes funcionais do dispositivo NI DAQ. O desenho original é preservado na página seguinte.
## Figura 3. Diagrama de blocos NI USB-6001/6002/6003
| Rótulo no desenho | Tradução |
| USB Connector (Micro-B) | Conector USB (Micro-B) |
| USB 2.0 Full Speed Interface | Interface USB 2.0 Full Speed |
| 80 MHz Clock | Clock de 80 MHz |
| 5 V Supply | Alimentação de 5 V |
| Control Logic | Lógica de controle |
| Analog Input | Entrada analógica |
| Analog Output | Saída analógica |
| Digital I/O | Entradas/saídas digitais |
| Counters & PFI | Contadores e PFI |
| 16-Position Screw Terminal Plug | Conector de borne a parafuso de 16 posições |
| I/O Connector | Conector de E/S |
Os identificadores AI 0 a AI 7, AO 0, AO 1, AI GND, AO GND, P0.0 a P2.0, PFI 0, PFI 1, 5 V e D GND são mantidos como no equipamento.


## Página 8 do original

## Indicador LED
O dispositivo possui um LED azul que indica seu estado, conforme a Tabela 3.
| Estado do LED | Estado do dispositivo |
| Apagado | Não conectado ou em modo de suspensão. |
| Aceso, sem piscar | Conectado e funcionando normalmente. |
| Piscando | Ocorreu um erro. Aguarde 10 segundos para permitir a tentativa de recuperação. Se continuar piscando, desconecte e reconecte o dispositivo. Se o erro persistir, entre em contato com a National Instruments. Consulte Suporte e serviços em todo o mundo para os contatos. |
## Conectores de borne a parafuso
O dispositivo inclui dois conectores removíveis: um para sinais analógicos e outro para sinais digitais. Cada conector possui 16 conexões para fios de 0,08 a 1,31 mm² (28 a 16 AWG). Consulte Pinagem e descrição dos sinais.
## Cabos e acessórios
A Tabela 4 apresenta cabos e acessórios disponíveis. A lista completa e informações de pedido estão na seção de preços da página do dispositivo em ni.com.
| Acessório | Código | Descrição |
| USB-600x Accessories | 782703-01 | Quatro conectores de borne adicionais e uma chave de fenda. |
| USB-600x Series Prototyping Accessories | 779511-01 | Acessório de prototipagem sem blindagem para condicionamento de sinais definido pelo usuário. Podem ser usados até dois por dispositivo. |
| Cabo Micro USB Hi-Speed, A para Micro-B | 782909-01, 782909-02 | Comprimentos de 1 m e 2 m. |
CUIDADO: Para garantir o desempenho EMC especificado, qualquer fio ou cabo conectado ao borne deve ter comprimento máximo de 0,5 m (20 pol.).


## Página 9 do original

## Pinagem e descrição dos sinais
A Figura 4 mostra a pinagem. Os nomes de entrada analógica aparecem primeiro na forma referenciada AI x e depois na forma diferencial (AI x+/-). A Tabela 5 descreve cada sinal.
## Figura 4. Pinagem NI USB-6001/6002/6003
LEFT VIEW = vista esquerda; RIGHT VIEW = vista direita. Os rótulos físicos são mantidos no desenho original seguinte. AI = entrada analógica; AO = saída analógica; DIO = entrada/saída digital.
## Tabela 5. Descrição dos sinais
| Sinal | Referência / direção | Descrição |
| AI GND | Sem referência/direção | Terra da entrada analógica: referência para medições de entrada analógica single-ended. |
| AI <0..7> | AI GND / entrada | Canais de entrada analógica 0 a 7. Em medições referenciadas, cada sinal corresponde a um canal de tensão. Em diferencial, AI 0 e AI 4 são as entradas positiva e negativa do canal 0. Os demais pares são AI 1 e AI 5; AI 2 e AI 6; AI 3 e AI 7. Consulte Entrada analógica. |
Correspondência dos rótulos diferenciais: AI 0 = AI 0+; AI 4 = AI 0-; AI 1 = AI 1+; AI 5 = AI 1-; AI 2 = AI 2+; AI 6 = AI 2-; AI 3 = AI 3+; AI 7 = AI 3-.


## Página 10 do original

## Tabela 5. Descrição dos sinais (continuação)
| Sinal | Referência / direção | Descrição |
| AO GND | Sem referência/direção | Terra da saída analógica: referência para a saída analógica. |
| AO <0,1> | AO GND / saída | Canais de saída analógica 0 e 1. Fornecem a tensão dos canais AO. Consulte Saída analógica. |
| P0.<0..7> | D GND / entrada ou saída | Canais digitais 0 a 7 da porta 0. Cada sinal pode ser configurado individualmente como entrada ou saída. Consulte Entradas e saídas digitais. |
| P1.<0..3> | D GND / entrada ou saída | Canais digitais 0 a 3 da porta 1. Cada sinal pode ser configurado individualmente como entrada ou saída. Consulte Entradas e saídas digitais. |
| P2.0 | D GND / entrada ou saída | Canal digital 0 da porta 2. Pode ser configurado individualmente como entrada ou saída. Consulte Entradas e saídas digitais. |
| PFI 0, 1 | D GND / entrada | Interface de função programável ou canais de E/S digital. Entrada de contador de bordas ou de disparo digital. Consulte PFI 0 e PFI 1. |
| D GND | Sem referência/direção | Terra digital: referência dos sinais digitais. |
| +5 V | D GND / saída | Fonte de +5 V: fornece até 150 mA. Consulte Fonte de alimentação de +5 V. |


## Página 11 do original

## Entrada analógica
O dispositivo possui oito canais de entrada analógica, utilizáveis para quatro medições diferenciais ou oito medições referenciadas. A Figura 5 mostra o circuito de entrada.
## Figura 5. Circuito de entrada analógica
Os principais blocos são:
- MUX: o multiplexador encaminha um canal AI por vez ao multiplexador de seleção de modo (DIFF/RSE MUX).
- DIFF/RSE MUX: seleciona entre medição diferencial (DIFF) e medição referenciada single-ended (RSE).
- IA: o amplificador de instrumentação remove o sinal de modo comum e atua como buffer do sinal de entrada antes de sua amostragem pelo conversor analógico-digital.
- ADC: digitaliza o sinal AI, convertendo a tensão analógica em código digital.
- AI FIFO: o dispositivo pode executar conversões únicas ou múltiplas, para um número fixo ou ilimitado de amostras. Um buffer primeiro a entrar, primeiro a sair (FIFO) armazena os dados durante a aquisição para evitar perdas.
- ADC Control: o circuito de controle define a taxa de conversão, configura a entrada, comanda a sequência de varredura e inicia aquisições sincronizadas com PFI 0 ou PFI 1.
Rótulos adicionais da figura: AI Data = dados de entrada analógica; AI Sampling Clock = clock de amostragem de AI; AI Start Trigger = disparo de início de AI; ADC Control = controle do ADC; I/O Connector = conector de E/S; 16-Position Screw Terminal Plug = conector de borne de 16 posições.


## Página 12 do original

## Modos de entrada analógica
Os canais podem ser configurados para até quatro medições diferenciais (DIFF) ou oito medições referenciadas (RSE).
- Modo diferencial: mede a diferença de tensão entre dois sinais AI.
- Modo referenciado single-ended: mede a tensão de um sinal AI em relação a AI GND.
Os modos são programados por canal. Por exemplo, é possível configurar a varredura de dois canais diferenciais e quatro canais referenciados. As configurações AI determinam como os sinais devem ser conectados.
## Realização de medições diferenciais
Conecte o terminal positivo do sinal ou fonte de tensão ao terminal AI+ e o negativo ao terminal AI-.
## Figura 6. Conexão de um sinal de tensão diferencial
Voltage Source = fonte de tensão; DAQ Device = dispositivo DAQ. As polaridades AI+ e AI- são preservadas no desenho.
## Figura 7. Exemplo de medição diferencial de ±10 V
Amplitude (V) = amplitude (V); Result = resultado. As curvas AI 1 e AI 5 representam as tensões nos dois terminais; os rótulos são mantidos no gráfico original.


## Página 13 do original

## Realização de medições referenciadas single-ended
Para conectar sinais de tensão RSE ao dispositivo, ligue o sinal de tensão positivo a um terminal AI e o sinal de terra a um terminal AI GND, conforme a Figura 8.
## Figura 8. Conexão de um sinal de tensão referenciado single-ended
Voltage Source = fonte de tensão; DAQ Device = dispositivo DAQ. AI e AI GND mantêm os nomes dos terminais do equipamento.


## Página 14 do original

## Fontes de sinal e configuração de entrada recomendada
A Tabela 6 apresenta os modos de entrada analógica recomendados para fontes flutuantes e fontes referenciadas ao terra.
## Tabela 6. Configuração da entrada analógica
| Tipo de fonte | Exemplos |
| Fonte flutuante, não conectada ao terra da instalação | Termopares não aterrados; condicionadores com saídas isoladas; dispositivos alimentados por bateria. |
| Fonte referenciada ao terra | Instrumentos conectados à rede elétrica com saídas não isoladas. |
Os quatro diagramas da tabela original mostram as conexões diferenciais (DIFF) e referenciadas (RSE) para cada tipo de fonte. Signal Source = fonte de sinal; DAQ Device = dispositivo DAQ; Vcm = tensão de modo comum. Na célula inferior direita: os potenciais da malha de terra (VA - VB) são somados ao sinal medido.
Nota * do original: consulte Realização de medições diferenciais para descrições dos modos RSE e DIFF e considerações de software.
Nota † do original: consulte Fontes de sinal referenciadas ao terra para mais informações.


## Página 15 do original

## Fontes de sinal flutuantes
Um instrumento ou dispositivo com saída isolada é uma fonte flutuante. Ela não está conectada ao sistema de aterramento da instalação, mas possui um ponto de referência de terra isolado. Exemplos: saídas de transformadores, termopares, dispositivos alimentados por bateria, isoladores ópticos e amplificadores de isolamento.
Para informações sobre fiação de campo e ruído em sinais analógicos, acesse ni.com/info e informe rdfwn3.
## Quando usar conexão diferencial com fontes flutuantes
Use entradas DIFF para qualquer canal que atenda a uma das condições:
- O sinal é de baixo nível e exige maior exatidão.
- Os fios entre a fonte e o dispositivo têm mais de 3 m (10 pés).
- O sinal exige um ponto separado de referência de terra ou de retorno.
- Os fios passam por ambientes ruidosos.
- Há dois canais AI, AI+ e AI-, disponíveis para o sinal.
Conexões DIFF reduzem a captação de ruído e aumentam a rejeição de ruído de modo comum. Também permitem que as entradas flutuem dentro da tensão de trabalho do dispositivo. O amplificador de instrumentação rejeita tanto o ruído de modo comum quanto a diferença de potencial entre o terra da fonte e o terra do dispositivo. Consulte Realização de medições diferenciais.
## Quando usar conexão RSE com fontes flutuantes
Use RSE somente quando todas as condições a seguir forem atendidas:
- O sinal pode compartilhar AI GND com os demais sinais RSE.
- Os fios entre a fonte e o dispositivo têm menos de 3 m (10 pés).
Para qualquer sinal que não atenda a essas condições, recomendam-se conexões DIFF para maior integridade do sinal.
Nas conexões single-ended, mais ruído eletrostático e magnético é acoplado aos sinais do que nas configurações DIFF. Isso resulta das diferenças nos caminhos do sinal. O acoplamento magnético é proporcional à área entre os dois condutores; o elétrico depende da diferença de campo elétrico entre eles. Consulte Realização de medições referenciadas single-ended.


## Página 16 do original

## Fontes de sinal referenciadas ao terra
Uma fonte referenciada ao terra está conectada ao sistema de aterramento da instalação. Ela já compartilha um ponto de terra com o dispositivo, supondo que o computador esteja conectado ao mesmo sistema de alimentação da fonte. Saídas não isoladas de instrumentos e dispositivos conectados à rede elétrica se enquadram nessa categoria.
A diferença de potencial de terra entre dois instrumentos ligados ao mesmo sistema elétrico da instalação é tipicamente de 1 a 100 mV, mas pode ser muito maior se os circuitos de distribuição estiverem ligados incorretamente. Se a fonte aterrada for medida de modo incorreto, essa diferença pode aparecer como erro. Siga as instruções de conexão para eliminar sua contribuição ao sinal medido.
Para informações sobre fiação de campo e ruído em sinais analógicos, acesse ni.com/info e informe rdfwn3.
## Quando usar conexão diferencial com fontes referenciadas ao terra
Use DIFF para qualquer canal que atenda a uma das condições:
- O sinal é de baixo nível e exige maior exatidão.
- Os fios entre a fonte e o dispositivo têm mais de 3 m (10 pés).
- O sinal exige um ponto separado de referência de terra ou de retorno.
- Os fios passam por ambientes ruidosos.
- Há dois canais AI, AI+ e AI-, disponíveis para o sinal.
Conexões DIFF reduzem a captação de ruído, aumentam a rejeição de modo comum e permitem que o sinal flutue dentro da tensão de trabalho. Consulte Realização de medições diferenciais.
## Quando usar conexão RSE com fontes referenciadas ao terra
Não use RSE com fontes referenciadas ao terra. Use conexões diferenciais.
Como mostra a célula inferior direita da Tabela 6, pode existir uma diferença de potencial entre AI GND e o terra do sensor. Em modo RSE, essa malha de terra provoca erros de medição.


## Página 17 do original

## Faixa de entrada
A faixa de entrada é de ±10 V. No modo diferencial, cada AI deve permanecer dentro de ±10 V em relação a AI GND, e a diferença entre as entradas positiva e negativa deve permanecer dentro de ±10 V. No modo RSE, sinais de ±10 V em qualquer entrada analógica em relação a AI GND são medidos com exatidão.
## Figura 9. Faixa de entrada analógica
DAQ Device = dispositivo DAQ; Vin = tensão de entrada; Vdiff = tensão diferencial; VCM = tensão de modo comum. Os sinais de polaridade e as conexões são preservados no original.
Acima de ±10 V, o sinal começa a ser recortado, como na Figura 10. Tipicamente, o recorte começa em ±10,5 V.
## Figura 10. Exceder ±10 V em AI produz resultados recortados
Amplitude (V) = amplitude (V); Result = resultado; AI 1 identifica a entrada. O gráfico original mostra níveis de 20, 10,5, 0, -10,5 e -20 V.
Sem sinal conectado ao terminal de entrada analógica, a leitura pode assumir qualquer valor entre +10,5 V e -10,5 V, ou saturar em ±10,5 V. Esse comportamento é normal e não afeta a medição quando um sinal é conectado. Para mais informações sobre fiação e ruído, acesse ni.com/info e informe rdfwn3.


## Página 18 do original

## Considerações sobre varredura multicanal
O dispositivo pode varrer vários canais em altas taxas e digitalizar os sinais com exatidão. Entretanto, o projeto do sistema deve considerar os pontos a seguir para garantir a exatidão das medições.
- Use fontes de baixa impedância: para rápido estabelecimento, a impedância da fonte deve ser <1 kΩ. Impedâncias altas aumentam o tempo de estabelecimento e reduzem a exatidão em altas taxas de varredura. Para informações sobre redução da impedância da fonte, acesse ni.com/info e informe rdbbis.
- Use cabos curtos e de boa qualidade: isso reduz diafonia, efeitos de linha de transmissão e ruído. A capacitância do cabo também pode aumentar o tempo de estabelecimento.
- Evite varrer mais rápido que o necessário: velocidades menores dão ao dispositivo mais tempo para atingir um nível mais exato ao alternar entre canais.
## Disparo de início de AI
PFI 0 ou PFI 1 podem ser configurados como AI Start Trigger. Consulte Uso de PFI para disparar uma aquisição de entrada analógica.
## Saída analógica
A Figura 11 mostra o circuito de saída analógica.
## Figura 11. Circuito de saída analógica
Rótulos: AO Data = dados de saída analógica; AO Sampling Clock = clock de amostragem de AO; AO Start Trigger = disparo de início de AO; DAC Control = controle do DAC; Buffer = estágio de saída/buffer; Protection = proteção; I/O Connector = conector de E/S; 16-Position Screw Terminal Plug = conector de borne de 16 posições. DAC 0, DAC 1, AO FIFO, AO 0, AO 1 e AO GND são mantidos.


## Página 19 do original

## Blocos principais do circuito de saída analógica
- Proteção: evita danos aos buffers em caso de curto-circuito ou sobretensão.
- Buffer: amplifica o sinal analógico para a faixa de ±10 V e garante a capacidade de acionamento da carga externa.
- DAC 0 e DAC 1: os conversores digital-analógicos transformam sinais digitais em sinais analógicos de baixo nível.
- AO FIFO: a memória primeiro a entrar, primeiro a sair assegura que os dados sejam transferidos aos DACs no tempo adequado, sem serem afetados pelas latências USB.
- Controle do DAC: define a taxa de dados e a condição de início, que pode ser disparada por PFI 0 ou PFI 1.
## Conexão dos sinais de saída analógica
Os sinais são referenciados a AO GND. Conecte as cargas entre AO 0 ou AO 1 e AO GND.
## Figura 12. Conexão das cargas de saída analógica
Load = carga; DAQ Device = dispositivo DAQ; Analog Output Channels = canais de saída analógica; Channel 0/1 = canal 0/1; VOUT = tensão de saída.
## Estado ao ligar
AO apresenta um breve transiente quando o dispositivo é ligado e quando sai do modo de suspensão. Após a energização, AO é redefinida para 0 V.
## Faixa de AO
A faixa de saída analógica é ±10 V.


## Página 20 do original

## Minimização de transientes no sinal de saída
Ao gerar uma forma de onda com um DAC, podem ocorrer transientes (glitches). Eles são normais: quando o DAC muda de uma tensão para outra, a liberação de cargas produz transientes. Os maiores ocorrem quando muda o bit mais significativo do código do DAC. Um filtro passa-baixas de supressão de transientes pode remover parte deles, dependendo da frequência e da natureza do sinal de saída. Consulte ni.com/support para mais informações.
## Métodos de geração de dados de saída analógica
A geração pode ser temporizada por software ou por hardware:
- Por software: o software controla a taxa de geração, enviando um comando separado ao hardware para iniciar cada conversão NI DAQ. No DAQmx, esse modo é chamado on-demand timing (temporização sob demanda). Também é chamado operação imediata ou estática e normalmente é usado para escrever um único valor, como uma tensão CC constante.
- Por hardware: um sinal digital de hardware gerado internamente controla a taxa. O intervalo entre amostras pode ser muito menor e a temporização pode ser determinística.
Operações temporizadas por hardware utilizam buffers. Durante a geração AO, os dados são transferidos de um buffer no computador para a FIFO do dispositivo por fluxos de sinais USB antes de serem escritos nos DACs, uma amostra por vez. A transferência em grandes blocos, em vez de ponto a ponto, permite taxas elevadas.
Uma propriedade das operações de E/S com buffer é o modo de amostragem, que pode ser finito ou contínuo:
- Finito: gera uma quantidade específica e predeterminada de amostras. A geração para após escrever essa quantidade.
- Contínuo: gera uma quantidade não especificada de amostras. A geração prossegue até ser interrompida, em vez de parar após um número definido.
## Disparo de início de AO
PFI 1 ou PFI 0 podem ser configurados como AO Start Trigger. Consulte Uso de PFI para disparar uma geração de saída analógica.


## Página 21 do original

## Entradas e saídas digitais
O dispositivo possui 13 linhas: P0.<0..7>, P1.<0..3> e P2.0. D GND é a referência de terra digital. Cada linha pode ser programada individualmente como entrada ou saída.
Todas as atualizações e amostragens de entradas e saídas digitais são temporizadas por software.
A Figura 13 mostra exemplos de conexão de P0.<0..7> como entradas e saídas. P1.<0..3> e P2.0 podem ser configuradas de maneira semelhante.
## Figura 13. Exemplo de conexão de carga
1. P0.0 configurada como saída digital em coletor aberto acionando um LED.
2. P0.2 configurada como saída digital com acionamento ativo acionando um LED.
3. P0.4 configurada como entrada digital recebendo um sinal TTL de um inversor com habilitação.
4. P0.7 configurada como entrada digital recebendo um sinal de 0 V ou 5 V de uma chave.
Rótulos: Switch = chave; TTL Signal = sinal TTL; DAQ Device = dispositivo DAQ; I/O Connector = conector de E/S; GND = terra; LED mantém a sigla.
CUIDADO: Exceder as tensões máximas de entrada ou os limites máximos de saída indicados nas especificações pode danificar o dispositivo e o computador. A National Instruments não se responsabiliza por danos decorrentes dessas conexões. Consulte as especificações em ni.com/manuals.
## Estados ao ligar
Na inicialização e na reinicialização do sistema, o hardware configura todas as linhas DIO como entradas de alta impedância. O dispositivo não força nível alto nem baixo. Cada linha possui um resistor de pull-down fraco conectado a ela.


## Página 22 do original

## Fornecimento e absorção de corrente (source/sink)
No modo de saída, a configuração padrão é acionamento ativo, permitindo operação em 3,3 V com limite de fornecimento/absorção de corrente de ±4 mA.
As portas podem ser configuradas como coletor aberto pela API NI-DAQmx. Com um resistor externo de pull-up fornecido pelo usuário, isso permite operar em outro nível de tensão. A Figura 14 mostra um exemplo.
## Figura 14. Conexão de resistor externo fornecido pelo usuário
DAQ Device = dispositivo DAQ; P0.0 with Output Drive Type Set to Open Collector = P0.0 configurada com saída em coletor aberto; External Load = carga externa; External Pull-Up Resistor = resistor externo de pull-up; 47.5 kΩ Onboard Pull-Down Resistor = resistor interno de pull-down de 47,5 kΩ; 47 Ω Protection Resistor = resistor de proteção de 47 Ω; Vpull-up (User Provided, ≤5 V) = tensão de pull-up fornecida pelo usuário, ≤5 V.
NOTA: Verifique se a corrente em Rpull não excede o limite máximo de absorção de corrente de 4 mA.
Para configurar dispositivos NI como dreno aberto/coletor aberto ou push-pull/acionamento ativo, acesse ni.com/info e informe ex52sp.
## Proteção de E/S
Para proteger contra sobretensão, subtensão, sobrecorrente e ESD, evite essas condições seguindo as orientações:
- Se uma linha DIO estiver como saída, não a conecte a fonte externa de sinal, sinal de terra ou fonte de alimentação.
- Se estiver como saída, conheça a corrente exigida pela carga e não exceda os limites especificados. A NI oferece soluções de condicionamento para aplicações digitais que exigem alta corrente.
- Se estiver como entrada, não aplique tensões fora da faixa normal. As linhas DIO têm faixa de operação menor que a dos sinais AI.
- Trate o dispositivo como sensível à eletricidade estática. Aterre corretamente você e os equipamentos ao manuseá-lo ou fazer conexões.


## Página 23 do original

## PFI 0 e PFI 1
## Uso de PFI como fonte do contador
PFI 0 ou PFI 1 podem ser fontes de contagem de bordas digitais. Nesse modo, bordas de subida ou de descida são contadas por um contador de 32 bits. Consulte as especificações em ni.com/manuals.
NOTA: A contagem é somente crescente, a partir de zero ou de um valor inicial, por exemplo 1, 2, 3... ou 1001, 1002, 1003. Não há contagem decrescente: não é possível iniciar em 100 e contar 99, 98, 97.
## Uso de PFI para disparar uma aquisição de entrada analógica
Uma tarefa AI pode aguardar uma borda em PFI 0 ou PFI 1 antes de começar. Configure a fonte AI Start Trigger como PFI 0 ou PFI 1 e selecione borda de subida ou descida.
## Uso de PFI para disparar uma geração de saída analógica
Uma tarefa AO pode aguardar uma borda em PFI 0 ou PFI 1 antes de começar. Configure a fonte AO Start Trigger como PFI 0 ou PFI 1 e selecione borda de subida ou descida.
## Fonte de alimentação de +5 V
A Figura 15 mostra o circuito da fonte de +5 V. Seus principais blocos são:
- Fonte de +5 V: alimentação regulada de 5 V.
- Proteção de +5 V: circuito contra sobretensão, sobrecorrente e curto-circuito.
A limitação da fonte é tipicamente de 200 mA. Em curto-circuito direto para o terra, o limite é reduzido para evitar dissipação excessiva de potência.
## Figura 15. Circuito da fonte de +5 V
To USB Connector = para o conector USB; +5 V Source = fonte de +5 V; +5 V Protection = proteção de +5 V; I/O Connector = conector de E/S; 16-Position Screw Terminal Plug = conector de borne de 16 posições. +5 V e D GND identificam os terminais.


## Página 24 do original

## Conexão da carga
O retorno da fonte de +5 V é o terminal D GND. A carga deve ser conectada entre +5 V e D GND. A corrente fornecida nesse terminal vem do conector USB. Para atender às especificações USB, pode-se utilizar no máximo 150 mA do terminal +5 V.
## Figura 16. Conexão da carga da fonte de +5 V
Load = carga; Optional Capacitor = capacitor opcional; 16-Position Screw Terminal Plug = conector de borne de 16 posições. +5 V e D GND mantêm os identificadores.
## Habilitação da fonte de +5 V
A fonte permanece habilitada e há tensão no terminal +5 V quando o dispositivo está ativo. A fonte fica indisponível por aproximadamente um segundo após a primeira conexão USB ou quando o dispositivo está suspenso.
## Documentação relacionada
As versões mais recentes estão em ni.com/manuals. As referências a seguir pressupõem NI-DAQmx 9.9 ou posterior e, quando aplicável, software de aplicação NI 8.5 ou posterior.
## Exemplos
Para localizar exemplos, acesse ni.com/info e informe daqmxexp.
## NI USB-6001/6002/6003
O documento Quick Start fornecido com o dispositivo descreve como instalá-lo e confirmar seu funcionamento. As especificações NI USB-6001 Specifications, NI USB-6002 Specifications e NI USB-6003 Specifications estão disponíveis em ni.com/manuals.


## Página 25 do original

## NI-DAQmx
O NI-DAQmx Readme lista dispositivos, ambientes de desenvolvimento de aplicações (ADEs) e softwares NI compatíveis com a versão instalada. Acesse Start > All Programs > National Instruments > NI-DAQmx > NI-DAQmx Readme.
A NI-DAQmx Help contém a API, conceitos e aplicações. Acesse Start > All Programs > National Instruments > NI-DAQmx > NI-DAQmx Help.
## LabVIEW
Se você é um novo usuário, acesse ni.com/gettingstarted. A LabVIEW Help, disponível em Help > LabVIEW Help, apresenta conceitos de programação. Na aba Contents, consulte:
- Start > National Instruments > NI-DAQmx > NI-DAQmx Help > Getting Started: visão geral e tutorial para medir no LabVIEW com NI-DAQ Assistant.
- VI and Function Reference > Measurement I/O VIs and Functions > DAQmx - Data Acquisition VIs and Functions: descrição dos VIs e funções NI-DAQmx.
- Property and Method Reference > NI-DAQmx Properties: referência de propriedades.
- Taking Measurements: conceitos e procedimentos para adquirir e analisar dados no LabVIEW.
## LabWindows/CVI
O capítulo Data Acquisition da LabWindows/CVI Help contém Taking an NI-DAQmx Measurement in LabWindows/CVI, com instruções para criar uma tarefa usando NI-DAQ Assistant. Acesse Help > Contents > Using LabWindows/CVI > Data Acquisition.
O capítulo NI-DAQmx Library contém visão geral da API e referência de funções. Acesse Library Reference > NI-DAQmx Library na ajuda do LabWindows/CVI.
## Measurement Studio
Ao programar um dispositivo compatível com NI-DAQmx em Visual C# ou Visual Basic .NET com Measurement Studio, você pode criar canais e tarefas abrindo NI-DAQ Assistant no NI MAX ou no Visual Studio. O Measurement Studio pode gerar o código de configuração a partir da tarefa ou canal. Consulte DAQ Assistant Help para mais informações.


## Página 26 do original

## Measurement Studio (continuação)
Para consultar a ajuda no Visual Studio, selecione Measurement Studio > NI Measurement Studio Help. Para desenvolvimento NI-DAQmx, consulte:
- Walkthrough: Creating a Measurement Studio NI-DAQmx Application: criação com Measurement Studio Application Wizard e NI-DAQ Assistant.
- NationalInstruments.DAQmx Namespace e NationalInstruments.DAQmx.ComponentModel Namespace: métodos e propriedades.
- Using the Measurement Studio NI-DAQmx .NET Library e Developing with Measurement Studio NI-DAQmx: ajuda conceitual.
- Getting Started with the Measurement Studio Class Libraries: orientação geral de programação.
Para criar uma aplicação em Visual Basic .NET ou Visual C#:
1. No Visual Studio, selecione File > New > Project para abrir New Project.
2. Em Project types, expanda Visual Basic ou Visual C#, conforme a linguagem desejada, e selecione Measurement Studio.
3. Escolha o tipo de projeto. Nessa etapa são adicionadas as tarefas NI DAQ.
## ANSI C sem software de aplicação NI
A NI-DAQmx Help apresenta a API e conceitos gerais de medição. Acesse Start > All Programs > National Instruments > NI-DAQmx > NI-DAQmx Help.
A NI-DAQmx C Reference Help descreve as funções da biblioteca para desenvolver instrumentação, aquisição e controle com dispositivos NI. Acesse Start > All Programs > National Instruments > NI-DAQmx > Text-Based Code Support > NI-DAQmx C Reference Help.
## Linguagens .NET sem software de aplicação NI
Com Microsoft .NET Framework 2.0 ou posterior, é possível criar aplicações NI-DAQmx em Visual C# e Visual Basic .NET sem Measurement Studio. É necessário Microsoft Visual Studio .NET 2005 ou posterior para instalar a documentação da API.
A documentação instalada apresenta a API, tarefas, conceitos e funções. Acesse Start > All Programs > National Instruments > NI-DAQmx > Text-Based Code Support. Para funções, consulte NationalInstruments.DAQmx Namespace e NationalInstruments.DAQmx.ComponentModel Namespace. Para conceitos, consulte Using the Measurement Studio NI-DAQmx .NET Library e Developing with Measurement Studio NI-DAQmx.
No Visual Studio 2005 ou 2008, acesse Help > Contents e selecione Measurement Studio em Filtered By. No Visual Studio 2010, acesse Help > View Help e selecione NI Measurement Studio Help em Related Links.


## Página 27 do original

## Cursos de treinamento
Se precisar de ajuda para começar a desenvolver uma aplicação NI, a empresa oferece cursos. Para inscrição ou conteúdo detalhado, consulte ni.com/training.
## Suporte técnico na Web
Para suporte adicional, acesse ni.com/support. Muitas especificações e guias NI DAQ estão em PDF. Para visualizá-los, o original exige Adobe Reader 7.0 ou posterior (PDF 1.6 ou posterior). Consulte www.adobe.com para obter Acrobat Reader. A biblioteca de manuais em ni.com/manuals contém documentação atualizada.
## Suporte e serviços em todo o mundo
O site NI reúne recursos de suporte técnico. Em ni.com/support há solução de problemas, recursos de autoatendimento para desenvolvimento de aplicações e assistência por e-mail e telefone de engenheiros de aplicações NI.
Em ni.com/services há instalação de fábrica, reparos, garantia estendida e outros serviços. Registre seu produto em ni.com/register para facilitar o suporte e receber atualizações importantes.
A Declaração de Conformidade (DoC) é a declaração do fabricante de atendimento ao Conselho das Comunidades Europeias. Esse sistema oferece proteção ao usuário quanto à compatibilidade eletromagnética e segurança. Obtenha a DoC em ni.com/certification. Se o produto oferecer calibração, o certificado pode ser obtido em ni.com/calibration.
A sede da National Instruments fica em 11500 North Mopac Expressway, Austin, Texas, 78759-3504. A empresa possui escritórios em vários países. Nos EUA, abra uma solicitação em ni.com/support ou ligue 1 866 ASK MYNI (275 6964). Fora dos EUA, consulte Worldwide Offices em ni.com/niglobal para acessar contatos, telefones, e-mails e eventos locais atualizados.
## Avisos legais
Consulte NI Trademarks and Logo Guidelines em ni.com/trademarks para informações sobre marcas da National Instruments. Outros nomes de produtos e empresas são marcas ou nomes comerciais de seus titulares. Para patentes referentes aos produtos/tecnologias NI, consulte Help > Patents no software, patents.txt na mídia ou National Instruments Patents Notice em ni.com/patents. EULAs e avisos legais de terceiros estão no readme do produto. Consulte ni.com/legal/export-compliance para a política de comércio global e códigos HTS, ECCN e outros dados de importação/exportação.
A NI NÃO OFERECE GARANTIAS EXPRESSAS OU IMPLÍCITAS QUANTO À EXATIDÃO DAS INFORMAÇÕES AQUI CONTIDAS E NÃO SE RESPONSABILIZA POR ERROS. Clientes do governo dos EUA: os dados foram desenvolvidos com recursos privados e estão sujeitos aos direitos limitados e restritos aplicáveis estabelecidos em FAR 52.227-14s, DFAR 252.227-7014 e DFAR 252.227-7015.
© 2014 National Instruments. Todos os direitos reservados. 374259A-01, maio de 2014.
