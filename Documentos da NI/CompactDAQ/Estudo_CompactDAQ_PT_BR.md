
# CompactDAQ como referência
## Estudo para um DAQ modular, aberto e de baixo custo
Seleção: cDAQ-9174 + NI-9205 + NI-9263 + NI-9401.
Preparado em 20/10/2026 para o TCC. Escopo escolhido pelo autor: estudar primeiro CompactDAQ, antes de CompactRIO.
Este caderno reúne quatro fichas em português, uma proposta de aplicação ao projeto e referências verificáveis. São resumos seletivos e análise própria, não traduções integrais nem documentação oficial NI.
## Por que esta seleção?
A configuração permite estudar separadamente a unidade central, a aquisição analógica, a geração analógica e os sinais digitais. Isso facilita relacionar cada função à arquitetura do nosso protótipo. A seleção é uma referência de estudo, não uma recomendação de compra.
## Material original arquivado
| Documento | Revisão / data | Páginas |
| Especificações cDAQ-9174 | 374045A-01 / maio de 2013 | 10 |
| Manual cDAQ-9171/9174/9178 | 372838E-01 / julho de 2016 | 105 |
| Datasheet NI-9205 | 374188B-02 / julho de 2017 | 14 |
| Datasheet NI-9263 | 373781B-02 / março de 2016 | 12 |
| Datasheet NI-9401 | 374068A-02 / dezembro de 2015 | 10 |
Os cinco PDFs vieram de servidores oficiais da NI. O arquivo fontes.json registra endereço de origem, data de acesso, número de páginas e SHA-256 para conferência das cópias.
## Como usar este caderno
1. Ler as quatro fichas para entender a função de cada componente.
2. Consultar os trechos indicados dos PDFs quando precisar de valores, condições de ensaio ou detalhes de ligação.
3. Usar a matriz da página 6 para formular requisitos e ensaios do protótipo.
4. Registrar a revisão documental junto a qualquer número transferido para o TCC.
## Controle das revisões
Os PDFs arquivados são edições históricas identificadas acima. A documentação on-line do NI-9263, revisada em maio de 2026 como 378838C-01, registra correção da tabela de exatidão [6]. Os limites de saída selecionados neste caderno também foram conferidos nessa página. A documentação atual deve ser consultada antes de dimensionamentos definitivos ou aquisição de equipamentos.

# cDAQ-9174
## A unidade central da configuração
Síntese documental [1], pp. 1-5: o chassi oferece quatro slots C Series e comunicação USB 2.0 Hi-Speed. Requer alimentação externa de 9 a 30 V; a especificação indica potência máxima de entrada de 15 W, incluindo a carga de módulos nas condições documentadas. Possui quatro contadores/temporizadores de 32 bits.
| Aspecto | Interpretação para o estudo |
| Taxa e canais analógicos | Dependem dos módulos e da configuração da tarefa. |
| Temporização | Resolução de 12,5 ns e exatidão de 50 ppm nas condições especificadas; não representam latência até o computador. |
| Buffers | Recursos de memória e regeneração variam conforme a operação. |
O manual [2], seção 4-13, documenta configuração do NI-9401 e reserva de tarefas antes de alterar a direção das linhas. A troca de direção pode conflitar com uma tarefa ativa. Isso é evidência específica de uso do módulo na família do chassi, além da compatibilidade C Series descrita pelos fabricantes dos módulos.
## O que proponho aproveitar no nosso DAQ
Separar a unidade central das placas de função específica. A central poderá cuidar de comunicação, identificação dos módulos, sincronização, diagnóstico e armazenamento temporário. Cada módulo terá uma função claramente delimitada.
A interface entre placas precisa ser especificada antes do desenho da PCI: alimentação disponível, níveis lógicos, pinagem, identificação, transporte de dados e sinais de sincronização. Um conector compatível mecanicamente não basta para garantir compatibilidade funcional.
## Decisão que o estudo deve ajudar a tomar
Comparar uma central com módulos de condicionamento ligados ao ADC do microcontrolador com módulos que possuem conversores próprios. A primeira opção pode simplificar o protótipo; a segunda permite estudar outras faixas e características de aquisição, mas acrescenta componentes e requisitos de comunicação.
## Ensaio proposto
Montar um teste de expansão: operar uma configuração mínima, acrescentar um módulo com a alimentação desligada e verificar identificação, configuração e aquisição. Registrar alterações necessárias no firmware e no supervisório. Inserção energizada fica fora da proposta inicial até haver requisito e projeto específicos.

