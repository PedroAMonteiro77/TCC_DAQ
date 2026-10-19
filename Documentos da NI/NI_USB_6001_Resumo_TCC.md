
# NI USB-6001
## Resumo técnico para o TCC
Base documental: guia NI USB-6001/6002/6003, 374259A-01, e especificações NI USB-6001, 374369A-01. Ambos são de maio de 2014 e foram fornecidos pelo autor. Este resumo caracteriza essas revisões documentais; não confirma estoque, preços ou compatibilidade atual de software.
## 1. Recursos e limites principais
| Recurso | Especificação dos PDFs | Localização |
| Entradas analógicas | 8 RSE ou 4 diferenciais; configuração mista possível | Guia, pp. 11-12 |
| Conversão de entrada | ADC de 14 bits, aproximações sucessivas | Especificações, p. 1 |
| Taxa de entrada | Até 20 kS/s agregados | Especificações, p. 1 |
| Faixa analógica de entrada | ±10 V; respeitar também limite de cada terminal em diferencial | Especificações, p. 2; guia, p. 17 |
| Qualidade da entrada | Erro absoluto típico no fundo de escala de 6 mV; máximo de 26 mV ao longo da temperatura; ruído de 0,7 mV RMS | Especificações, p. 2 |
| Saídas analógicas | 2; DAC de 14 bits; ±10 V; 5 kS/s simultâneos por canal, temporizados por hardware; ±5 mA | Especificações, p. 2 |
| Entrada/saída digital | 13 linhas, direção individual; atualizações/amostragens por software | Guia, p. 21 |
| Contador | 1 de 32 bits, crescente, bordas de subida ou descida, entrada até 5 MHz | Especificações, p. 5 |
| PFI | PFI 0 ou PFI 1 como fonte do contador ou disparo de início de AI/AO | Guia, p. 23 |
| Comunicação | USB Full Speed, 12 Mb/s | Especificações, p. 6 |
| Alimentação auxiliar | +5 V, até 150 mA para a carga | Especificações, p. 6; guia, p. 24 |
| Buffers | FIFO de AI e FIFO de AO, cada uma com 2.047 amostras | Especificações, pp. 1-2 |
## 2. Leitura correta dos números
A taxa de 20 kS/s é compartilhada entre canais. Exemplo calculado: dividindo igualmente entre oito canais, obtêm-se 2,5 kS/s por canal. Isso não representa aquisição simultânea: o guia mostra um multiplexador que encaminha um canal por vez ao ADC (p. 11).
A base de tempo de 80 MHz e resolução temporal de 12,5 ns não significam aquisição a 80 MS/s nem latência USB de 12,5 ns. São características da temporização analógica por hardware (especificações, p. 3).
Resolução nominal não é exatidão. Cálculo ideal: uma faixa total de 20 V dividida em 2^14 níveis resulta em aproximadamente 1,22 mV por código; esse passo não substitui os limites de erro e ruído da cadeia de medição.

## 3. Condicionamento, aterramento e saídas
O guia recomenda fontes com impedância menor que 1 kΩ para rápido estabelecimento durante varredura multicanal, cabos curtos de boa qualidade e taxas não maiores que as necessárias (p. 18). Isso justifica estudar buffers e condicionamento nos módulos do nosso DAQ.
Em medição diferencial, cada terminal deve permanecer entre -10 V e +10 V em relação a AI GND, além da diferença entre os terminais ficar nessa faixa (guia, p. 17). Entrada diferencial não comprova isolamento galvânico. Os documentos fornecidos não especificam uma barreira de isolamento para o USB-6001.
O guia recomenda conexão diferencial para fontes referenciadas ao terra e explica os erros por malhas de terra (pp. 15-16). As menções genéricas a cabos de 3 m nessa discussão não anulam o limite de 0,5 m indicado para atender ao desempenho EMC especificado (pp. 3, 5 e 8).
As saídas analógicas fornecem ±5 mA: são saídas de sinal, não estágios de potência. Devem ser considerados carga, proteção e eventuais drivers externos. O documento especifica um transiente de inicialização de -7 V por 10 µs antes do estado de 0 V (especificações, pp. 2-3).
Nas linhas digitais, entrada de até 5 V com dispositivo ligado não significa saída ativa de 5 V. O guia descreve acionamento ativo de 3,3 V; o coletor aberto admite pull-up externo até 5 V, respeitados os limites de corrente (guia, p. 22; especificações, pp. 4-5).
## 4. Implicações para HIL
As saídas analógicas podem operar com temporização por hardware e buffer, enquanto a E/S digital comum é temporizada por software. O contador é um recurso específico e não transforma todas as linhas digitais em E/S temporizada por hardware (guia, pp. 20-23).
Os PDFs não garantem um prazo para o ciclo computador → saída → entrada → computador. Para a nossa demonstração HIL, será necessário medir latência, jitter, perdas e cumprimento do período definido. Buffers favorecem continuidade, mas também devem ser dimensionados considerando o atraso.
O contador descrito realiza contagem crescente de bordas. Estes documentos não estabelecem suporte a geração PWM ou decodificação de encoder em quadratura. Não incluir essas capacidades na comparação do USB-6001 sem outra evidência específica.