# NI-9205
## Referência de entrada analógica
Síntese documental [3], pp. 3-6: o módulo oferece 32 entradas referenciadas ou 16 diferenciais, ADC de 16 bits e até 250 kS/s agregados em CompactDAQ. Os canais compartilham o amplificador de instrumentação com ganho programável e o ADC, por multiplexação. As faixas nominais são ±10 V, ±5 V, ±1 V e ±0,2 V.
O comum dos canais é compartilhado; há isolamento em relação ao restante do sistema, mas não isolamento individual entre canais. A variante de conector deve ser identificada ao consultar limites de isolamento.
O tempo de estabelecimento modifica o compromisso entre velocidade e erro. O datasheet informa intervalos de conversão de 4 µs e 8 µs para níveis distintos de estabelecimento.
## Cálculo ilustrativo
Distribuindo igualmente 250.000 conversões/s entre 32 canais, a média seria 7.812,5 amostras/s por canal. Este cálculo não garante a mesma taxa com qualquer exigência de estabelecimento ou configuração.
## O que proponho aproveitar no nosso DAQ
Definir quais amplitudes precisam ser medidas antes de escolher ganho fixo ou programável. Faixas menores só são úteis se o ruído, a estabilidade e a proteção do circuito forem compatíveis com o sinal.
Registrar a calibração e os fatores de conversão por configuração. No software, manter separadas a leitura bruta, a correção aplicada e a unidade de engenharia. Isso facilita reproduzir os ensaios e identificar mudanças de módulo.
## Ensaios propostos
- Aplicar níveis conhecidos ao longo da faixa e comparar com um instrumento de referência.
- Alternar dois canais com amplitudes diferentes e verificar o erro após a comutação.
- Repetir o teste com diferentes impedâncias de fonte e taxas de aquisição.
- Medir ruído com entrada adequadamente referenciada e documentar o tratamento dos dados.
## Decisão que permanece aberta
A existência de ganho programável neste módulo não obriga a incluí-lo na primeira versão do nosso protótipo. A escolha deve resultar das faixas e dos sinais da aplicação.

# NI-9263
## Referência de saída analógica
Síntese documental [4], pp. 1 e 4-6: são quatro saídas de tensão com DACs de 16 bits, faixa nominal de ±10 V e atualização simultânea de até 100 kS/s por canal. A capacidade máxima de corrente é ±1 mA por canal.
O documento distingue atualização e estabelecimento: para um degrau de fundo de escala, indica 20 µs até 1 LSB, com carga de 100 pF. Portanto, atualizar uma amostra não significa que a saída já atingiu a exatidão final.
As especificações on-line atuais [6] mantêm esses parâmetros selecionados e descrevem transientes de energização e desligamento. Seu histórico registra correção da tabela de exatidão em maio de 2026. Não usar uma tabela antiga sem identificar sua revisão.
## O que proponho aproveitar no nosso DAQ
Tratar a saída analógica como uma cadeia própria: conversão, estágio de saída, proteção, conector e carga. O requisito deve declarar tensão, corrente, faixa de carga e comportamento na inicialização.
Para HIL, estabelecer o instante em que a resposta precisa estar válida no terminal físico. Essa definição evita medir apenas o tempo de envio de um comando ou escrita em um registrador.
## Ensaios propostos
- Aplicar valores constantes e medir erro e dispersão com diferentes cargas.
- Gerar degraus e medir o tempo até a faixa de erro definida.
- Verificar o comportamento durante energização, reinicialização e perda de comunicação.
- Registrar simultaneamente o evento de comando e a tensão real de saída.
## Decisão que permanece aberta
Selecionar entre DAC interno, DAC externo ou outra solução após definir a qualidade exigida. Se a aplicação demandar acionamento de potência, especificar um estágio separado e contabilizar seu custo.

# NI-9401
## Referência de E/S digital e sinais temporizados
Síntese documental [5], pp. 1 e 4-6: são oito linhas digitais TTL de 5 V, com direção configurada em dois grupos de quatro. Ao energizar, as linhas ficam como entradas. O atraso de propagação de E/S é de até 100 ns.
| Configuração | Frequência máxima de comutação indicada no módulo |
| Oito entradas | 9 MHz |
| Oito saídas | 5 MHz, para a carga especificada de 1 mA e 50 pF |
Esses limites elétricos não são a taxa garantida de uma aplicação no computador. O chassi, a tarefa e o transporte impõem outras restrições.
A página de produto [7] diferencia os recursos programáveis com LabVIEW FPGA, disponíveis em CompactRIO, do uso em CompactDAQ. Não transferir automaticamente uma capacidade de programação FPGA para o cDAQ-9174.
## O que proponho aproveitar no nosso DAQ
Definir funções digitais em grupos claros: leitura de estados, comando de saídas, contagem de eventos, captura de tempo e geração de pulsos. Elas podem compartilhar pinos, portanto a configuração deve detectar e rejeitar conflitos.
É necessário definir se a direção será configurável por linha ou por grupo. Essa decisão afeta os circuitos de adaptação de nível, a pinagem e a interface de software.
## Ensaios propostos
- Verificar níveis elétricos com as cargas previstas.
- Medir frequência, largura de pulso e variação temporal da geração.
- Comparar contagem e captura com um gerador ou instrumento de referência.
- Testar conflitos de recursos, reinicialização e estado das saídas após desconexão.
## Decisão que permanece aberta
A presença de sinais digitais não exige implementar todos os protocolos possíveis. Devemos selecionar as funções necessárias para os experimentos e para a demonstração HIL.

# Aplicação ao nosso projeto
## Proposta de arquitetura a discutir
Computador com supervisório → interface de comunicação documentada → unidade central ARM → módulos de entrada analógica, saída analógica e E/S digital.
Esta é uma proposta para orientar requisitos, sem compromisso com o formato físico ou com o protocolo interno da NI.
## Três objetivos, três evidências
| Objetivo | Entrega verificável proposta |
| Modular | Pelo menos duas funções implementadas em módulos intercambiáveis ou expansíveis, com interfaces documentadas e demonstração de alteração de configuração. |
| Open source | Esquemáticos, PCI editável, lista de materiais, firmware, supervisório, protocolo, instruções de reprodução e licenças definidos. |
| Low cost | Custo da unidade central e de cada módulo, com orçamento datado de materiais, fabricação, montagem, conectores e software necessário. |
## Matriz inicial de decisões e validação
| Decisão | Critério de aceitação a definir | Evidência experimental |
| Entrada analógica | Faixa, taxa por canal, erro e ruído admissíveis | Varredura de tensão e teste multicanal |
| Saída analógica | Faixa, carga e tempo para atingir a resposta | Degraus e comparação com referência |
| E/S digital | Níveis, frequência e recursos simultâneos | Captura de sinais e testes de conflito |
| Comunicação | Vazão, perdas e comportamento em interrupções | Ensaio contínuo com números de sequência |
| HIL | Período da aplicação e atraso admissível do ciclo completo | Aquisição e observação externa de entrada/saída |
## Comparação econômica justa
Comparar configurações com funções equivalentes, declarando diferenças de desempenho. Somar ao sistema comercial chassi, módulos, alimentação, acessórios e licenças necessárias. No protótipo, separar custo de reprodução e esforço de desenvolvimento.
Este estudo não apresenta preços nem porcentagem de economia: ainda faltam uma configuração comercial cotada e a lista de materiais do protótipo. “Baixo custo” deverá ser convertido em uma meta numérica.
## Próxima entrega sugerida
Uma tabela de requisitos mínimos para o protótipo, seguida de duas alternativas de arquitetura e do orçamento preliminar. A demonstração HIL deve fornecer os sinais e prazos que orientam essa escolha.

# Fontes e rastreabilidade
## PDFs originais arquivados
[1] National Instruments. NI cDAQ-9174 Specifications. 374045A-01, maio de 2013. Arquivo: cDAQ_9174_Especificacoes_374045a.pdf.
https://download.ni.com/support/manuals/374045a.pdf
[2] National Instruments. NI cDAQ-9171/9174/9178 User Manual. 372838E-01, julho de 2016. Arquivo: cDAQ_9171_9174_9178_Guia_372838e.pdf. A seção 4-13 está na página 52 do arquivo PDF.
https://docs-be.ni.com/bundle/cdaq-9171-9174-9178-features/raw/resource/enus/372838e.pdf
[3] National Instruments. NI 9205 Datasheet. 374188B-02, julho de 2017. Arquivo: NI_9205_Datasheet_374188b_02.pdf.
https://download.ni.com/support/manuals/374188b_02.pdf
[4] National Instruments. NI 9263 Datasheet. 373781B-02, março de 2016. Arquivo: NI_9263_Datasheet_373781b_02.pdf.
https://download.ni.com/support/manuals/373781b_02.pdf
[5] National Instruments. NI 9401 Datasheet. 374068A-02, dezembro de 2015. Arquivo: NI_9401_Datasheet_374068a_02.pdf.
https://download.ni.com/support/manuals/374068a_02.pdf
## Fontes on-line complementares
[6] NI. NI-9263 Specifications. Página consultada com revisão 378838C-01, de maio de 2026.
https://www.ni.com/docs/en-US/bundle/ni-9263-specs/page/specs.html
[7] NI. NI-9401: página do produto. Consultada para direção em grupos e distinção de recursos FPGA.
https://www.ni.com/en/shop/hardware/digital-i-o/model-ni-9401
[8] NI. C Series Module and CompactDAQ or CompactRIO Hardware Compatibility with LabVIEW. Consulta complementar; verificar a combinação de hardware, modo e versão de software ao implementar tarefas.
https://www.ni.com/en/support/documentation/supplemental/08/c-series-module-and-compactdaq-compactrio-hardware-compatibility.html
[9] NI. cDAQ-9174 Specifications. Página de documentação on-line consultada como referência complementar.
https://www.ni.com/docs/en-US/bundle/cdaq-9174-specs/page/specs.html
Todas as fontes on-line foram acessadas em 20/10/2026. Os resumos distinguem dados do fabricante, cálculos ilustrativos e propostas para o TCC. Arquivos originais preservados sem alteração; fichas e matriz são material de estudo elaborado para o projeto.