## 5. Aplicação aos objetivos do TCC
| Objetivo | Consequência proposta para nosso projeto |
| Modular | Separar unidade central e módulos de E/S; documentar pinagem, alimentação, interfaces e limites de expansão. O USB-6001 estudado tem funções integradas e conectores removíveis; conectores removíveis não demonstram expansão modular funcional. |
| Aberto | Publicar esquemático, PCB editável, lista de materiais, firmware, supervisório, protocolo e licenças. Estes manuais documentam o uso do equipamento, mas não constituem um projeto aberto reproduzível. |
| Baixo custo | Definir configuração mínima e apurar custo de placa central, módulos, conectores, proteção, montagem e software. Os PDFs não fornecem preços; não há base aqui para afirmar uma economia percentual. |
| DAQ | Definir taxa por canal, faixa, erro admissível, integridade do fluxo, condição de fonte e proteção; validar a cadeia completa. |
| HIL introdutório | Selecionar aplicação, estabelecer período e orçamento de latência e medir o ciclo completo. |
## 6. Correções e cautelas documentais
DAC: os dois PDFs de 2014 indicam 14 bits para o USB-6001 (guia, p. 1; especificações, p. 2). Uma página comercial consultada anteriormente apresentou 16 bits. Para a comparação baseada nesses PDFs, registrar 14 bits e explicitar a revisão; confirmar a divergência com documentação atual do exemplar antes de eventual seleção ou compra.
Não atribuir NI-MCal ou NI-PGIA 2 ao USB-6001 com base em páginas gerais da NI. Os dois documentos analisados não confirmam essas tecnologias nesse modelo. O guia identifica um amplificador de instrumentação, sem caracterizá-lo como NI-PGIA 2.
O cabo chamado Hi-Speed no guia não altera a interface do equipamento: as especificações informam USB Full Speed a 12 Mb/s. Velocidade de barramento também não equivale a vazão útil de amostras.
Os manuais tratam de NI-DAQmx 9.9 e sistemas Windows da época. Caminhos de menus, suporte e requisitos foram preservados nas traduções como informação histórica, sem presumir validade atual.
## 7. O que acrescentar à revisão bibliográfica
Usar o USB-6001 como estudo de caso de DAQ multifuncional compacto, com uma tabela de recursos e limites. Relacionar aquisição multiplexada, estabelecimento, aterramento, temporização e buffers aos conceitos já discutidos.
O estudo não substitui o caso de uma plataforma modular NI. As decisões de modularidade do nosso projeto devem também ser confrontadas com uma configuração CompactDAQ definida.
## Referências locais
National Instruments. NI USB-6001/6002/6003 User Guide. Documento 374259A-01, maio de 2014. Arquivo original: 374259a.pdf.
National Instruments. NI USB-6001 Specifications. Documento 374369A-01, maio de 2014. Arquivo original: 374369a.pdf.
Análise e cálculos deste resumo: elaborados para o TCC em 19/10/2026. Propostas de projeto permanecem sujeitas à definição dos requisitos e aos ensaios.
