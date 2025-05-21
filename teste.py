import json


all_data = [
  {
    "id": 57726,
    "customFieldValues": [
      {
        "value": "Como excluir uma parcela do numerário?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "É necessário excluir a parcela de numerário dentro do processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57785,
    "customFieldValues": [
      {
        "value": "Erro ao enviar a NF",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "O cliente reportou erro no envio da Nota Fiscal de código 536 para a SEFAZ, solicitando retorno urgente. Ao investigar, foi identificado que o problema estava no preenchimento do campo \"Adição\" do Item 7 na aba Importação da nota fiscal. Este campo estava zerado, o que impede o envio da NF-e, pois valores válidos para o campo “Adição” devem estar entre 1 e 999.\n\nA equipe de suporte realizou o ajuste no sistema, inserindo o valor 1 no campo “Adição” do item em questão. Após essa correção, solicitou-se ao cliente a validação do envio novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57605,
    "customFieldValues": [
      {
        "value": "Como aparecer o contas a receber do processo expo? ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Para aparecer, precisa criar uma operação financeira, e gerar parcela no fechamento financeiro dessa despesa. \n\nApós os ajustes, o fechamento ficou de acordo. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57491,
    "customFieldValues": [
      {
        "value": "Divergência de valores no fechamento financeiro do processo/ajuste necessário por diferença cambial",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Quando há variação cambial no processo, é necessário haver uma despesa de variação cambial.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56381,
    "customFieldValues": [
      {
        "value": "Erro no campo \"Enviar arquivo\" ao inserir uma planilha",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar importar um planilha para dentro do Narwal era apresentado um erro e o arquivo ficava vermelho, em tela.",
        "customFieldId": 206843
      },
      {
        "value": "Ocorreu pois a Planilha do usuário estava com campos corrompidos. Ao criar uma planilha nova, importou normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57093,
    "customFieldValues": [
      {
        "value": "Falta de saldo ao integrar XML Nfe",
        "customFieldId": 206842
      },
      {
        "value": "Ao integrar XML foi apontado o erro de falta de saldo.",
        "customFieldId": 206843
      },
      {
        "value": "Ao analisar o XML foi identificado que a quantidade de itens presente estava diferente do que foi cadastrado no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57774,
    "customFieldValues": [
      {
        "value": "Parametrização para gerar nota com formula divergente. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro usuário",
        "customFieldId": 206843
      },
      {
        "value": "Cliente não configurou parametrização de acordo para o cenário. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57716,
    "customFieldValues": [
      {
        "value": "A DATA previsão ETA vem ao consultar o Shipstracking?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Não, apenas a data ETA.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57612,
    "customFieldValues": [
      {
        "value": "Não está puxando o autocomplete, está sendo verificado.",
        "customFieldId": 206842
      },
      {
        "value": "IIS estava com erro de memória",
        "customFieldId": 206843
      },
      {
        "value": "IIS estava com erro de memória",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57702,
    "customFieldValues": [
      {
        "value": "Botão de integrar XML da DI desabilitado.",
        "customFieldId": 206842
      },
      {
        "value": "dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Quando o botão está desabilitado é porque o processo está com status \"fechado\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57733,
    "customFieldValues": [
      {
        "value": "IPI não estava sendo preenchido na nota fiscal, e o valor do IPI estava divergente. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário",
        "customFieldId": 206843
      },
      {
        "value": "Em analise a parametrização foi identificado que as exceções fiscais cadastrada, o destino da mercadoria estava informado como consumo, porém dentro do processo estava como Não informado. \n\nApós ajuste, cliente seguiu com a nota correta. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57108,
    "customFieldValues": [
      {
        "value": "Cliente solicitando manual das rotinas narwal?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Cliente solicitando manual das rotinas Narwal, e o link do ambiente hml ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54681,
    "customFieldValues": [
      {
        "value": "Título de pagamento da invoice está sendo criado como Previsto.",
        "customFieldId": 206842
      },
      {
        "value": "Ao criar um título de câmbio, o mesmo é criado como Previsão.",
        "customFieldId": 206843
      },
      {
        "value": "Por padrão, o titulo de câmbio quando criado, automaticamente deve cair na operação financeira de previsão, pois o material não tem nacionalização, ou seja, ainda está em \"transito\". Para efetivar o título é necessário realizar a baixa via contrato de câmbio. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57713,
    "customFieldValues": [
      {
        "value": "não sendo possível ajustar data de atracação após encerramento do processo",
        "customFieldId": 206842
      },
      {
        "value": "não sendo possível ajustar data de atracação após encerramento do processo",
        "customFieldId": 206843
      },
      {
        "value": "por padrão, não é possível alterar informações do processo após ele ser encerrado",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57354,
    "customFieldValues": [
      {
        "value": "Como proceder com erro de permissão ao registrar DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "É necessário acessar a rotina \"Usuário\" e vincular o usuário a um representante legal.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55070,
    "customFieldValues": [
      {
        "value": "Como corrigir avisos de follow de vencimento de documentos do cliente?",
        "customFieldId": 206842
      },
      {
        "value": "O follow que estava sendo disparado era referente aos documentos no ambiente de homologação.",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso basta ir em Contrato comissão tipo documento >  editar e retirar o email em cópia!\ndessa forma não irá ter excesso de emails vencidos ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57690,
    "customFieldValues": [
      {
        "value": "Resolvido",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57694,
    "customFieldValues": [
      {
        "value": "Cancelamento de processo sem querer.",
        "customFieldId": 206842
      },
      {
        "value": "Usuário cancelou o processo(expo) sem querer, e já tinha nota emitida.",
        "customFieldId": 206843
      },
      {
        "value": "Reaberto o processo via banco, visto que já tinha NF para o processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57485,
    "customFieldValues": [
      {
        "value": "Erro ao tentar integrar XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Você não possui acesso ao menu selecionado: Importacao/NPI/IntegrarXmlDiProcesso.\n\nEsse erro ocorre pois é necessário da permissão no grupo de usuário.",
        "customFieldId": 206843
      },
      {
        "value": "Adicionado a permissão no cadastro de grupo usuário",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56143,
    "customFieldValues": [
      {
        "value": "Como alterar o \"pago por\" dos impostos?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Na aba \"di/da\" do processo, é possível alterar o \"pago por\" dos impostos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56424,
    "customFieldValues": [
      {
        "value": "Demora no envio de follows.",
        "customFieldId": 206842
      },
      {
        "value": "O cliente estava cadastrado com o SMTP narwal, e a caixa de email estava praticamente cheia.",
        "customFieldId": 206843
      },
      {
        "value": "Solicitado ao time de infra para liberar a caixa de email. \n\nCliente seguiu com alteração para o SMTP deles, havia sido alterado para o SMTP narwal pois estavam com problema no SMTP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57496,
    "customFieldValues": [
      {
        "value": "Novo cenário de nota e a parametrização estava divergente. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro  do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Para que a nota saísse de acordo, o calculo dentro da rotina filial ele deve estar como Valor total da nota de entrada menos o IPI, estava apenas como base de ICMS com isso não estava deduzindo o IPI da entrada.\n\n \nTambém foi preciso ajustar as formulas dentro da parametrização, como valor total dos produtos e a formula da base de ICMS. \n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57642,
    "customFieldValues": [
      {
        "value": "Campo \"transit time\" bloqueado para edição manual",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando editar o campo transit time de forma manual, porém, o campo não fica habilitado para edição.",
        "customFieldId": 206843
      },
      {
        "value": "O campo Transit Time, dentro do processo, não pode ser alterado manualmente. Isso ocorre porque, por padrão, ele é calculado automaticamente pelo sistema, conforme definido no código-fonte do Narwal.\n\n\n\nEsse cálculo é feito com base nas seguintes datas:\n\n\n\nETD (Estimated Time of Departure): Data estimada de partida.\n\nETA (Estimated Time of Arrival): Data estimada de chegada.\n\nPortanto, o Transit Time representa a diferença entre a data de chegada (ETA) e a data de partida (ETD).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57087,
    "customFieldValues": [
      {
        "value": "Consulta shipstracking",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao consultar o navio",
        "customFieldId": 206843
      },
      {
        "value": "Cliente estava informando o BL no numero do booking, após colocar os números correto o mesmo realizou a consulta.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56915,
    "customFieldValues": [
      {
        "value": "Erro ao gerar LI substitutiva.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: O(s) campo(s) [Fabricante] descaracteriza(m) a LI original em caso de substituição e não pode(m) ser alterado(s).\n\nEsse erro ocorre pois a LI não possui vinculo com o Fabricante, dessa forma não é possível gerar a LI substitutiva.",
        "customFieldId": 206843
      },
      {
        "value": "Solicitado ao cliente que fosse cancelado a LI e gerada novamente, visto que o Fabricante foi removido na edição da LI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56493,
    "customFieldValues": [
      {
        "value": "Inserção de pedido de compra atualiza se o pedido ja existe",
        "customFieldId": 206842
      },
      {
        "value": "O parceiro questionou se ao integrar uma planilha de pedido de compra com um pedido que ja existe se atualizaria o pedido do Narwal",
        "customFieldId": 206843
      },
      {
        "value": "o Modelo de Inserção de Pedido de compra, não atualiza os pedidos ja existentes, apenas cria novos pedidos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57116,
    "customFieldValues": [
      {
        "value": "Cliente relatando que valor do ICMS não estava puxando na DI. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro usuário",
        "customFieldId": 206843
      },
      {
        "value": "O valor da AFRMM ele no processo já está como base de ICMS, de certa forma está compondo a base de ICMS. Outro ponto dentro do processo na aba de entrega precisa ser informado as parametrizações de entrada e saída. \n\n\n\nOutro ponto dentro do processo possui uma exceção fiscal para os produtos como o ICMS SC - EXONERADO, se ele está exonerado ele não vai puxar o ICMS no processo. \n\nDentro da rotina de declaração de Importação, o valor da AFRMM ele fica nos dados adicionais da DI, dentro do Narwal na rotina de Declaração importação a aba de básica, consegue conferir a prévia das informações complementares. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54088,
    "customFieldValues": [
      {
        "value": "Por que está gerando títulos de NFSe?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Sempre que há uma operação financeira cadastrada, um título é gerado. Foi desabilitada a operação financeira.\nSobre a exclusão desses títulos, teve que ser realizado um ajuste via banco para liberar o estorno da parcela.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55703,
    "customFieldValues": [
      {
        "value": "Como inserir a taxa ce mercante no processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Você deve lançar a despesa \"CE Mercante\" na aba \"Despesas\" do processo.\nApós inserir esta despesa, ao gerar a DI, a mesma será migrada automaticamente para a aba \"acréscimos\" da DI.\n\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57596,
    "customFieldValues": [
      {
        "value": "Aba de numerários não estava aparecendo no Narwal. ",
        "customFieldId": 206842
      },
      {
        "value": "Usuário colocou como oculta  a aba de numerários dentro do processo impo. ",
        "customFieldId": 206843
      },
      {
        "value": "Acessei o processo e fleguei para voltar a aparecer a aba de numerários. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56901,
    "customFieldValues": [
      {
        "value": "Código de verificação.",
        "customFieldId": 206842
      },
      {
        "value": "dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido com KB 53394.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56906,
    "customFieldValues": [
      {
        "value": "Erro ao acessar ambiente de homologação.",
        "customFieldId": 206842
      },
      {
        "value": "Credenciais de SMTP incorretas.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido com KB 55984.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56064,
    "customFieldValues": [
      {
        "value": "Por que está sendo possível utilizar o saldo inativado?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Problema não resolvido, cliente não deu andamento no chamado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55951,
    "customFieldValues": [
      {
        "value": "Como ajustar as informações complementares da DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina \"Informação complementar Siscomex\", inserindo as chaves { e as respectivas TAGs.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57212,
    "customFieldValues": [
      {
        "value": "Cliente com erro em nota fiscal. ",
        "customFieldId": 206842
      },
      {
        "value": "Parametrização",
        "customFieldId": 206843
      },
      {
        "value": "Foi ajustado a parametrização para a emissão da nota. \n\nEm analise verificamos que os impostos de PIS e cofins não tinham incidência e na parametrização estava utilizando um CST com tributação. \n\nInformando parametrização divergente na nota fiscal. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57536,
    "customFieldValues": [
      {
        "value": "Erro ao tentar registrar DI.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Unable to connect to the remote server.\n\nTivemos problemas de comunicação/roteamento para os IPs da rede da SERPRO, lá na EQUINIX, e por isso os serviços do siscomex ficaram indisponiveis momentaneamente.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido pelo time de infra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57520,
    "customFieldValues": [
      {
        "value": "Erro ao tentar registrar DI.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Unable to connect to the remote server.\n\nTivemos problemas de comunicação/roteamento para os IPs da rede da SERPRO, lá na EQUINIX, e por isso os serviços do siscomex ficaram indisponiveis momentaneamente.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido pelo time de infra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57338,
    "customFieldValues": [
      {
        "value": "Erro ao realizar consulta Shipstracking",
        "customFieldId": 206842
      },
      {
        "value": "Mensagem de erro ao realizar consulta",
        "customFieldId": 206843
      },
      {
        "value": "Foi verificado que o erro estava acontecendo devido ao - no numero do container, apos retirar o -, a consulta funcionou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55549,
    "customFieldValues": [
      {
        "value": "Títulos previstos de POs duplicados",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Havia um pedido com o mesmo número, porém ele foi cancelado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57126,
    "customFieldValues": [
      {
        "value": "Nota fiscal não gerando, pois possuía muito item no processo. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Foi orientado como fazer a divisão das notas, quando o processo possui muitos itens.  ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57521,
    "customFieldValues": [
      {
        "value": "Erro ao tentar registrar DI.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Unable to connect to the remote server.\n\nTivemos problemas de comunicação/roteamento para os IPs da rede da SERPRO, lá na EQUINIX, e por isso os serviços do siscomex ficaram indisponiveis momentaneamente.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido pelo time de infra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57525,
    "customFieldValues": [
      {
        "value": "Unable to connect to the remote server",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando registrar uma DI no narwal, porém é retornada a mensagem \"Unable to connect to the remote server\".",
        "customFieldId": 206843
      },
      {
        "value": "Claro! Aqui está uma versão mais técnica e resumida do texto:\n\nEsse comportamento pode ter duas causas:\n\n1. Instabilidade no próprio Siscomex — nesse caso, é necessário apenas aguardar a normalização.\n\n2. Problemas na infraestrutura da Narwal — se confirmado, abra um chamado via SDK solicitando análise do time de infraestrutura.\n\nAntes de acionar o suporte, verifique se o problema não é decorrente de instabilidade no Siscomex.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57538,
    "customFieldValues": [
      {
        "value": "Usuário inexistente no sistema",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava colocando o usuário de login com acento.",
        "customFieldId": 206843
      },
      {
        "value": "Após redefinir a senha do usuário e colocar o login de forma correta o mesmo se estabeleceu conexão com o sistema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57515,
    "customFieldValues": [
      {
        "value": "Erro ao tentar registrar LI.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Unable to connect to the remote server.\n\nTivemos problemas de comunicação/roteamento para os IPs da rede da SERPRO, lá na EQUINIX, e por isso os serviços do siscomex ficaram indisponiveis momentaneamente.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido pelo time de infra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56984,
    "customFieldValues": [
      {
        "value": "Relatório previsão numerário com \"valor total\" zerado/nulo",
        "customFieldId": 206842
      },
      {
        "value": "Tabela do banco MoedaTaxa sem valores atualizados para o dia.",
        "customFieldId": 206843
      },
      {
        "value": "Caso a ferramenta de ajuste das moedas não tenha rodado, precisa executar o insert nas modas. Presente no atendimento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57426,
    "customFieldValues": [
      {
        "value": "Campos sumiram da Nota fiscal.",
        "customFieldId": 206842
      },
      {
        "value": "Um usuário com permissão de ocultar campo acabou ocultando sem querer.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido com KB 55768.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57331,
    "customFieldValues": [
      {
        "value": "Título antecipado (Contrato de cambio) não aparece no contas a pagar.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O título estava aparecendo de acordo, o cliente não estava procurando pelo título com o Status \"Baixado\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57488,
    "customFieldValues": [
      {
        "value": "Contrato de cambio não aparece para compensação na invoice",
        "customFieldId": 206842
      },
      {
        "value": "Foi criado um contrato de cambio do tipo antecipado, porém ele não aparece para compensar a invoice no botão \"adiantamento manual\"",
        "customFieldId": 206843
      },
      {
        "value": "Confirmar se o título do adiantamento está como baixado, e se não estiver, alterar para baixado",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57257,
    "customFieldValues": [
      {
        "value": "NF não está integrando no SAP.",
        "customFieldId": 206842
      },
      {
        "value": "Erro ocorreu pois o processo não possui vinculo com o pedido de compra, dessa forma a NF não possui o vinculo também.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente seguiu com o registro manualmente no SAP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57182,
    "customFieldValues": [
      {
        "value": "Como um pedido de compra é cancelado?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Quando o saldo do pedido é zerado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56203,
    "customFieldValues": [
      {
        "value": "Mnesagem retorno do narwal após integrar xml no processo expo? ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente tentando entregar xml de nota em processo expo, com o retorno de que possuía uma chave de produto criada. ",
        "customFieldId": 206843
      },
      {
        "value": "Em analise o cliente estava tentando integrar o XML para criar novos produtos, porém já possuía uma chave de produto criada, deveria ser preenchido para associar a produtos existentes. \n\nTeste feito em ambiente de HML, nota integrada com sucesso. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57434,
    "customFieldValues": [
      {
        "value": "Por que não consigo clicar no botão \"Integrar XML DI\"?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O processo precisa estar aberto para integrar o XML.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57441,
    "customFieldValues": [
      {
        "value": "Como cancelar processo com parcela d enumerário?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A parcela deve ser excluída.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57437,
    "customFieldValues": [
      {
        "value": "Erro 503 ao tentar acessar ambiente.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A principio se tratou de uma instabilidade momentanea, pois conseguimos acessar normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57410,
    "customFieldValues": [
      {
        "value": "Erro ao tentar enviar NF para Sefaz.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Array may not be empty or null. Parameter name: rawData\n\nEsse erro foi retornado pois o certificado digital não estava anexado no cadastro da filial.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário anexar o certificado digital no cadastro da filial, após informado o certificado foi possível autorizar a NF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57334,
    "customFieldValues": [
      {
        "value": "Duimp permanece com o diagnóstico \"Em processamento\"",
        "customFieldId": 206842
      },
      {
        "value": "Instabilidade com o Portal Único.",
        "customFieldId": 206843
      },
      {
        "value": "Seguiu com o registro de uma DI. Foi passado para ele que isso aconteceu por conta de instabilidade.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55570,
    "customFieldValues": [
      {
        "value": "Feito ajuste no processo expo após envio ao ERP e não estou conseguindo enviar novamente",
        "customFieldId": 206842
      },
      {
        "value": "Feito ajuste no processo após envio ao ERP e não estou conseguindo enviar novamente (botão enviar erp no menu de ação do processo (expo))",
        "customFieldId": 206843
      },
      {
        "value": "Necessário remover o valor do campo AtualizadoAllog via banco",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56854,
    "customFieldValues": [
      {
        "value": "Não está trazendo as despesas para gerar a parcela de numerário.",
        "customFieldId": 206842
      },
      {
        "value": "Ao acessar a rotina de parcela do numerário, as despesas não aparecem.",
        "customFieldId": 206843
      },
      {
        "value": "Deve-se clicar no botão \"Gerar nova parcela\", e assim seguir com a emissão da parcela do numerário.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57113,
    "customFieldValues": [
      {
        "value": "Erro ao receber email do cliente",
        "customFieldId": 206842
      },
      {
        "value": "Quando recebemos email do cliente, o email era colocado em quarentena ou enviado direto para o lixo eletrônico",
        "customFieldId": 206843
      },
      {
        "value": "Foi verificado que o AntiSpam Narwal estava fazendo isso, então foi colocado o dominio do cliente como remetente confiavel",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57292,
    "customFieldValues": [
      {
        "value": "Erro ao integrar XML da DI.",
        "customFieldId": 206842
      },
      {
        "value": "Erro retornado: Erro no documento XML (2, 2).\n\nQuando retornado esse erro, é por conta que o documento não está no formato correto para integrar no Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário seguir com o preenchimento das informações manualmente no Narwal, pois o documento gerado pelo siscomex não estava de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56920,
    "customFieldValues": [
      {
        "value": "preço dos itens alterados na invoice e não ajustado no pedido",
        "customFieldId": 206842
      },
      {
        "value": "Foi alterado (para mais) o preço dos itens na invoice vinculada a um pedido, porém não foi ajustado esse valor no pedido. O que gerou um problema ao gerar o contrato de câmbio",
        "customFieldId": 206843
      },
      {
        "value": "Excluir a invoice, ajustar o preço no pedido e gerar a invoice novamente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57208,
    "customFieldValues": [
      {
        "value": "Qual NCM é considerado para fazer a DUIMP?",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Tanto o NCM vinculado ao catálogo de produto, quanto o NCM preenchido no item do processo devem estar equivalentes, uma vez que não estiverem, ocasionará em erro ao realizar a sincronização na DUIMP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56928,
    "customFieldValues": [
      {
        "value": "Cotação de frete aprovada e reprovada para o mesmo armador.",
        "customFieldId": 206842
      },
      {
        "value": "Ao aprovar a cotaçaõ de frete, o armador está recebendo os e-mails de cotação aprovada e reprovada juntamente.",
        "customFieldId": 206843
      },
      {
        "value": "Validado que foi feito a tentativa de aprovar 2 cotações, fazendo com que o e-mail seja disparado 2x.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57342,
    "customFieldValues": [
      {
        "value": "Título previsto de Câmbio baixado foi enviado ao Sênior, porém não consigo visualizá-lo no ERP",
        "customFieldId": 206842
      },
      {
        "value": "Título de câmbio de previsão foi baixado e enviado ao Narwal, porém não consigo encontrá-lo  no Sênior",
        "customFieldId": 206843
      },
      {
        "value": "O Sênior não recebe títulos de previsão baixados. \n\nPara que a baixa seja aceita corretamente, é necessário que o título esteja efetivado.\n\nA efetivação dos títulos de câmbio pode ser feita de duas formas:\n\nPela criação da nota fiscal no Narwal;\n\nOu pela criação de um contrato de câmbio do tipo antecipado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56141,
    "customFieldValues": [
      {
        "value": "Erro ao tentar integrar pedidos de compra via planilha",
        "customFieldId": 206842
      },
      {
        "value": "Cliente tenta integrar uma planilha no Narwal para criação de pedido de compra e recebe um erro dizendo: \"Operação abortada, The INSERT statement conflicted with the FOREIGN KEY constraint 'FK_dbo.PedidoCompraItem_dbo.Produto_ProdutoId'. The conflict occurred in database[Nome da Base], table 'dbo.Produto', column 'ProdutoId'. The statement has been terminated.\"",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro ocorre porque não há um Produto cadastrado com a chave informada na planilha.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54574,
    "customFieldValues": [
      {
        "value": "Como resolver o erro de permissão ao registrar uma DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O usuário dele deve ter vínculo com o representante legal no cadastro de usuário.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57330,
    "customFieldValues": [
      {
        "value": "Erro ao ativar o catalogo de produto",
        "customFieldId": 206842
      },
      {
        "value": "Erro: \"O valor informado no campo NCM é invalido\"",
        "customFieldId": 206843
      },
      {
        "value": "Foi feito a troca do NCM do Produto, o mesmo estava gerando o erro pois já tinha um catalogo criado com o NCM antigo, ao desativar o catalogo antigo foi possível ativar o novo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57315,
    "customFieldValues": [
      {
        "value": "Botão \"Adicionar\" na aba transporte do processo sumiu",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando incluir um container em um processo, porém, o botão \"Adicionar\" na aba \"Transporte\" sumiu.",
        "customFieldId": 206843
      },
      {
        "value": "O botão ou campo sumiu porque, no sistema Narwal, existe um parâmetro que permite ocultar esses elementos. Costuma ser ativada acidentalmente durante o uso. No caso dos botões, a opção de ocultar/exibir fica localizada na bolinha azul acima do botão; para os campos, o ícone está ao lado, representado por um asterisco (*).\n\nSolução:\nOrientar o cliente a solicitar que o administrador ou key user reative a visualização do botão ou campo através via tela do narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56909,
    "customFieldValues": [
      {
        "value": "Dados de cadeira ou binários seriam truncados. A instrução foi finalizada.",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro ocorre quando a planilha utilizada na integração possui dados que excedem o limite de caracteres permitido em determinadas colunas no banco de dados. Isso pode incluir, por exemplo, colunas com textos muito extensos ou caracteres não permitidos.",
        "customFieldId": 206843
      },
      {
        "value": "No caso analisado, o erro foi causado pelo excesso de caracteres inseridos nas seguintes colunas da planilha:\n\nPRODUTO_DESCRICAO, PRODUTO_DESCRICAO_COMPLETA, e PRODUTO_DESCRICAO_COMPLETADI.\n\nCada uma dessas colunas continha linhas com mais de 12 mil caracteres, ultrapassando o limite definido no banco de dados.\n\nPara resolver o problema, recomenda-se revisar e ajustar o conteúdo dessas colunas para que estejam dentro do limite permitido (verificar o limite exato no banco, geralmente em torno de 255 a 4000 caracteres, dependendo do tipo de dado definido).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57255,
    "customFieldValues": [
      {
        "value": "Houve um problema ao integrar Xml Nota Fiscal Serviço",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar um XML de nota fiscal de serviço, é exibida a mensagem: \"Houve um problema ao integrar Xml Nota Fiscal Serviço\". Como posso resolver esse erro?",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro costuma ocorrer quando o XML contém caracteres inválidos. O mais comum é o caractere & (E comercial) presente entre as tags <Discriminacao> e </Discriminacao>.\n\nPara corrigir:\n\n1. Abra o arquivo XML.\n\n2. Localize o caractere & dentro da tag <Discriminacao>.\n\n3. Remova o caractere ou substitua por uma forma válida (por exemplo, &amp;, se necessário).\n\n4. Salve o arquivo e tente realizar a integração novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57278,
    "customFieldValues": [
      {
        "value": "Instabilidade base Narwal.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Aberto chamado com o time de infra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57258,
    "customFieldValues": [
      {
        "value": "Instabilidade base narwal.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Aberto chamado com o time de infra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57319,
    "customFieldValues": [
      {
        "value": "Erro de SMTP ao tentar acessar.",
        "customFieldId": 206842
      },
      {
        "value": "Foi identificado que a senha do SMTP da Narwal havia expirado.",
        "customFieldId": 206843
      },
      {
        "value": "Solicitado a infra que fosse realizado a alteração e logo após voltado para a senha anterior, para assim não ser necessário alterar em todos os clientes.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57323,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57273,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57275,
    "customFieldValues": [
      {
        "value": "Integração de XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não sabe como Integrar XML da DI (Importa).",
        "customFieldId": 206843
      },
      {
        "value": "Processo > Menu de Ação > Integrar DI/DUIMP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57287,
    "customFieldValues": [
      {
        "value": "Power BI Inicial não aparece",
        "customFieldId": 206842
      },
      {
        "value": "O BI do painel principal não aparece na tela inicial.",
        "customFieldId": 206843
      },
      {
        "value": "Link que estava cadastrado tinha expirado, necessário por um novo, após colocar o novo o mesmo teve sua visualização.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57186,
    "customFieldValues": [
      {
        "value": "Nota fiscal com base de calculo diferente da planilha do cliente. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Para ajuste foi informado a formula na parametrização, após disse foi parametrizado e calculado a nota fiscal. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57068,
    "customFieldValues": [
      {
        "value": "Código: BHISS0003 Descrição: Essa prefeitura não suporta emissão de Nota Fiscal com tomador com end",
        "customFieldId": 206842
      },
      {
        "value": "Dados de Endereço do cliente",
        "customFieldId": 206843
      },
      {
        "value": "Acessar o cadastro do cliente e alterar para o endereço conforme consta no portal da prefeitura.\nO endereço poderá ser validado também no portal do Sintegra e no cadastro de CNPJ(Receita Federal).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56505,
    "customFieldValues": [
      {
        "value": "Campo local de embarque sumindo ao enviar DI para Analise.",
        "customFieldId": 206842
      },
      {
        "value": "Não identificado, pois o erro aconteceu apenas com um processo, realizei o envio da DI para analise e o erro não ocorreu.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente seguirá com os processos, caso volte a ocorrer entrará em contato, visto que não está mais ocorrendo o problema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55694,
    "customFieldValues": [
      {
        "value": "Duplicação de itens na integração da due",
        "customFieldId": 206842
      },
      {
        "value": "Ambiente HML Handle, cliente tem apenas um cenário e nos disponibilizou apenas um XML de NF que anexei aqui no chamado\n\n\n\nAo fazer o input manual do XML da NF no Processo(expo), salvo e confiro na aba produtos dentro do processo que foi carregado da forma correta. Porém quando consulto a rotina Registro DU-E, na aba Produtos, o narwal está duplicando, ou seja, fico com duas linhas de itens e seus valores e quantidades em dobro.\n\n\n\nInicialmente a base estava na versão v2025.R2.0.0 onde esse problema foi percebido. Atualizei a base para v2025.R2.1.1 e o problema continuou.\n\nFiz então um teste em uma outra base que estava na versão V2025.R1.2.9 e não apresentou o erro.\n\nEntão fiz uma regressão de versão e deixei a base da Handle também na v2025.R1.2.9.\n\n\n\nFiz um novo teste e o problema permaneceu. ou seja, esse é um problema que não está relacionado com versão e nem está acontecendo em outros ambientes.\n\n\n\nVerifiquei algumas variáveis de ambiente, mas não achei nenhuma que pudesse ter relação com isso.",
        "customFieldId": 206843
      },
      {
        "value": "A questão da duplicação da linha ao integrar o XML era devido ao cadastro duplicado da NCM.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57207,
    "customFieldValues": [
      {
        "value": "Envio de nota para o SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "Codigo Municipio do Destinatario: difere da UF do Destinatario ",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro do cliente estava com a UF divergente da correta, puxando outro estado, após colocar a correta foi possivel o envio. Ilustração com imagens no chamado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57178,
    "customFieldValues": [
      {
        "value": "Menu de rotinas sumiu",
        "customFieldId": 206842
      },
      {
        "value": "O menu de rotinas do meu usuário sumiu. O que devo fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Esse cenário pode ter duas causas específicas:\n\n1. Cache do navegador: Faça um teste acessando o sistema em uma guia anônima. Se o menu de rotinas aparecer normalmente, será necessário limpar o cache do navegador.\n\n2. Zoom do navegador: Verifique se o zoom está ajustado em 100%. Valores acima ou abaixo disso podem afetar a exibição correta do menu.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56989,
    "customFieldValues": [
      {
        "value": "Despesas duplicadas numerário e sem conseguir excluir. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Em analise verificamos que foi calculado duas vezes o pré calculo. \n\nReferente as despesas que não estavam conseguindo excluir no numerário, já possui uma parcela parcialmente baixada no contas a pagar, por esse motivo não estavam conseguindo excluir. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57150,
    "customFieldValues": [
      {
        "value": "mesmo caso do ticket 57162",
        "customFieldId": 206842
      },
      {
        "value": ".",
        "customFieldId": 206843
      },
      {
        "value": ".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57020,
    "customFieldValues": [
      {
        "value": "Por que os impostos não batem?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A taxa moeda estava errada, após alterar, ficou de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57164,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF para o ERP.",
        "customFieldId": 206842
      },
      {
        "value": "An error occurred while parsing EntityName. Line 21, position 46.\n\nEsse erro ocorre por conta de algum caracter especial, seja no nome do fabricante, numero do pedido, etc.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário remover o \"&\" do nome do Fornecedor, após renomear basta cancelar a NF e gera-la novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57162,
    "customFieldValues": [
      {
        "value": "unable to connect to the remote server",
        "customFieldId": 206842
      },
      {
        "value": "erro ao tentar atualizar o ambiente.",
        "customFieldId": 206843
      },
      {
        "value": "Serviço do atualizador não instalado",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53384,
    "customFieldValues": [
      {
        "value": "Despesas não migra para o fechamento",
        "customFieldId": 206842
      },
      {
        "value": "Estou lançando os honorários e serviços direto no cadastro do cliente -> aba dados gerais, porém não estão indo para o fechamento do processo.",
        "customFieldId": 206843
      },
      {
        "value": "a variável NWL_HABILITAPROCESSAMENTOCONTRATOCOMISSAO estava ativa, o que impede que o valor de honorários seja refletido na aba principal do contrato de comissão durante o fechamento financeiro, pois o sistema considera os serviços registrados em vez da página principal. Após desativa-la, foi possível migrar as despesas para o fechamento do processo através da aba dados gerais do cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56162,
    "customFieldValues": [
      {
        "value": "OC Senior não integrando",
        "customFieldId": 206842
      },
      {
        "value": "OC do cliente integrado com ERP Senior não estava integrando. Após analise do log do integrador foi identificada a seguinte mensagem de erro: \"Informe a descrição da forma de pagamento para: 112\". Essa mensagem significa que não existe nenhuma forma de pagamento cadastrada no Narwal com a chave 112",
        "customFieldId": 206843
      },
      {
        "value": "Informar no campo chave o valor 112 para uma forma de pagamento já existente no Narwal ou criar uma nova forma de pagamento com a chave 112",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56868,
    "customFieldValues": [
      {
        "value": "Erro de validação de campos: Informe a coluna Peso liquido unitário da grade de itens do processo.",
        "customFieldId": 206842
      },
      {
        "value": "Erro é retornado pois o peso liquido unitario não estava informado.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário informar o peso liquido unitario dos itens.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54847,
    "customFieldValues": [
      {
        "value": "Taxa da moeda não atualizou automaticamente",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada.",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56206,
    "customFieldValues": [
      {
        "value": "Ao informar os containers, a consulta ships tracking traz as informações para o processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Sim, ao consultar tanto pelo booking quanto pelos containers o ships tracking atualiza as informações no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56809,
    "customFieldValues": [
      {
        "value": "Cliente não sabendo utilizar Narwal, para configuração de parametrização e despesas do processo. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Ajustado a parametrização conforme o cenário do cliente. \n\nInformamos também a despesa de AFRMM que não estava informada no processo e na nota fiscal, e o cliente estava configurando como despesa acessória, sendo que deveria ser como Base de ICMS. \n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57081,
    "customFieldValues": [
      {
        "value": "Taxa da moeda não atualiza mesmo rodando o job manual",
        "customFieldId": 206842
      },
      {
        "value": "Entre os dias 29/04 e 07/05, as taxas de câmbio deixaram de ser atualizadas automaticamente no sistema.\n\nCausa:\nA falha ocorreu porque o processo automatizado, que anteriormente utilizava um arquivo .txt para atualização das bases no Narwal via job agendado, deixou de funcionar corretamente.\n\nDesde então, essa rotina foi substituída por um novo software exclusivo, que passou a ser responsável pela atualização automática das taxas, eliminando a dependência do arquivo .txt.",
        "customFieldId": 206843
      },
      {
        "value": "O problema já foi corrigido. Para normalizar os dados, basta executar novamente o job de atualização.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56795,
    "customFieldValues": [
      {
        "value": "Cliente não sabendo utilizar Narwal, para configuração de parametrização e despesas do processo. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Ajustado a parametrização conforme o cenário do cliente. \n\nInformamos também a despesa de AFRMM que não estava informada no processo e na nota fiscal, e o cliente estava configurando como despesa acessória, sendo que deveria ser como Base de ICMS. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56006,
    "customFieldValues": [
      {
        "value": "Por que a logo em relatórios está saindo diferente do que está no cadastro da empresa?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Alguns relatórios buscam a logo do parâmetros do sistema",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56336,
    "customFieldValues": [
      {
        "value": "Arquivo modelo Catalogo de Produtos",
        "customFieldId": 206842
      },
      {
        "value": "Filtro de produtos ativados/desativados",
        "customFieldId": 206843
      },
      {
        "value": "Atualmente o Narwal não tem esse filtro, assim trazendo todos os produtos da base ao baixar o arquivo modelo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57065,
    "customFieldValues": [
      {
        "value": "De onde puxa a informação do peso bruto na NF, aba transporte?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Está sendo informado este valor na aba produtos do processo, coluna \"Peso bruto\".\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55059,
    "customFieldValues": [
      {
        "value": "Duplicidade de título.",
        "customFieldId": 206842
      },
      {
        "value": "Fluxo seguido incorretamente pelo cliente. Como o cliente realiza adiantamento pelo contrato de cambio, é necessário que os adiantamentos estejam devidamente criados antes de criar a invoice.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário cancelar a invoice, e ter ambos adiantamentos de cambio realizados para assim gerar a invoice com as devidas parcelas baixadas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56941,
    "customFieldValues": [
      {
        "value": "Como fazer com que os impostos não entrem no fechamento financeiro?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "os impostos que forem pagos pelo cliente não entram no fechamento financeiro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57005,
    "customFieldValues": [
      {
        "value": "Como reabrir processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Pode reabrir o processo através do menu de ação> reabrir processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56470,
    "customFieldValues": [
      {
        "value": "Realizar sincronização de catálogos existentes no Narwal",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Rotina: Importação -> Catálogo de Produtos -> Gestão de catálogo.\n\nAo clicar no botão \"Sincronizar PUCOMEX\", precisamos informar um Importador e temos a possibilidade de sincronizar de duas formas: \"Atualizar existentes\" ou \"Associar produtos automaticamente\".\n\n\"Atualizar existentes\" há a possibilidade de criar catálogos que ainda não estão no Narwal e atualizar catálogos já criados.\n\n\"Associar produtos automaticamente\" irá sincronizar todos os catálogos com base na raiz de CNPJ do Importador informado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57029,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56997,
    "customFieldValues": [
      {
        "value": "Follow-up não está sendo enviado.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Quando a flag \"executa na criação\" está preenchida, o follow é disparado somente na criação do processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56960,
    "customFieldValues": [
      {
        "value": "Valor do II estava divergente da DI?",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Em analise verifiquei que o rateio dos acréscimos era o que estava impactando no valor do II, após o ajuste os valores ficaram de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55824,
    "customFieldValues": [
      {
        "value": "Por que a NF está demorando para calcular?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Normalmente ela demora a atualizar/parametrizar quando há muitos itens.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54753,
    "customFieldValues": [
      {
        "value": "Como fazer com que o Narwal calcule o seguro com moedas diferentes?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Mercadoria e frete com a mesma moeda:\n\n(({ValorTotalSemTaxa} + {ValorFrete})*({SeguroPercentual} / 100))\n\n\n\nMercadoria diferente USD + frete USD:\n\n(((({ValorTotalSemTaxa}* {TaxaMoeda}) / {TaxaFrete}) + {ValorFrete})*({SeguroPercentual} / 100))\n\n\n\nMercadoria USD + Frete EUR:\n\n(({ValorTotalSemTaxa} + ({ValorFrete} * {TaxaFrete}) / {TaxaMoeda})*({SeguroPercentual} / 100))",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56945,
    "customFieldValues": [
      {
        "value": "200 - GissOnline ao enviar NF de serviço",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar enviar uma NF de serviço, é retornado a mensagem \"200 - Código: Descrição: Por favor, entre em contato com o suporte GissOnline e informe o código do erro.\"",
        "customFieldId": 206843
      },
      {
        "value": "Para solucionar este caso, é preciso alterar o status da NF via banco e solicitar para o cliente que reenvie e a NF. Pois, ao retornar a mensagem, o status da NF fica com o status \"Enviando\".\n\nSintaxe para alterar o status via SQL Server: UPDATE Notafiscalservico SET StatusNotaFiscalServico = 0 WHERE Notafiscalservicoid = ID NF serviço\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56090,
    "customFieldValues": [
      {
        "value": "Erro de SMTP por conta de dados incorretos.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava com problema no seu SMTP, havia um problema de encaminhamento a aplicativos menos seguros pelo gmail.",
        "customFieldId": 206843
      },
      {
        "value": "Substituimos paliativamente para SMTP Narwal até que o cliente realizasse o ajuste no seu SMTP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56439,
    "customFieldValues": [
      {
        "value": "Documento com as travas nativas do sistema ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Foi passado que no momento não possui o documento, com as travas nativas do sistema. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56488,
    "customFieldValues": [
      {
        "value": "Informe a sigla na unidade de medida no item processo",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar emitir uma nota fiscal espelho, o sistema exibe o alerta: \"Informe a sigla na unidade de medida no item processo\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Esse alerta ocorre quando a unidade de medida vinculada ao item do processo não possui uma sigla informada. Para corrigir:\n\n1. Acesse a rotina Unidade de Medida no sistema.\n\n2. Localize a unidade de medida associada ao item do processo.\n\n3. Edite o registro e preencha o campo Sigla com o valor correspondente à unidade.\n\nExemplos:\n\nUnidade de Medida: CAIXA → Sigla: CX\nUnidade de Medida: KILOGRAMA → Sigla: KG\n\nApós ajustar, salve e tente emitir a NF espelho novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56412,
    "customFieldValues": [
      {
        "value": "Há como deixar uma rotina visível apenas para um grupo usuário?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Sim, na rotina \"grupo usuário\", escolher o grupo usuário em questão e flegar a rotina para o mesmo, dessa forma, irá aparecer em seu menu. Se desmarcar o \"olho\" ao lado do nome da rotina, o analista tem acesso a rotina, mas não consegue editar as informações.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56399,
    "customFieldValues": [
      {
        "value": "Nota fiscal com divergência na base de calculo e no valor do ICMS?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Em analise verifiquei que o que estava ocasionando o erro era o rateio das despesas, no0 Narwal ele constava como CIF fiz o rateio alterando para valor a nota saiu de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56925,
    "customFieldValues": [
      {
        "value": "Como fazer com que a aba \"Serviços\" apareça na rotina de contrato de comissão.",
        "customFieldId": 206842
      },
      {
        "value": "Para que a aba \"Serviços\" apareça na rotina de contrato de comissão, é necessário ativar o valor da variavel de ambiente: \n\nNWL_HABILITAPROCESSAMENTOCONTRATOCOMISSAO",
        "customFieldId": 206843
      },
      {
        "value": "Para que a aba \"Serviços\" apareça na rotina de contrato de comissão, é necessário ativar o valor da variavel de ambiente: \n\nNWL_HABILITAPROCESSAMENTOCONTRATOCOMISSAO",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55385,
    "customFieldValues": [
      {
        "value": "Porque o modelo de inserção não funciona? ",
        "customFieldId": 206842
      },
      {
        "value": "Se a coluna descrição de todos os produtos da planilha não estiver preenchida, o narwal não irá aceitar a integração do modelo de inserção. ",
        "customFieldId": 206843
      },
      {
        "value": "Preencher a coluna descrição dos produtos. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56351,
    "customFieldValues": [
      {
        "value": "Erro ao compensar o segundo contrato câmbio",
        "customFieldId": 206842
      },
      {
        "value": "O cliente estava seguindo o fluxo de maneira incorreta. Como os pagamentos são realizados via contrato de cambio, para criar a invoice é necessário ter todos os contratos já criados.",
        "customFieldId": 206843
      },
      {
        "value": "Cancelar a invoice e criar novamente com o adiantamento devidamente criado e baixado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56956,
    "customFieldValues": [
      {
        "value": "Senha atualizada via SSO não refletiu no ambiente de homologação do Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Atualizei a senha do meu usuário via SSO, mas ao tentar acessar o ambiente de homologação (HML) do Narwal, o login ainda considera a senha antiga. O que devo fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Esse comportamento pode ocorrer devido a uma instabilidade temporária que impede a sincronização imediata da nova senha com o ambiente de homologação. Recomendamos aguardar alguns minutos e tentar novamente. No caso relatado, a sincronização foi concluída automaticamente após um curto período, e o acesso via SSO foi normalizado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56963,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 55614.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53427,
    "customFieldValues": [
      {
        "value": "Como fazer com que, ao integrar o XML da DI, o desconto da Invoice seja integrado junto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Em conversa com nosso time de produtos, informo que os ajustes dos descontos de Invoices devem ser manuais. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52477,
    "customFieldValues": [
      {
        "value": "Por que o ICMS antecipado está sendo calculado errado?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Acredito que a cliente estava se referindo ao crédito presumido, no fim não tivemos retorno e não foi devidamente confirmado e resolvido.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56968,
    "customFieldValues": [
      {
        "value": "Narwal fora do ar",
        "customFieldId": 206842
      },
      {
        "value": "Instabilidade no servidor.",
        "customFieldId": 206843
      },
      {
        "value": "Solicitado apoio ao time de infra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56921,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 56418.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56306,
    "customFieldValues": [
      {
        "value": "Authorization has been denied for this request ao integrar planilha em pedido de compra",
        "customFieldId": 206842
      },
      {
        "value": "Causa: Este erro ocorre devido a perda de conexão do usuário com o narwaw.",
        "customFieldId": 206843
      },
      {
        "value": "Solução: A solução pode ser realizada apenas relogando no narwal e realizando a mesma operação para integrar a planilha.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56146,
    "customFieldValues": [
      {
        "value": "Não é possível vincular a invoice ao processo e ocorre erro de saldo.",
        "customFieldId": 206842
      },
      {
        "value": "Não é possível vincular a invoice ao processo e ocorre erro de saldo menor que zero.",
        "customFieldId": 206843
      },
      {
        "value": "Verifique se o processo foi criado a partir do \"Pedido de Compra\".\n\nCaso a invoice também tenha sido criada a partir do \"Pedido de Compra\", ao tentar associá-la ao \"Processo\", ocorrerá o erro de saldo.\n\nPara corrigir, será necessário cancelar a invoice e criar uma nova a partir do \"Processo\". Utilize o botão \"Nova Invoice\" para isso.\n\nPara futuros processos, siga o fluxo correto:\n\nPedido de Compra > Invoice > Processo\n\nSempre crie a invoice a partir do pedido de compra e o processo a partir da invoice para evitar erros de saldo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56202,
    "customFieldValues": [
      {
        "value": "Base de calculo de PIS/COFINS, saindo divergente na nota. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Em analise, o frete estava para ser destacado na nota dessa forma ele precisa dentro da parametrização na parte de PIS/COFINS informar a formula. \n\n{valortotal}+{frete}, teste realizado em HML versão 2025.2.1.2 nota saiu de acordo após ajustes. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56192,
    "customFieldValues": [
      {
        "value": "Pedido de compra que estava desativado. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro de usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Em auditoria verificamos que o pedido de compra tinha sido desativado, por um usuária Larissa, dessa forma conseguimos ativar ele novamente. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56872,
    "customFieldValues": [
      {
        "value": " Cálculo dos Imposto da Simulação de Importação",
        "customFieldId": 206842
      },
      {
        "value": "Calculo de Impostos do relatório de Simulação de Importação não esta correto\nVMLE x Alíquota",
        "customFieldId": 206843
      },
      {
        "value": "Verifiquei que o relatório está correto. A divergência no valor entre VMLD e Taxa II ocorre porque a Taxa II é apenas informativa. Observei que nesta simulação há vários itens com alíquotas diferentes. Se você pegar as alíquotas de cada item, multiplicá-las pelo valor total do produto e somar todos os resultados, verá que o valor dos impostos está correto. Portanto, a confusão está sendo causada pelas diferentes alíquotas dos itens.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56904,
    "customFieldValues": [
      {
        "value": "Clientes não estão recebendo o código de autenticação através do automatico@narwal",
        "customFieldId": 206842
      },
      {
        "value": "Foi relatado por 1 cliente que não estava recebendo o código de verificação",
        "customFieldId": 206843
      },
      {
        "value": "A solução para este caso foi limpar a caixa de entrada do automatico@narwalsistemas.com.br",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56338,
    "customFieldValues": [
      {
        "value": "Está sendo resolvido no ticket 56812",
        "customFieldId": 206842
      },
      {
        "value": "Está sendo resolvido no ticket 56812",
        "customFieldId": 206843
      },
      {
        "value": "Está sendo resolvido no ticket 56812",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56804,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56359,
    "customFieldValues": [
      {
        "value": "Como posso cadastrar E-CPF e E-CNPJ no Narwal?",
        "customFieldId": 206842
      },
      {
        "value": "Gostaria de saber quais caminhos devo seguir para cadastrar os certificados E-CPF e E-CNPJ no Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Encerrar os chamados:\n\n56804\n55226\n56191\n55814\n56359\n\nComo incluir o certificado digital do E-CPF no Narwal?\n\n1. Acesse a rotina Representante Legal.\n\n2. Localize o representante desejado.\n\n3. Edite o cadastro do representante.\n\n4. Inclua o novo certificado digital E-CPF e insira a senha correspondente.\n\nComo cadastrar o certificado digital E-CNPJ para emissão de notas fiscais no Narwal?\n\nPara a emissão de notas fiscais, cadastre o certificado digital E-CNPJ da Filial.\n\nCaso a nota fiscal seja emitida por um importador, é necessário cadastrar o certificado digital do importador na rotina de Importador.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55111,
    "customFieldValues": [
      {
        "value": "Alguns processos sumindo o fluxo de caixa ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Atualmente o relatório de Fluxo de Caixa Impostos e Despesas possui 2 regras para mostrar um processo.\n\nA primeira regra e que deve ter alguma invoice vinculada a esse processo.\n\n\n\nA segunda Regra e que deve o processo não pode ter Numero de Di e Data Registro Di informada\n\nAo verificar os processos WEL-000033 e LSC-00195 foi visto que os dois possuem Numero DI e Data Registro Di informada, por este motivo esses processos não estão aparecendo no relatório.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55992,
    "customFieldValues": [
      {
        "value": "Como funciona o fechamento financeiro?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Valor do adiantamento: numerário de nacionalização + câmbio.\nValor pago: despesas do processo.\n\n\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56887,
    "customFieldValues": [
      {
        "value": "Tem a possibilidade de Amarrar a parametrização ao processo importação automatico?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Apenas informando na aba de entrega do processo, dessa forma a parametrização  ficará vinculada ao processo ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56882,
    "customFieldValues": [
      {
        "value": "Atualização de certificado do representante legal.",
        "customFieldId": 206842
      },
      {
        "value": "dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Basta acessar a rotina \"representante legal\" e editar o cadastro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56884,
    "customFieldValues": [
      {
        "value": "ERRO ao gerar a parcela do numerário",
        "customFieldId": 206842
      },
      {
        "value": "Erro: \"Informe o fornecedor no cadastro de despachante\"",
        "customFieldId": 206843
      },
      {
        "value": "Necessário informar o fornecedor no cadastro do despachante.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56807,
    "customFieldValues": [
      {
        "value": "Erro ao realizar envio de NF para Sankhya.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Erro durante a análise de EntityName. Linha 21, posição 439.\n\nEsse erro ocorreu por conta de um caracter especial, nesse caso o \"&\" comercial. \n\nEsse erro ocorre pois o arquivo enviado é um XML, e alguns caracteres não são permitidos.\n",
        "customFieldId": 206843
      },
      {
        "value": "Alterar o valor que estava informado no campo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55868,
    "customFieldValues": [
      {
        "value": "Como gerar NFSe Expo com serviço?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Adicionado serviço no contrato de comissão\nAba \"Serviços\" da rotina \"Fechamento Financeiro\"\nClicar em \"Processar contrato\"\nAba \"Fechamento financeiro\" e \"Gerar parcela\";\nE o pedido será gerado com o valor do serviço do processo",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55163,
    "customFieldValues": [
      {
        "value": "Como gerar NFSe Expo com valor do serviço?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.\n",
        "customFieldId": 206843
      },
      {
        "value": "Adicionado serviço no contrato de comissão\nAba \"Serviços\" da rotina \"Fechamento Financeiro\"\nClicar em \"Processar contrato\"\nAba \"Fechamento financeiro\" e \"Gerar parcela\";\nE o pedido será gerado com o valor do serviço do processo\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56418,
    "customFieldValues": [
      {
        "value": "Narwal não está atualizando.",
        "customFieldId": 206842
      },
      {
        "value": "Não estava sendo possível atualizar pois o nome do pool de aplicação estava incorreto nas configurações.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustado o nome de acordo como estava no servidor, após isso foi possível atualizar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56460,
    "customFieldValues": [
      {
        "value": "Valor do VMLD nas informações complementares da DI. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Em analise a auditoria verificado que o cliente informou o valor divergente no seguro, dessa forma o ajuste ocorreu apenas nas adições, as informações ficaram divergente. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54523,
    "customFieldValues": [
      {
        "value": "Alterar horário de execução dos Jobs.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A partir das novas versões, a data de execução dos jobs podem ser alteradas pela rotina HangfireJobs. Para isso, é necessario marcar uma flag no cadastro do usuário.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56801,
    "customFieldValues": [
      {
        "value": "Ao vincular o pedido de compra no processo estava solicitando um NCM",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Verificamos que no pedido de compra o item estava sem o ncm, após informar o processo saiu de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55415,
    "customFieldValues": [
      {
        "value": "Erro consulta shipstracking: Não é possível realizar a ativação com os mesmos dados utilizados anteriormente",
        "customFieldId": 206842
      },
      {
        "value": "Número do booking já utilizado anteriormente em outro processo.",
        "customFieldId": 206843
      },
      {
        "value": "Verificar o número do booking via banco e retornar para o cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56498,
    "customFieldValues": [
      {
        "value": "Como resolver o erro \"Object reference not set to an instance of an object\" ao integrar a planilha de produtos?",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar uma planilha de produtos no processo e clicar em \"Avançar\", você recebe a mensagem de erro \"Object reference not set to an instance of an object\". O que devo fazer para solucionar isso?",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro ocorre quando há um dado inserido incorretamente na planilha. Após investigar, foi identificado que o erro estava relacionado a um dado localizado algumas linhas abaixo das informações dos produtos. Para resolver, basta remover esse dado incorreto e tentar a integração novamente. Após a correção, a integração poderá ser realizada sem problemas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55871,
    "customFieldValues": [
      {
        "value": "Erro SQL - Baixa de Título",
        "customFieldId": 206842
      },
      {
        "value": "Erro no select do addon que continha uma palavra reservada.",
        "customFieldId": 206843
      },
      {
        "value": "Corrigo SQL.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56400,
    "customFieldValues": [
      {
        "value": "Ao registrar uma DI ocorria o erro \"VALOR EM REAL DO VMLE - VALOR INFORMADO INCOMPATIVEL COM O CALCULADO PELO SISTEMA\"",
        "customFieldId": 206842
      },
      {
        "value": " O preço unitário dos itens estava diferente entre LI e Processo.",
        "customFieldId": 206843
      },
      {
        "value": "Verificar valores na LI para condizer com o Processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56422,
    "customFieldValues": [
      {
        "value": "Rotina Portos Desembarque.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "A rotina \"Portos desembarque\" foi renomeada e agora pode ser encontrada em \"Contrato de Fornecedores\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56205,
    "customFieldValues": [
      {
        "value": "Como seguir na emissão de uma NF de retorno de exportação?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Pode gerar a partir da rotina de nota fiscal:\n\"Novo (Exportação)\" caso tenha vinculo com processo, e caso deseja realizar a criação de uma NF de exportação sem processo vinculado, pode optar por \"Novo (Saída)\".\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55472,
    "customFieldValues": [
      {
        "value": "Por que foi disparado um follow \"aleatoriamente\"?",
        "customFieldId": 206842
      },
      {
        "value": "Foi verificado que, a informação está sendo alterada diretamente da integração do processo.\n\n",
        "customFieldId": 206843
      },
      {
        "value": "Foi verificado que, a informação está sendo alterada diretamente da integração do processo.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54078,
    "customFieldValues": [
      {
        "value": "Erro ao integrar o XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não estava fazendo o calculo correto",
        "customFieldId": 206843
      },
      {
        "value": "O calculo fob e cif nao estavam de acordo, resultam em impostos e valores divergentes.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56451,
    "customFieldValues": [
      {
        "value": "Erro \"Informe o NCM\" ao Integrar XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar um XML da DI, a mensagem de erro \"Informe o NCM\" é exibida.",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro ocorre quando o sistema não encontra o NCM correspondente no cadastro. O XML da DI procura o NCM pelo campo chave, e é necessário que o valor da chave do NCM no cadastro seja exatamente igual ao especificado no XML.\n\nSolução:\n\n- Verifique se o NCM presente no XML está correto.\n\n- Acesse o cadastro do NCM e confira se o valor da chave corresponde ao que está no XML.\n\n- Caso necessário, ajuste o NCM no cadastro para garantir que a chave coincida com a do XML.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56210,
    "customFieldValues": [
      {
        "value": "Descrição dos produtos duplicados",
        "customFieldId": 206842
      },
      {
        "value": "Estou vinculando alguns produtos do pedido de compra para o processo mas a descrição dos produtos está duplicando. O que devo fazer?",
        "customFieldId": 206843
      },
      {
        "value": "A solução para este caso foi alterar manualmente a descrição dos produtos. Foi tentando replicar o mesmo cenário mas sem sucesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55027,
    "customFieldValues": [
      {
        "value": "Erro ao importar produtos via planilha?",
        "customFieldId": 206842
      },
      {
        "value": "Cliente importando planilha com as informações divergentes. ",
        "customFieldId": 206843
      },
      {
        "value": " Narwal realiza a validação pela chave do produto, note que a chave está igual para os produtos. \n\nPeço que informe 1 chave para cada produto e realize o teste novamente, visto que não é possível cadastrar somente 1 chave para vários produtos",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56466,
    "customFieldValues": [
      {
        "value": "Erro ao gerar nota de saída, valores divergentes da planilha de calculo. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao cadastrar parametrização. ",
        "customFieldId": 206843
      },
      {
        "value": "Para esse cliente já tivemos duas notas com a mesma situação, conforme atendimentos passados ao cliente, precisa alterar a configuração do cliente informando o calculo da nota fiscal como Valor total - ICMS. \n\nAssim como já configurado a parametrização para emissão da nota. \n\nNesse caso ele fez o ajuste cadastro do cliente, porém não gerou uma segunda nota, após cancelar e gerar uma nova nota os valores saíram de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56454,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56417,
    "customFieldValues": [
      {
        "value": "Referência de objeto ao tentar enviar nota fiscal de saída (expo) ao ERP (Sênior)",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar enviar ao Sênior uma NF de exportação, o Narwal acusou uma referência de objeto.",
        "customFieldId": 206843
      },
      {
        "value": "Faltou o preenchimento da informação de forma de pagamento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55693,
    "customFieldValues": [
      {
        "value": "Dúvida na composição do cálculo da NF de saída",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "baixo os pontos em que a flag IPI na Base do ICMS impacta quando marcado (true) e desmarcado(false).\n\n \n\n1 -  Caso true, Adiciona o ValorIpi no ValorBaseIcms\n\n2 - Caso true e o item seja Consumo interno, ele calcula o ValorBaseIpi = ValorSubTotal / (1 - TaxaIcms / 100 * (1 + TaxaIpi / 100)), e então ele seta no ValorBaseIcms o ValorBaseIpi + ValorIpiSaida.\n\n3 - Caso false, Ele soma o ValorIpiSaida na BaseCustoTotal.\n\n4 - Caso for Conta e Ordem, a flag falsa e se Credita Ipi, ele remove do base custo o ValorIpiSaida.\n\n5 - Caso true adiciona o ValorIpi no ValorSubTotal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55801,
    "customFieldValues": [
      {
        "value": "Os 3 campos de descrição da planilha de inserção de produtos no processo devem estar preenchidos?",
        "customFieldId": 206842
      },
      {
        "value": "Os 3 campos de descrição, tem que estar preenchidos na planilha para que ela possa ser integrada, faltou preencher o campo descrição completa que na planilha é \n\n \n\n\n",
        "customFieldId": 206843
      },
      {
        "value": "Os 3 campos de descrição, tem que estar preenchidos na planilha para que ela possa ser integrada, faltou preencher o campo descrição completa que na planilha é \n\n \n\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56118,
    "customFieldValues": [
      {
        "value": "Porque o campo país não fica editável na DUIMP?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "O código do País na DUIMP irá sempre migrar do país do Fabricante Duimp, ele deve ser alimentado no processo de embarque antes de processar a DUIMP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56428,
    "customFieldValues": [
      {
        "value": "Porque não consigo gerar um numerário complementar?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Importante que ao criar a primeira parcela, ao aparecer a mensagem \"deseja enviar parcela\" seja confirmado.\n\nApós realizar a baixa da primeira parcela no contas á pagar, retornar ao processo, criar uma nova despesa na tela de numerário e realizar o lançamento da parcela complementar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56411,
    "customFieldValues": [
      {
        "value": "Pedido de venda não integra no Narwal.",
        "customFieldId": 206842
      },
      {
        "value": "Identificado que a chave do campo \"via transporte\" estava vindo com um espaço em branco.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário ajustar o pedido no ERP, após ajuste o pedido integrou normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56407,
    "customFieldValues": [
      {
        "value": "Ao gerar nota complementar os valores ficam divergentes ao ajustar manual. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro usuário",
        "customFieldId": 206843
      },
      {
        "value": "Em analise verifiquei que cliente não estava preenchendo alguns campos no ajuste manual, não informou a despesa no processo para gerar nota complementar. \n\nNa nota complementar quando complementa valor dos produtos precisa ser ajustado a quantidade e valor unitário de cada item. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54763,
    "customFieldValues": [
      {
        "value": "Qual a regra do filtro \"Devolução container\" na nova tela inicial?",
        "customFieldId": 206842
      },
      {
        "value": "Processos aéreos e rodoviários estão sendo informados dentro do filtro de devolução container na página inicial do Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "vão ser relacionados para o quadro Devolução Container, os processos que estejam com o Status Aberto, Ativos e que possuam uma Data Atracação no período informado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52905,
    "customFieldValues": [
      {
        "value": "Nota Fiscal com valor divergente no valor do produto quando no processo está informado o campo \"Valor Frete território nacional\"",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Frete em território nacional:\n\nNa hora de gerar uma declaração de importação, irá criar uma dedução dentro da aba Acréscimos/Deduções e dentro da adição > valor aduaneiro > Deduções.\nEssa dedução é usada para ajustar o valor do item conforme o Incoterm, descontando o frete em território nacional na composição do VMLE, especialmente nos casos em que o frete é prepaid.\n\nQuando o XML é integrado, o valor do frete collect/prepaid passa a ser a soma do frete informado na DI mais o valor do frete em território nacional.\nIsso acontece tanto nos processos quanto nos numerários e nas simulações de importação.\n\nOu seja, para o cálculo do valor aduaneiro do processo, o sistema considera o valor total do frete no campo frete collect/prepaid e, depois, desconta automaticamente o valor correspondente ao frete em território nacional.\n\nSe a variável NWL_CRIADESPFRETE estiver ativa, ele cria tb a despesa, fazendo o mesmo cálculo de desconto informado acima. (Frete - frete em território nacional)",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56397,
    "customFieldValues": [
      {
        "value": "Duas linhas da mesma despesa na NFD",
        "customFieldId": 206842
      },
      {
        "value": "Na integração de NFD como custo ao SAP B1, não pode haver mais de uma linha da mesma despesa.",
        "customFieldId": 206843
      },
      {
        "value": "Unir as duas linhas da mesma despesa.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56110,
    "customFieldValues": [
      {
        "value": "Número de Lacre não aparece no rascunho.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Essa informação não consta por padrão na DI, para adicionar é necessário informar a tag \"{CONTAINERS.LACRE}\" nas informações complementares da DI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54992,
    "customFieldValues": [
      {
        "value": "Adicionar ou remover item no pedido.",
        "customFieldId": 206842
      },
      {
        "value": "Não estava sendo possível adicionar ou remover itens do pedido pois o Status era diferente de \"aberto\".",
        "customFieldId": 206843
      },
      {
        "value": "Cancelar processo e invoice vinculada ao pedido de compra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56337,
    "customFieldValues": [
      {
        "value": "Por que alguns processos com DI registrada não atualizam a data desembaraço?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O Narwal realiza a alteração de acordo com o que está no SISCOMEX,. Neste caso, o Narwal consultou a informação e realizou o insert da data no processo",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56184,
    "customFieldValues": [
      {
        "value": "Gerar segunda parcela de numerario.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido com KB 55794.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56392,
    "customFieldValues": [
      {
        "value": "Volume informado não é valido para produto",
        "customFieldId": 206842
      },
      {
        "value": "A chave da unidade de medida informada no cadastro do produto utilizado na NF era diferente da unidade de medida informada no Sankhya",
        "customFieldId": 206843
      },
      {
        "value": "Alterar a unidade de medida dentro do item da NFe no Narwal para a unidade de medida corre, ou seja, a unidade de medida que possui uma chave válida dentro do Sankhya.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56100,
    "customFieldValues": [
      {
        "value": "Emissão de relatório.",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Atualmente, o sistema da Narwal não dispõe desse relatório, e a sugestão de melhoria apresentada foi recusada pelo cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55489,
    "customFieldValues": [
      {
        "value": "Erro ao consultar o Siscarga – \"Dados do BL informado não encontrados\"",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar realizar uma consulta no Siscarga via Narwal, é exibida a seguinte mensagem de erro:\n\"Dados do BL informado não encontrados. Verifique se a sincronização das cargas do importador está habilitada.\"\nO que deve ser feito para resolver esse problema?",
        "customFieldId": 206843
      },
      {
        "value": "Causa:\nEsse erro geralmente ocorre quando a variável de ambiente NWL_LINKJOBAPI está configurada incorretamente. Ela deve conter a URL correta de acesso ao portal — seja local ou externa.\n\nSolução:\nVerifique se houve alguma migração recente de servidores. Em muitos casos, a variável NWL_LINKJOBAPI não é atualizada para refletir o novo ambiente, resultando nesse erro.\n\nPara resolver:\n\n1. Acesse o ambiente onde o Narwal está configurado.\n\n2. Verifique o valor da variável NWL_LINKJOBAPI.\n\n3. Atualize a variável com a URL externa correta do portal (https://ativo.narwalsistemas.com.br/)\n\n4. Salve as alterações e reinicie o serviço.\n\nApós o ajuste, as consultas ao Siscarga devem funcionar normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55659,
    "customFieldValues": [
      {
        "value": "Erro do cliente",
        "customFieldId": 206842
      },
      {
        "value": "Erro do cliente",
        "customFieldId": 206843
      },
      {
        "value": "Erro do cliente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53496,
    "customFieldValues": [
      {
        "value": "Como funciona a inserção de lotes no processo e a exibição dessas informações na Nota Fiscal? ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "A inserção dos lotes deve ser feita manualmente na aba \"Produtos\" do processo dentro da Narwal, uma vez que essa informação não é trazida pela integração com o F&O.\nCaso um item possua múltiplos lotes, todos devem ser informados individualmente, pois o sistema não consolida diferentes lotes em uma única linha de item.\n\nEm relação à Nota Fiscal eletrônica (NF-e), a exibição dos lotes pode ser limitada devido ao número máximo de caracteres permitidos nos campos da NF, conforme o leiaute estabelecido pelo Portal NFe. Dessa forma, quando há grande volume de lotes por item, pode ocorrer truncamento e nem todos os dados serão exibidos no XML e no PDF da NF.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56382,
    "customFieldValues": [
      {
        "value": "Ocorreu um erro ao enviar o e-mail.",
        "customFieldId": 206842
      },
      {
        "value": "Empresa estava sem URL Externa no cadastro.",
        "customFieldId": 206843
      },
      {
        "value": "Informar URL Externa.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55574,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido com KB",
        "customFieldId": 206843
      },
      {
        "value": "Ticket: 55930",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56190,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido com KB",
        "customFieldId": 206843
      },
      {
        "value": "Ticket: 55930",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55266,
    "customFieldValues": [
      {
        "value": "Valor da despesa é alterado após integrar DI.",
        "customFieldId": 206842
      },
      {
        "value": "dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O valor é alterado por conta que há variação na taxa de conversão. Para ter o valor da diferença, basta preencher o campo \"taxa pagamento frete\" com a taxa paga, e o campo \"taxa frete\" será preenchido com a taxa da DI. Dessa forma é gerado a despesa \"diferença de frete\" no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56358,
    "customFieldValues": [
      {
        "value": "Ao gerar nota complementar o valor dos produtos estava ficando divergente. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente gerando nota fiscal complementar, porém não foi retificado a DI iria fazer o ajuste manual. ",
        "customFieldId": 206843
      },
      {
        "value": "O que está interferindo no calculo do produto é a parametrização utilizada, o correto seria criar uma parametrização de nota fiscal como complementar, para que seja utilizada nas notas fiscais. \n\n\n\nTirei a formula e ajustei a nota e a nota ficou conforme os ajustes, quando informo a formula na parametrização a nota fiscal ela fica alterada. \n\n\n\nPossui apenas um processo que a nota está gerada, dessa forma caso deseja continuar com a mesma parametrização remover a formula do valor total dos produtos e ajustar, após a nota autorizada informar a formula novamente. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56121,
    "customFieldValues": [
      {
        "value": "É obrigatório informar o Fabricante na DUIMP mesmo sendo o mesmo que o Fornecedor? ",
        "customFieldId": 206842
      },
      {
        "value": "Sim. Mesmo que o Fabricante e o Fornecedor sejam a mesma empresa, o Portal Único exige que ambos sejam informados separadamente no processo.\nIsso se deve ao fato de que o sistema utiliza o campo \"Fabricante\" de forma independente, para fins de validação e análise da operação.",
        "customFieldId": 206843
      },
      {
        "value": "Informar o Fabricante no processo é obrigatório, independente de ele ser ou não igual ao Fornecedor.\nComo os cadastros de Fabricante e Fornecedor compartilham a mesma tabela, não haverá qualquer conflito com o código Pucomex.\nEssa obrigatoriedade vem de uma exigência direta do Portal Único, conforme orientação repassada pelo time de NPI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55077,
    "customFieldValues": [
      {
        "value": "Desativar Follow-up padrão.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Não é possível desativar um follow-up padrão do sistema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56170,
    "customFieldValues": [
      {
        "value": "Sistema não entra",
        "customFieldId": 206842
      },
      {
        "value": "Problema de rota.",
        "customFieldId": 206843
      },
      {
        "value": "Conectar a internet.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56379,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 55768.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56360,
    "customFieldValues": [
      {
        "value": "Certificado Informado expirou favor atualizar, erro ao enviar nota para sefaz?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Verificar que está flegado para emissão de nota pelo Importador, e no cadastro da BM3 da rotina importador não possui o certificado. Poderia por gentileza informar o certificado no cadastro ou estar removendo a flag da tag e enviar a nota novamente. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55927,
    "customFieldValues": [
      {
        "value": "------",
        "customFieldId": 206842
      },
      {
        "value": "-----",
        "customFieldId": 206843
      },
      {
        "value": "-------",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55963,
    "customFieldValues": [
      {
        "value": "Como conferir a movimentação bancária?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Há um relatório de movimentação bancária que pode ser impresso para realizar a conferencia.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56325,
    "customFieldValues": [
      {
        "value": "Onde cadastrar o Consignee?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "As informações do campo 'Consignee' são trazidas do cadastro do cliente. Dessa forma quando cadastrado um novo cliente, o mesmo é possível informar nesse campo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56340,
    "customFieldValues": [
      {
        "value": "Erro ao salvar pedido de compra \"Informe o fornecedor no cadastro de origem!\"",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar salvar um pedido de compra, a seguinte mensagem é exibida: \"Informe o fornecedor no cadastro de origem!\".",
        "customFieldId": 206843
      },
      {
        "value": "Até a data de hoje (23/04/2025), a mensagem de alerta ainda não possui um tratamento adequado no sistema, o que dificulta a identificação do problema.\n\nPara solucionar esse caso, siga os passos abaixo:\n\n1. Identifique o nome do despachante vinculado ao pedido de compra (ou ao processo, se for o caso).\n\n2. Acesse a rotina \"Despachante\".\n\n3. Edite o cadastro do despachante correspondente -> Vá até a aba \"Integração\".\n\n4. No campo \"Fornecedor\", selecione e atribua um fornecedor válido.\n\nApós realizar essa atribuição, o sistema permitirá salvar o pedido de compra normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56277,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido com KB",
        "customFieldId": 206843
      },
      {
        "value": "Ticket: 55930",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56185,
    "customFieldValues": [
      {
        "value": "Como deixar verde o semáforo Correção BL",
        "customFieldId": 206842
      },
      {
        "value": "Campo \"Data correção do conhecimento\" no processo está em branco.",
        "customFieldId": 206843
      },
      {
        "value": "Informar campo \"Data correção do conhecimento\" no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55217,
    "customFieldValues": [
      {
        "value": "Qual cálculo é feito no Custo Unitário",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Para o campo Custo Unitário do relatório:\n\n Custo Unitário = (ValorSubTotal + ValorIcms + ValorHonorario - ValorDiferencaIcms ) / Quantidade\nSubcalculos:\n\nValorSubTotal = ValorCif + ValorIi + ValorPis + ValorCofins + ValorDespesasAduaneiras \nValorDiferencaIcms = ValorIcms - ValorIcmsAntecipado",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56109,
    "customFieldValues": [
      {
        "value": "Como gerar duas notas para o mesmo produto no processo. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Para que você consiga gerar nota fiscal de um item e conforme a planilha de rateio dividindo esse item em duas notas, precisa no momento de gerar a nota manual selecionar a quantidade de item a ser gerada naquela nota, depois vai fazer o processo para a quantidade de item restantes. \n\n\n\nOutro ponto a se observar as parametrizações de entrada e de saída da nota fiscal, elas precisam estar informadas dentro da aba entrega do processo, e antes de gerar a nota os impostos precisam estar calculados. \n\nPasso para gerar a nota com as quantidades de cada nota. \n\n\n\nVai acessar a rotina de nota fiscal- nova importação- informar processo e parametrização- após isso flegar manual- selecionar o produto e na quantidade alterar para quantidade da nota especifica. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56302,
    "customFieldValues": [
      {
        "value": "Erro ao acessar o narwal.",
        "customFieldId": 206842
      },
      {
        "value": "Usuário relata que, ao tentar realizar login no sistema Narwal, é exibida a seguinte mensagem de erro:\n\"Ocorreu um erro ao enviar o e-mail. Por favor, verifique as configurações SMTP da conta.\"",
        "customFieldId": 206843
      },
      {
        "value": "Foi identificado que o servidor SMTP configurado pelo cliente apresentava falhas de autenticação, impedindo o envio de e-mails e, consequentemente, o processo de login.\nPara restabelecer o acesso, foi configurado temporariamente o SMTP interno da Narwal (automatico@narwalsistemas.com.br), normalizando o funcionamento do sistema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56328,
    "customFieldValues": [
      {
        "value": "Erro ao integrar planilha de produtos.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: Divisão por zero. Revise a Formula de calculo do seguro.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário informar a taxa da moeda no processo para prosseguir com a integração. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56314,
    "customFieldValues": [
      {
        "value": "Por que é necessário excluir uma Invoice para integrar o XML da DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "No XML deve possuir a mesma numeração de invoice que está no processo, caso contrário não será possível integrar, somente excluindo a invoice existente.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55187,
    "customFieldValues": [
      {
        "value": "Título duplicado ",
        "customFieldId": 206842
      },
      {
        "value": "Dois usuários criaram o título simultâneamente.",
        "customFieldId": 206843
      },
      {
        "value": "Excluir um dos títulos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56260,
    "customFieldValues": [
      {
        "value": "Por que os impostos não estão de acordo com a DI?",
        "customFieldId": 206842
      },
      {
        "value": "Impostos divergentes.",
        "customFieldId": 206843
      },
      {
        "value": "O valor dela na DI está R$ 1526,09 e no Narwal R$ 726,15, o que causou a diferença. Após o ajuste, os valores ficaram de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55928,
    "customFieldValues": [
      {
        "value": "Erro ao vincular invoice ao processo.",
        "customFieldId": 206842
      },
      {
        "value": "Erro de saldo estava ocorrendo por conta que o processo foi criado a partir do pedido, nesse caso a invoice precisa ser criada dentro do processo, ao invés de ser criada a partir do pedido.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário cancelar a invoice e cria-la por dentro da rotina \"processo\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55714,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 53892.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56060,
    "customFieldValues": [
      {
        "value": "Como definir os valores de impostos da NF-e na integraçao Senior",
        "customFieldId": 206842
      },
      {
        "value": "duvida",
        "customFieldId": 206843
      },
      {
        "value": "Ativando a variável de ambiente: NWL_DESATIVARECALCULONFEERP",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53788,
    "customFieldValues": [
      {
        "value": "Como emitir nota fiscal complementar no Sankhya",
        "customFieldId": 206842
      },
      {
        "value": "Como emitir nota fiscal complementar no Sankhya",
        "customFieldId": 206843
      },
      {
        "value": "Para garantir que o processo ocorra corretamente, siga os passos abaixo para validar a TOP (Tipo de Operação) nos sistemas Sankhya e Narwal:\n\nNo Sankhya:\n\nAcesse a aba NF-e.\nVerifique se o campo Tipo de Emissão está configurado como Complementar.\nNo Narwal:\n\nAcesse a operação financeira e localize o campo Nota Fiscal (antes de editar, valide o campo correto, pois cada cliente pode ter um cadastro diferente).\nEm seguida, edite a aba Sankhya.\nValide o campo Código de Operação de Envio (TOP).\nImportante: Compare o código de operação registrado no Sankhya com o que está registrado no Narwal. Caso eles não coincidam, o cliente deverá realizar a correção, pois a operação não ocorrerá corretamente se os dados não estiverem alinhados.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55777,
    "customFieldValues": [
      {
        "value": "Processo com duas adições e apenas uma LI",
        "customFieldId": 206842
      },
      {
        "value": "Estou com um processo que possui duas adições, mas apenas uma Licença de Importação (LI) vinculada. Como posso corrigir essa situação?",
        "customFieldId": 206843
      },
      {
        "value": "Os dois itens estavam sendo separados por causa da ausência do part number cadastrado em um deles. Após o cadastro correto, o narwal passou a agrupar os itens sob a mesma LI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56047,
    "customFieldValues": [
      {
        "value": "Se considerando o pagamento dois dias após a previsão de chegada/chegada, ele vai atualizando o vencimento automaticamente caso a previsão seja alterada?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A data de vencimento do título do numerário não tem a opção de inserir \"dias após a chegada\" como data de vencimento, é necessário escolher uma data fixa no momento de gerar a parcela.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56311,
    "customFieldValues": [
      {
        "value": "Após atualizar, ocorre erro 500 ao logar no sistema",
        "customFieldId": 206842
      },
      {
        "value": "Aplicação atualizou e o banco de dados não",
        "customFieldId": 206843
      },
      {
        "value": "Rodar migration do banco manualmente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54849,
    "customFieldValues": [
      {
        "value": "Ao criar um processo a partir do pedido de compra, o numerário já vem preenchido?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Não. Ao criar um processo a partir de um pedido de compra, é necessário adicionar as despesas no numerário.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56061,
    "customFieldValues": [
      {
        "value": "Por que o campo \"contrato de cambio\" dentro da forma de pagamento da Invoice não fica preenchido?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.\n\n",
        "customFieldId": 206843
      },
      {
        "value": "Você consegue visualizar as informações desejadas entrando pelo botão \"visualizar\" na invoice.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54880,
    "customFieldValues": [
      {
        "value": "Como manter o histórico na rotina Fluxo de Caixa Operacional",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "O Fluxo operacional não compreende títulos baixados pois ele sempre olha para os titulos futuros, o que ele olha é o saldo em conta dos bancos selecionados.\nJá lhe adianto que essa rotina não será modificada para olhar para títulos baixados, pois não faz sentido para a finalidade da rotina.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54878,
    "customFieldValues": [
      {
        "value": "Tem um campo na TGFIDI do Sankhya que o Narwal está enviando um ' ' (espaço)",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Não houve solução, pois do lado da Narwal (Produto / API) constatamos através da consulta do LOG de envio da Nota Fiscal para o ERP (SANKHYA) que não estamos enviando nenhum espaço em branco. \nDirecionamos ao cliente que entre em contato com sua consultoria do ERP e tente verificar se há um default aplicado na API de recepção dos dados.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56291,
    "customFieldValues": [
      {
        "value": "Nota fiscal com valor divergente de ICMS?",
        "customFieldId": 206842
      },
      {
        "value": "Cliente informando que o valor do ICMS não estava de acordo na nota fiscal. ",
        "customFieldId": 206843
      },
      {
        "value": "Em analise identifiquei que não tinham exceções criadas para os produtos com tributação do ICMS, dessa forma solicitei que fosse configurado e que gerasse a nota novamente. \n\nEm analise identificamos que possuía produtos com diferimento de ICMS, após os ajustes feitos na parametrização a nota saiu de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56093,
    "customFieldValues": [
      {
        "value": "Erro IDX_PRODUTO_CHAVE_EMP_FIL ao tentar cadastrar novo produto",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar cadastrar um novo produto, o sistema exibe o erro IDX_PRODUTO_CHAVE_EMP_FIL. O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro geralmente ocorre quando a chave definida para o próximo produto já está sendo utilizada por outro cadastro. Isso está relacionado à variável de ambiente NWL_SEQUENCIALPRODUTO, que controla a numeração automática das chaves de produtos.\n\nPara corrigir, qualquer usuário com acesso à rotina \"Variáveis de Ambiente\" deve verificar o valor atual da variável NWL_SEQUENCIALPRODUTO e atualizá-lo para uma numeração que ainda não esteja em uso no sistema",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55967,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 55007.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55907,
    "customFieldValues": [
      {
        "value": "Erro \"Usuário sem permissão para realizar essa operação\" ao integrar DI/DUIMP",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar uma DI, ao clicar em \"Processar\", aparece a mensagem de erro: \"Usuário sem permissão para realizar essa operação\". Como posso resolver isso?",
        "customFieldId": 206843
      },
      {
        "value": "Acesse a rotina \"Administração -> Grupo de Usuário\" e verifique se o grupo de usuários vinculado possui o parâmetro de permissão \"Integra DI/DUIMP\" habilitado. Caso não esteja habilitado, ative esse parâmetro para permitir a operação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56069,
    "customFieldValues": [
      {
        "value": "erro 'Não é possível deletar a despesa'",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar calcular os impostos do processo, o erro  'Não é possível deletar a despesa' é disparado em tela.",
        "customFieldId": 206843
      },
      {
        "value": "Deve-se cancelar os títulos mencionados pela mensagem de erro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56068,
    "customFieldValues": [
      {
        "value": "Dúvida quanto a regra do semáforo chegada dos documentos originais e liberação BL",
        "customFieldId": 206842
      },
      {
        "value": "Semáforo estava apresentando uma cor divergente da esperada.",
        "customFieldId": 206843
      },
      {
        "value": "A regra do semáforo está presente no manual de semáforo padrão do Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56258,
    "customFieldValues": [
      {
        "value": "É possível exportar o espelho da nota fiscal em XML no sistema Narwal?",
        "customFieldId": 206842
      },
      {
        "value": "Atualmente, o sistema Narwal possui apenas a funcionalidade de geração do espelho da nota fiscal em formato PDF. A exportação em XML não está disponível como funcionalidade nativa nas versões atuais.",
        "customFieldId": 206843
      },
      {
        "value": "A exportação do espelho da nota fiscal em XML trata-se de uma melhoria não contemplada na versão atual do sistema. Foi oferecida uma proposta via solicitação de F08 para viabilizar essa funcionalidade, mas o cliente optou por não prosseguir.\n\nCaso haja interesse futuro, a solicitação poderá ser reavaliada e encaminhada como sugestão de melhoria. Até o momento, a geração permanece disponível apenas em formato PDF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56053,
    "customFieldValues": [
      {
        "value": "Como editar o deposito da NF-e de envio ao ERP Sênior? ",
        "customFieldId": 206842
      },
      {
        "value": "Está informação é configurável através do cadastro de filial ",
        "customFieldId": 206843
      },
      {
        "value": "Está informação é configurável através do cadastro de filial ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56262,
    "customFieldValues": [
      {
        "value": "Por que o processo não está aparecendo no Narwal?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O processo estava inativo e cancelado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56236,
    "customFieldValues": [
      {
        "value": "Erro no Follow-up",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Explicado a regra de disparo do follow-up de atracação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56230,
    "customFieldValues": [
      {
        "value": "Atualização de Certificado Digital",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Para atualizar o certificado digital é necessário acessar a rotina \"Filial\", editar a filial desejada, e ir na aba \"Nota Fiscal\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56213,
    "customFieldValues": [
      {
        "value": "Mensagem Informe o estado do Destinatário ao gerar a nota fiscal?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Para a mensagem, basta acessar o cadastro do fornecedor, e adicionar as informações de estado exterior assim as informações vão conforme o informado. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56243,
    "customFieldValues": [
      {
        "value": "Valor da Nota Fiscal divergente do valor do Processo.",
        "customFieldId": 206842
      },
      {
        "value": "Alguns valores não estava batendo na NF, pois o valor do seguro deveria ser collect ao invés de prepaid.",
        "customFieldId": 206843
      },
      {
        "value": "Após ajustar o valor do seguro para collect, e calculado os impostos, foi possível gerar a NF com os devidos valores. Os demais ajustes foram feitos por parte do cliente. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56221,
    "customFieldValues": [
      {
        "value": "Portal fora do ar",
        "customFieldId": 206842
      },
      {
        "value": "Estamos tentando acessar o portal, mas ele está fora do ar. O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Primeiramente, verifique se a application pool está ativa ou se houve alguma migração recente da aplicação. Se nenhuma dessas for a causa, entre em contato com a equipe de infraestrutura para uma análise mais detalhada.\n\nNeste caso em específico, application pool estava parada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56043,
    "customFieldValues": [
      {
        "value": "O saldo do fornecedor do pedido X não pode ser menor que zero.",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar vincular o item de um processo a uma invoice, o erro de saldo do fornecedor é disparado.",
        "customFieldId": 206843
      },
      {
        "value": "Validar a variável de ambiente NWL_VALIDAQTDDISPFORNEC, se a mesma estiver ativa e o saldo fornecedor do pedido compra item estiver zerado, o erro aparecerá.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56138,
    "customFieldValues": [
      {
        "value": "Como alterar o \"pagos por\" dos impostos?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A alteração pode ser realizada  na aba \"DI/DA\" do processo.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55897,
    "customFieldValues": [
      {
        "value": "Como fazer com que o valor dos produtos se iguale a base de ICMS?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Os valores da Base de ICMS e total dos produtos ficaram de acordo após inserir na parametrização a TAG {baseicms} no total dos produtos, na parametrização.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56199,
    "customFieldValues": [
      {
        "value": "Atualização trocou o token do cliente ",
        "customFieldId": 206842
      },
      {
        "value": "Atualização trocou o token do cliente ",
        "customFieldId": 206843
      },
      {
        "value": "adicionei para o token dinâmico e voltou a funcionar",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56183,
    "customFieldValues": [
      {
        "value": "Chave Bacen do Pais sem 0",
        "customFieldId": 206842
      },
      {
        "value": "A chave bacen do pais estava vindo sem os zeros na frente.\nErrado: 230\nCorreto: 00230",
        "customFieldId": 206843
      },
      {
        "value": "Alterado para que venha com os zeros",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55700,
    "customFieldValues": [
      {
        "value": "SAP B1 - Envio da invoice apenas com um item na linha",
        "customFieldId": 206842
      },
      {
        "value": "Ao enviar a invoice foi notado que está apenas com um item na linha e tem mais itens na fatura, isso é um erro? O valor está correto! Apenas não apareceu os itens.",
        "customFieldId": 206843
      },
      {
        "value": "​Sim, hoje nas integrações de adiantamento ao fornecedor com o SAP B1, nos enviamos o valor total no primeiro item e enviamos apenas uma linha. Isso foi uma recomendação da propria SAP para que os valores ficassem corretos, pois quando faziamos o rateio por item o SAP recalculava e gerava um valor final incorreto!",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56225,
    "customFieldValues": [
      {
        "value": "Chave do Fabricante Estrangeiro Invalida",
        "customFieldId": 206842
      },
      {
        "value": "Chave do Fabricante Estrangeiro informado no item da NFe estava com uma virgula e o Sankhya aceita apenas numeros.",
        "customFieldId": 206843
      },
      {
        "value": "Retirado a vírgula da chave do fabricante estrangeiro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56104,
    "customFieldValues": [
      {
        "value": "Senior Sapiens - Transportadora não foi enviada na nota fiscal",
        "customFieldId": 206842
      },
      {
        "value": "Transportadora não apareceu no ERP Senior Sapiens no envio da nota",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver o problema basta realizar o de/para da chave do Narwal com o codigo da transportadora do Senior Sapiens",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56038,
    "customFieldValues": [
      {
        "value": "Chave do Fabricante Não encontrada no Sankhya",
        "customFieldId": 206842
      },
      {
        "value": "A chave no cadastro do Fabricante dentro do Narwal não correspondia a um código de parceiro no Sankhya",
        "customFieldId": 206843
      },
      {
        "value": "Alterar a chave do cadastro do fabricante para uma chave válida, ou seja, que corresponda a um parceiro existente e ativo no Sankhya.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56051,
    "customFieldValues": [
      {
        "value": "erro do cliente, ao fazer processo errado",
        "customFieldId": 206842
      },
      {
        "value": "erro do cliente, ao fazer processo errado,",
        "customFieldId": 206843
      },
      {
        "value": "erro do cliente, ao fazer processo errado,",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56195,
    "customFieldValues": [
      {
        "value": "Erro ao vincular XML de NF de exportação",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar um XML de Nota Fiscal de Exportação, é exibida a seguinte mensagem de erro:\n\nA instrução DELETE conflitou com a restrição de REFERENCE\n\"FK_dbo.ExportacaoNfeReferenciada_dbo.Exportac\".\nO conflito ocorreu no banco de dados \"NelimportPRDComex\", tabela\n\"dbo.ExportacaoNfeReferenciada\", coluna 'ExportacaoNfeltemId'.\nA instrução foi finalizada.",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro ocorre porque já existe uma ou mais Notas Fiscais vinculadas ao processo. Ao tentar vincular um novo XML, o sistema tenta remover o vínculo anterior, o que viola uma restrição de integridade referencial no banco de dados.\n\nSolução:\nVerifique se já existem Notas Fiscais vinculadas ao processo. Caso existam, será necessário encerrar o processo e criar um novo para que possa prosseguir com o registro da DU-E.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56055,
    "customFieldValues": [
      {
        "value": "Integração ocorrendo com duplicidade",
        "customFieldId": 206842
      },
      {
        "value": "Verificado que o middleware travou durante um periodo de 5 min ocasionando no envio duplicado da mesma nota de despesas",
        "customFieldId": 206843
      },
      {
        "value": "Adicionado um storage pra verificar se a ultima execução finalizou, se finalizar ele segue pra proxima se não ele para e espera o proximo passo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56187,
    "customFieldValues": [
      {
        "value": "Erro ao registrar DUE no Narwal.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente emitiu a nota incorretamente e integrou a nota ao Narwal. Dessa forma ocorrendo erro ao tentar realizar o registro da DU-E.",
        "customFieldId": 206843
      },
      {
        "value": "Reemitir a nota fiscal e vincular novamente ao Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56178,
    "customFieldValues": [
      {
        "value": "Erro ao tentar registrar DU-E. \"O PESO LIQUIDO INFORMADO E INVALIDO. POR FAVOR, REVEJA A INFORMACAO\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse problema ocorreu pois o peso liquido unitado estava negativo no processo.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário ajustar o peso liquido unitario do item no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55695,
    "customFieldValues": [
      {
        "value": "Processo expo, estava permitindo salvar os processos mesmo que o analista não estivesse preenchido?",
        "customFieldId": 206842
      },
      {
        "value": "Mesmo deixando o campo como obrigatório, ao salvar o processo não estava pedindo que o campo fosse preenchido, deixando salvar o processo. ",
        "customFieldId": 206843
      },
      {
        "value": "Feita uma auditoria e foi identificado que o campo foi preenchido como obrigatório no dia 02/04, sendo assim os processos anteriores não solicitou pois não estava como obrigatório. \n\nOutro ponto é a flag de permitir e obrigar campo, quando flegada permite que o processo salve sem a informação, quando está sem a flag ao salvar o processo solicita o preenchimento do analista ao salvar. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55960,
    "customFieldValues": [
      {
        "value": "Resolvido no KB 55896",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido no KB 55896",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido no KB 55896",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55193,
    "customFieldValues": [
      {
        "value": "Erro na rotina de recebimento.",
        "customFieldId": 206842
      },
      {
        "value": "Erro(s) de validação : The field MensagemErro must be a string or array type with a maximum length of '100'.\n\nO erro não é retornado e tela devido ao tamanho da mensagem de erro retornada.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário cancelar o título no contas a receber e gera-lo novamente, após isso foi possível fazer a consulta da situação do boleto.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56159,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55888,
    "customFieldValues": [
      {
        "value": "Erro ao integrar a DUIMP no processo impo.",
        "customFieldId": 206842
      },
      {
        "value": "Erro 'Sequence contains no matching element' ao integrar a DUIMP no processo.",
        "customFieldId": 206843
      },
      {
        "value": "Deve-se associar o item do processo corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55896,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55591,
    "customFieldValues": [
      {
        "value": "Corrigido internamente pelo cliente",
        "customFieldId": 206842
      },
      {
        "value": "Corrigido internamente pelo cliente",
        "customFieldId": 206843
      },
      {
        "value": "Corrigido internamente pelo cliente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56134,
    "customFieldValues": [
      {
        "value": "Na NF o valor do IPI está divergente do processo",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na parametrização NF, na guia Transporte verificar se o campo Rateio frete está com a opção Peso. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55323,
    "customFieldValues": [
      {
        "value": "Ao alterar o plano de contas contabeis, no narwal tem a possibilidade de excluir em massa? ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Não tem a possibilidade de estra excluindo, o que pode fazer é desativar a conta contábil. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55539,
    "customFieldValues": [
      {
        "value": "Não está listando o menu com as rotinas.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Configurar Zoom a 100% ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56157,
    "customFieldValues": [
      {
        "value": "Ao gerar a NF está ocorrendo a mensagem: As adições do processo precisam estar geradas",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Acessar a Declaração de Importação, clicar no menu de ação e clicar em Processar. Informar o tipo de declaração e salvar;\nSeguir com a criação da NF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55812,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 55164.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55974,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54236,
    "customFieldValues": [
      {
        "value": "Produto não é identificado automaticamente no registro da DI",
        "customFieldId": 206842
      },
      {
        "value": "O Narwal realiza o vínculo automático com base na chave/part number do produto informada no XML. Quando essa chave não está presente, o sistema não consegue identificar o produto automaticamente, exigindo a associação manual pelo usuário.",
        "customFieldId": 206843
      },
      {
        "value": "Para que o vínculo automático ocorra corretamente no registro da DI, é necessário que o XML contenha a chave do produto previamente cadastrada no sistema Narwal. Recomendamos verificar a possibilidade de incluir essa informação no XML gerado para garantir o reconhecimento automático pelo sistema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55815,
    "customFieldValues": [
      {
        "value": "Como remover/abrir/fechar um período financeiro?",
        "customFieldId": 206842
      },
      {
        "value": "Ao dar baixa em um título, ocorre um erro em que período de fechamento financeiro está fechado.",
        "customFieldId": 206843
      },
      {
        "value": "Precisa verificar o cadastro da conta bancária na rotina \"Fechamento período financeiro\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55986,
    "customFieldValues": [
      {
        "value": "Narwal aceita CNPJ alfanumérico?",
        "customFieldId": 206842
      },
      {
        "value": "A partir de Julho de 2026 novas empresas terão CNPJ alfanumérico.",
        "customFieldId": 206843
      },
      {
        "value": "Narwal estará preparado para aceitar CNPJ alfanumérico.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56136,
    "customFieldValues": [
      {
        "value": "Erro ao logar/redefinir senha \" Authentication unsuccessful\" - SMTP",
        "customFieldId": 206842
      },
      {
        "value": "Quando tento acessar o Narwal ou enviar algum e-mail de redefinição, está sendo exibida a mensagem:\n\"Authentication unsuccessful: O login na conta falhou — ou por senha incorreta, ou por bloqueio de autenticação.\" O que posso fazer para resolver?",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro indica que o sistema não conseguiu autenticar a conta de e-mail configurada no servidor SMTP. Para resolver, é necessário que a equipe de infraestrutura do cliente verifique se as configurações estão corretas.\n\nVerificações recomendadas:\n\n- A senha da conta pode estar incorreta ou expirada.\n\n- A conta pode ter autenticação multifator (MFA) ativada, o que exige o uso de senha de aplicativo ou autenticação via OAuth2.\n\n- O acesso SMTP pode estar desativado para a conta utilizada.\n\n- A configuração de segurança do cliente (como porta e TLS) pode estar incorreta.\n\n- A conta pode ter sido temporariamente bloqueada por medidas de segurança da Microsoft.\n\nComo solução paliativa, é possível solicitar à equipe de infraestrutura da Narwal a substituição temporária do SMTP do cliente pelo SMTP interno da empresa (automatico@narwalsistemas.com.br).\n\nPara isso, entre em contato com a equipe de infraestrutura ou com o time de suporte e solicite a atribuição do SMTP interno da Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56096,
    "customFieldValues": [
      {
        "value": "Contrato de câmbio antecipado não aparece para compensar invoice",
        "customFieldId": 206842
      },
      {
        "value": "Foi criado um contrato de câmbio de antecipação ele não aparece para adiantamento manual na invoice",
        "customFieldId": 206843
      },
      {
        "value": "O status do contas a pagar do título de antecipação precisa ser 1 (fechado)",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56070,
    "customFieldValues": [
      {
        "value": "Falha na integração de pedidos SAP x Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido com KB",
        "customFieldId": 206843
      },
      {
        "value": "Ticket: 54645",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56002,
    "customFieldValues": [
      {
        "value": "No Processo, menu de ação Documento de Importação/Enviar Impostos: Informe o fornecedor no cadastro do despachante do processo!",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro de Despachante, guia Integração informar o fornecedor, nesse caso será o próprio despachante. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55853,
    "customFieldValues": [
      {
        "value": "Lentidão geral!",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido com KB",
        "customFieldId": 206843
      },
      {
        "value": "Ticket: 55930",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56105,
    "customFieldValues": [
      {
        "value": "Erro na emissão da previa DANFE",
        "customFieldId": 206842
      },
      {
        "value": "Informações faltantes.",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro do fornecedor o campo \"Cidade\" e \"Estado\" não estava informado, e o numero de documento em branco (preencher entre 5 a 20 caracteres).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53963,
    "customFieldValues": [
      {
        "value": "Valor da Base de cálculo PIS/COFINS no xml da Nota Fiscal",
        "customFieldId": 206842
      },
      {
        "value": "Desconhecimento cliente",
        "customFieldId": 206843
      },
      {
        "value": "Valor da base de cálculo no xml da NF de saida deve ser igual ao valor aduaneiro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56111,
    "customFieldValues": [
      {
        "value": "Erro There is an error in XML document (3, 2) ao integrar NF",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar a Nota Fiscal via XML, o sistema retorna o erro There is an error in XML document (3, 2). O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro indica que o XML da NF está com a estrutura incorreta: (linha 3, coluna 2). Isso pode ocorrer por:\n\n- Arquivo XML corrompido ou incompleto;\n-Caracteres inválidos na estrutura do XML;\n- Falta da declaração correta no início do arquivo;\n\nRecomenda-se validar o XML em um validador oficial da SEFAZ ou reexportar o arquivo direto da fonte emissora (sistema contábil, ERP, etc.) antes de realizar a integração novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56063,
    "customFieldValues": [
      {
        "value": "Onde inserir o certificado digital do despachante.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente com dúvida em qual rotina deve ser inserido o certificado digital do despachante.",
        "customFieldId": 206843
      },
      {
        "value": "Deve-se inserir o mesmo no cadastro de representante legal, juntamente com a senha de instalação do certificado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54660,
    "customFieldValues": [
      {
        "value": "Dúvidas gerais sobre shipstracking",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido com KB https://portal.narwalsistemas.com.br/wiki/ships-tracking/ships-tracking-logcomex/",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54416,
    "customFieldValues": [
      {
        "value": "Como fazer com que o frete venha sempre pago por \"Não informado\"?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Existe a varável NWL_OPCAOPAGOPORDESPESA, onde é configurado quem realiza o pagamento do frete, sendo: \n0-Não informado\n1-Despachante \n2-Importador \n3-Cliente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56102,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF para o SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando enviar uma NF para o SEFAZ, porém, está retornando o erro \"'dhEmi' no espaço para nome 'http://www.portalfiscal.inf.br/nfe'. \". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Solução paliativa é reiniciar a pool de aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56095,
    "customFieldValues": [
      {
        "value": "Cliente com mensagem retorno do Sefaz- erro 610 Valor difere do somatório?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Nessa situação era uma nota fiscal de ajuste, estorno para o exterior, como notas para exterior não possui destaque de Impostos, deve manter a seguintes informações:\nCFOP 7949-\nCST ICMS 41- NÃO TRIBUTADO \n\nPara o valor de PIS/COFINS, deve destacar ele no totais da nota, que vai totalizar a outras despesas, e informar o CST do importo como 49. \n\nApós os ajustes a nota será autorizada. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55856,
    "customFieldValues": [
      {
        "value": "Campo oculto.",
        "customFieldId": 206842
      },
      {
        "value": "Campo oculto pelo usuário admin",
        "customFieldId": 206843
      },
      {
        "value": "desocultar o campo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56089,
    "customFieldValues": [
      {
        "value": "Sem acesso ao portal",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "TI do cliente não deu a devida permissão no firewall.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53903,
    "customFieldValues": [
      {
        "value": "Por que o botão de \"Enviar impostos\" da DI não está habilitado?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "a DI não foi gerada, por esse motivo o botão não está habilitado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56106,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 55043.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55949,
    "customFieldValues": [
      {
        "value": "Como configurar a criação automática da despesa \"honorário\"?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina \"Contrato comissão\" realizamos cadastros de contratos por clientes.\nÉ possível configurar um cálculo para que o honorário seja gerado de forma automática no fechamento financeiro. Basta preencher os campos necessários, salvar e aplicar os requisitos aos processos.\nApós este procedimento, processar os requisitos no fechamento financeiro.\nHabilitei a variável \"NWL_HONORARIOFCH\" para que seja calculados os requisitos.\nCom isso, o valor do honorário irá aparecer no processo e no fechamento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55729,
    "customFieldValues": [
      {
        "value": "Erro ao enviar DI para analise. \"PESO LIQUIDO - DIFERENTE DO SOMATORIO DO PESO LIQUIDO DAS MERCADORIAS\"",
        "customFieldId": 206842
      },
      {
        "value": "O problema estava sendo causado pois havia divergencia entre o peso liquido da LI e o peso liquido na declaração de importação.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente seguiu com o ajuste manualmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56088,
    "customFieldValues": [
      {
        "value": "Erro ao tentar acessar URL Narwal \"HTTP Error 503. The service is unavailable.\".",
        "customFieldId": 206842
      },
      {
        "value": "Instabilidade no servidor.",
        "customFieldId": 206843
      },
      {
        "value": "Assim que realizamos a tentativa de acesso, foi possível acessar o Narwal normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55431,
    "customFieldValues": [
      {
        "value": "Não consigo editar ou visualizar alguns campos no processo",
        "customFieldId": 206842
      },
      {
        "value": "Alguns campos do processo estão bloqueados para edição ou desapareceram. O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "1. Desbloquear ou reexibir o campo manualmente clicando no ícone ao lado do campo (se disponível).\n\n2. Ativar o parâmetro \"Permite obrigar campos\" no cadastro do usuário. Após essa alteração, é necessário sair e entrar novamente no sistema para aplicar a mudança.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55873,
    "customFieldValues": [
      {
        "value": "Erro ao tentar cadastrar usuário em portal do cliente",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Usuário estava tentando cadastrar o \"usuário\" de acesso com o proprio e-mail informado, porém, no portal do cliente, não se permite nome de usuário com quantidade superior de 30 caracteres, dessa forma, cadastrado apenas o sufixo do usuário e seu sobrenome, obtido sucesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55708,
    "customFieldValues": [
      {
        "value": "Usuários externos sem acesso após atualização para R2.1.2",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Para os clientes que já utilizam seu próprio SMTP na sua base Narwal, por algum motivo na versão R2, os usuários externos estão perdendo acesso.\nFoi necessário recolocar o email e senha da Narwal para recuperar o acesso dos usuários.\nImportante entrar em contato com Suporte Narwal para apoio.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55822,
    "customFieldValues": [
      {
        "value": "Erro ao integrar XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando integrar uma XML da DI, mas está dando erro de permissão \"Você não possui acesso ao menu selecionado: Importação/NPI/IntegrarXmlDiProcesso. O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "KB no chamado 55672",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55619,
    "customFieldValues": [
      {
        "value": "Por que o valor do fechamento financeiro está divergente da DI? ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Foi realizado \"ajustes\" manuais pelo cliente, por esse motivo os valores não ficaram de acordo. Nesse caso, deve-se realizar os cálculos e validar se há algum valor faltando no processo, realizar auditorias para entender se ele foi retirado. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55728,
    "customFieldValues": [
      {
        "value": "Por qual motivo o rateio dos imposto pode estar incorreto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O rateio da despesa interfere no seu cálculo.\nDeve-se ser ajustado no tipo despesa.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55878,
    "customFieldValues": [
      {
        "value": "Envio de follow desnecessário",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Follow up em questão estava ativa incorretamente, sendo assim enviando follows desnecessários.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55264,
    "customFieldValues": [
      {
        "value": "Descrição detalhada da mercadoria na DI",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina Composição da Descrição da DI incluir a tag {DescricaoCompletaDi}",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55315,
    "customFieldValues": [
      {
        "value": "Erro ao fazer vinculação de ordens de compra/contas a pagar",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso Como eles re-integraram a OC com uma forma de pagamento sem financeiro, o Narwal não vai cancelar os titulos já criados anteriormente.\n\nNesse caso, favor alterar via banco o status das parcelas para 'excluído' \nO passo a ser seguido deveria ter sido:\n\n1. Editar a ordem de compra 'excluir' as parcelas da forma de pagamento;\n\n    Conferir exclusão das parcelas no contas a pagar;\n\n2. Ajustar ordens no ERP alterando a forma de pagamento para CO - SEM CAMBIO;\n\n3. Cancelar ordem no ERP e Narwal.\n\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55947,
    "customFieldValues": [
      {
        "value": "Cliente informando que o processo expo estava vinculando nota de outro processo. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Em auditoria verificamos que a usuária Raquel quem estava integrando o XML da nota no processo expo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56017,
    "customFieldValues": [
      {
        "value": "Acesso Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Link da aplicação.",
        "customFieldId": 206843
      },
      {
        "value": "O cliente estava tentando acessar por um link incorreto. Após o envio do endereço correto, o acesso foi realizado com sucesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55872,
    "customFieldValues": [
      {
        "value": "Processo não aparece na grid de consultas da rotina \"Declaração de Importação\"",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar buscar um processo na grid de consultas da rotina \"Declaração de Importação\", ao clicar em \"Consultar\", o processo não é retornado. O que devo fazer?\n",
        "customFieldId": 206843
      },
      {
        "value": "Primeiramente, verifique se o processo está faltando apenas para um usuário específico. Caso seja esse o problema, a solução é resetar a grid de consulta, o que irá restaurar o estado inicial da busca. Após realizar o reset da grid, tente realizar a consulta novamente para verificar se o processo é retornado corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56016,
    "customFieldValues": [
      {
        "value": "Erro 403 Forbidden ao enviar a NFe para o SEFAZ.",
        "customFieldId": 206842
      },
      {
        "value": "'The remote server returned an error: (403) Forbidden.'",
        "customFieldId": 206843
      },
      {
        "value": "Certificado digital da filial inválido ou vencido, necessário ajustá-lo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55915,
    "customFieldValues": [
      {
        "value": "Como resolver o erro de integração \"Tipo de movimento inválido nesta opção.\" de nota com Sankhya?",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "É necessário avaliar o tipo da modalidade importação se está de acordo com a configuração da TOP. Quando a modalidade de importação está como \"Encomenda\" enviamos o tipo de movimento como \"V\" no contrario mandamos \"C\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55976,
    "customFieldValues": [
      {
        "value": "Resolvido com KB. 54515",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55748,
    "customFieldValues": [
      {
        "value": "Como acompanho o andamento de minha solicitação F08?",
        "customFieldId": 206842
      },
      {
        "value": "De que forma posso acompanhar o progresso da minha solicitação de melhoria (F08)?",
        "customFieldId": 206843
      },
      {
        "value": "Ao encerrar um chamado de melhoria (F08), é fundamental comunicar ao cliente que, após o fornecimento do ID da solicitação, o acompanhamento do status da mesma deverá ser realizado diretamente por meio do e-mail servicoscomplementares@narwalsistemas.com.br, informando o respectivo ID da solicitação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55224,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55984,
    "customFieldValues": [
      {
        "value": "SMTP expirado",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário solicitar a senha ao cliente. \nRotina: Empresa > Parametros > SMTP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55981,
    "customFieldValues": [
      {
        "value": "Erro ao tentar excluir despesa.",
        "customFieldId": 206842
      },
      {
        "value": "Estava sendo retornado erro informando que o título havia sido baixado, esse erro ocorreu pois o valor do estorno do título não tinha sido correto, ainda assim permanecendo valor baixado.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário realizar a baixa do título novamente, e em seguida realizar o estorno. Após essa ação foi possível excluir a despesa.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55114,
    "customFieldValues": [
      {
        "value": "Porque a moeda muda quando chega no contas a pagar",
        "customFieldId": 206842
      },
      {
        "value": "Cliente tinha no processo uma moeda especifica porém quando integrou no contas a pagar apareceu outra moeda",
        "customFieldId": 206843
      },
      {
        "value": "Esse caso acontece pois o que vale é o que esta na invoice e se verificar a invoice estava com a moeda chinesa porém foi alterado para USD, dessa forma precisa editar a invoice e enviar novamente para o contas a pagar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55401,
    "customFieldValues": [
      {
        "value": "LI não gera numero após cria-la",
        "customFieldId": 206842
      },
      {
        "value": "A LI estava sem numero pois ainda não havia sido deferida.",
        "customFieldId": 206843
      },
      {
        "value": "Para que a LI apresente numero, data de deferimento e demais informações, é necessário ir na rotina de \"Licença de importação\", clicar no botão de ação da LI e ir na opção \"Deferir\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55816,
    "customFieldValues": [
      {
        "value": "Erro 403 forbidden ao acessar a API",
        "customFieldId": 206842
      },
      {
        "value": "Os endereços do cliente não estavam liberado para acesso a API.",
        "customFieldId": 206843
      },
      {
        "value": "Aberto chamado com o time de infra (Narwal) para liberação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54953,
    "customFieldValues": [
      {
        "value": "Por que não é possível cancelar a Invoice ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Há títulos em aberto com a Invoice vinculada. É necessário realizar o cancelamento para excluir a Invoice.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55734,
    "customFieldValues": [
      {
        "value": "Alteração de dados do usuário.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Não alteramos os dados cadastrais de clientes. Sempre orientar o cliente a cadastrar um novo usuário com um novo e-mail.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55966,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55950,
    "customFieldValues": [
      {
        "value": "Valor da NF de saída valor divergente.",
        "customFieldId": 206842
      },
      {
        "value": "Falha usuário",
        "customFieldId": 206843
      },
      {
        "value": "No Processo, guia Entrega informar a parametrização NF Entrada / Saída.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55941,
    "customFieldValues": [
      {
        "value": "Como deve ficar a inclusão do frete na incoterm CFR, dentro da DI?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso o valor do frete ele não ficará lançado no valor do VLME, ele vai estar totalizando ao VMCV. \n\nNa declaração de importação ele vai totalizar ao VMLD. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55559,
    "customFieldValues": [
      {
        "value": "Lentidão aba Numerario",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido com KB",
        "customFieldId": 206843
      },
      {
        "value": "Ticket: 55930",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55968,
    "customFieldValues": [
      {
        "value": "Retorno SEFAZ no envio da NF: NF-e ja esta inutilizada na Base de dados da SEFAZ ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Acessar portal NFe e verificar se a numeração que está sendo enviada já consta inutilizada.\nhttps://www.nfe.fazenda.gov.br/ ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55919,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55914,
    "customFieldValues": [
      {
        "value": "Como extrair dados de processo via API",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Voce pode extrair os dados do processo de importação atravez do odataProcesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55851,
    "customFieldValues": [
      {
        "value": "Erro ao acessar o portal do cliente",
        "customFieldId": 206842
      },
      {
        "value": "Ao acessar o portal do cliente, a página não abre.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente estava utilizando o link incorreto da aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55939,
    "customFieldValues": [
      {
        "value": "Erro ao consultar a rotina Simulação de Importação",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Necessário resetar a grid e retirar os filtros aplicamos nas colunas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55289,
    "customFieldValues": [
      {
        "value": "Como majorar COFINS?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.\n\n",
        "customFieldId": 206843
      },
      {
        "value": "Se não houver majoração, deve-se clicar na flag \"não majora COFINS\", se majorar, deixar desflegado.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55946,
    "customFieldValues": [
      {
        "value": "MENSAGEM: 866 - Rejeicao: Ausencia de troco quando o valor dos pagamentos informados for maior que o total da nota",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Verificar na guia Cobrança se o valor está superior ao total da NF. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55930,
    "customFieldValues": [
      {
        "value": "Lentidão numerário",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Após a reinicialização do servidor o comportamento da aplicação se normalizou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55961,
    "customFieldValues": [
      {
        "value": "Você não possui acesso ao menu selecionado: Importacao/NPI/IntegrarXmlDuProcesso",
        "customFieldId": 206842
      },
      {
        "value": "Falha após atualização",
        "customFieldId": 206843
      },
      {
        "value": "Acessar/Editar Grupo usuário e selecionar a opção  \"Integrar DI/DUIMP\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55788,
    "customFieldValues": [
      {
        "value": "Resolvido com KB",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido com KB - chamado: 53613",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido com KB - chamado: 53613",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55792,
    "customFieldValues": [
      {
        "value": "Erro de Chave Duplicada ao Cadastrar Produto",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar cadastrar um produto, aparece a mensagem de erro: \"Não é possível inserir uma linha com chave duplicada no objeto 'dbo.Produto' devido ao índice único 'IDX_PRODUTO_CHAVE_EMP_FIL'\". O que fazer para resolver esse problema?",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro ocorre quando, anteriormente, a variável NWL_SEQUENCIALPRODUTO estava ativa, garantindo que a chave do produto seguisse um padrão específico. Quando essa variável foi desativada, o sistema tentou cadastrar novos produtos, mas a chave gerada já estava registrada no banco de dados. Para resolver, basta seguir os passos abaixo:\n\n- Localize a chave do produto mencionada na mensagem de erro.\n\n- Altere a chave para um valor aleatório (certifique-se de que a chave não esteja em uso).\n\nApós realizar essa alteração, os próximos produtos cadastrados seguirão a sequência correta e o erro não ocorrerá mais.\n\nEsse procedimento garante que a chave dos produtos seja única, evitando conflitos futuros.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55731,
    "customFieldValues": [
      {
        "value": "Código: IPM002 - O nome do país do tomador informado está errado: BRAZIL",
        "customFieldId": 206842
      },
      {
        "value": "Ao enviar a NFSE para a prefeitura o erro 'Código: IPM002 - O nome do país do tomador informado está errado: BRAZIL' é disparado em tela.",
        "customFieldId": 206843
      },
      {
        "value": "Foi analisado que o problema em questão estava ocorrendo devido ao município informado no cadastro do cliente, que estava incorreto.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55737,
    "customFieldValues": [
      {
        "value": "Criar operação financeira com a mesma função financeira já cadastrada.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Para cadastrar uma operação financeira com a mesma função financeira já utilizada anteriormente, apenas é possível quando é criada para uma nova filial. \n\nQuando houver a tentativa de criar para a mesma filial, deverá dar erro na criação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55552,
    "customFieldValues": [
      {
        "value": "valor do IPI não compondo base de calculo ICMS",
        "customFieldId": 206842
      },
      {
        "value": "Duvida-  Chamado 555552",
        "customFieldId": 206843
      },
      {
        "value": "Para solucionar a situação, a configuração necessária esta na sua Parametrização NF para Processos de Conta e Ordem\n\nCampo ICMS > Flag \"IPI na Base ICMS\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55931,
    "customFieldValues": [
      {
        "value": "Tamanho da mensagem excedeu o limite estabelecido",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Cancelar a NF e gerar novamente a NF. No quadro \"Configurar\" selecionar a opção correspondente de divisão da NF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55912,
    "customFieldValues": [
      {
        "value": "Rateio do peso bruto divergente na nota fiscal. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente gerando tres notas de nacionalização, porém o peso bruto dos produtos está ficando divergente do processo, e do pedido de compra. ",
        "customFieldId": 206843
      },
      {
        "value": "Como medida contorno, inserimos de forma manualmente na nota fiscal. \n\nOrientamos ao cliente como informar na nota fiscal. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55657,
    "customFieldValues": [
      {
        "value": "Por que o digito de origem da ntoa saiu divergente do cadastro produto?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Dentro da parametrização utilizada consta o digito de origem como 6, por isso a divergência na nota fiscal. Lembrando que as informações de CST e digito de origem da nota elas puxam da parametrização da NF. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55911,
    "customFieldValues": [
      {
        "value": "Tipo despesa Diferença de frete não encontrado!",
        "customFieldId": 206842
      },
      {
        "value": "Duvida.",
        "customFieldId": 206843
      },
      {
        "value": "O campo \"Taxa pagamento frete\" no processo preenche automaticamente uma despesa referente à diferença de frete. Para que isso ocorra corretamente, é necessário que exista uma despesa configurada com o tipo \"Diferença de frete\" na rotina \"Tipo despesa\". Caso não haja essa despesa configurada, o erro será gerado. Se o campo \"Taxa pagamento frete\" estiver preenchido e a informação estiver correta, será preciso criar a despesa com o tipo correspondente. Caso contrário, basta remover o valor do campo",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55944,
    "customFieldValues": [
      {
        "value": "Sistema fora do ar",
        "customFieldId": 206842
      },
      {
        "value": "O narwal está apresentando apresentando o erro \"HTTP Error 404\" ao acessar. Como posso resolver?",
        "customFieldId": 206843
      },
      {
        "value": "É necessário verificar a pool de aplicação do cliente, dentro do servidor. Caso esteja parada, é necessário entender o que houve. Após iniciar a pool, o sistema voltará ao ar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55588,
    "customFieldValues": [
      {
        "value": "Como fazer a vinculação de pagamento no extrato bancário?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Para o extrato bancário. \n\nAcessar o menu: Financeiro > Extrato Bancário > “Informar Conta Bancária” > Clicar em “Selecionar” para buscar o arquivo > Clicar no botão “Processar Arquivo”\n\nFeito isso, aparecerá o extrato e os valores sinalizados em “VERMELHO” referem-se aos títulos não conciliados ou não lançados no sistema, já os sinalizados em “AZUL” são os valores já conciliados.\n\nDe acordo com os valores listados, saberemos se são créditos ou débitos para assim acessarmos as rotinas correspondentes, Contas a Pagar, a Receber ou Movimentação Bancária para identificarmos se os títulos estão inseridos e baixados de forma correta no sistema, ver item 2, 3 e 4 a seguir.\nSerá possível neste momento registrar lançamentos de ‘movimentação bancaria’ dos valores sinalizados em “VERMELHO” para finalizar a conciliação bancária. Para isso preecher os campos manualmente conforme abaixo ou ‘vincular’ um lançamento já realizado e conciliar manualmente.\n\nAo ‘salvar’ uma conciliação bancária (integração do extrato bancário), irá aparecer a mensagem perguntando se deseja fechar o período financeiro.\nConfirmar: irá realizar o fechamento automaticamente;\nCancelar: não irá realizar o fechamento automaticamente. Nesse caso, ele precisará ser fechado depois manualmente direto na rotina de Fechamento período financeiro.\n\nA rotina de conciliação será executada mesmo se não ocorrer o fechamento do período.\n\n1. Contas a pagar\nAcessar: Financeiro > Contas a Pagar > Filtrar por “Data de vencimento” e “Filial” > Clicar em “Consultar”\n\nAo localizar o valor a ser conciliado e o mesmo não estiver com status “baixado”, realizar a baixa do valor. Feita a baixa, voltar na tela de “Extrato Bancário” e clicar em voltar para selecionar novamente o extrato e processar o arquivo novamente. Notará que o valor baixado será puxado na cor “AZUL”.\n\n2. Contas a receber\nAcessar: Financeiro > Contas a Receber > Filtrar por “Data de vencimento” e “Filial” > Clicar em “Consultar”.\nInforme a data de vencimento e conta bancária de acordo com o extrato bancário.\n\nAo localizar o valor a ser conciliado e o mesmo não estiver com status “baixado”, realizar a baixa do valor. Feita a baixa, voltar na tela de “Extrato Bancário” e clicar em voltar para selecionar novamente o extrato e processar o arquivo novamente. Notará que o valor baixado será puxado na cor “AZUL”.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55910,
    "customFieldValues": [
      {
        "value": "Resolvido no KB 55911",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido no KB 55911",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido no KB 55911",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55566,
    "customFieldValues": [
      {
        "value": "Numerário de Nacionalização Não Aparece no Contas a Receber",
        "customFieldId": 206842
      },
      {
        "value": "Numerário de Nacionalização Não Aparece no Contas a Receber",
        "customFieldId": 206843
      },
      {
        "value": "Não está gerando um título a receber, pois não há uma operação financeira de \"Numerário câmbio receber\" cadastrado para essa filial.\nSugiro que em \"Operação financeira\" você duplique o cadastro 19 e selecione a filial desejada.\nApós esse procedimento, salve o numerário de câmbio, e o respectivo contas a receber será gerado automaticamente.\n\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55899,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Este caso foi resolvido no ticket 55790.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55123,
    "customFieldValues": [
      {
        "value": "Como desativar follow de importação?",
        "customFieldId": 206842
      },
      {
        "value": "Como desativar um follow de importação no narwal.",
        "customFieldId": 206843
      },
      {
        "value": "\nNesse caso voce pode estar desativando através da rotina Follow de importação, nele voce terá os follow de importação no qual esta sendo enviado aos cliente, ao entrar na rotina precisa editar e inativar , assiim evitando e envair mais follows aos cliente que nao embarcaram.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55667,
    "customFieldValues": [
      {
        "value": " ERRO INTEGRAÇÃO XML NF",
        "customFieldId": 206842
      },
      {
        "value": "incidente",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso foi uma instabilidade pois logo após o erro cliente conseguiu integrar o xml corretamente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55672,
    "customFieldValues": [
      {
        "value": "Integrar XML de DI no processo: Você não possui acesso ao menu selecionado: Importacao/NPI/IntegrarXMLDIProcesso",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Acessar Grupo de usuário e selecionar o campo \"[x] Integrar DI/DUIMP\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55281,
    "customFieldValues": [
      {
        "value": "Cliente não retornou com informações",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não retornou com informações",
        "customFieldId": 206843
      },
      {
        "value": "Cliente não retornou com informações",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53521,
    "customFieldValues": [
      {
        "value": "Processo de entreposto apresentando erro de saldo.",
        "customFieldId": 206842
      },
      {
        "value": "Problema ocorre pois estava sendo gerado os demais processos, sem que a invoice do processo mãe tivesse uma forma de pagamento informada.",
        "customFieldId": 206843
      },
      {
        "value": "Antes de dar sequencia no registro da DI como \"entreposto aduaneiro\" é necessário garantir que a invoice tenha forma de pagamento informada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54532,
    "customFieldValues": [
      {
        "value": "Na rotina \"Produto\" não está sendo listo os produtos quando realizado filtro.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na parte inferior da grid do cadastro de Produto está com um filtro, por esse motivo não esta sendo considerado os campos do filtro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55855,
    "customFieldValues": [
      {
        "value": "Por qual motivo o botão \"Cancelar pedido de compra\" do pedido de compra está inativo.",
        "customFieldId": 206842
      },
      {
        "value": "Pedido de compra já encontra-se fechado.",
        "customFieldId": 206843
      },
      {
        "value": "Pedido de compra está com status Fechado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55837,
    "customFieldValues": [
      {
        "value": "Não estou recebendo o código de acesso",
        "customFieldId": 206842
      },
      {
        "value": "Resolvido no KB 53880",
        "customFieldId": 206843
      },
      {
        "value": "Resolvido no KB 53880",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55764,
    "customFieldValues": [
      {
        "value": "Por que não está aparecendo para selecionar o relatório customizado no fechamento financeiro?",
        "customFieldId": 206842
      },
      {
        "value": "Ao imprimir o relatório de conferência de fechamento, o Narwal abre automaticamente o relatório .aspx ao invés de aparecer para selecionar o relatório personalizado.",
        "customFieldId": 206843
      },
      {
        "value": "Para que seja possível utilizar os relatórios personalizados na rotina de fechamento financeiro, deve-se primeiramente ativar a variável de ambiente \"NWL_IMPRIMIRNOVOFECHAMENTOFINANCEIRO\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55874,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 53892.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55301,
    "customFieldValues": [
      {
        "value": "Quantas vezes as moedas são atualizadas por dia?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Esta atualização ocorre 2x por dia (manhã e tarde) e atualiza a taxa ptax das moedas",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55007,
    "customFieldValues": [
      {
        "value": "Geração de títulos previstos a partir do pedido.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Necessário cadastrar as operações financeiras para a filial que deseja criar os títulos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55395,
    "customFieldValues": [
      {
        "value": "Por que o valor do CIF está incorreto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Está sendo utilizada uma taxa de frete divergente da taxa que estava na planilha do cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55857,
    "customFieldValues": [
      {
        "value": "Mensagem ao enviar NF para SEFAZ: Rejeicao: Valor do Produto difere do produto Valor Unitario de Tributacao e Quantidade Tributavel",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "A mensagem de rejeição do SEFAZ está ocorrendo pois na NF não consta a informação da Unidade tributável.\n\nVocê poderá informar manualmente, para isso:\n\n1-Editar a NF;\n2- Na guia Produto, editar a o produto;\n3- Na guia Informações informar o Valor e Quantidade;  \n\nPara que o campo seja preenchido automaticamente para as próximas notas, você poderá cadastrar a \"Conversão de Unidade de medida\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55809,
    "customFieldValues": [
      {
        "value": "Mensagem ao enviar NF: Informe o Estado do local de desembaraço do item 1",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na Nota Fiscal, guia Transporte verificar a Origem destino. Verificar na rotina Origem destino se o Estado está informado. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55758,
    "customFieldValues": [
      {
        "value": "Qual usuário que estava reabrindo os processos fechados? ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Ao  realizar uma auditoria, verifiquei que era usuário Rhaphael, que estava com os dados da Ventisol. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55848,
    "customFieldValues": [
      {
        "value": "Processo (expo) não retorna na grid.",
        "customFieldId": 206842
      },
      {
        "value": "Isso ocorre por dois motivos, o processo pode ter sido inativado sem querer, ou o filtro de pesquisa não estar de acordo.",
        "customFieldId": 206843
      },
      {
        "value": "O filtro do processo não estava de acordo, estava para trazer apenas processos com a \"posição do processo\" como em \"transito\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54917,
    "customFieldValues": [
      {
        "value": "Como é zerado um saldo de uma importação com entreposto aduaneiro?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Em casos de entreposto aduaneiro, ao decorrer de a carga ser nacionalizada, o saldo irá zerando. Mas em casos onde a mercadoria irá voltar para o fornecedor, por exemplo, ou não vai mais ser nacionalizada, o Narwal não tem um cenário que atenda. Sendo assim, será necessário abrir um processo de expo, caso desejam controlar dentro do Narwal.\nQuanto ao processo de importação mãe, ele ficará com a quantidade em aberto. Contudo, é possível gerar um processo filho apenas pra consumir saldo com alguma identificação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55836,
    "customFieldValues": [
      {
        "value": "Cliente com erro ao enviar nota para prefeitura. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente com registro de notas na prefeitura, estava dando instabilidade de certificado. ",
        "customFieldId": 206843
      },
      {
        "value": "Verificou que o certificado no site da prefeitura estava divergente, pois foi renovado não foi trocado. \nApós fazer alterações notas saíram de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55839,
    "customFieldValues": [
      {
        "value": "Mensagem do Totvs: Exportador não encontrado! EXPORTADOR=",
        "customFieldId": 206842
      },
      {
        "value": "Erro estava ocorrendo ao tentar realizar o envio da NF para o ERP.",
        "customFieldId": 206843
      },
      {
        "value": "Após reiniciar o sistema foi possível realizar o envio da Nota.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55450,
    "customFieldValues": [
      {
        "value": "Cancelamento de Contrato de Cambio",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava fazendo o cancelamento do fechamento de cambio.",
        "customFieldId": 206843
      },
      {
        "value": "Instruido o cliente a realizar o cancelamento pela rotina \"contrato de cambio\" apertando no botão \"X\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55790,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o narwal",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando realizar o login no Narwal, mas ao inserir meus dados e clicar em login, é exibido o erro \"Erro HTTP 500\". O que fazer?",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro foi corrigido em versões superiores à 2024.4.8.0. Para resolver, recomendamos atualizar para uma versão mais recente. Como alternativa, você pode contornar o problema enviando um link de redefinição de senha através da rotina \"Usuário\".\n\nÉ importante observar que, se você optar por enviar o link de redefinição de senha diretamente pela tela de login clicando em \"Esqueci minha senha\", o erro continuará ocorrendo ao tentar acessar, portanto, essa opção não resolverá o problema permanentemente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55071,
    "customFieldValues": [
      {
        "value": "Como ativar o campo \"Cubagem Total\" no processo de exportação?",
        "customFieldId": 206842
      },
      {
        "value": "Como habilitar a edição do campo \"Cubagem Total\", localizado na aba \"Transporte\" em um processo de exportação?",
        "customFieldId": 206843
      },
      {
        "value": "Para habilitar a edição manual do campo \"Cubagem Total\", é necessário verificar o tipo de embalagem vinculada ao processo (na aba \"Embalagens\" do processo) e, em seguida, marcar a opção \"Permite informar cubagem\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54716,
    "customFieldValues": [
      {
        "value": "Dúvida sobre itens com múltiplos NVEs no processo",
        "customFieldId": 206842
      },
      {
        "value": "É possível importar uma planilha de produtos contendo mais de 1 NVE em um mesmo processo?",
        "customFieldId": 206843
      },
      {
        "value": "Atualmente, o Narwal não suporta a importação de planilhas de produtos que contenham mais de 1 NVE para o item em questão.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54496,
    "customFieldValues": [
      {
        "value": "Teremos um caso de importação por encomenda, poderiam informar aonde consigo informar o adquirente no Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Esse item está previsto como melhoria de produto e esta presente em nosso roadmap, contudo ainda não há uma data prevista de liberação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55838,
    "customFieldValues": [
      {
        "value": "Botão de excluir despesas do processo não está sendo exibido.",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando excluir algumas despesas de um processo de importação, mas o ícone de exclusão (\"X\") não está aparecendo. O que posso fazer?",
        "customFieldId": 206843
      },
      {
        "value": "O ícone de exclusão de despesas não é exibido porque há uma ou mais parcelas geradas na rotina de \"Fechamento Financeiro\". Para resolver isso, siga os passos abaixo:\n\nPrimeiro, acesse a rotina de \"Fechamento Financeiro\" e localize o fechamento financeiro relativo ao processo em questão. Dentro dessa rotina, exclua a parcela gerada e, em seguida, clique em \"Salvar\" para registrar a alteração. Após salvar, retorne à aba de despesas do processo, e o ícone de exclusão será exibido, permitindo que você exclua as despesas conforme necessário.\n\nEsse procedimento deve resolver o problema e permitir a exclusão das despesas do processo de importação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55754,
    "customFieldValues": [
      {
        "value": "Estorno de NF complementar",
        "customFieldId": 206842
      },
      {
        "value": "Como posso realizar o estorno de uma nota fiscal complementar?",
        "customFieldId": 206843
      },
      {
        "value": "O estorno deve ser realizado via banco, pois será necessário desvincular a NF complementar das adições.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55739,
    "customFieldValues": [
      {
        "value": "Verificar o motivo das nomenclaturas de despesa, não aparece para usuário?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Verifiquei que no cadastro de usuário não estava com a tag flegada de administrador, para outros usuários do grupo financeiro, estava flegada e as despesas estavam de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55317,
    "customFieldValues": [
      {
        "value": "Nota ficou com uma diferença de valores, cliente deseja saber causa raiz?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "A diferença que ocorreu na nota foram baixa, podendo observar que na planilha da cliente ela faz o rateio por valor CIF, dentro do Narwal as despesas estavam rateadas por valor. \n\nDessa forma podemos observar que a diferença se dá devido ao rateio das despesas. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55808,
    "customFieldValues": [
      {
        "value": "Credito presumido não estava puxando na nota. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário, ao preencher as parametrizações corretas. \n",
        "customFieldId": 206843
      },
      {
        "value": "Cliente ativou a variável NWL_CALCULOCREDITOPRESUMIDO após gerar a nota fiscal, dessa forma as informações do credito presumido, não vieram informadas no XML. \n\nCancelei a nota e gerei novamente veio de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55817,
    "customFieldValues": [
      {
        "value": "Porque ao enviar a NF ao Senior, retorna erro que a transação exige uma parcela?",
        "customFieldId": 206842
      },
      {
        "value": "Chamado 55817",
        "customFieldId": 206843
      },
      {
        "value": "Isso ocorre porque a transação utilizada exige que seja informada uma condição de pagamento, pois no fluxo do Senior, após a emissão da nota fiscal, deve-se gerar um titulo efetivo de câmbio.\n\nNo caso do Narwal, esse titulo irá ser integrado após, via contas á pagar, atualizado com a taxa da DI.\n\nSolução é solicitar ao consultor Senior remover obrigatoriedade da Transação ou informar na aba Cobrança do NArwal, a condição de pagamento no rodapé da tela.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55794,
    "customFieldValues": [
      {
        "value": "Novas parcelas Numerario",
        "customFieldId": 206842
      },
      {
        "value": "Cliente precisa criar uma nova parcela no numerário, porém o botão gerar uma nova some.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário enviar a parcela já aberta para o ERP ou baixa-la, assim liberando o botão novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55767,
    "customFieldValues": [
      {
        "value": "Erro de saldo ao tentar cancelar processo.",
        "customFieldId": 206842
      },
      {
        "value": "Havia 2 processos vinculados ao mesmo pedido, ambos os processos estavam consumindo a quantidade do total do pedido, assim ficando com saldo negativo.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário excluir os itens de um dos processos, e adicionar novos itens, assim permitindo cancelar os processos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55806,
    "customFieldValues": [
      {
        "value": "Por que não estou conseguindo integrar XML da DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O arquivo a ser integrado deve ser um XML. PDF ou outros formatos não serão aprovados pelo Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54874,
    "customFieldValues": [
      {
        "value": "Qual o cálculo do custo unitário do relatório de custo?",
        "customFieldId": 206842
      },
      {
        "value": "Qual o cálculo do custo unitário do relatório de custo.",
        "customFieldId": 206843
      },
      {
        "value": "BaseCustoTotal = ValorSubTotal + ValorIcms + ValorHonorario - ValorDiferencaIcms + ValorIcmsSt + ValorFreteNacional + ValorSeguroNacional + (ValorDespesa - ValorDespesaBaseIcms) - (DescontoCustoMoeda * taxaMoeda) - OutrosDescontos;\nValorDiferencaIcms = ValorIcms - ValorIcmsAntecipado;\nValorDespesa é o somatório de todas as despesas;\n\nValorSubTotal = ValorCif + ValorIi + ValorPis + ValorCofins + Antidumping + ValorDespesaBaseIcms - ValorAcrescimosPrePaid;",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55581,
    "customFieldValues": [
      {
        "value": "Nota fiscal é enviada ao Sênior e permanece como não enviada",
        "customFieldId": 206842
      },
      {
        "value": "Timeout na da request da resposta do Senior para o Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Timeout na da request da resposta do Senior para o Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54245,
    "customFieldValues": [
      {
        "value": "Como realizar fechamento de câmbio para despesas?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Ativar a variável NWL_ATIVATAXAFECHAMENTOBAIXAMANUAL e realizado a baixa manual informando a taxa de fechamento",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55787,
    "customFieldValues": [
      {
        "value": "Narwal fora do ar",
        "customFieldId": 206842
      },
      {
        "value": "Usuario ISS",
        "customFieldId": 206843
      },
      {
        "value": "Identificado pelo TI do cliente que o usuario tinha expirado a senha, após realizar a troca o mesmo voltou a funcionar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55768,
    "customFieldValues": [
      {
        "value": "No processo/Integrar DI o botão Processar não está visível para os usuários.",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "O botão Processar está com a coloração azul clara, nesse caso está visível apenas para os usuários que no cadastro de usuário esteja com campo \"Permitir obrigar campos\" selecionado. Para demais usuários que não tenham permissão, o botão estará oculto.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55235,
    "customFieldValues": [
      {
        "value": "Resolvido com Wiki.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "https://portal.narwalsistemas.com.br/wiki/integrar-xml-da-di/",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55384,
    "customFieldValues": [
      {
        "value": "Resolvido com KB 55089.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55081,
    "customFieldValues": [
      {
        "value": "Erro ao tentar salvar processo. \"Erro(s) de validação : The fiel NumeroPo must be a string or array type with a maximum lenght of '50'.\"",
        "customFieldId": 206842
      },
      {
        "value": "Erro ocorre pois estava sendo informado mais de 50 caracteres no campo \"NumeroPO\".",
        "customFieldId": 206843
      },
      {
        "value": "Diminuir a quantidade de caracteres do campo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55732,
    "customFieldValues": [
      {
        "value": "Duvida no calculo de rateio dos produtos",
        "customFieldId": 206842
      },
      {
        "value": "Duvida do usuário",
        "customFieldId": 206843
      },
      {
        "value": "Usuário conferiu errado os valores total do rateio",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55745,
    "customFieldValues": [
      {
        "value": "Reiniciar Pool aplicação",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Reiniciar Pool aplicação",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55779,
    "customFieldValues": [
      {
        "value": "Ao gerar prévia da Nota Fiscal está gerando a mensagem \"Informe o Estado do local de desembaraço do item 1\"",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Editar a Nota Fiscal e na guia Importação, verificar o local do Desembaraço.\nAcessar a rotina \"Origem destino\" procurar pelo local do desembaraço e informar o Estado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55571,
    "customFieldValues": [
      {
        "value": "Erro na URL ao logar via SSO.",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar realizar o login via SSO no Narwal, o seguinte erro é informado na URL:\nerrormessage=\"OpenIdConnectMessage.Error%20was%20not%20null,%20indicating%20an%20error.%20Error:%20%27invalid_client%27",
        "customFieldId": 206843
      },
      {
        "value": "A client secret expirou, deve-se gerar uma nova e alterá-la no web.config.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55585,
    "customFieldValues": [
      {
        "value": "Porque meu XML da DI está com erro de arquivo?",
        "customFieldId": 206842
      },
      {
        "value": "Resolução chamado 55585",
        "customFieldId": 206843
      },
      {
        "value": "É importante que a estrutura do XML esteja de acordo com a aceita, sem nenhum dado corrompido.\nNo caso desse chamado o xml enviado pelo consultor estava corrompido, foi possível verificar isso tanto abrindo o próprio xml, aonde é possível ver erro de \"This page contains the following errors\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55753,
    "customFieldValues": [
      {
        "value": "Por que os impostos não estão de acordo com a DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O Valor CIF estava incorreto devido a um erro de conversão ao integrar o XML. Após ML integrado novamente, os valores ficaram ok.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55530,
    "customFieldValues": [
      {
        "value": "Erros de Validação ao Gerar DI",
        "customFieldId": 206842
      },
      {
        "value": "Estou enfrentando problemas ao gerar a DI. Estão sendo exibidos os seguintes alertas:\n\n- ValorTotalMLEMoedaNacional: O campo deve ser numérico.\n\n- ValorUnidadeLocalEmbarque: O campo deve ser numérico.\n\nO que devo fazer para resolver?",
        "customFieldId": 206843
      },
      {
        "value": "Essas mensagens indicam que o valor total da mercadoria está negativo. Para resolver o problema, siga os passos abaixo:\n\n1. Verifique o VMLE: Acesse a aba \"Produtos\" do processo e analise o valor do VMLE. Caso o valor esteja negativo, investigue a causa.\n\n2. Revise o Incoterm: Muitas vezes, esse erro ocorre devido ao Incoterm utilizado na invoice. No caso específico, o CFR (Cost and Freight) foi utilizado.\n\n3. O Incoterm CFR estabelece que o vendedor paga o frete até o porto de destino, mas o valor do frete não pode ser incluído no valor da mercadoria.\n\n4. Ajuste na Invoice: Para corrigir, acesse a invoice e desmarque a opção \"Frete Incluso\". Em seguida, atribua manualmente o valor do frete com base no peso bruto da mercadoria.\n\n5. Recalcule o VMLE: Após realizar o ajuste no valor do frete, o VMLE deverá ficar positivo, permitindo o registro da DI.\n\nSe o erro persistir após essas etapas, entre em contato com o suporte para mais assistência.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55043,
    "customFieldValues": [
      {
        "value": "Como cancelar um processo?",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Para cancelar um processo, é necessário acessar a rotina e pesquisar pelo processo desejado.\n\nAssim que encontrado, clicar no menu de ação onde apresentar diversas opções, e uma delas seria \"Cancelar processo\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55686,
    "customFieldValues": [
      {
        "value": "Invalid OFX file ao integrar arquivo na rotina extrato bancário.",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar o arquivo na rotina extrato bancário, o erro 'Invalid OFX file' é disparado.",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina extrato bancário somente é possível integrar arquivos .OFX (tipo de arquivo digital que armazena informações financeiras, como extratos bancários).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55336,
    "customFieldValues": [
      {
        "value": "Processos sem atualizar a data ETD/ETA automaticamente.",
        "customFieldId": 206842
      },
      {
        "value": "Processos sem atualizar a data ETD/ETA automaticamente.",
        "customFieldId": 206843
      },
      {
        "value": "O shipstracking que é responsável por alterar a informação dos campos ETA e ETD, se não estiver disponível para consulta no BL/AWB, não será inserido.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55092,
    "customFieldValues": [
      {
        "value": "Informações Complementares Siscomex não estão sendo listadas para Declaração Duimp.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na Informação complementar Siscomex poderá ser informado o Tipo DI ou Duimp.   ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55162,
    "customFieldValues": [
      {
        "value": "Por que o valor do percentual está zerado na parcela da Invoice?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "As parcelas foram alteradas manualmente, o percentual foi zerado e o valor foi preenchido:\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55715,
    "customFieldValues": [
      {
        "value": "Erro ao tentar autorizar NF no sefaz.",
        "customFieldId": 206842
      },
      {
        "value": "Erro: The 'http://www.portalfiscal.inf.br/nfe:nAdicao' element is invalid - The value '0' is invalid according to its datatype 'String' - The Pattern constraint faild.\n\nErro ocorre pois o numero das adições estava com o valor '0'.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário processar a DI para gerar as adições, assim que gerada as adições é necessário cancelar a NF e gera-la novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55107,
    "customFieldValues": [
      {
        "value": "Nota Fiscal - Emissão pelo Importador",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "É importante considerar que o Narwal possui uma funcionalidade que, quando a flag na filial \"Emite NF pelo Importador\" estiver TRUE, as configurações de numero de série, certificado, ambiente sefaz deve ser informado na aba Nota Fiscal do Cadastro de Importador.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55713,
    "customFieldValues": [
      {
        "value": "Porque não estou recebendo o código de autenticação para realizar o login?",
        "customFieldId": 206842
      },
      {
        "value": "Estou tentando fazer o login, mas não estou recebendo o código de autenticação de 2 fatores.",
        "customFieldId": 206843
      },
      {
        "value": "Peça ao cliente para verificar as pastas de spam e lixo eletrônico, garantindo que o e-mail com o código não foi filtrado. Além disso, confirme se outros usuários estão recebendo o código normalmente. Se apenas um usuário não estiver recebendo, pode haver um bloqueio no e-mail dele ou o código pode ter sido redirecionado para a pasta de spam ou lixo eletrônico.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55690,
    "customFieldValues": [
      {
        "value": "Por que a despesa de Antidumping está sendo criada de forma automática?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A variável NWL_CRIADESANTIDUMPING\t de ambiente estava habilitada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55547,
    "customFieldValues": [
      {
        "value": "Mensagem \"Informe o campo NCM\" ao integrar o xml da DI no processo.",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro NCM campo Chave alterar conforme campo \"Código NCM\"; ou Acessar o processo e alterar as informações manualmente, conforme o xml da DI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55660,
    "customFieldValues": [
      {
        "value": "Token de autenticação",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Por conta da atualização realizada na ultima semana, acabou perdendo o token de autenticação, informamos novamente e a integração deve voltar a ocorrer.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55618,
    "customFieldValues": [
      {
        "value": "SMTP Cliente",
        "customFieldId": 206842
      },
      {
        "value": "Após a atualização do sistema versão 2025.2.1.2 o SMTP do Cliente parou de funcionar.",
        "customFieldId": 206843
      },
      {
        "value": "Colocado o SMTP da Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54589,
    "customFieldValues": [
      {
        "value": "Como resolver pagamento de cambio duplicado",
        "customFieldId": 206842
      },
      {
        "value": "Neste caso, o câmbio do pedido está aparecendo como baixado duas vezes com o mesmo valor, embora o contrato vinculado contenha apenas um valor.",
        "customFieldId": 206843
      },
      {
        "value": "Para ajuste do processo precisamos seguir os seguintes passos:\n\nExcluir o fechamento de cambio do cambio a prazo das 2 invoices do processo;\nEditar o processo e excluir a invoice;\nExcluir os itens do processo da invoice especifica;\nAdicionar um item fictício no processo, salvar e continuar; > não foi necessário pois tinha outra invoice vinculada ao processo.\nExcluir o contrato de cambio antecipado da invoice especifica;\nCriar novo contrato de cambio antecipado vinculado ao pedido de compra;\nCriar a invoice via pedido de compra (por fora do processo);\nVerificar a compensação do adiantamento na invoice;\nEditar o processo e vincular a invoice;\nExcluir o item fictício do processo, salvar e continuar. > não foi necessário pois tinha outra invoice vinculada ao processo;\nAjustar a parcela de cambio futuro (caso especifico de 2 pagamentos);\nRefazer o fechamento de cambio a prazo das 2 invoices do processo.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55654,
    "customFieldValues": [
      {
        "value": "rotina \"Eventos de Integração - Pedido de Compras\"",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Rotina Descontinuada.\n\nA rotina para consultas de logs de integração é:\nQuando Fluid: Evento de Integração\nAlguns ERP padrão: Evento de Integração\nAPI Padrão: Evento do Contas á Pagar\nAlgunas ERP padrão, fluxo antigo: Evento do Contas á Pagar",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55614,
    "customFieldValues": [
      {
        "value": "Como validar cliente sem acesso ao narwal",
        "customFieldId": 206842
      },
      {
        "value": "Neste caso, o cliente estava enfrentando dificuldades ao acessar o Narwal, pois a página caía sempre que realizava o login",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso específico, enviei um link interno de redefinição de senha do Narwal. Com isso, o cliente conseguiu redefinir a senha e continuar o processo normalmente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55367,
    "customFieldValues": [
      {
        "value": "Como puxar logo da empresa ao emitir fatura",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso em especifico voltou a funcionar após reiniciar o servidor",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54673,
    "customFieldValues": [
      {
        "value": "Como fazer a transferência de saldo entre processos? ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Menu Narwal: Financeiro > Contas a pagar e Financeiro > Contas a receber \n\nCriar dois processos, com todo o passo a passo até chegar o fechamento financeiro;  \n\nAcessando uma das contas a receber, indo em baixa manual:  \n\nAlterar para Por compensação Contas a pagar;  \n\nAdicionar linhas de contas a pagar e o valor a utilizar (por padrão vem o valor total);  \n\nSalvar e verificar o resultado final.  \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54759,
    "customFieldValues": [
      {
        "value": "Valor do Produto difere do produto Valor Unitario de Tributacao e Quantidade Tributavel KASVI - Nota Fiscal Sefaz - Valor do Produto difere do produto Valor Unitario de Tributacao e Quantidade Tributavel",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "A rejeição do SEFAZ está ocorrendo pois a informação do \"Valor unid. tributada\" não está informado na NF. Poderá informar manualmente editando o produto e informando  no grupo Unidade tributável. Ou\nNa rotina Conversão de unidade de medida criar a conversão correspondente para que as próximas NFs seja realizado de forma automática.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54275,
    "customFieldValues": [
      {
        "value": "Parametrização NF para ICMS ST",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Para que o valor do ICMS ST resulte corretamente na NF. Na parametrização NF no grupo ICMS informar o CST 10 e no grupo \"ICMS substituição tributária\" no campo CST ICMS ST informar o CST 10.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53775,
    "customFieldValues": [
      {
        "value": "Sequencial da NF na Filial e/ou Importador ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Para informar a numeração sequancial, acesse a rotina \"Nota Fiscal série\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55583,
    "customFieldValues": [
      {
        "value": "Como conceder permissão aos usuários.",
        "customFieldId": 206842
      },
      {
        "value": "Usuário não possui acesso a rotina e gostaria que fosse liberado.",
        "customFieldId": 206843
      },
      {
        "value": "Acessar a rotina \"Grupo usuário\" e escolher o grupo ao qual o usuário está vinculado. Assim que identificado, editar e marcar a flag da rotina que deseja liberar o acesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53639,
    "customFieldValues": [
      {
        "value": "CÓDIGO 217 - STATUS Rejeicao: NF-e nao consta na base de dados da SEFAZ - PROTOCOLO  MENSAGEM: 229 - Rejeicao: IE do emitente nao informada",
        "customFieldId": 206842
      },
      {
        "value": "Envio de NF para SEFAZ: IE do emitente nao informada",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro do Importador ou Filial validar a informação da Inscrição Estadual. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53514,
    "customFieldValues": [
      {
        "value": "Rejeicao: Duplicidade de NF-e, com diferença na Chave de Acesso",
        "customFieldId": 206842
      },
      {
        "value": "Rejeicao: Duplicidade de NF-e, com diferença na Chave de Acesso",
        "customFieldId": 206843
      },
      {
        "value": "A Numeração/Série que está sendo enviada para o SEFAZ já existe no ambiente do ZEFAZ.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54481,
    "customFieldValues": [
      {
        "value": "Como ocultar campo de criar produtos novos, ao integrar xml DI ou DUIMP? ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Ocultação do campo de criar novos produtos ao integrar DUIMP ou xml da DI. \n\nNo processo ao integrar o arquivo, clicar no olho para ocultar o campo, após essa alteração na rotina de cadastro do usuário tirar a tag de permitir e obrigar campo, assim o campo ficará oculto para usuários. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54825,
    "customFieldValues": [
      {
        "value": "Mensagem aparecendo ao retornar a nota de serviço para Narwal. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente encaminhou nota para a prefeitura e ao retornar para Narwal deu a mensagem \"Informe valor da despesa\". ",
        "customFieldId": 206843
      },
      {
        "value": "Nessa situação identificamos que a nota estava com o ISS para o tomador do serviço recolher. \n\nNo cadastro do cliente estava informado uma tag de Recolhe ISS, sendo assim o serviço ele não possuía retenção mas na nota fiscal o valor estava deduzindo o ISS do valor liquido. \n\nCliente retirou a tag de recolhe ISS e a nota saiu de acordo com o informado, e retornando a informação correta para sistema. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55426,
    "customFieldValues": [
      {
        "value": "Como deve estar na parametrização, quando a nota fiscal possui ICMS ST?",
        "customFieldId": 206842
      },
      {
        "value": "Alteração na parametrização. ",
        "customFieldId": 206843
      },
      {
        "value": "Para calcular o ICMS ST de acordo com a planilha. \n\nDentro da rotina de parametrização, ajustamos a parametrização informando o CST de acordo com a tributação da mercadoria, foi ajustado a formula do calculo do ICMS ST. \n\nInformamos para deduzir a despesa base de ICMS, pois a mesma já está sendo utilizada no calculo do ICMS normal, como o ICMS st ela soma o ICMS normal, a despesa não deve estar informada na formula. \n\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55546,
    "customFieldValues": [
      {
        "value": "Somar a despesas Taxa Siscomex na Nota Fiscal de saída.",
        "customFieldId": 206842
      },
      {
        "value": "Fora de escopo",
        "customFieldId": 206843
      },
      {
        "value": "A despesa \"Taxa siscomex\" já entra na NF de entrada por essa ser devida no ato de registro da Declaração de Importação (DI).\nPara que essa despesa seja somado ao valor do produto e base de cálculo do ICMS deverá se inserido a despesa na guia Totais da NF de saída.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55261,
    "customFieldValues": [
      {
        "value": "Ao gerar DI para análise: A cadeia de caracteres de entrada não estava em um formato correto.",
        "customFieldId": 206842
      },
      {
        "value": "Incidente / Falha do usuário",
        "customFieldId": 206843
      },
      {
        "value": "Ao gerar DI para análise ocorreu mensagem: A cadeia de caracteres de entrada não estava em um formato correto..\nEditar a DI e na guia Básicas verificar se está faltando algum caracter especial, por exemplo {}",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54998,
    "customFieldValues": [
      {
        "value": "É possivel lançar duas despesas com codigo de acrescimos de siscomex iguais na DI?",
        "customFieldId": 206842
      },
      {
        "value": "Erro impeditivo de registro de DI na analise:\n001 - código de acréscimo - repetido na mesma adição.",
        "customFieldId": 206843
      },
      {
        "value": "No Siscomex, ao registrar uma Declaração de Importação (DI) com acréscimos, cada tipo de acréscimo deve ser identificado corretamente. No entanto, não é possível incluir dois acréscimos com o mesmo código dentro de uma mesma DI, pois o sistema exige que cada acréscimo tenha um código distinto para evitar duplicidade e inconsistências nos cálculos dos tributos e despesas.\n\nSe houver necessidade de incluir o mesmo tipo de acréscimo mais de uma vez, você pode:\n\nSomar os valores e registrar o acréscimo uma única vez.\n\nVerificar se há um código alternativo que possa ser utilizado para diferenciar as ocorrências.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55513,
    "customFieldValues": [
      {
        "value": "Por que o valor de ICMS está incorreto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Parametrização estava com a fórmula incorreta.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55560,
    "customFieldValues": [
      {
        "value": "Documentos faltantes nos processos.",
        "customFieldId": 206842
      },
      {
        "value": "Ao abrir os processos, os documentos sumiram.",
        "customFieldId": 206843
      },
      {
        "value": "Validar se a variável de ambiente NWL_ROOTGESTAODOCS está apontando para o local correto no servidor, e se existe a pasta do processo com os docs.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54740,
    "customFieldValues": [
      {
        "value": "Quando o processo não tem frete e seguro e pede para informar uma Fórmula?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Para os processos que não tem valor algum, no campo de formula dentro do frete é só informar como valor no cálculo do seguro, que o campo vai ficar sem obrigatoriedade de preenchimento. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54949,
    "customFieldValues": [
      {
        "value": "Como a Narwal garante a segurança dos dados no sistema?",
        "customFieldId": 206842
      },
      {
        "value": "Como a Narwal protege os dados no sistema, incluindo o uso de criptografia, firewall, VPN, MFA/2FA, monitoramento de logs, SIEM e proteção contra DDoS.",
        "customFieldId": 206843
      },
      {
        "value": "A infraestrutura Narwal conta com criptografia na VPN e nas conexões aos sites e endpoints de APIs e Portais através de protocolos de encriptação (SSL para WEB e TLS para VPN contra ataques de Man-In-the-Middle), o produto possui MFA também (consultar versões).\n\n\n\nRealizamos monitoramento de ambientes ativamente 24h através de Zabbix + Grafana + Monitoramento ativo de banco de dados que disparam chamados e alertas automaticamente quando detectado anomalias nos servidores.\n\n\n\nA rede Narwal conta com Firewall Fortinet + IDS + IPS + Anti DDoS + Firewall de Segmentação Interna + ACLs para ambientes privados (caso solicitado).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55034,
    "customFieldValues": [
      {
        "value": "Chamado aberto erroneamente.",
        "customFieldId": 206842
      },
      {
        "value": "Chamado aberto erroneamente.",
        "customFieldId": 206843
      },
      {
        "value": "Chamado aberto erroneamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54852,
    "customFieldValues": [
      {
        "value": "Quais valores alimentam meu fluxo de caixa?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Todos os valores abertos no Contas á Pagar e Receber, ao qual foi informado a conta bancária destino irão alimentar a rotina de fluxo de caixa, independente da natureza do título.\n\nTitulos baixados/cancelados/excluídos já não compõem pois a finalidade do modulo é controlar valores á pagar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55537,
    "customFieldValues": [
      {
        "value": "Erro ao enviar nota fiscal de entrada para o ERP ",
        "customFieldId": 206842
      },
      {
        "value": "ERRo \"Internal error (-5002)\"",
        "customFieldId": 206843
      },
      {
        "value": "O incidente ocorreu devido a uma divergência entre a chave de despesa da nota fiscal e o mapeamento de de/para no SAP",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54030,
    "customFieldValues": [
      {
        "value": " Nota Fiscal de Transito com erro de calculo quando com diferimento ICMS",
        "customFieldId": 206842
      },
      {
        "value": "notas de transito originadas de notas fiscais com diferimento de ICMS, não possui o calculo correto.",
        "customFieldId": 206843
      },
      {
        "value": "por padrão o sistema não soma o valor do ICMS Diferido nos produtos ou no total da nota fiscal, por isso que a nota de transito não está somando, verifiquei que a nota de entrada foi colocado formula para somar o diferimento no total da nota fiscal, caso seja realmente necessário somar o diferimento para fechar os valores e consequentemente somar na nota fiscal de transito, deve ser colocado na formula essa configuração.Além dessa configuração a variável NWL_UTILIZAFORMULAPARAMNFETRANSITO deve ser sim, para considerar a formula da parametrização para os cálculos dos totais da nota fiscal de transito.\"\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55503,
    "customFieldValues": [
      {
        "value": "Valor do produto na Nota Fiscal de anulação estava divergente da NF original. ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na Nota Fiscal de anulação, guia Totais  não constava as despesas;",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55151,
    "customFieldValues": [
      {
        "value": "Porque retorna erro de certificado vencido se o mesmo está dentro da validade?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "È importante que todos os dados cadastrados no E-notas estejam identicos no Narwal.\nInclusive a chave gerada para o cliente no Enotas, incluído na aba NFSe do cadastro da filial (chave alfa numérica)",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54978,
    "customFieldValues": [
      {
        "value": "Valor de Frete sendo calculado nas despesas do processo mesmo tendo Incoterm DAP",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Para que o problema parasse de ocorrer, desabilitada a variável de ambiente NWL_CRIADESPFRETE, dessa forma, só irá criar a despesa de frete quando processadas despesas na aba numerário e se o valor do Frete estiver como Collect na aba valores.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55164,
    "customFieldValues": [
      {
        "value": "Campo personalizado trazendo dados de forma automática",
        "customFieldId": 206842
      },
      {
        "value": "Porque quando crio um processo novo, meu campo personalizado está trazendo dados de forma automática?",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver essa situação, é necessário identificar qual campo personalizado está preenchendo os dados automaticamente. Em seguida, clique no ícone de edição ao lado do campo, apague o conteúdo do campo \"Valor\" e salve as alterações. Ao deixá-lo em branco, os próximos processos manterão o campo personalizado vazio, permitindo que ele seja preenchido manualmente conforme as especificidades de cada processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55514,
    "customFieldValues": [
      {
        "value": "Erro ao tentar excluir invoice \"Não é possível excluir a informação devido ao vinculo -> FK_dbo.NotaFislcaDespesaProduto_dbo.ItemProcesso\".",
        "customFieldId": 206842
      },
      {
        "value": "Quando é retornado esse erro ao tentar excluir a invoice, é por conta que o processo possui NF despesa vinculado.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário cancelar as despesas criadas na rotina \"Nota fiscal despesa\", após excluir é possível cancelar a invoice.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53890,
    "customFieldValues": [
      {
        "value": "Quando utilizada a TAG da taxa AFRMM na DI, deve puxar o valor da moeda negociada para a despesa ou o valor na moeda da Invoice ?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "As TAGs {MOEDA.TAXA.CE} e {TAXA.CE.MOEDA} trazem a CE Mercante com moeda que é inserida na Invoice.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54581,
    "customFieldValues": [
      {
        "value": "Erro ao enviar dados no sankhya",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava sem conseguir enviar dados das invoices do narwal ao sankhya",
        "customFieldId": 206843
      },
      {
        "value": "O integrador legado foi desligado e a migração para a plataforma Fluid foi concluída com sucesso. Com essa mudança, todas as integrações da Proauto ocorrerão normalmente a partir de agora.\nSe a integração por algum motivo parar validar o log de erro da Fluid.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55101,
    "customFieldValues": [
      {
        "value": "Por que o valor do ICMS está somando no fechamento financeiro mesmo que eu exclua do processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Quando uma despesa é criada de forma automática pelo Narwal, sempre irá aparecer no fechamento financeiro, mesmo que seja excluída manualmente no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54855,
    "customFieldValues": [
      {
        "value": "ALTERAÇÃO PREVISÃO ETA E ETA",
        "customFieldId": 206842
      },
      {
        "value": "ALTERAÇÃO PREVISÃO ETA E ETA\n",
        "customFieldId": 206843
      },
      {
        "value": "Valide o XML da DI: Certifique-se de que o XML da DI está correto e conforme as especificações exigidas.\n\nVerifique a data no XML: Verifique se a data presente no XML corresponde à data desejada.\n\nProblema de alteração de data: Se ao tentar alterar a data, o sistema não permitir, isso pode ocorrer porque a data da integração da DI foi definida pelo despachante. Nesse caso, o sistema retorna automaticamente a data de integração previamente registrada.\n\nSolução: Em situações como essa, a solução é garantir que a data no XML esteja correta antes da integração. Caso a data precise ser alterada, é importante verificar com o despachante ou responsável pela integração para que o sistema permita a atualização corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55480,
    "customFieldValues": [
      {
        "value": "Erro ao importar planilha de produtos",
        "customFieldId": 206842
      },
      {
        "value": "Porque quando vou integrar uma planilha de produtos está retornando a mensagem \"\"The operation failed: The relationship could not be changed because one or more of the foreign-key properties is non-nullable. When a change is made to a relationship, the related foreign-key property is set to a null value. If the foreign-key does not support null values, a new relationship must be defined, the foreign-key property must be assigned another non-null value, or the unrelated object must be deleted.\"?",
        "customFieldId": 206843
      },
      {
        "value": "Para solucionar este problema, é necessário preencher a coluna PRODUTO_REFERENCIA, pois o erro ocorre quando ela está em branco.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54682,
    "customFieldValues": [
      {
        "value": "Como identificar token fixo e dinâmico?",
        "customFieldId": 206842
      },
      {
        "value": "Como identificar token fixo e dinâmico?",
        "customFieldId": 206843
      },
      {
        "value": "No web.config da API é possível descobrir se o token de autenticação da API é fixo ou dinâmico.\n\nCaso a tag UseTokenAuthentication estiver como \"false\" o token é fixo, caso esteja como \"true\" o token é dinâmico.\n\nCaso o token seja fixo, é preciso ter valor na tag \"ApiKeyAuthentication\", caso não tenha valor nas novas versões a API ficará bloqueada por motivos de segurança.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55304,
    "customFieldValues": [
      {
        "value": "Relatório Previsão Numerário tipo despesas em branco",
        "customFieldId": 206842
      },
      {
        "value": "O cliente interpôs um intervalo de tempo final  igual 31/04/2025, como não existe 31/04/2025, o relatório implementou um parâmetro de data padrão -\"1990/01/01\" o que causou o relatório gerando em branco. ",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso, o relatório foi gerado em branco devido à inserção de uma data inválida (31/04/2025). A solução foi ajustar a data para um valor válido, visto que não existe 31/04/2025. Uma data válida seria, por exemplo, 30/04/2025.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55152,
    "customFieldValues": [
      {
        "value": "Lentidão de sistema",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Lentidão resolvida com a infra no qual servidor estava com 100% da CPU",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55029,
    "customFieldValues": [
      {
        "value": "Meu Ships Tracking não está funcionando",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "As variáveis de ambiente devem estar configuradas de acordo com a imagem abaixo:\n(vide imagem no chamado 55029)\nIsso já está ok no ambiente.\n\nDentro do processo:\n\nCaso seja marítimo:\n      \nInformar o armador;\nInformar o número do container ou do booking;\nsalvar o processo;\napertar no botão \"Consulta shipstracking\" na aba transporte (caso use container) ou na aba tracking (caso use booking).\n\nCaso seja aéreo:\n\nInformar o AWB na aba embarque (apenas os números (11 dígitos));\nSalvar o processo\nClicar no botão consulta shipstracking da aba embarque\n\nGeralmente a consulta demora umas 12 horas para retornar os dados na tela do tracking.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54946,
    "customFieldValues": [
      {
        "value": " Integração: inconsistência nas datas",
        "customFieldId": 206842
      },
      {
        "value": "Ao abrir a nota o campo Data de emissão / Data Vencimento estão preenchidos no Narwal. No entanto quando observado no SAP as datas estão diferentes.",
        "customFieldId": 206843
      },
      {
        "value": "Identificamos que enviávamos o campo DocDueDate(Data vencimento) o campo dataCadastro do Narwal, agora ajustamos para buscar o campo data de vencimento informado de dentro da nota que é o comportamento correto. \n\n\n\nQuanto ao campo DocDate que seria o campo data de lançamento/ Data do documento no SAP B1 estamos enviando a informação da data de integração com o ERP SAP B1 que é o comportamento correto segundo própria consultoria SAP B1, visto que a data de criação do documento é a mesma que será integrada, sendo assim não é necessário o ajuste nessa data\n\nOBS: A Data do documento SAP é o SAP que atualiza de acordo com a data de lançamento enviada para o ERP. Caso seja necessário o envio ou algum outro comportamento diferente disso, deve ser tratado via F08, para que a equipe avalie e desenvolva caso aprovado. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54787,
    "customFieldValues": [
      {
        "value": "Chamado aberto erroneamente.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente relatou que a nota estava sem saldo mas o saldo já havia sido consumido em outra nota.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente relatou que a nota estava sem saldo mas o saldo já havia sido consumido em outra nota.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54526,
    "customFieldValues": [
      {
        "value": "Dúvida sobre o rateio do acréscimo",
        "customFieldId": 206842
      },
      {
        "value": "Após integrar o xml da DI e adicionar todas as despesas do Processo o cliente calculou os impostos parar gerar o relatório de Custo Importação Própria. Ao analisar o relatório, o cliente percebeu que o valor do Acréscimo (taxa CE Mercante) não foi rateado entre os itens conforme a regra de cálculo aplicada para a Despesa.",
        "customFieldId": 206843
      },
      {
        "value": "O sistema está considerando os valores dos acréscimos por adição como está no XML. da DI . Para isso não ocorrer, as adições teriam que estar com a opção abaixo desflegada \"Desativar rateio automático por..\" na rotina de Declaração de Importação, Aba \"Valor aduaneiro\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55343,
    "customFieldValues": [
      {
        "value": "Erro SOAP conexão Senior",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "esse erro foi causado por falta da comunicação com Servidor do Sênior.\nQuando isso ocorre é porque o servidor do WSDL do Sênior está fora do ar. O Cliente deve ser acionado para que ative esse serviço do lado deles.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55447,
    "customFieldValues": [
      {
        "value": "Porque meus impostos não consideram o acrescimo lançado no numerário?",
        "customFieldId": 206842
      },
      {
        "value": "Despesa lançada no local errado",
        "customFieldId": 206843
      },
      {
        "value": "mportante que para o calculo dos impostos na aba Numerário considerem um acrescimo, ele precisa estar já informado na aba pré-calculo ou na própria tabela pré calculo a ser processada, porém, precisa estar informado despesa/valor antes do processamento.\n\n\n\n​Feito isso em chamada, tivemos então o valor do II recalculado.\n\nImportante levar em conta que o tipo de rateio da despesa, o valor aduaneiro da adição e peso liquido da adição, pode vir a dar alguma diferença de valor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53663,
    "customFieldValues": [
      {
        "value": "Baixa manual/fechamento de câmbio em títulos de previsão no Narwal estão excluindo os títulos no Sênior.",
        "customFieldId": 206842
      },
      {
        "value": "Usuário tenta realizar baixa manual ou um fechamento de câmbio no contas a pagar em título de previsão, título não é mais encontrado no ERP Sênior",
        "customFieldId": 206843
      },
      {
        "value": "Isso é um comportamento padrão no fluxo Narwal x Sênior. É necessário efetivar o título de previsão para realizar a baixa dele. Efetive o título criando um contrato de câmbio de adiantamento ou aguarde até a criação da Nota fiscal para realizar o fechamento de câmbio",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55136,
    "customFieldValues": [
      {
        "value": "Qual a taxa usada para os gerar os títulos efetivos de produto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "É utilizada a taxa da DI",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54922,
    "customFieldValues": [
      {
        "value": "Despesas geradas automaticamente a partir do processamento da DI não vem com a flag \"Cria Financeiro\" ativadas",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Esse é um comportamento padrão, pois é necessário informar o fornecedor e a data de vencimento para que o título seja criado corretamente.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55248,
    "customFieldValues": [
      {
        "value": "Campo Measure não sendo emitido no relatório packing list",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não estava preenchendo o campo para a base de calculo.",
        "customFieldId": 206843
      },
      {
        "value": "Dentro do Container precisa ser informado a \"quantidade no container\" para realizar a base de calculo e ser emito no relatório, caso contrario ele entende como NULL e deixa em branco.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54299,
    "customFieldValues": [
      {
        "value": "Valor da nota fiscal em cenário de recolhimento de IIcom divergência após recalcular no Sênior",
        "customFieldId": 206842
      },
      {
        "value": "Valores da NF são enviados corretamente, porém, ao recalcular no Sênior o valor fica incorreto.",
        "customFieldId": 206843
      },
      {
        "value": "Solução aplicada internamente no Sênior pelo cliente: criação de uma parametrização de NF onde o custo do produto passa a ser valor da mercadoria + valor de frete para processos que tem recolhimento de II.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55412,
    "customFieldValues": [
      {
        "value": "Despesa AFRMM não estava somando a BC do ICMS. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário. \n",
        "customFieldId": 206843
      },
      {
        "value": "Despesa AFRMM não estava somando a BC do ICMS, dessa forma verificamos que no tipo despesa ela estava informando somente como custo do produto. \n\nAlteração feita para base de ICMS e a informação puxou de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55332,
    "customFieldValues": [
      {
        "value": "Erro no envio de follow",
        "customFieldId": 206842
      },
      {
        "value": "Operação incorreta",
        "customFieldId": 206843
      },
      {
        "value": "Follow estava inativo, após ativar o mesmo funcionou corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55094,
    "customFieldValues": [
      {
        "value": "Duplicidade de Fabricantes",
        "customFieldId": 206842
      },
      {
        "value": "Integração de XML",
        "customFieldId": 206843
      },
      {
        "value": "Ao integrar o XML o cliente estava informando um fabricante que estava desativado assim gerando mais um com as mesmas informações no sistema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55239,
    "customFieldValues": [
      {
        "value": "Mensagem sefaz: The 'http://portalfiscal.inf.br/nfe:xPed' element is invalid - The value 'INV1747 + INV1748' is invalid according to its datatype 'String' - The actual lenght is greater than the MaxLenght value.",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro ocorre quando no XML o elemento \"xPed\" possui mais de 15 caracteres.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário cancelar a NF, após cancelar a NF, alterar no processo o campo \"Referência adquirente / numero po\" para ter menos de 15 caracteres.\n\nAssim que alterado no processo, a NF pode ser gerada novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55095,
    "customFieldValues": [
      {
        "value": "Por que a despesa base de imposto reduz a base de ICMS?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Havia uma variável de ambiente (NWL_PREPAIDICMS) que estava habilitada, descontando a base de imposto da base de ICMS.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55028,
    "customFieldValues": [
      {
        "value": "É possível configurar o número de casas decimais do campo 'quantidade' nas NFes enviadas para o Senior?",
        "customFieldId": 206842
      },
      {
        "value": "Sim temos uma variável de ambiente NWL_SENIORDECIMAISNAQTDNFE que altera isso",
        "customFieldId": 206843
      },
      {
        "value": "Sim temos uma variável de ambiente NWL_SENIORDECIMAISNAQTDNFE que altera isso",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55293,
    "customFieldValues": [
      {
        "value": "Produtos não integrando",
        "customFieldId": 206842
      },
      {
        "value": "Senior Sapiens foi atualizado e em algumas situações essa atualização faz o integrador perder as referencias.",
        "customFieldId": 206843
      },
      {
        "value": "Atualizar as referencias no integrador e gerar uma nova DLL.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55258,
    "customFieldValues": [
      {
        "value": "lentidão Sistema narwal",
        "customFieldId": 206842
      },
      {
        "value": "incidente",
        "customFieldId": 206843
      },
      {
        "value": "A lentidão foi identificada como sendo relacionada a instabilidade, mas logo foi resolvida e o sistema voltou a operar normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54417,
    "customFieldValues": [
      {
        "value": "Forma de pagamento em branco",
        "customFieldId": 206842
      },
      {
        "value": "Ao registrar a forma de pagamento, em alguns casos, a grid pode não exibir o lançamento de imediato, o que pode dar a impressão de que a parcela não foi gerada.",
        "customFieldId": 206843
      },
      {
        "value": "Uma das soluções para esse caso é resetar a grid \"Forma de pagamento\". Após o reset e o retorno ao estado atual, a parcela lançada deverá ser exibida corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55337,
    "customFieldValues": [
      {
        "value": "Ao criar a NF está sendo gerado a mensagem: Saldo insuficiente",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Acessar a rotina Nota Fiscal e verificar se já existe NF criada para o processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54854,
    "customFieldValues": [
      {
        "value": "Mensagem ao enviar NF ao SEFAZ: Informe a cidade o fornecedor da Nota Fiscal",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Acesse o cadastro do fornecedor, os campos Estado e Cidade devem estar preenchidos. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55231,
    "customFieldValues": [
      {
        "value": "Como gerar nota fiscal, puxando alíquota correta do crédito presumido?",
        "customFieldId": 206842
      },
      {
        "value": "Cliente com nota que tinha crédito presumido e a alíquota que puxava era alíquota do ICMS. ",
        "customFieldId": 206843
      },
      {
        "value": "Para que a nota fiscal puxe com o crédito presumido precisa ser informado os percentuais dentro da parametrização, e também o código do crédito presumido. \n\nDentro da rotina de Variáveis de Ambiente, na variável \" NWL_CALCULOCREDITOPRESUMIDO\", precisa estar informado no Valor com o número da variável que corresponde ao calculo, nessa situação que o percentual Credito presumido estava igual ao percentual do ICMS, vai ser informada a variável 2. \n\n2= BC ICMS * PERCENTUAL DO CRÉDITO PRESUMIDO. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54321,
    "customFieldValues": [
      {
        "value": "Habilitar botão \"Adiantamento manual\" na tela de invoice",
        "customFieldId": 206842
      },
      {
        "value": "Após atualizar o ambiente o botão \"Adiantamento manual\" não está mais aparecendo na tela de Invoice",
        "customFieldId": 206843
      },
      {
        "value": "Desabilitar a variável NWL_PROCESSAACCAUTOMATICAMENTE",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55115,
    "customFieldValues": [
      {
        "value": "Saldo do processo item não pode ser menor que zero",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada.",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55066,
    "customFieldValues": [
      {
        "value": "Background job creation failed. See inner exception for details",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Após atualizar versão não ocorreu a mensagem Background job creation failed. See inner exception for details ao salvar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54628,
    "customFieldValues": [
      {
        "value": "Por que o valor total das despesas base ICMS está incorreto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Pois no tipo despesa as configurações não estão de acordo, é necessário realizar os ajustes informando se a despesa é mesmo base de ICMS.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55134,
    "customFieldValues": [
      {
        "value": "Por que o valor do ICMS está sendo gerado negativo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Na exceção fiscal desta NCM a flag de diferimento sobre alíquota não estava marcada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54110,
    "customFieldValues": [
      {
        "value": "Por que os valores ficam incorretos ao integrar XML da DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Nos processos CIP – CIF – CFR – CPT, ao integrar o XML da Declaração de Importação que contenha registros de Incoterms com frete e/ou seguro prepaid, é crucial revisar as informações das abas:\n\nAba Invoice (campos de frete e seguro incluso);\n\nAba Valores (campos de “valor frete prepaid” e “valor frete collect”, “flag de frete prepaid incluso” e no seguro os campos “prepaid” e “collect” );\n\nAba Produtos (campos de Preço).\n\nNão há uma maneira de determinar as informações pro processo como, a flag de frete incluso e se os valores de frete e seguro já estão embutidos no preço da mercadoria. Por isso, após a integração do XML, é necessário revisar essas informações da DI e ajustar manualmente se necessário.\n\nPortanto, em processos que envolvam este tipo de Incoterm, é realmente crucial que seja feita esta revisão de valores.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55148,
    "customFieldValues": [
      {
        "value": "COmo validar erro de Timeout na extração de dados para o BI",
        "customFieldId": 206842
      },
      {
        "value": "Incidente ao fazer extração de dados do BI",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro é reflexo dos erros que estávamos recebendo também nas APIs de Integração de Pedido.\n Realizado limpeza de logs e serviço windows no ambiente e a parte de Pedidos voltou ao normal.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54693,
    "customFieldValues": [
      {
        "value": "Informar dentro da parametrização como excluir o ICMS da BC do pis e cofins. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Para nota fiscal de Encomenda, onde na BC do PIS/COFINS, não deve mais estar incluído o ICMS, dessa forma orientação é que dentro da parametrização utilizada, que fosse informado a formula para o calculo. \n\n\"Valor total - ICMS\" \n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55184,
    "customFieldValues": [
      {
        "value": "instabilidade no BI do cliente",
        "customFieldId": 206842
      },
      {
        "value": "instabilidade no BI do cliente",
        "customFieldId": 206843
      },
      {
        "value": "instabilidade no BI do cliente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55183,
    "customFieldValues": [
      {
        "value": "Existem outras invoices que não estão no XML ou JSON, é necessário excluir antes de continuar",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "O numero da Invoice está diferente do numero da FATURA COMERCIAL no XML da DI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55205,
    "customFieldValues": [
      {
        "value": "Cadastro do fabricante com chave inválida",
        "customFieldId": 206842
      },
      {
        "value": "O cadastro do fabricante no narwal estava com uma chave GUID",
        "customFieldId": 206843
      },
      {
        "value": "Informar uma chave no cadastro do fabricante que exista no Sankhya",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54443,
    "customFieldValues": [
      {
        "value": "Erro de permissão ao integrar pedido de compra via modelo de inserção",
        "customFieldId": 206842
      },
      {
        "value": "O consultor relata que estava com problemas ao tentar integrar pedido de compra via modelo de inserção.",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver este caso, verificamos que  ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55198,
    "customFieldValues": [
      {
        "value": "Informe a sigla da unidade de medida no item processo",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver esse caso, é necessário identificar qual unidade de medida está associada aos itens do processo. Neste caso, a unidade de medida utilizada foi \"CONJUNTOS\". O erro \"Informe a sigla da unidade de medida no item processo\" significa que, no cadastro da unidade de medida vinculada ao item do processo, a sigla não foi cadastrada.\n\nPara corrigir, basta acessar a rotina \"Unidade de medida\", verificar qual unidade de medida está vinculada aos itens do processo e atribuir a sigla no cadastro da unidade. Neste caso, a sigla utilizada para a unidade \"CONJUNTOS\" foi \"CJ\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55130,
    "customFieldValues": [
      {
        "value": "Envio da nota fiscal com mensagem do Gcred em tela, não conseguindo enviar ao sefaz. ",
        "customFieldId": 206842
      },
      {
        "value": "Nota fiscal com credito presumido, cliente estava enviando a nota para sefaz e dava mensagem em tela do Gcred",
        "customFieldId": 206843
      },
      {
        "value": "Verificado que no XML, não estava puxando informação do código credito presumido, por que o cliente dentro da parametrização estava informando no campo incorreto. \n\nO correto para parametrização de saída, é código crédito presumido, cliente informando no código beneficio. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55138,
    "customFieldValues": [
      {
        "value": "NCM null no item do pedido de compra - Senior",
        "customFieldId": 206842
      },
      {
        "value": "O integrador estava montando o JSON do pedido sem informar o NCM do item, pois a regra parametrizada era de buscar o NCM do produto já cadastrado no Narwal. E esse produto por sua vez estava sem NCM",
        "customFieldId": 206843
      },
      {
        "value": "Alterada Key (ConsultaNcmProduto) no config do integrador para preencher o NCM no JSON com o CODCLF que vem no pedido, ao inves de buscar do cadastro do produto no Narwal",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55100,
    "customFieldValues": [
      {
        "value": "Erro ao Salvar a DUIMP",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "A despesa vinculada a DUIMP não está relacionada com o Acréscimo do SISCOMEX, após apontar os dois para o mesmo foi possível salvar a DUIMP ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54942,
    "customFieldValues": [
      {
        "value": "Integração NF Despesa, campos N° e Série",
        "customFieldId": 206842
      },
      {
        "value": "Número e a Série foram informados dentro do Narwal, contudo, dentro do SAP não constam",
        "customFieldId": 206843
      },
      {
        "value": "hoje não possuímos a integração do numero da NF e da Serie no padrão de integração, caso o cliente deseje que integre deverá ser aberto um F08 para analisarmos a viabilidade desse campo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55075,
    "customFieldValues": [
      {
        "value": "Como inativar cadastro de importador?",
        "customFieldId": 206842
      },
      {
        "value": "Como inativar cadastro de importador dentro do narwal.",
        "customFieldId": 206843
      },
      {
        "value": " é possível realizar a inativação do importador. Para isso, basta acessar a rotina de importador>adicionar o código ou nome do importador desejado> editar > clicar em inativar e salvar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54725,
    "customFieldValues": [
      {
        "value": "Follow não envia para alguns e-mails.",
        "customFieldId": 206842
      },
      {
        "value": "Apenas um endereço de cliente no cadastro do follow-up não estava recebendo os follows.",
        "customFieldId": 206843
      },
      {
        "value": "TI do cliente deve verificar o motivo de não estar recebendo e-mails. Possivelmente alguma configuração de segurança do sistema de e-mails.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53918,
    "customFieldValues": [
      {
        "value": "Nota fiscal de despesa não integra",
        "customFieldId": 206842
      },
      {
        "value": "Nota fiscal de despesa não integra",
        "customFieldId": 206843
      },
      {
        "value": "O cliente não preencheu um campo obrigatório exigido pelo SAP: a Data de Vencimento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55182,
    "customFieldValues": [
      {
        "value": "Falha ao carregar dados anexos ao recebimento(Filial)",
        "customFieldId": 206842
      },
      {
        "value": "No recebimento, o campo Filial estava em branco.",
        "customFieldId": 206843
      },
      {
        "value": "Realizar o preenchimento do campo Filial.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53966,
    "customFieldValues": [
      {
        "value": "Problemas ao realizar a conciliação bancária",
        "customFieldId": 206842
      },
      {
        "value": "Como sei quando minha operação de conciliação do extrato bancário teve sucesso?",
        "customFieldId": 206843
      },
      {
        "value": "Se o valor for idêntico, ele será reconhecido automaticamente.\n\nVermelho: Indica o valor não identificado.\nVerde: Refere-se aos valores já conciliados em outro momento com o extrato.\nAzul: Significa que o valor foi identificado corretamente.\n\nCaso o valor não seja reconhecido, é necessário realizar a conciliação. Por exemplo, se no extrato há um recebimento de 50,00 e, nas contas a receber, existem dois valores de 25,00 do mesmo pagador, será necessário conciliar esses valores manualmente, via tela.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55091,
    "customFieldValues": [
      {
        "value": "Valores de impostos incorretos",
        "customFieldId": 206842
      },
      {
        "value": "Valores do custo de importação estava incorreto",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso foi calculado impostos e dessa forma os valores ficaram corretos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55040,
    "customFieldValues": [
      {
        "value": "AUTHENTICATION: USER NOT AUTHORIZED",
        "customFieldId": 206842
      },
      {
        "value": "Atualização Protheus",
        "customFieldId": 206843
      },
      {
        "value": "Após atualizar sistema Protheus não foi possível salvar no Narwal ocasionando mensagem AUTHENTICATION: USER NOT AUTHORIZED.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54997,
    "customFieldValues": [
      {
        "value": "Modalidade importação Conta e Ordem no PDF da DI quando a importação é Encomenda",
        "customFieldId": 206842
      },
      {
        "value": "n/a",
        "customFieldId": 206843
      },
      {
        "value": "\nIsso ocorre porque, no Portal Siscomex, não há uma opção de declaração de importação especificamente denominada \"Encomenda\". Dessa forma, como o sistema Narwal foi desenvolvido com base nas mesmas premissas do Siscomex, por isso a informação que fica evidenciada nos documentos oficiais PDF e XML é apenas Conta e ordem. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55154,
    "customFieldValues": [
      {
        "value": "Rejeição: Informado código de município diferente de \"9999999\" para operação com o exterior",
        "customFieldId": 206842
      },
      {
        "value": "Informação errada no cadastro do fornecedor",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro do Fornecedor, quando o PAÍS é do Exterior, obrigatoriamente a Cidade e Estado devem ser do Exterior.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55093,
    "customFieldValues": [
      {
        "value": "NF sem Pis Cofins",
        "customFieldId": 206842
      },
      {
        "value": "Nota integrando sem PIS/COFINS",
        "customFieldId": 206843
      },
      {
        "value": "Reenviada a mesma requisição e o valor integrou",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53889,
    "customFieldValues": [
      {
        "value": "Separando assuntos no atendimento",
        "customFieldId": 206842
      },
      {
        "value": "Separando assuntos no atendimento",
        "customFieldId": 206843
      },
      {
        "value": "Separando assuntos no atendimento",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55099,
    "customFieldValues": [
      {
        "value": "Como configurar uma despesa para não ir para o fechamento financeiro?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Despesas pagas pelo importador e despachante entram no fechamento. Quando é paga pelo cliente não entra. Poderia realizar esta alteração na aba \"DI/DA\" do processo, campo \"Impostos Estaduais\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53934,
    "customFieldValues": [
      {
        "value": "Código de autenticação não chega no e-mail.",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54711,
    "customFieldValues": [
      {
        "value": "cEAN inválido ao enviar nota para o SEFAZ.",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar enviar a nota para o SEFAZ, o erro \"cEAN é inválido\" é disparado.",
        "customFieldId": 206843
      },
      {
        "value": "Dentro do cadastro de produto, no campo \"Código EAN\", deve-se inserir do valor correto ou retirá-lo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54630,
    "customFieldValues": [
      {
        "value": "Por que constou erro ao tentar integrar XML de uma DI no processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O erro ocorreu porque havia mais Invoices no processo do que no XML integrado. Assim, quando um processo já contém uma Invoice criada e um XML de DI será integrado, é essencial que a quantidade de Invoices seja a mesma.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55089,
    "customFieldValues": [
      {
        "value": "ERRO AO REGISTRAR DI - NAO PUXA DESCRIÇÃO DO ITEM",
        "customFieldId": 206842
      },
      {
        "value": "ERRO AO REGISTRAR DI - NAO PUXA DESCRIÇÃO DO ITEM",
        "customFieldId": 206843
      },
      {
        "value": "Ajustar a descrição em rotina composição de descrição na DI",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55076,
    "customFieldValues": [
      {
        "value": "Porque da erro 500 ao visualizar anexos do processo?",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro pode ocorrer por conta do nome do arquivo, caso tenha E comercial \"&\", não será possível visualizar.",
        "customFieldId": 206843
      },
      {
        "value": "Renomear o arquivo removendo o E comercial \"&\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54086,
    "customFieldValues": [
      {
        "value": "INCLUSÃO DE DESPESAS NO PEDIDO DE SERVIÇO",
        "customFieldId": 206842
      },
      {
        "value": "INCLUSÃO DE DESPESAS NO PEDIDO DE SERVIÇO",
        "customFieldId": 206843
      },
      {
        "value": "possível a inclusão de despesas no pedido de serviço após o envio para a nota de serviço, assim as despesas adicionadas depois do envio, sairiam no relatório corretamente e ficariam somente com informativo, sem compor o valor da nota.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54991,
    "customFieldValues": [
      {
        "value": "Por que o valor da NF estão incorretos?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A parametrização deve ser informada no processo e na NF para que os valores fiquem de acordo no fechamento.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54582,
    "customFieldValues": [
      {
        "value": "Relatório com informações faltando.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente imprimiu o relatório e relatou ausência de  informações.",
        "customFieldId": 206843
      },
      {
        "value": "Verifiquei e estava de acordo, pedi para que cliente confirmasse e a mesma confirmou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53228,
    "customFieldValues": [
      {
        "value": "Por que as parcelas dos pedidos de compra são sobrescritas ao atualizar o pedido com api",
        "customFieldId": 206842
      },
      {
        "value": "duvida",
        "customFieldId": 206843
      },
      {
        "value": "Por que o cliente estão mandando a forma de pagamento na atualização e isso acaba gerando novas parcelas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54934,
    "customFieldValues": [
      {
        "value": "Alíquota ICMS incorreta no relatório de custo.",
        "customFieldId": 206842
      },
      {
        "value": "Há uma exceção fiscal para parametrizar as alíquotas. ",
        "customFieldId": 206843
      },
      {
        "value": "Quando entrei no processo já estava de acordo. Mas nesses casos, deve-se olhar a parametrização> exceção fiscal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54626,
    "customFieldValues": [
      {
        "value": "MENSAGEM: 629 - Rejeicao: Valor do Produto difere do produto Valor Unitario de Comercializacao e Quantidade Comercial",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Verificar no xml da NF o resultado das tags <qCom>, <vUnCom> e <vProd>.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54672,
    "customFieldValues": [
      {
        "value": "Informações não integram do Senior para o Narwal.",
        "customFieldId": 206842
      },
      {
        "value": "O ERP do cliente havia sido atualizado, após a atualização as informações pararam de integrar.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário abrir card com o time de integração para atualização das referencias do integrador.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55042,
    "customFieldValues": [
      {
        "value": "Usuario IIS",
        "customFieldId": 206842
      },
      {
        "value": "Usuário expirado.",
        "customFieldId": 206843
      },
      {
        "value": "Após realizar os ajustes e configurar as permissões do usuário, o problema foi resolvido e o sistema passou a funcionar corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55098,
    "customFieldValues": [
      {
        "value": "Erro ao logar no narwal",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar logar no narwal o sistema fica fora",
        "customFieldId": 206843
      },
      {
        "value": "Se você está recebendo um erro ao tentar fazer login, pode ser que sua conta tenha sido bloqueada devido a várias tentativas de login com a senha errada. Para resolver isso, siga os passos abaixo:\n\nVerifique no banco de dados: Acesse a tabela AspNetUsers.\nCheque a coluna LockoutEndDateUtc: Se o valor dessa coluna estiver nulo, isso significa que a conta não está bloqueada. Se a coluna contiver uma data e hora, significa que a conta está bloqueada até esse momento.\nO que fazer se a coluna não for nula: Caso o valor não seja nulo, significa que o cliente precisará aguardar o desbloqueio automático ou um administrador precisará liberar a conta manualmente.\nEsse bloqueio ocorre para proteger a conta, pois o cliente pode ter tentado acessar com a senha errada várias vezes.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54940,
    "customFieldValues": [
      {
        "value": "Como resolver problema  vinculação de importador X Exportador",
        "customFieldId": 206842
      },
      {
        "value": "Erro vinculação de importador X Exportador DI",
        "customFieldId": 206843
      },
      {
        "value": "o vínculo não estava sendo exibido devido ao fato de o nome do cliente estar em maiúsculas. Realizamos o ajuste para a forma minúscula, e o vínculo foi corretamente exibido na Declaração de Importação (DI).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54410,
    "customFieldValues": [
      {
        "value": "Informação na API /api/contaspagar/v1/consultarpendentes",
        "customFieldId": 206842
      },
      {
        "value": "O título do contas a pagar não estava retornando na API /api/contaspagar/v1/consultarpendentes.",
        "customFieldId": 206843
      },
      {
        "value": "Para que as informações sejam retornadas no EndPoint mencionado, é necessário que o título seja enviado ao ERP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54956,
    "customFieldValues": [
      {
        "value": "Nota fiscal com mensagem em tela ao enviar para sefaz. ",
        "customFieldId": 206842
      },
      {
        "value": "Usuário com divergência certificado ao gerar a nota para SEFAZ. ",
        "customFieldId": 206843
      },
      {
        "value": "Mensagem em tela \" THE REMOTE SERVER RETURNED EN ERROR: (403) FORBIDDEN\"\n\nEssa mensagem se da devido ao certificado digital utilizado para emissão da nota, nesse caso precisaria ver se a nota ia ser emitida pela filial ou importador. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54888,
    "customFieldValues": [
      {
        "value": "CST imposto não puxando nota e Conversão de unidade medida. ",
        "customFieldId": 206842
      },
      {
        "value": "Em agenda realizada com o cliente, verificamos que os campos onde precisavam estar preenchidos para puxar a informação estava divergente. \n\nErro do Usuário não preencheu os campos para que puxasse a informação na nota fiscal. ",
        "customFieldId": 206843
      },
      {
        "value": "Cliente com cenário ontem o CST dos impostos não estava puxando nota fiscal e  conversão unidade também não puxava de forma automática. \n\nPara que a unidade conversão puxe na nota fiscal precisa estar cadastrada dentro do NCM, e também na rotina de unidade de conversão. \n\nDentro da parametrização para que o CST puxe em nota, precisa estar informado dentro da parametrização. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54492,
    "customFieldValues": [
      {
        "value": "Por que é possível realizar alterações na Invoice mesmo com a DI processada?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A DI precisa estar GERADA para bloquear a Invoice.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54786,
    "customFieldValues": [
      {
        "value": "Por que o valor do IPI não está sendo considerado na NF complementar?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente relatou que a NF não precisaria mais ser emitida pois haviam se enganado e a despesa já havia sido paga.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53786,
    "customFieldValues": [
      {
        "value": "Como enviar o campo pesoBrutoUnitario na API?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Não há como fazer o envio pois o campo nao existe na API ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53902,
    "customFieldValues": [
      {
        "value": "Quando o processo possui alíquotas diferentes de pis e cofins, como deve ficar a conversão dentro do sistema.  ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "esses casos, as quantidades e valor de pauta precisam ser ajustadas diretamente na tela de declaração de importação, aba adições, aba PIS/COFINS.\n\nDessa forma o valor calculado irá ficar da forma correta.\n\nAtualmente o sistema puxa automaticamente apenas a quantidade padrão do item e não a unidade de medida estatística, por isso não vai automaticamente do processo, por esse motivo precisam ser ajustadas diretamente na DI.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55041,
    "customFieldValues": [
      {
        "value": "Como configurar despesas para que não entrem no fechamento financeiro?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Para que as despesas de adiantamento não entrem no cálculo do fechamento financeiro, é necessário que elas estejam configuradas como \"Pago pelo cliente\" no numerário ou na aba despesas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54609,
    "customFieldValues": [
      {
        "value": "NARWAL ERRO DE INTEGRAÇÃO DOS PEDIDOS",
        "customFieldId": 206842
      },
      {
        "value": "NARWAL ERRO DE INTEGRAÇÃO DOS PEDIDOS",
        "customFieldId": 206843
      },
      {
        "value": "Verificado que a nota estava travada na fila de integração, fiz o disparo e o mesmo integrou automaticamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55057,
    "customFieldValues": [
      {
        "value": "Falha ao acessar o ambiente",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar acessar o ambiente da Lorenzetti, estava retornando a mensagem de erro \"O nome da rede não está mais disponível.",
        "customFieldId": 206843
      },
      {
        "value": "o ambiente da Lorenzetti teve uma parada inesperada na conexão do banco. Foi acionada a CDB para que a conexão fosse reestabelecida.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54621,
    "customFieldValues": [
      {
        "value": "Por que o ICMS esta com valor incorreto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A base estava incorreta devido a uma despesa faltando, assim que foi inserida, o valor ficou de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54701,
    "customFieldValues": [
      {
        "value": "Como fazer o preenchimento da NVE na planilha de importação?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Utilizar a planilha pelo Processo/menu de ação / Importar produtos;\n\nNa planilha preencher a informação conforme está no cadastro do produto na opção de NVE. \n\nAtributo- Especialização- Descrição",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 44408,
    "customFieldValues": [
      {
        "value": "Parametrização NF",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Assunto já sendo tratado no atendimento de suporte 53049",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54993,
    "customFieldValues": [
      {
        "value": "Usuário preso editando processo",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Foi desabilitado a variável ambiente \"NWL_HABILITABLOQUEIOUSUARIO\", assim não aparece mais que os usuários estão editando o processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55052,
    "customFieldValues": [
      {
        "value": "Unidade tributada e quantidade tributada nota fiscal. ",
        "customFieldId": 206842
      },
      {
        "value": "Ao enviar a nota para Sefaz o Narwal acusou uma mensagem em tela.\n\n\" Erros na validação: the element 'prod' in namespace: Cbarratrib, utrib. \n\nErro referente a unidade tributada e a quantidade tributada. ",
        "customFieldId": 206843
      },
      {
        "value": "Dentro da rotina NCM vai buscar pelo NCM da nota fiscal e informar na unidade de medida a conversão da unidade. \n\nExemplo no produto está unida como .TONELADA METRICA, no NCM tem que ficar a conversão. \n\nDentro da rotina de Conversão de unidade de medida, precisa estar cadastrado a conversão também. \n\nConversões que possui cadastrada para essa unidade de medida do produto. \n\nApós ajustes, precisa cancelar  gerar novamente a nota. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54631,
    "customFieldValues": [
      {
        "value": "Não estava refletindo as despesas no contas a pagar. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Para que crie o contas a pagar dentro do Narwal precisa ter a operação financeira cadastrada, caso na rotina de operação financeira já tenham cadastrado, pode estar criando o financeiro,  precisa sempre que o processo esteja calculado os impostos. \n\nCliente fez ajuste manual. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54383,
    "customFieldValues": [
      {
        "value": "Erro na Integração com o CustoEX",
        "customFieldId": 206842
      },
      {
        "value": "duvida",
        "customFieldId": 206843
      },
      {
        "value": "Cancelado dentro do Narwal, tinha um pedido e um contrato de câmbio vinculado a invoice.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55001,
    "customFieldValues": [
      {
        "value": "sistema não traz Extarifário atual. ",
        "customFieldId": 206842
      },
      {
        "value": "O JOB não trouxe a informação atualizada do extarifario.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário inserir a informação manualmente via banco.\n\nFoi aberto card com o time de produto para correção.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53859,
    "customFieldValues": [
      {
        "value": "Cliente com duvida na rotina de gestão de Eventos. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "A CS alinhou com a cliente, e foi passado ao suporte para finalizar o atendimento. \n\nConforme passado o Narwal ainda não está maduro para essa rotina, sendo assim foi informando sobre o módulo não estar maduro e não ter clientes utilizando, bem como não termos conhecimento sobre a ferramenta para uma demonstração da mesma. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54222,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54229,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54747,
    "customFieldValues": [
      {
        "value": "Disparo de Follow Up avisando o status de ETA/ETD",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Não há possibilidade de alteração neste follow em específico, pois o mesmo se trata de um follow-up padrão do sistema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54774,
    "customFieldValues": [
      {
        "value": "O que pode causar divergencia no valor do ICMS na NF?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A parametrização é um dos pontos que podem interferir no valor dos impostos na NF. Neste caso o que estava causando a divergencia era a alíquota reduzida da parametrização. Após a mesma ser retirada, o valor ficou de acordo.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53063,
    "customFieldValues": [
      {
        "value": "O que fazer quando  o pedido de toneladas no sap estiver convertendo para  (ton) para quilogramas (kg)?",
        "customFieldId": 206842
      },
      {
        "value": "Pedido do sap  está convertendo o pedido de toneladas (ton) para quilogramas (kg) ao chegar no narwal",
        "customFieldId": 206843
      },
      {
        "value": "Foi identificado que o problema acontecia pois o certificado estava vencido e não havia sido alterado, ocasionando em um erro ao tentar autenticar com a API do Narwal. Foi necessário substituir o certificado para o ambiente de produção e homologação\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53425,
    "customFieldValues": [
      {
        "value": "Código de duplo fator sendo enviado mais de uma vez",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Foi criado por padrão para não pedir o duplo fator a cada 3 horas, caso o cliente queria aumentar ou tirar esse tempo seria via melhoria. BL anexado no card",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54911,
    "customFieldValues": [
      {
        "value": "O item 1 não possui unidade de medida",
        "customFieldId": 206842
      },
      {
        "value": "Quando o alerta \"\"O item 1 não possui unidade de medida\" for exibida ao salvar o pedido ou processo, é necessário verificar se de fato, a unidade de medida está informada direto no cadastro do produto. ",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55026,
    "customFieldValues": [
      {
        "value": "RETIRAR OBRIGATORIEDADE  DO PEDIDO DE SERVIÇO",
        "customFieldId": 206842
      },
      {
        "value": "Cliente solicita retirar obrigatoriedade do campo transporte na rotina pedido de serviço",
        "customFieldId": 206843
      },
      {
        "value": "infelizmente não é possível realizar a alteração, pois a definição da via de transporte é obrigatória por padrão do sistema. Ou seja, todo pedido de serviço deve incluir qual será a via de transporte utilizada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54841,
    "customFieldValues": [
      {
        "value": "Valor do ICMS na nota de uso e consumo, por se tratar de uma importação tributada ele não estava totalizando o valor total da nota fiscal. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Por se tratar de uma nota fiscal de uso e consumo e de uma importação tributada, o valor do ICMS ele integra o valor total da nota fiscal de entrada. \n\nDessa forma para que puxasse o valor do ICMS, informamos dentro da parametrização no total da nota fiscal a formula abaixo.  \n\n{ValorTotal}+{Icms}+{DespesaBaseIcms}+{Pis}+{Cofins}+{Ii}\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54303,
    "customFieldValues": [
      {
        "value": "Anexo de documentos para visualização no portal do cliente",
        "customFieldId": 206842
      },
      {
        "value": "Cliente necessita que os documentos anexados nos processos aparece para o cliente dentro do portal do cliente.",
        "customFieldId": 206843
      },
      {
        "value": "É necessário flagrar o documento na rotina de gestão de documentos, ou, ao anexá-lo, já realizar o flag, conforme descrito passo a passo no chamado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54527,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54369,
    "customFieldValues": [
      {
        "value": "Por que o adiantamento não está compensando na Invoice?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Após criação do contrato de câmbio de adiantamento. Realizar o adiantamento manual na rotina processo -> invoice. Ou ativar a variável NWL_PROCESSAACCAUTOMATICAMENTE para processar o adiantamento de forma automática",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55013,
    "customFieldValues": [
      {
        "value": "Erro ao tentar Autorizar NF no sefaz \"Valor do Produto difere do produto Valor Unitario de Tributacao e Quantidade Tributavel\".",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro é retornado pois algum item da nota fiscal está com o campo \"Valor unid. tributada\" com valor 0.",
        "customFieldId": 206843
      },
      {
        "value": "Editar o produto e informar o valor. Ou criar na rotina \"Conversão de unidade de medida\" a conversão entre unidade de medida e unidade tributada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54807,
    "customFieldValues": [
      {
        "value": "Rotina \"Portos desembarque\" não encontrado",
        "customFieldId": 206842
      },
      {
        "value": "Foi verificado que esta rotina sofreu alteração na nomenclatura. Agora esta rotina foi alterada para Contrato de Fornecedores. ",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55000,
    "customFieldValues": [
      {
        "value": "Invalido, era duvida sobre outro erp",
        "customFieldId": 206842
      },
      {
        "value": "Invalido, era duvida sobre outro erp",
        "customFieldId": 206843
      },
      {
        "value": "Invalido, era duvida sobre outro erp",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54995,
    "customFieldValues": [
      {
        "value": "Qual a origem do valor do campo chaveMoeda retornado da API para lançamentos contábeis",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "O campo é preenchido com a moeda do contas a pagar relacionado ao lançamento contábil.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53907,
    "customFieldValues": [
      {
        "value": "Erro no Adquirente da Mercadoria",
        "customFieldId": 206842
      },
      {
        "value": "Ao realizar o registro da DI do Processo o Adquirente da Mercadoria mudou para o mesmo do fornecedor.",
        "customFieldId": 206843
      },
      {
        "value": "Antes de realizar o registro da DI a flag do campo 'encomenda' estava false, por esse motivo puxou para o cnpj da MVX.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54914,
    "customFieldValues": [
      {
        "value": "Erro ao calcular os impostos.",
        "customFieldId": 206842
      },
      {
        "value": "Filial estava divergente no processo e na invoice.",
        "customFieldId": 206843
      },
      {
        "value": "Filial estava divergente no processo e na invoice.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54768,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54979,
    "customFieldValues": [
      {
        "value": "Erro quando Supply ainda não foi aprovado porém cliente não utiliza esta rotina",
        "customFieldId": 206842
      },
      {
        "value": "Supply é uma rotina que envia um follow para o Fornecedor do pedido de Compra é criado. O Fornecedor precisa entrar no link do follow e colocar informações sobre os produtos. Após o Fornecedor dar o Aceite, as informações são integradas no Pedido de Compra.",
        "customFieldId": 206843
      },
      {
        "value": "Desativar o Supply Internacional no cadastro do Fornecedor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54568,
    "customFieldValues": [
      {
        "value": "Erro ao gerar nota",
        "customFieldId": 206842
      },
      {
        "value": "Cliente ao tentar gerar a nota o mesmo estava gerando erro de senha de certificado.",
        "customFieldId": 206843
      },
      {
        "value": "Identificado que o cliente informou a senha do certificado no campo errado, após colocar no campo correto o mesmo funcionou normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54788,
    "customFieldValues": [
      {
        "value": "Ao abrir um processo, não puxa o único despachante cadastrado.",
        "customFieldId": 206842
      },
      {
        "value": "Quando há apenas um despachante cadastrado, ele puxa de forma automática.",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso, realizei o teste e deu certo. Cliente n retornou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54879,
    "customFieldValues": [
      {
        "value": "E que momento é criado o título INV (Definitivo)?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A alteração do titulo previsto para o titulo efetivo da invoice pode ocorrer em 2 momentos, sendo eles:\n\n1. Quando for realizado um contrato de cambio do tipo antecipado e compensado na invoice;\n\n2. Quando a NFentrada for emitida, qualquer valor em aberto muda automaticamente para titulo efetivo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54839,
    "customFieldValues": [
      {
        "value": "Você não possui acesso ao menu selecionado: Importacao/NPI/IntegrarXmlDiProcesso.",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "Acessar Grupo de usuário e selecionar o campo \"[x] Integrar DI/DUIMP\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54945,
    "customFieldValues": [
      {
        "value": "Rejeição SEFAZ: Duplicidade de NF-e, com diferença na Chave de Acesso ",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "A mensagem ocorre pois a numeração/série que está sendo enviada para SEFAZ já existe no SEFAZ. No Narwal, nesse momento para liberar a NF, deverá ser realizado ação interna para liberar a NF para que o cliente cancele ou envie novamente para SEFAZ.  ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54957,
    "customFieldValues": [
      {
        "value": "Casas decimais da taxa moeda.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina Variáveis de ambiente NWL_DECCASPRO alterar no campo Valor a quantidade conforme a necessidade. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54493,
    "customFieldValues": [
      {
        "value": "Qual o motivo para o elevado número de usuários Narwal cadastrados no sistema?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Todos usuários Narwal que em algum momento acessaram o ambiente ficam registrados no cadastro de usuários, essa é uma ação automática.  ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53755,
    "customFieldValues": [
      {
        "value": "539-Rejeição: Duplicidade de NF-e com diferença na Chave de Aceso.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Clicar no menu de ação da NF e clicar em Eventos. No evento vai gerar a chave de acesso da NF que está autorizada no SEFAZ.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53703,
    "customFieldValues": [
      {
        "value": "630 - Rejeicao: Valor do Produto difere do produto Valor Unitario de Tributacao e Quantidade Tributavel",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina Conversão Unidade de Medida cadastrar a conversão. Cancelar a NF e criar novamente para que assuma a conversão automática.\nTambém poderá ser informado manualmente, para isso, editar a NF na guia Produtos informar a Unidade tributável.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54958,
    "customFieldValues": [
      {
        "value": "Informe o Banco Informe a agencia bancária ao registrar a DI ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Acessar a rotina Declaração Importação, guia Pagamentos e informar os dados bancários.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54402,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54260,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54778,
    "customFieldValues": [
      {
        "value": "Neste caso, foi resolvido pelo cliente",
        "customFieldId": 206842
      },
      {
        "value": "Neste caso, foi resolvido pelo cliente",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso, foi resolvido pelo cliente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54927,
    "customFieldValues": [
      {
        "value": "Erro ao calcular taxa da DI",
        "customFieldId": 206842
      },
      {
        "value": "Alerta exibido ao tentar calcular os impostos da DI: \"Base de Cálculo Ad Valorem II - Incorreta. É necessário extrair a tabela de Taxa de Conversão de Câmbio.\"\n",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver este caso, é necessário verificar se a taxa da moeda DÓLAR foi devidamente atualizada. Para isso, acesse a rotina Moeda -> Dólar e verifique os campos \"Data Fim Vigência Ptax Venda\" e \"Valor Ptax Venda\". Ambos os campos devem estar atualizados com a taxa correspondente ao mesmo dia em que os cálculos dos impostos da DI forem realizados.\n\nPara confirmar as taxas atualizadas, você pode consultar diretamente o portal do Banco Central, no seguinte link: https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54908,
    "customFieldValues": [
      {
        "value": "Não é possível criar uma nova pasta na gestão de documentos.",
        "customFieldId": 206842
      },
      {
        "value": "Ao acessar a rotina Pastas para gestão documentos -> Importação, o botão \"Novo\" não aparece.",
        "customFieldId": 206843
      },
      {
        "value": "Validar dentro da rotina de grupo de usuário, se a rotina está somente como visualização.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54809,
    "customFieldValues": [
      {
        "value": "E-mail de autenticação não chega - SMTP",
        "customFieldId": 206842
      },
      {
        "value": "Quando o código de autenticação não é entregue ao e-mail do usuário, pode haver diferentes causas que precisam ser verificadas.",
        "customFieldId": 206843
      },
      {
        "value": "Para identificar e resolver o problema, siga os passos abaixo:\n\n1. Verifique se o e-mail não foi para a caixa de spam.\n\n2. Confirme se o SMTP utilizado pelo cliente é o da Narwal ou do próprio cliente.\n\n3. Se for o SMTP da Narwal e estiver apresentando erro, acione a equipe de infraestrutura para análise.\n\n4. Se o SMTP for do cliente, oriente-o a verificar se a senha expirou ou se houve alteração nos parâmetros de configuração, localizados na rotina Empresa -> Aba Parâmetros.\n\n5. Para testar o funcionamento do SMTP, acesse Empresa -> Aba Parâmetros e clique no botão \"Validar SMTP\":\n\n- Se aparecer a mensagem \"Operação realizada com sucesso\", as configurações estão corretas.\n\n- Se aparecer um alerta amarelo com outra mensagem, há divergências na configuração do SMTP que precisam ser corrigidas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54474,
    "customFieldValues": [
      {
        "value": "Ao deixar o campo \"Status\" em branco no contas a pagar, deveria trazer todos os registros ou só trazer o que está em aberto?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Títulos excluídos/cancelados não são filtrados quando retiramos o filtro de status, apenas os que estão ativos.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54850,
    "customFieldValues": [
      {
        "value": "Integração de planilha no processo (Dados de cadeira binários seriam truncados)",
        "customFieldId": 206842
      },
      {
        "value": "Um dos erros mais comuns no Narwal ocorre quando há uma tentativa de vincular uma planilha de produtos a um processo. Nesse caso, recebemos o seguinte alerta: \"Operação abortada, dados de cadeira ou binários seriam truncados. A instrução foi finalizada.\"",
        "customFieldId": 206843
      },
      {
        "value": "Neste cenário, a primeira verificação que precisamos realizar é a estrutura da tabela. É fundamental conferir se há colunas inválidas, campos em branco ou qualquer outro fator que possa afetar a inserção dos dados. Para resolver esse caso específico, foi identificado que alguns campos estavam em branco, o que fazia com que a inserção fosse interrompida e a tela de erro fosse exibida.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54228,
    "customFieldValues": [
      {
        "value": "Por que a DI não foi registrada com a informação alterada no processo?",
        "customFieldId": 206842
      },
      {
        "value": "Verificamos internamente, através de uma auditoria, que o registro da DI foi feito enquanto o processo ainda estava salvando e enviando a requisição para o banco de dados.\n\n",
        "customFieldId": 206843
      },
      {
        "value": "Ativar a variável NWL_HABILITABLOQUEIOUSUARIO. \nEssa variável também impede o acesso a uma rotina caso você esteja utilizando outra que interfira nela.\nPor exemplo: Se o processo estiver aberto na tela, não será possível acessar a rotina de declaração de importação, pois há a seguinte trava:",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54972,
    "customFieldValues": [
      {
        "value": "Erro ao tentar acessar URL Narwal \"HTTP Error 503. The service is unavailable.\".",
        "customFieldId": 206842
      },
      {
        "value": "Foi identificado que o servidor estava travado, fazendo com que o sistema ficasse fora do ar. Também devido a VM estar travada, não estava sendo possível acessa-la para verificar o motivo do sistema estar fora do ar.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário abrir chamado com o time de infra para verificar o problema.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54848,
    "customFieldValues": [
      {
        "value": "Nota fiscal não integrando ao SAP",
        "customFieldId": 206842
      },
      {
        "value": "Nota fiscal do cliente não estava enviando ao SAP pelo seguinte erro :\nUM=m ou mais erros.",
        "customFieldId": 206843
      },
      {
        "value": "Verificado que houve o integrador não estava instável, porém ao esperar alguns minutos o mesmo foi enviado corretamente, esse erro aconteceu somente para essa nota especifica.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54587,
    "customFieldValues": [
      {
        "value": "O que deve-se verificar quando a NF retorna com erro no valor unitário e quantidade?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Deve-se analisar se os valores estão corretos e se os campos na nota> produtos estão preenchidos. Neste caso algumas informações estavam faltando.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53839,
    "customFieldValues": [
      {
        "value": "O Narwal possui alerta no envio da cotação informando o tempo restante para dar o retorno?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O Narwal não possui este alerta, mas é possível inserir uma mensagem nas observações da cotação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54461,
    "customFieldValues": [
      {
        "value": "Inserçaõ de lote - Erro ao Inserir Planilha",
        "customFieldId": 206842
      },
      {
        "value": "Numero do pedido não indo pro item de drawback",
        "customFieldId": 206843
      },
      {
        "value": "Trigger aplicada para levar a condição.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54506,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "NA",
        "customFieldId": 206843
      },
      {
        "value": "NA",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54857,
    "customFieldValues": [
      {
        "value": "Cliente sem conseguir informar os dados no cadastro do fornecedor. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Nessa situação foi analisado que no cadastro do estado estava informado como um cadastro que não estava ativo. \n\nInformaram um cadastro do exterior que estivesse ativo no Narwal. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54100,
    "customFieldValues": [
      {
        "value": "Como deixar a Taxa SISCOMEX vir paga sempre pelo cliente?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso, se for utilizado o numerário é possível configurar a Taxa Siscomex ser paga pelo cliente. No cadastro \"Tipo despesa\", é possivel realizar a seguinte configuração:\nAo gerar no numerário, irá respeitar esta configuração, e ao transferir as despesas para a aba \"Despesas\", permanece como estava no numerário.\nCaso a dúvida seja se é possível realizar esta configuração na aba \"Despesas\", seria um serviço complementar.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54875,
    "customFieldValues": [
      {
        "value": "Porque meus pedidos não integram do Sankhya?",
        "customFieldId": 206842
      },
      {
        "value": "A fila de requisições estava com um numero exacerbante de registros",
        "customFieldId": 206843
      },
      {
        "value": "Acionar time de integração para reiniciar a API.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54749,
    "customFieldValues": [
      {
        "value": "Informações duplicadas na descrição do produto ao gerar a nota fiscal. ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida \n",
        "customFieldId": 206843
      },
      {
        "value": "Para essa descrição possui uma variável de ambiente NWL_CAMPODESCRICAONOTAFISCAL. \n\nCaso for \"1\" informa a descrição do produto e descrição da DI.\n\nCaso for \"2\" informa apenas a descrição do produto.\n\nProcurar na rotina Variáveis de ambiente pela variável, caso esteja 1, vai puxar a descrição DI e produto, se quer apenas uma descrição informar 2.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54754,
    "customFieldValues": [
      {
        "value": "Nota complementar não estava complementando o imposto do IPI. ",
        "customFieldId": 206842
      },
      {
        "value": "Incidente ",
        "customFieldId": 206843
      },
      {
        "value": "Para a nota fiscal foi aplicado um ajuste manual para que o valor do IPI fosse complementado também. \n\nJá possui um BL para investigação do por que a nota não complementa o Ipi. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53612,
    "customFieldValues": [
      {
        "value": "Documentação API.",
        "customFieldId": 206842
      },
      {
        "value": "Como verificar a documentação da API?",
        "customFieldId": 206843
      },
      {
        "value": "A documentação é possível ser consultada com o link da API, basta o swagger estar liberado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53977,
    "customFieldValues": [
      {
        "value": "Como verificar se o título integrou para o Sankhya?",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Para verificar se um título do contas a pagar foi integrado para o Sankhya, podemos ir diretamente na rotina, e na grid habilitar para mostrar o campo \"Chave\". Caso o campo chave esteja preenchido com uma chave \"guid\", significa que o título não foi integrado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54391,
    "customFieldValues": [
      {
        "value": "Qual a regra utilizada para o campo \"Devolução container\" na nova tela inicial?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida quanto aos processos que estão aparecendo na aba \"Devolução container\"",
        "customFieldId": 206843
      },
      {
        "value": "O processo deve estar ativo, ter uma data de atracação registrada e essa data precisa estar dentro do período definido no filtro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54867,
    "customFieldValues": [
      {
        "value": "Por que a NFe foi gerada com número incorretp?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Pois na rotina \"Nota fiscal serie\" o número atual estava incorreto. É necessário saber qual o próximo número da nota para ser ajustado e o SEFAZ aceitar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54756,
    "customFieldValues": [
      {
        "value": "Processo com divergencia do narwal para sua planilha de calculo. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro em parametrização do usuário ",
        "customFieldId": 206843
      },
      {
        "value": "Consultor auxiliou e verificaram que se tratava de parametrizações ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54257,
    "customFieldValues": [
      {
        "value": "Porque Flag \"Possui Cobertura Câmbial\" não acata alteração do Processo para DUE?",
        "customFieldId": 206842
      },
      {
        "value": "Pelo fato de que após o registro da DUE, não há interação com dados do processo",
        "customFieldId": 206843
      },
      {
        "value": "Solução no caso, é preencher os mesmos campos nos dois locais: DUE e Processo Expo OU\nCancelar a Nota Fiscal, fazer todos os ajustes necessários no processo e integrá-la novamente, assim, ao gerar a DUE, os dados do processo serão consumidos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53769,
    "customFieldValues": [
      {
        "value": " Duvida calcular impostos na ADMISSÃO TEMPORÁRIA",
        "customFieldId": 206842
      },
      {
        "value": "Quando processo de admissão temporária, por padrão, o botão calcular impostos fica inativo",
        "customFieldId": 206843
      },
      {
        "value": "Para que o cliente possa ter acesso ao valor dos impostos quando admissão temporária, ele poderá utilizar duas formas:\n1. No proprio processo, na aba numerário > pré calculo, informar uma taxa de conversão e processar impostos.\n\n2. Abrir uma simulação de importação a partir do botão de ação do processo e calcular os impostos e gerar relatorios pela ferramenta.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54870,
    "customFieldValues": [
      {
        "value": "Erro \"palito de picolé\" ao editar ou criar novo processo.",
        "customFieldId": 206842
      },
      {
        "value": "Não estava sendo possível editar ou consultar pois havia apresentado erro de migration. (Estava faltando informação no banco)",
        "customFieldId": 206843
      },
      {
        "value": "Aberto chamado com dev, após rodar o migration novamente, foi possível criar e editar os processos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53353,
    "customFieldValues": [
      {
        "value": "Cálculo do IPI ",
        "customFieldId": 206842
      },
      {
        "value": "Quando questionado que o IPI foi calculado erroneamente em relação ao calculo do sistema \n",
        "customFieldId": 206843
      },
      {
        "value": "A base do IPI, é acumulativo em cascata. Ou seja, a base do IPI é o valor aduaneiro + o valor calculado do II.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54813,
    "customFieldValues": [
      {
        "value": "Como posso reabrir um processo que está inativo?",
        "customFieldId": 206842
      },
      {
        "value": "Esta FAQ fornecerá orientações e direcionamentos para a alteração do status do processo de \"Inativo\" para \"Ativo\".",
        "customFieldId": 206843
      },
      {
        "value": "Os processos que estão inativados não são visíveis na grid de consulta na tela do Narwal, sendo possível visualizá-los apenas através do número ou ID do processo diretamente no banco de dados. Caso seja necessário alterar o status de um processo de \"Inativo\" para \"Ativo\" via banco de dados, basta localizar o processo e realizar um update na coluna \"Ativo\".\n\nCom isso, o processo voltará a ser visível na grid de consultas da tela, permitindo que o usuário reabra o processo.\n\nImportante: Essa alteração não gerará impacto em outras rotinas, pois o campo \"Ativo\" serve exclusivamente para controlar a visibilidade do processo.\n\nSintaxe para o update:\n\nSintaxe para update via ID do processo:\n\nUPDATE Processo\nSET Ativo = 1\nWHERE ProcessoId = ID do processo\n\nSintaxe para update via número do processo:\n\nUPDATE Processo\nSET Ativo = 1\nWHERE Numero = Número do processo",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54126,
    "customFieldValues": [
      {
        "value": "Erro ao enviar Pedido pela API \"Non-static method requires a target.\"",
        "customFieldId": 206842
      },
      {
        "value": "N/A.",
        "customFieldId": 206843
      },
      {
        "value": "Atualizar a versão.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54826,
    "customFieldValues": [
      {
        "value": "Como solucionar o erro \"É necessário cancelar o título antes de cancelar a exportação\"?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Excluir os títulos no contas a pagar/receber vinculados com este processo. \n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54026,
    "customFieldValues": [
      {
        "value": "377 - Codigo de Pais do destinatario Inexistente",
        "customFieldId": 206842
      },
      {
        "value": "Código BACEN errado no cadastro do País",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro do País Alemanha no campo Bacen estava informado o código 23, sendo que o correto é o código 230. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54546,
    "customFieldValues": [
      {
        "value": "Erro ao integrar pedido de compra com SAP B1: \"unexpected character encountered while parsing value: < Path \", line 0, position 0\"",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao integrar pedido de compra com SAP B1: \"unexpected character encountered while parsing value: < Path \", line 0, position 0\" pool de aplicação esta parado.",
        "customFieldId": 206843
      },
      {
        "value": "O erro ocorreu pois o pool da aplicação de PRD e HML estavam parados. Foi solicitado acesso ao servidor SAP do cliente e iniciado os pools. Conforme o cliente, as notas voltaram a integrar, dessa forma estarei encerrando o BL:",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54791,
    "customFieldValues": [
      {
        "value": "Erro ao enviar a nota fiscal ao SAP: \"Sap b1 status 200: falha - não foi possível executar a função adicionar NFe",
        "customFieldId": 206842
      },
      {
        "value": "O erro ocorre quando a nota fiscal é integrada ao SAP e a transportadora informada na NFe não possui um cadastro correspondente no SAP. Especificamente, o erro foi causado por uma chave de cadastro inválida para a transportadora utilizada, gerada automaticamente pelo sistema como um GUID (Identificador Único Global), em vez de uma chave válida que corresponda a um cadastro existente no SAP.",
        "customFieldId": 206843
      },
      {
        "value": "Verificação dos Cadastros: Para que a integração da NFe ao SAP ocorra corretamente, é essencial que todos os cadastros envolvidos, como o da transportadora, já existam previamente no SAP.\n\nChave de Cadastro: A chave do cadastro da transportadora na NFe deve ser a mesma utilizada no SAP, garantindo a correspondência correta (DE/PARA) entre os registros no sistema de origem e no SAP.\n\nCorreção do Erro: A auditoria revelou que a transportadora utilizada na NFe 464 foi criada com uma chave inválida. Para corrigir isso, o cliente atualizou a chave do cadastro da transportadora para a mesma chave utilizada no SAP.\n\nResultado: Após a correção da chave da transportadora, a integração da NFe foi realizada com sucesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54806,
    "customFieldValues": [
      {
        "value": "Pedido de compra exigindo fleg \"Utiliza prefixo\"",
        "customFieldId": 206842
      },
      {
        "value": "Ao criar o pedido de compra, é possível utilizar uma numeração manual para a criação do pedido, sem a necessidade de marcar a checkbox \"Utiliza prefixo\".",
        "customFieldId": 206843
      },
      {
        "value": "Para remover a obrigatoriedade deste campo, considerando que no cadastro de filial ele não está marcado, o que exige que esteja flegrado, é necessário verificar se o parâmetro \"Marcar campo como obrigatório\" está ativado ao lado do campo. Caso esteja, basta orientar o usuário a desmarcar essa opção.\n\nEste problema ocorreu exclusivamente no cliente Benassi SP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54833,
    "customFieldValues": [
      {
        "value": "Por que os títulos efetivos (contas a pagar) não estão sendo enviado automaticamente ao ERP?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Por questão de segurança da conferência dos valores, o Narwal não faz o envio automático dos títulos efetivos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54842,
    "customFieldValues": [
      {
        "value": "Quais campos integram um pedido de compra?",
        "customFieldId": 206842
      },
      {
        "value": "caminho correto para integração via API os campos abaixo que inicialmente temos contato na rotina pedido de compras",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso precisa ter os campos correspondente ao que esta na nossa api :\n{\n  \"chave\": \"string\",\n  \"numero\": \"string\",\n  \"filial\": {\n    \"chave\": \"string\",\n    \"chaveEmpresa\": \"string\",\n    \"cnpj\": \"string\",\n    \"nome\": \"string\",\n    \"linhaEndereco1\": \"string\",\n    \"linhaEndereco2\": \"string\",\n    \"zipCode\": \"string\",\n    \"filialMercosul\": true,\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"estado\": {\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"percentualIcms\": 0,\n      \"prazoCancelamentoNfeHoras\": 0,\n      \"codigoIbge\": \"string\"\n    },\n    \"nomeCidade\": \"string\",\n    \"utilizaNumeracaoImportacao\": true,\n    \"prefixoImportacao\": \"string\",\n    \"paisCodigo\": \"string\",\n    \"estadoSigla\": \"string\",\n    \"filialId\": 0\n  },\n  \"cliente\": {\n    \"chave\": \"string\",\n    \"empresaChave\": \"string\",\n    \"filialChave\": \"string\",\n    \"nome\": \"string\",\n    \"tipoPessoa\": \"Fisica\",\n    \"cpfCnpj\": \"string\",\n    \"percentualComissao\": 0,\n    \"corrigeDocumentos\": true,\n    \"contrataFreteInter\": true,\n    \"freteContratado\": true,\n    \"contrataFreteRodo\": true,\n    \"pgtoImpostosAntecipados\": true,\n    \"diasEnvioNumerario\": 0,\n    \"endereco\": \"string\",\n    \"endereco2\": \"string\",\n    \"bairro\": \"string\",\n    \"nomeCidade\": \"string\",\n    \"estado\": {\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"percentualIcms\": 0,\n      \"prazoCancelamentoNfeHoras\": 0,\n      \"codigoIbge\": \"string\"\n    },\n    \"nomeEstado\": \"string\",\n    \"chaveBacen\": \"string\",\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"antecipaNumerario\": \"Proprio\",\n    \"antecipaNumerarioValor\": \"string\",\n    \"prazoPgtoNfServico\": \"Antecipado\",\n    \"inscricaoSuframa\": \"string\",\n    \"inscricaoMunicipal\": \"string\",\n    \"enderecoNumero\": \"string\",\n    \"cep\": \"string\",\n    \"inscricaoEstadual\": \"string\",\n    \"paisCodigo\": \"string\",\n    \"bancoNome\": \"string\",\n    \"agenciaCompleta\": \"string\",\n    \"contaCompleta\": \"string\",\n    \"ativo\": true,\n    \"email\": \"string\",\n    \"telefone\": \"string\",\n    \"creditaIcms\": true,\n    \"creditaIpi\": true,\n    \"creditaCofins\": true,\n    \"creditaPis\": true,\n    \"campoUsuario\": [\n      {\n        \"nomeVariavel\": \"string\",\n        \"valor\": \"string\",\n        \"campoAdicionalId\": 0\n      }\n    ],\n    \"listaDocExpo\": [\n      {\n        \"nomeVariavel\": \"string\",\n        \"valor\": \"string\",\n        \"campoAdicionalId\": 0\n      }\n    ]\n  },\n  \"consignee\": {\n    \"chave\": \"string\",\n    \"empresaChave\": \"string\",\n    \"filialChave\": \"string\",\n    \"nome\": \"string\",\n    \"tipoPessoa\": \"Fisica\",\n    \"cpfCnpj\": \"string\",\n    \"percentualComissao\": 0,\n    \"corrigeDocumentos\": true,\n    \"contrataFreteInter\": true,\n    \"freteContratado\": true,\n    \"contrataFreteRodo\": true,\n    \"pgtoImpostosAntecipados\": true,\n    \"diasEnvioNumerario\": 0,\n    \"endereco\": \"string\",\n    \"endereco2\": \"string\",\n    \"bairro\": \"string\",\n    \"nomeCidade\": \"string\",\n    \"estado\": {\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"percentualIcms\": 0,\n      \"prazoCancelamentoNfeHoras\": 0,\n      \"codigoIbge\": \"string\"\n    },\n    \"nomeEstado\": \"string\",\n    \"chaveBacen\": \"string\",\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"antecipaNumerario\": \"Proprio\",\n    \"antecipaNumerarioValor\": \"string\",\n    \"prazoPgtoNfServico\": \"Antecipado\",\n    \"inscricaoSuframa\": \"string\",\n    \"inscricaoMunicipal\": \"string\",\n    \"enderecoNumero\": \"string\",\n    \"cep\": \"string\",\n    \"inscricaoEstadual\": \"string\",\n    \"paisCodigo\": \"string\",\n    \"bancoNome\": \"string\",\n    \"agenciaCompleta\": \"string\",\n    \"contaCompleta\": \"string\",\n    \"ativo\": true,\n    \"email\": \"string\",\n    \"telefone\": \"string\",\n    \"creditaIcms\": true,\n    \"creditaIpi\": true,\n    \"creditaCofins\": true,\n    \"creditaPis\": true,\n    \"campoUsuario\": [\n      {\n        \"nomeVariavel\": \"string\",\n        \"valor\": \"string\",\n        \"campoAdicionalId\": 0\n      }\n    ],\n    \"listaDocExpo\": [\n      {\n        \"nomeVariavel\": \"string\",\n        \"valor\": \"string\",\n        \"campoAdicionalId\": 0\n      }\n    ]\n  },\n  \"despachante\": {\n    \"chave\": \"string\",\n    \"nome\": \"string\",\n    \"modeloIntegracaoDespesas\": \"Nenhum\",\n    \"modeloIntegracaoDespesasValor\": \"string\",\n    \"despachanteProprio\": true,\n    \"chaveFornecedor\": \"string\",\n    \"fornecedor\": {\n      \"chave\": \"string\",\n      \"empresaChave\": \"string\",\n      \"filialChave\": \"string\",\n      \"nome\": \"string\",\n      \"nomeFantasia\": \"string\",\n      \"numeroDocumento\": \"string\",\n      \"agencia\": \"string\",\n      \"conta\": \"string\",\n      \"responsavel\": \"string\",\n      \"linhaEndereco1\": \"string\",\n      \"linhaEndereco2\": \"string\",\n      \"enderecoNumero\": \"string\",\n      \"nomeCidade\": \"string\",\n      \"cidade\": {\n        \"codigoIbge\": \"string\",\n        \"nome\": \"string\",\n        \"chave\": \"string\",\n        \"codigoMunicipio\": \"string\",\n        \"estado\": {\n          \"sigla\": \"string\",\n          \"nome\": \"string\",\n          \"percentualIcms\": 0,\n          \"prazoCancelamentoNfeHoras\": 0,\n          \"codigoIbge\": \"string\"\n        }\n      },\n      \"cidadeId\": 0,\n      \"estadoExterior\": \"string\",\n      \"bairro\": \"string\",\n      \"cep\": \"string\",\n      \"telefone\": \"string\",\n      \"digitoAgencia\": \"string\",\n      \"agenciaCompleta\": \"string\",\n      \"digitoConta\": \"string\",\n      \"swift\": \"string\",\n      \"iban\": \"string\",\n      \"contaCompleta\": \"string\",\n      \"estado\": {\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"percentualIcms\": 0,\n        \"prazoCancelamentoNfeHoras\": 0,\n        \"codigoIbge\": \"string\"\n      },\n      \"estadoId\": 0,\n      \"pais\": {\n        \"codigoPais\": 0,\n        \"chave\": \"string\",\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"sigla2\": \"string\",\n        \"sigla3\": \"string\",\n        \"chaveBacen\": \"string\",\n        \"moeda\": {\n          \"codigoMoeda\": 0,\n          \"chave\": \"string\",\n          \"descricao\": \"string\",\n          \"simbolo\": \"string\"\n        }\n      },\n      \"banco\": {\n        \"chave\": \"string\",\n        \"codigoBancoCentral\": \"string\",\n        \"codigoSwift\": \"string\",\n        \"codigoAba\": \"string\",\n        \"nome\": \"string\",\n        \"pais\": {\n          \"codigoPais\": 0,\n          \"chave\": \"string\",\n          \"sigla\": \"string\",\n          \"nome\": \"string\",\n          \"sigla2\": \"string\",\n          \"sigla3\": \"string\",\n          \"chaveBacen\": \"string\",\n          \"moeda\": {\n            \"codigoMoeda\": 0,\n            \"chave\": \"string\",\n            \"descricao\": \"string\",\n            \"simbolo\": \"string\"\n          }\n        },\n        \"moeda\": {\n          \"codigoMoeda\": 0,\n          \"chave\": \"string\",\n          \"descricao\": \"string\",\n          \"simbolo\": \"string\"\n        }\n      },\n      \"paisCodigo\": \"string\",\n      \"paisId\": 0,\n      \"email\": \"string\",\n      \"tipoFornecedor\": \"Terceiro\",\n      \"tipoFornecedorValor\": \"string\",\n      \"contaContabil\": {\n        \"chave\": \"string\",\n        \"codigo\": \"string\",\n        \"descricao\": \"string\",\n        \"tipo\": \"Sintetico\"\n      },\n      \"ativo\": true,\n      \"supplyInternacional\": true,\n      \"campoUsuario\": [\n        {\n          \"nomeVariavel\": \"string\",\n          \"valor\": \"string\",\n          \"campoAdicionalId\": 0\n        }\n      ],\n      \"fornecedorContatos\": [\n        {\n          \"chave\": \"string\",\n          \"nome\": \"string\",\n          \"telefone\": \"string\",\n          \"email\": \"string\"\n        }\n      ]\n    }\n  },\n  \"importador\": {\n    \"chave\": \"string\",\n    \"nome\": \"string\",\n    \"numeroDocumento\": \"string\",\n    \"linhaEndereco1\": \"string\",\n    \"linhaEndereco2\": \"string\",\n    \"nomeCidade\": \"string\",\n    \"enderecoNumero\": \"string\",\n    \"bairro\": \"string\",\n    \"cep\": \"string\",\n    \"telefone\": \"string\",\n    \"estado\": {\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"percentualIcms\": 0,\n      \"prazoCancelamentoNfeHoras\": 0,\n      \"codigoIbge\": \"string\"\n    },\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"cidade\": {\n      \"codigoIbge\": \"string\",\n      \"nome\": \"string\",\n      \"chave\": \"string\",\n      \"codigoMunicipio\": \"string\",\n      \"estado\": {\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"percentualIcms\": 0,\n        \"prazoCancelamentoNfeHoras\": 0,\n        \"codigoIbge\": \"string\"\n      }\n    },\n    \"codigoTipoImportador\": \"PessoaJuridica\",\n    \"codigoTipoImportadorValor\": \"string\",\n    \"estadoSigla\": \"string\",\n    \"paisCodigo\": \"string\",\n    \"inscricaoEstadual\": \"string\"\n  },\n  \"origemDestinoOrigem\": {\n    \"chave\": \"string\",\n    \"codigoOrigemDestino\": \"string\",\n    \"nome\": \"string\",\n    \"siglaOrigemDestino\": \"string\",\n    \"estado\": \"string\",\n    \"codigoRecintoAlfandegado\": \"string\",\n    \"siglaRecintoAlfandegado\": \"string\",\n    \"tipoViaTransporte\": \"Maritimo\",\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    }\n  },\n  \"origemDestinoDestino\": {\n    \"chave\": \"string\",\n    \"codigoOrigemDestino\": \"string\",\n    \"nome\": \"string\",\n    \"siglaOrigemDestino\": \"string\",\n    \"estado\": \"string\",\n    \"codigoRecintoAlfandegado\": \"string\",\n    \"siglaRecintoAlfandegado\": \"string\",\n    \"tipoViaTransporte\": \"Maritimo\",\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    }\n  },\n  \"navioEmbarque\": {\n    \"codigoMercante\": \"string\",\n    \"nome\": \"string\"\n  },\n  \"navioTransbordo\": {\n    \"codigoMercante\": \"string\",\n    \"nome\": \"string\"\n  },\n  \"modalidadeImportacao\": \"ImportacaoPropria\",\n  \"dataPedidoCompra\": \"2025-03-13T12:16:35.698Z\",\n  \"numeroPo\": \"string\",\n  \"referenciaDespachante\": \"string\",\n  \"fornecedor\": {\n    \"chave\": \"string\",\n    \"empresaChave\": \"string\",\n    \"filialChave\": \"string\",\n    \"nome\": \"string\",\n    \"nomeFantasia\": \"string\",\n    \"numeroDocumento\": \"string\",\n    \"agencia\": \"string\",\n    \"conta\": \"string\",\n    \"responsavel\": \"string\",\n    \"linhaEndereco1\": \"string\",\n    \"linhaEndereco2\": \"string\",\n    \"enderecoNumero\": \"string\",\n    \"nomeCidade\": \"string\",\n    \"cidade\": {\n      \"codigoIbge\": \"string\",\n      \"nome\": \"string\",\n      \"chave\": \"string\",\n      \"codigoMunicipio\": \"string\",\n      \"estado\": {\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"percentualIcms\": 0,\n        \"prazoCancelamentoNfeHoras\": 0,\n        \"codigoIbge\": \"string\"\n      }\n    },\n    \"cidadeId\": 0,\n    \"estadoExterior\": \"string\",\n    \"bairro\": \"string\",\n    \"cep\": \"string\",\n    \"telefone\": \"string\",\n    \"digitoAgencia\": \"string\",\n    \"agenciaCompleta\": \"string\",\n    \"digitoConta\": \"string\",\n    \"swift\": \"string\",\n    \"iban\": \"string\",\n    \"contaCompleta\": \"string\",\n    \"estado\": {\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"percentualIcms\": 0,\n      \"prazoCancelamentoNfeHoras\": 0,\n      \"codigoIbge\": \"string\"\n    },\n    \"estadoId\": 0,\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"banco\": {\n      \"chave\": \"string\",\n      \"codigoBancoCentral\": \"string\",\n      \"codigoSwift\": \"string\",\n      \"codigoAba\": \"string\",\n      \"nome\": \"string\",\n      \"pais\": {\n        \"codigoPais\": 0,\n        \"chave\": \"string\",\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"sigla2\": \"string\",\n        \"sigla3\": \"string\",\n        \"chaveBacen\": \"string\",\n        \"moeda\": {\n          \"codigoMoeda\": 0,\n          \"chave\": \"string\",\n          \"descricao\": \"string\",\n          \"simbolo\": \"string\"\n        }\n      },\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"paisCodigo\": \"string\",\n    \"paisId\": 0,\n    \"email\": \"string\",\n    \"tipoFornecedor\": \"Terceiro\",\n    \"tipoFornecedorValor\": \"string\",\n    \"contaContabil\": {\n      \"chave\": \"string\",\n      \"codigo\": \"string\",\n      \"descricao\": \"string\",\n      \"tipo\": \"Sintetico\"\n    },\n    \"ativo\": true,\n    \"supplyInternacional\": true,\n    \"campoUsuario\": [\n      {\n        \"nomeVariavel\": \"string\",\n        \"valor\": \"string\",\n        \"campoAdicionalId\": 0\n      }\n    ],\n    \"fornecedorContatos\": [\n      {\n        \"chave\": \"string\",\n        \"nome\": \"string\",\n        \"telefone\": \"string\",\n        \"email\": \"string\"\n      }\n    ]\n  },\n  \"notify\": {\n    \"chave\": \"string\",\n    \"empresaChave\": \"string\",\n    \"filialChave\": \"string\",\n    \"nome\": \"string\",\n    \"nomeFantasia\": \"string\",\n    \"numeroDocumento\": \"string\",\n    \"agencia\": \"string\",\n    \"conta\": \"string\",\n    \"responsavel\": \"string\",\n    \"linhaEndereco1\": \"string\",\n    \"linhaEndereco2\": \"string\",\n    \"enderecoNumero\": \"string\",\n    \"nomeCidade\": \"string\",\n    \"cidade\": {\n      \"codigoIbge\": \"string\",\n      \"nome\": \"string\",\n      \"chave\": \"string\",\n      \"codigoMunicipio\": \"string\",\n      \"estado\": {\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"percentualIcms\": 0,\n        \"prazoCancelamentoNfeHoras\": 0,\n        \"codigoIbge\": \"string\"\n      }\n    },\n    \"cidadeId\": 0,\n    \"estadoExterior\": \"string\",\n    \"bairro\": \"string\",\n    \"cep\": \"string\",\n    \"telefone\": \"string\",\n    \"digitoAgencia\": \"string\",\n    \"agenciaCompleta\": \"string\",\n    \"digitoConta\": \"string\",\n    \"swift\": \"string\",\n    \"iban\": \"string\",\n    \"contaCompleta\": \"string\",\n    \"estado\": {\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"percentualIcms\": 0,\n      \"prazoCancelamentoNfeHoras\": 0,\n      \"codigoIbge\": \"string\"\n    },\n    \"estadoId\": 0,\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"banco\": {\n      \"chave\": \"string\",\n      \"codigoBancoCentral\": \"string\",\n      \"codigoSwift\": \"string\",\n      \"codigoAba\": \"string\",\n      \"nome\": \"string\",\n      \"pais\": {\n        \"codigoPais\": 0,\n        \"chave\": \"string\",\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"sigla2\": \"string\",\n        \"sigla3\": \"string\",\n        \"chaveBacen\": \"string\",\n        \"moeda\": {\n          \"codigoMoeda\": 0,\n          \"chave\": \"string\",\n          \"descricao\": \"string\",\n          \"simbolo\": \"string\"\n        }\n      },\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"paisCodigo\": \"string\",\n    \"paisId\": 0,\n    \"email\": \"string\",\n    \"tipoFornecedor\": \"Terceiro\",\n    \"tipoFornecedorValor\": \"string\",\n    \"contaContabil\": {\n      \"chave\": \"string\",\n      \"codigo\": \"string\",\n      \"descricao\": \"string\",\n      \"tipo\": \"Sintetico\"\n    },\n    \"ativo\": true,\n    \"supplyInternacional\": true,\n    \"campoUsuario\": [\n      {\n        \"nomeVariavel\": \"string\",\n        \"valor\": \"string\",\n        \"campoAdicionalId\": 0\n      }\n    ],\n    \"fornecedorContatos\": [\n      {\n        \"chave\": \"string\",\n        \"nome\": \"string\",\n        \"telefone\": \"string\",\n        \"email\": \"string\"\n      }\n    ]\n  },\n  \"dataEncerramento\": \"2025-03-13T12:16:35.699Z\",\n  \"quantidadeContainer\": 0,\n  \"numeroBooking\": \"string\",\n  \"dataEntrega\": \"2025-03-13T12:16:35.699Z\",\n  \"status\": \"Aberto\",\n  \"viaTransporte\": {\n    \"chave\": \"string\",\n    \"nome\": \"string\",\n    \"tipo\": \"Maritimo\",\n    \"tipoValor\": \"string\"\n  },\n  \"liAnuente\": \"Nao\",\n  \"numeroLi\": \"string\",\n  \"dataValidadeLi\": \"2025-03-13T12:16:35.699Z\",\n  \"dataDeferimentoLi\": \"2025-03-13T12:16:35.699Z\",\n  \"liDeferido\": true,\n  \"liRestricao\": true,\n  \"dataEtd\": \"2025-03-13T12:16:35.699Z\",\n  \"dataEta\": \"2025-03-13T12:16:35.699Z\",\n  \"valorOutrasDespesas\": 0,\n  \"valorSeguro\": 0,\n  \"valorFrete\": 0,\n  \"observacao\": \"string\",\n  \"referencia\": \"string\",\n  \"chaveParamNfe\": \"string\",\n  \"itensPedidoCompra\": [\n    {\n      \"chave\": \"string\",\n      \"ordem\": 0,\n      \"paisOrigem\": {\n        \"codigoPais\": 0,\n        \"chave\": \"string\",\n        \"sigla\": \"string\",\n        \"nome\": \"string\",\n        \"sigla2\": \"string\",\n        \"sigla3\": \"string\",\n        \"chaveBacen\": \"string\",\n        \"moeda\": {\n          \"codigoMoeda\": 0,\n          \"chave\": \"string\",\n          \"descricao\": \"string\",\n          \"simbolo\": \"string\"\n        }\n      },\n      \"ncm\": {\n        \"chave\": \"string\",\n        \"codigo\": \"string\",\n        \"descricao\": \"string\",\n        \"ncmSiscomex\": \"string\",\n        \"percentualIi\": 0,\n        \"percentualIpi\": 0,\n        \"percentualPis\": 0,\n        \"percentualCofins\": 0\n      },\n      \"hsCode\": {\n        \"chave\": \"string\",\n        \"codigo\": \"string\",\n        \"descricao\": \"string\",\n        \"percentualIi\": 0,\n        \"percentualIva\": 0\n      },\n      \"produto\": {\n        \"chave\": \"string\",\n        \"ativo\": true,\n        \"fabricanteId\": 0,\n        \"fabricanteChave\": \"string\",\n        \"empresaChave\": \"string\",\n        \"filialChave\": \"string\",\n        \"descricao\": \"string\",\n        \"descricaoResumida\": \"string\",\n        \"descricaoCompleta\": \"string\",\n        \"descricaoCompletaDi\": \"string\",\n        \"ncm\": {\n          \"chave\": \"string\",\n          \"codigo\": \"string\",\n          \"descricao\": \"string\",\n          \"ncmSiscomex\": \"string\",\n          \"percentualIi\": 0,\n          \"percentualIpi\": 0,\n          \"percentualPis\": 0,\n          \"percentualCofins\": 0\n        },\n        \"ncmCodigo\": \"string\",\n        \"hsCode\": {\n          \"chave\": \"string\",\n          \"codigo\": \"string\",\n          \"descricao\": \"string\",\n          \"percentualIi\": 0,\n          \"percentualIva\": 0\n        },\n        \"pesoLiquidoUnitario\": 0,\n        \"pesoBruto\": 0,\n        \"anuente\": true,\n        \"paisOrigem\": {\n          \"codigoPais\": 0,\n          \"chave\": \"string\",\n          \"sigla\": \"string\",\n          \"nome\": \"string\",\n          \"sigla2\": \"string\",\n          \"sigla3\": \"string\",\n          \"chaveBacen\": \"string\",\n          \"moeda\": {\n            \"codigoMoeda\": 0,\n            \"chave\": \"string\",\n            \"descricao\": \"string\",\n            \"simbolo\": \"string\"\n          }\n        },\n        \"partNumber\": \"string\",\n        \"unidadeMedidaChave\": \"string\",\n        \"campoUsuario\": [\n          {\n            \"nomeVariavel\": \"string\",\n            \"valor\": \"string\",\n            \"campoAdicionalId\": 0\n          }\n        ],\n        \"grupoProduto\": {\n          \"chave\": \"string\",\n          \"descricao\": \"string\",\n          \"codigo\": \"string\",\n          \"sequencial\": 0,\n          \"classeProduto\": {\n            \"chave\": \"string\",\n            \"descricao\": \"string\",\n            \"codigo\": \"string\"\n          }\n        },\n        \"larguraCbm\": 0,\n        \"alturaCbm\": 0,\n        \"comprimentoCbm\": 0,\n        \"cubagemEmbalagem\": 0,\n        \"quantidadeNaEmbalagem\": 0,\n        \"partNumberFornecedor\": \"string\",\n        \"cargaIMO\": \"string\",\n        \"codigoBarras\": \"string\",\n        \"tipoProduto\": {\n          \"chave\": \"string\",\n          \"codigo\": \"string\",\n          \"descricao\": \"string\"\n        },\n        \"produtoDerivacoes\": [\n          {\n            \"codigo\": \"string\",\n            \"descricao\": \"string\",\n            \"descricaoCompletaDi\": \"string\",\n            \"descComplementar\": \"string\",\n            \"codigoReferencia\": \"string\",\n            \"precoCusto\": 0,\n            \"pesoBruto\": 0,\n            \"pesoLiquido\": 0,\n            \"volume\": 0,\n            \"codigoEmbalagem\": \"string\",\n            \"qtdProdEmbalagem\": 0,\n            \"largura\": 0,\n            \"altura\": 0,\n            \"comprimento\": 0\n          }\n        ],\n        \"produtoIdioma\": [\n          {\n            \"idiomaDocumentos\": \"string\",\n            \"descricao\": \"string\",\n            \"descricaoEncode\": \"string\",\n            \"descricaoProduto\": \"string\",\n            \"cabedal\": \"string\",\n            \"cabedalComposicao\": \"string\",\n            \"solado\": \"string\",\n            \"soladoComposicao\": \"string\",\n            \"forro\": \"string\",\n            \"forroComposicao\": \"string\",\n            \"alturaSalto\": \"string\",\n            \"cor\": \"string\",\n            \"tipoProduto\": \"string\",\n            \"codigoCombinacao\": \"string\",\n            \"marca\": \"string\",\n            \"colecao\": \"string\",\n            \"artigo\": \"string\",\n            \"composicao\": \"string\",\n            \"estruturaTecido\": \"string\",\n            \"naturezaMateriaPrima\": \"string\",\n            \"tipoLigamentoFios\": \"string\",\n            \"largura\": 0,\n            \"gramaturaMetroQuadrado\": 0,\n            \"tipoAcabamento\": \"string\",\n            \"gramaturaAcabamento\": 0,\n            \"trama\": \"string\",\n            \"urdume\": 0,\n            \"gramaturaMililitro\": 0,\n            \"medidas\": 0,\n            \"gramatura\": 0\n          }\n        ],\n        \"nve\": [\n          {\n            \"atributo\": \"string\",\n            \"especificacao\": \"string\"\n          }\n        ],\n        \"origemMercadoria\": \"Nenhum\",\n        \"aplicacaoMercadoria\": \"Indefinido\",\n        \"aplicacaoMercadoriaValor\": \"string\",\n        \"contaContabil\": {\n          \"chave\": \"string\",\n          \"codigo\": \"string\",\n          \"descricao\": \"string\",\n          \"tipo\": \"Sintetico\"\n        },\n        \"destaqueAnuencia\": \"string\",\n        \"custoPrevisto\": 0,\n        \"dataCalculoCustoPrevisto\": \"2025-03-13T12:16:35.699Z\"\n      },\n      \"descricaoCompletaDi\": \"string\",\n      \"fornecedor\": {\n        \"chave\": \"string\",\n        \"empresaChave\": \"string\",\n        \"filialChave\": \"string\",\n        \"nome\": \"string\",\n        \"nomeFantasia\": \"string\",\n        \"numeroDocumento\": \"string\",\n        \"agencia\": \"string\",\n        \"conta\": \"string\",\n        \"responsavel\": \"string\",\n        \"linhaEndereco1\": \"string\",\n        \"linhaEndereco2\": \"string\",\n        \"enderecoNumero\": \"string\",\n        \"nomeCidade\": \"string\",\n        \"cidade\": {\n          \"codigoIbge\": \"string\",\n          \"nome\": \"string\",\n          \"chave\": \"string\",\n          \"codigoMunicipio\": \"string\",\n          \"estado\": {\n            \"sigla\": \"string\",\n            \"nome\": \"string\",\n            \"percentualIcms\": 0,\n            \"prazoCancelamentoNfeHoras\": 0,\n            \"codigoIbge\": \"string\"\n          }\n        },\n        \"cidadeId\": 0,\n        \"estadoExterior\": \"string\",\n        \"bairro\": \"string\",\n        \"cep\": \"string\",\n        \"telefone\": \"string\",\n        \"digitoAgencia\": \"string\",\n        \"agenciaCompleta\": \"string\",\n        \"digitoConta\": \"string\",\n        \"swift\": \"string\",\n        \"iban\": \"string\",\n        \"contaCompleta\": \"string\",\n        \"estado\": {\n          \"sigla\": \"string\",\n          \"nome\": \"string\",\n          \"percentualIcms\": 0,\n          \"prazoCancelamentoNfeHoras\": 0,\n          \"codigoIbge\": \"string\"\n        },\n        \"estadoId\": 0,\n        \"pais\": {\n          \"codigoPais\": 0,\n          \"chave\": \"string\",\n          \"sigla\": \"string\",\n          \"nome\": \"string\",\n          \"sigla2\": \"string\",\n          \"sigla3\": \"string\",\n          \"chaveBacen\": \"string\",\n          \"moeda\": {\n            \"codigoMoeda\": 0,\n            \"chave\": \"string\",\n            \"descricao\": \"string\",\n            \"simbolo\": \"string\"\n          }\n        },\n        \"banco\": {\n          \"chave\": \"string\",\n          \"codigoBancoCentral\": \"string\",\n          \"codigoSwift\": \"string\",\n          \"codigoAba\": \"string\",\n          \"nome\": \"string\",\n          \"pais\": {\n            \"codigoPais\": 0,\n            \"chave\": \"string\",\n            \"sigla\": \"string\",\n            \"nome\": \"string\",\n            \"sigla2\": \"string\",\n            \"sigla3\": \"string\",\n            \"chaveBacen\": \"string\",\n            \"moeda\": {\n              \"codigoMoeda\": 0,\n              \"chave\": \"string\",\n              \"descricao\": \"string\",\n              \"simbolo\": \"string\"\n            }\n          },\n          \"moeda\": {\n            \"codigoMoeda\": 0,\n            \"chave\": \"string\",\n            \"descricao\": \"string\",\n            \"simbolo\": \"string\"\n          }\n        },\n        \"paisCodigo\": \"string\",\n        \"paisId\": 0,\n        \"email\": \"string\",\n        \"tipoFornecedor\": \"Terceiro\",\n        \"tipoFornecedorValor\": \"string\",\n        \"contaContabil\": {\n          \"chave\": \"string\",\n          \"codigo\": \"string\",\n          \"descricao\": \"string\",\n          \"tipo\": \"Sintetico\"\n        },\n        \"ativo\": true,\n        \"supplyInternacional\": true,\n        \"campoUsuario\": [\n          {\n            \"nomeVariavel\": \"string\",\n            \"valor\": \"string\",\n            \"campoAdicionalId\": 0\n          }\n        ],\n        \"fornecedorContatos\": [\n          {\n            \"chave\": \"string\",\n            \"nome\": \"string\",\n            \"telefone\": \"string\",\n            \"email\": \"string\"\n          }\n        ]\n      },\n      \"fabricante\": {\n        \"chave\": \"string\",\n        \"empresaChave\": \"string\",\n        \"filialChave\": \"string\",\n        \"nome\": \"string\",\n        \"numeroDocumento\": \"string\",\n        \"responsavel\": \"string\",\n        \"linhaEndereco1\": \"string\",\n        \"linhaEndereco2\": \"string\",\n        \"enderecoNumero\": \"string\",\n        \"nomeCidade\": \"string\",\n        \"telefone\": \"string\",\n        \"bairro\": \"string\",\n        \"cep\": \"string\",\n        \"email\": \"string\",\n        \"cidade\": {\n          \"codigoIbge\": \"string\",\n          \"nome\": \"string\",\n          \"chave\": \"string\",\n          \"codigoMunicipio\": \"string\",\n          \"estado\": {\n            \"sigla\": \"string\",\n            \"nome\": \"string\",\n            \"percentualIcms\": 0,\n            \"prazoCancelamentoNfeHoras\": 0,\n            \"codigoIbge\": \"string\"\n          }\n        },\n        \"estado\": {\n          \"sigla\": \"string\",\n          \"nome\": \"string\",\n          \"percentualIcms\": 0,\n          \"prazoCancelamentoNfeHoras\": 0,\n          \"codigoIbge\": \"string\"\n        },\n        \"pais\": {\n          \"codigoPais\": 0,\n          \"chave\": \"string\",\n          \"sigla\": \"string\",\n          \"nome\": \"string\",\n          \"sigla2\": \"string\",\n          \"sigla3\": \"string\",\n          \"chaveBacen\": \"string\",\n          \"moeda\": {\n            \"codigoMoeda\": 0,\n            \"chave\": \"string\",\n            \"descricao\": \"string\",\n            \"simbolo\": \"string\"\n          }\n        },\n        \"estadoSigla\": \"string\",\n        \"paisCodigo\": \"string\",\n        \"ativo\": true,\n        \"estadoExterior\": \"string\"\n      },\n      \"embalagem\": {\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"sigla\": \"string\",\n        \"codigoSiscomex\": \"string\",\n        \"pesoQuilograma\": 0,\n        \"comprimento\": 0,\n        \"largura\": 0,\n        \"altura\": 0,\n        \"dimensoes\": \"string\",\n        \"ativo\": true,\n        \"cubagem\": 0\n      },\n      \"quantidade\": 0,\n      \"quantidadeEmbalagens\": 0,\n      \"percentualIi\": 0,\n      \"percentualIpi\": 0,\n      \"percentualPis\": 0,\n      \"percentualCofins\": 0,\n      \"percentualIva\": 0,\n      \"aliquotaIntegradaErp\": true,\n      \"preco\": 0,\n      \"pesoLiquidoUnitario\": 0,\n      \"pesoBruto\": 0,\n      \"consumoInterno\": true,\n      \"destinacaoMercadoria\": \"NaoInformado\",\n      \"origemMercadoria\": \"Nenhum\",\n      \"rateioAntiDumping\": \"Nenhum\",\n      \"baseAntidumping\": 0,\n      \"referenciaProduto\": \"string\",\n      \"itemPedido\": \"string\",\n      \"pesoLiquido\": 0,\n      \"valorTotal\": 0,\n      \"atoConcessorioDrawback\": \"string\",\n      \"itemConcessorioDrawback\": \"string\",\n      \"dataSolicitacaoEntrega\": \"2025-03-13T12:16:35.699Z\",\n      \"dataConfirmacaoFornecedor\": \"2025-03-13T12:16:35.699Z\",\n      \"dataPrevisaoFornecedor\": \"2025-03-13T12:16:35.699Z\",\n      \"dataPrevisaoChegada\": \"2025-03-13T12:16:35.699Z\",\n      \"justificativaAlteracao\": \"string\",\n      \"unidadeMedidaChave\": \"string\",\n      \"grupoMercadoria\": \"string\",\n      \"centro\": \"string\",\n      \"observacao\": \"string\",\n      \"lote\": \"string\",\n      \"dataPrevisaoColeta\": \"2025-03-13T12:16:35.699Z\",\n      \"dataEfetivaColeta\": \"2025-03-13T12:16:35.699Z\",\n      \"dataFabrica\": \"2025-03-13T12:16:35.699Z\",\n      \"grupoCompradores\": {\n        \"chave\": \"string\",\n        \"descricao\": \"string\"\n      },\n      \"centroCusto\": {\n        \"centroCustoPaiId\": 0,\n        \"centroCustoPaiDescricao\": \"string\",\n        \"chave\": \"string\",\n        \"codigo\": \"string\",\n        \"descricao\": \"string\",\n        \"filtroExcetoCentroCustoId\": 0\n      },\n      \"incoterm\": {\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"sigla\": \"string\",\n        \"calculaFrete\": true,\n        \"calculaSeguro\": true,\n        \"tipoFrete\": \"PrePaid\",\n        \"tipoFreteValor\": \"string\"\n      },\n      \"valorProvisorio\": 0,\n      \"requerente\": \"string\",\n      \"planejador\": \"string\",\n      \"campoUsuario\": [\n        {\n          \"nomeVariavel\": \"string\",\n          \"valor\": \"string\",\n          \"campoAdicionalId\": 0\n        }\n      ],\n      \"partNumberFornecedor\": \"string\",\n      \"cargaIMO\": \"string\",\n      \"codigoDerivacao\": \"string\",\n      \"transacao\": \"string\",\n      \"areaLinha\": \"string\",\n      \"material\": \"string\",\n      \"aprovacaoComercial\": \"Nao\",\n      \"billingInvoice\": \"string\",\n      \"numeroSerie\": \"string\",\n      \"quantidadeEntregueOrigem\": 0,\n      \"statusInspecaoItem\": \"AguardandoAgendamento\",\n      \"ordemVenda\": \"string\",\n      \"projetoWBS\": \"string\",\n      \"saldoFornecedor\": 0,\n      \"elementoPEP\": \"string\",\n      \"classificacaoPEP\": \"Sobressalente\"\n    }\n  ],\n  \"moeda\": {\n    \"codigoMoeda\": 0,\n    \"chave\": \"string\",\n    \"descricao\": \"string\",\n    \"simbolo\": \"string\"\n  },\n  \"incotermChave\": \"string\",\n  \"tipoDocumentoExportacao\": {\n    \"chave\": \"string\",\n    \"descricao\": \"string\"\n  },\n  \"termoCondicoes\": \"string\",\n  \"formaPagamento\": {\n    \"chave\": \"string\",\n    \"descricao\": \"string\",\n    \"campoUsuario\": [\n      {\n        \"nomeVariavel\": \"string\",\n        \"valor\": \"string\",\n        \"campoAdicionalId\": 0\n      }\n    ],\n    \"itensFormaPagamento\": [\n      {\n        \"tipoFormaPagamento\": \"Antecipado\",\n        \"dias\": 0,\n        \"percentual\": 0,\n        \"dataBaseAntecipado\": \"DataAberturaProcesso\",\n        \"dataBaseFuturo\": \"DataEmissaoImpoExpoPedVenda\"\n      }\n    ]\n  },\n  \"campoUsuario\": [\n    {\n      \"nomeVariavel\": \"string\",\n      \"valor\": \"string\",\n      \"campoAdicionalId\": 0\n    }\n  ],\n  \"paisProcedencia\": {\n    \"codigoPais\": 0,\n    \"chave\": \"string\",\n    \"sigla\": \"string\",\n    \"nome\": \"string\",\n    \"sigla2\": \"string\",\n    \"sigla3\": \"string\",\n    \"chaveBacen\": \"string\",\n    \"moeda\": {\n      \"codigoMoeda\": 0,\n      \"chave\": \"string\",\n      \"descricao\": \"string\",\n      \"simbolo\": \"string\"\n    }\n  },\n  \"agenteCarga\": {\n    \"chave\": \"string\",\n    \"nome\": \"string\",\n    \"chaveFornecedor\": \"string\",\n    \"numeroDocumento\": \"string\",\n    \"tipoPessoa\": \"Fisica\",\n    \"tipoPessoaValor\": \"string\",\n    \"tipoArmadorAgente\": \"Armador\",\n    \"tipoArmadorAgenteValor\": \"string\",\n    \"codigoInttra\": \"string\",\n    \"pais\": {\n      \"codigoPais\": 0,\n      \"chave\": \"string\",\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"sigla2\": \"string\",\n      \"sigla3\": \"string\",\n      \"chaveBacen\": \"string\",\n      \"moeda\": {\n        \"codigoMoeda\": 0,\n        \"chave\": \"string\",\n        \"descricao\": \"string\",\n        \"simbolo\": \"string\"\n      }\n    },\n    \"estado\": {\n      \"sigla\": \"string\",\n      \"nome\": \"string\",\n      \"percentualIcms\": 0,\n      \"prazoCancelamentoNfeHoras\": 0,\n      \"codigoIbge\": \"string\"\n    },\n    \"nomeEstado\": \"string\",\n    \"nomeCidade\": \"string\",\n    \"codigoIbge\": \"string\",\n    \"enderecoNumero\": \"string\",\n    \"linhaEndereco1\": \"string\",\n    \"linhaEndereco2\": \"string\",\n    \"bairro\": \"string\",\n    \"cep\": \"string\",\n    \"telefone\": \"string\",\n    \"email\": \"string\",\n    \"emailAereo\": \"string\",\n    \"emailFerroviario\": \"string\",\n    \"emailRodoviario\": \"string\"\n  },\n  \"comissao\": 0,\n  \"unidadeNegocio\": {\n    \"chave\": \"string\",\n    \"descricao\": \"string\"\n  },\n  \"coordenadorCompras\": {\n    \"chave\": \"string\",\n    \"nome\": \"string\"\n  },\n  \"valorDescontos\": 0,\n  \"contatoFornecedor\": \"string\",\n  \"telefoneFornecedor\": \"string\",\n  \"emailFornecedor\": \"string\",\n  \"precoProvisorio\": true,\n  \"statusSupply\": \"Aprovado\"\n}",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54540,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF para o Sankhya \"The operation has timed out\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro estava ocorrendo pois no servidor do cliente estava sendo identificado como DDOS, devido a quantidade de chamadas realizada pelo servidor da Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário a liberação do endereço Narwal no firewall do cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54561,
    "customFieldValues": [
      {
        "value": "Usuário não consegue redefinir o narwal",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53732,
    "customFieldValues": [
      {
        "value": "Nota Fiscal de saída com IPI na base",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na parametrização no grupo Produto campo \"Valor total dos produtos (Fórmula):\" deverá ser informado a fórmula ({ValorTotal})/((100 - {TaxaIcms})/100), no campo \"Valor total da nota fiscal (Fórmula):\" informar {ValorTotal}+{Ipi}. No grupo IPI campo Base de cálculo (Fórmula):\n({ValorTotal})/((100 - {TaxaIcms})/100). No grupo ICMS no campo \"Base de cálculo (Fórmula)\" ({ValorTotal} + {Ipi}) - (({ValorTotal} + {Ipi}) * ({TaxaIcms}/100))+(({ValorTotal}) * ({TaxaIcms}/100))\n\nNo cadastro do cliente:\nSelecionar o campo \"[x] Considerar configuração do cliente\";\nNa guia Fiscal, grupo Conta e Ordem nos campos:\nValor produtos NF entrada: VMLD(CIF)\nValor produtos NF saída: Base do ICMS\nBase IPI saída: Base do ICMS",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54751,
    "customFieldValues": [
      {
        "value": "Alerta \"O campo NumeroPo deve ser uma cadeia de caracteres ou tipo de matriz com comprimento máximo de '50' caracteres\"",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar salvar um processo criado a partir de um pedido de compra o sistema acusa o alerta \"O campo NumeroPo deve ser uma cadeia de caracteres ou tipo de matriz com comprimento máximo de '50' caracteres\" que remete ao campo Referencia do Pedido de Compra.",
        "customFieldId": 206843
      },
      {
        "value": "Limitar o campo Referencia do Pedido de Compra a 50 caracteres.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54595,
    "customFieldValues": [
      {
        "value": "Configuração de conta SMTP com host do GMAIL.",
        "customFieldId": 206842
      },
      {
        "value": "Ao inserir as informações da conta SMTP gmail no Narwal, o sistema não consegue enviar os e-mails de acordo.",
        "customFieldId": 206843
      },
      {
        "value": "Quando host smtp for smtp.gmail.com ou qualquer domínio do gmail, deve-se gerar uma senha de app para que o Narwal consiga realizar o envio dos follow-ups.\n\nObs: A senha de app só poderá ser configurada caso a conta contenha autenticação de 2 etapas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54810,
    "customFieldValues": [
      {
        "value": "Caixa de correio não disponível ao redefinir a senha do usuário.",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar redefinir a senha do usuário via interface, o erro \"Caixa de correio não disponível, Daily user sending limit exceeded\" é disparado.",
        "customFieldId": 206843
      },
      {
        "value": "A conta SMTP cadastrada na rotina \"Empresa\" -> Aba parâmetros excedeu o limite diário de envio de e-mails, deve-se aguardar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54746,
    "customFieldValues": [
      {
        "value": "Nota fiscal com valor divergente ao gerar a nota. ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do Usuário ao preencher a parametrização. ",
        "customFieldId": 206843
      },
      {
        "value": "É importante salientar que é recomendável marcar a flag no cadastro antes de emitir as notas fiscais quando houver processos de ativo/consumo com IPI na BC do ICMS. Recomenda-se remover a flag do cadastro após a emissão das notas, caso o cliente trabalhe com cenários padrões de conta e ordem, para que não interfira nos demais cálculos. \n\nPara que a nota saísse de acordo, fiz o ajuste no cadastro do cliente informando no campo de Fiscal, para que o valor total dos produtos da NF ficasse como \" TOTAL DA NF DE ENTRADA- ICMS \"\n\nFoi realizado o ajuste na parametrização código 31, informando as formulas valor total dos produtos, valor total NF, valos bc ICMS e valor do IPI. \n\nApós os ajustes a nota foi gerada e saiu de acordo com o calculo da cliente.  ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53853,
    "customFieldValues": [
      {
        "value": "Problemas de integração com a Tradings e Angeloni / Open Market",
        "customFieldId": 206842
      },
      {
        "value": "Problemas de integração com a Tradings e Angeloni / Open Market",
        "customFieldId": 206843
      },
      {
        "value": "Cliente não deu retorno, dessa forma encerrei chamado como sem retorno ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53465,
    "customFieldValues": [
      {
        "value": "Como utilizar a rotina de LPCO no Narwal?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Pré-requisitos:\n\nRepresentante legal com certificado válido;\nImportador;\nCatálogo de produto ativado;\n\nÉ importante pontuar que essa tela contém apenas produtos que possuem catálogos ativados para o Importador utilizado no cadastro do LPCO. \n\nÉ importante frisar que a geração do LPCO depende totalmente da necessidade dele, e há vários fatores que contribuem para isso, tais como o preenchimento de atributos no catálogo, fundamento legal ou país de origem. \n\nPara finalizar o pedido, basta clicar em Gerar LPCO no menu de ação do registro escolhido. Estando tudo certo, o pedido recebe um número, que pode ser utilizado para pesquisá-lo no Portal único, uma alteração de status e um número de registro. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53894,
    "customFieldValues": [
      {
        "value": "Por que a THC está entrando no valor aduaneiro?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Pois a despesa está configurada como \"Base de imposto\". Para que a despesa THC não entre no valor aduaneiro, é necessário realizar a alteração no \"Tipo despesa\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53949,
    "customFieldValues": [
      {
        "value": "Por que o peso bruto não está sendo preenchido na nota fiscal?",
        "customFieldId": 206842
      },
      {
        "value": "dúvida",
        "customFieldId": 206843
      },
      {
        "value": "O peso bruto na nota fiscal é resgatado a partir do peso bruto total do processo, utilizando o rateio de peso entre os itens. Para que esse campo seja preenchido corretamente, é necessário:\n\n1️⃣ Preencher o campo \"Peso Bruto\" na aba de Transporte do processo.\n2️⃣ Realizar o processamento da DI antes da criação da nota fiscal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54080,
    "customFieldValues": [
      {
        "value": "Esta baixa deve ser realizada pelo financeiro > Fechamento de câmbio titulo",
        "customFieldId": 206842
      },
      {
        "value": "Exclusão do fechamento de cambio",
        "customFieldId": 206843
      },
      {
        "value": "Acessar a rotina Fechamento de cambio e realizar a exclusão. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54111,
    "customFieldValues": [
      {
        "value": "Por que os números da nota fiscal estavam sendo pulados?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A numeração do sequencial da NF seguiu corretamente conforme definição da série.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54171,
    "customFieldValues": [
      {
        "value": "Habilitar guia/campo",
        "customFieldId": 206842
      },
      {
        "value": "Usuário com permissão desabilitou visualização",
        "customFieldId": 206843
      },
      {
        "value": "Clicar na guia ou campo para habilitar visualização.\nNo cadastro de usuário, quando o campo \"[x] Permitir obrigar campos\" está selecionado, esse usuário tem a permissão para habilitar/desabilitar visualizações no Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54199,
    "customFieldValues": [
      {
        "value": "Por que o valor CIF do relatório do Fechamento Financeiro está divergente do CIF do processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Este relatório é padrão do Narwal, ele puxa o valor informado na coluna \"Valor total\" da aba \"Produto\" do processo, no caso deste chamado, havia adicional na Invoice, mas ele não entra no \"Valor total\" da aba produto. Caso seja necessário realizar alterações, seria serviços complementares.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54220,
    "customFieldValues": [
      {
        "value": "Cadastro de fornecedor, cliente não conseguia preencher os campos de endereço. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não conseguia inserir os dados de endereço no cadastro do fornecedor. ",
        "customFieldId": 206843
      },
      {
        "value": "Para a solução pedimos que dentro do cadastro de usuário ela habilitasse o campo de permitir e obrigar campos, dessa forma conseguiu fazer o preenchimento. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53552,
    "customFieldValues": [
      {
        "value": "Erro ao enviar pedido para o Narwal \"Falha de integração: E-mail inválido\"",
        "customFieldId": 206842
      },
      {
        "value": "O e-mail no cadastro do fabricante estava com 3 caracteres ZWSP, por conta desses caracteres estava sendo ocasionado o erro.",
        "customFieldId": 206843
      },
      {
        "value": "Remover os caracteres do cadastro do E-mail no ERP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53211,
    "customFieldValues": [
      {
        "value": "API's sem Token.",
        "customFieldId": 206842
      },
      {
        "value": "Estas estão apontadas alarmadas no monitoramento como não contendo Token",
        "customFieldId": 206843
      },
      {
        "value": "APIs abertas e sob controle, verificado pelo Alessandro",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54132,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão em todas as rotinas.",
        "customFieldId": 206843
      },
      {
        "value": "Reinicialização do servidor de aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53914,
    "customFieldValues": [
      {
        "value": " Integração despesas importação em duplicidade",
        "customFieldId": 206842
      },
      {
        "value": " Integração despesas importação em duplicidade",
        "customFieldId": 206843
      },
      {
        "value": "Chamado encerrado pois cliente resolveu internamente assim nao dando um retorno do que foi feito, apenas pedindo para fechar o chamado",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53481,
    "customFieldValues": [
      {
        "value": "Ordem não aparece no narwal - Integração",
        "customFieldId": 206842
      },
      {
        "value": "A ordem de compras CP0030102, não está integrando do LN para o narwal. ",
        "customFieldId": 206843
      },
      {
        "value": "O erro foi causado por uma alteração no web.config do cliente, configurando para o uso de um token dinâmico. Isso impediu a aplicação do cliente de se conectar à nossa API, resultando na interrupção da fila de processamento.\n\nPara mitigar o problema, temporariamente desativamos a autenticação por token na API do cliente, definindo UseTokenAuthentication = false e deixando ApiKeyAuthentication vazio. Essa medida permite que a API continue operando até que o cliente implemente corretamente o suporte ao token dinâmico em sua aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53250,
    "customFieldValues": [
      {
        "value": "Por que o valor da despesa de frete está alterando o valor mesmo depois de baixada?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O valor da despesa será ajustado automaticamente se o cálculo for realizado pelo Narwal. Por exemplo, se o tipo de cálculo da despesa na rotina \"Tipo despesa\" for II, ele sempre ajustará para o valor correto do II, pois está configurado para o sistema calcular automaticamente.\nOutras despesas, cujo tipo de cálculo é \"Considera parâmetros\" e que não são inseridas automaticamente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53519,
    "customFieldValues": [
      {
        "value": "Integração Narwal x Narwal, não retornou ao cliente",
        "customFieldId": 206842
      },
      {
        "value": "Invoice estava com numero duplicado na base do cliente importador, isso faz com que a integração se perca e não consiga integrar as informações corretamente.",
        "customFieldId": 206843
      },
      {
        "value": "A solução aplicada foi realizar a troca do numero da invoice, permitindo com que não tivesse trava na integração entre bases Narwal",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53782,
    "customFieldValues": [
      {
        "value": "Alíquota tem com valor, porém deveria ser imune.",
        "customFieldId": 206842
      },
      {
        "value": "Não está com alíquota zerada na parametrização.",
        "customFieldId": 206843
      },
      {
        "value": "Zerar alíquota na parametrização ou informar diferimento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54036,
    "customFieldValues": [
      {
        "value": "Cliente não retornou",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não retornou",
        "customFieldId": 206843
      },
      {
        "value": "Cliente não retornou",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53394,
    "customFieldValues": [
      {
        "value": "Codigo de duplo fator solicitando diversas vezes",
        "customFieldId": 206842
      },
      {
        "value": "Cliente relatou que toda vez que vai entrar no narwal solicita o codigo de duplo fator.",
        "customFieldId": 206843
      },
      {
        "value": "Medida contorno foi alterar o duplo fator via banco para este usuario, e criado um chamado em paralelo para dev verificar a regra de disparo no codigo fonte.\nTicket BL: 53394",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53511,
    "customFieldValues": [
      {
        "value": "Não consigo salvar edições na DI Processada sem informar o numero da DI no Processo",
        "customFieldId": 206842
      },
      {
        "value": "A partir da Versão R6, é necessário que o despachante cadastrado no processo esteja com a flag \"próprio\" selecionada.\n\n",
        "customFieldId": 206843
      },
      {
        "value": "Para clientes que desejam realizar o processamento das adições da DI pelo Narwal, ou seja, processos que não possuem o xml da DI integrada, deve considerar que se o despachante informado no processo não for \"próprio\", será necessário que informe o numero da DI no Processo para prosseguir com as edições.\n\nPara resolver o problema da mensagem \"Informe o número DI/DIRE ou despachante proprio\", basta informar o despachante cadastrado como próprio = sim.\n\nCaso já tenha processado a DI, será necessário cancelar o processamento.\nCaso o erro permaneça, importante realizar a seguinte ação:\n1.Remover o despachante do processo > salvar\n2.Cancelar o processamento da DI > Editar Processo > Informar o Despachante novamente > Salvar\n3. Processar a DI pelo botão de ação do Processo > Documento de Importação > Processar\nDepois > Atualizar Taxas\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53731,
    "customFieldValues": [
      {
        "value": "Erro no envio da NF de despesa para Sênior",
        "customFieldId": 206842
      },
      {
        "value": "Nota de entrada não estava como enviada para o ERP.",
        "customFieldId": 206843
      },
      {
        "value": "Enviar nota de entrada para o ERP",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53780,
    "customFieldValues": [
      {
        "value": "Erro ao cadastrar usuario",
        "customFieldId": 206842
      },
      {
        "value": "O mesmo estava com e-mail cadastrado na coluna aspnetusers",
        "customFieldId": 206843
      },
      {
        "value": "Feito a exclusão da coluna pois não tinha vinculo algum com nenhum usuário.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53958,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF: \"MENSAGEM DO SANKHYA: Erro de conversão de valor para o campo 'CODCIDORIGEM': EX \"",
        "customFieldId": 206842
      },
      {
        "value": "Ao enviar a nota fiscal para o  Sankhya, está gerando erro pois o Fornecedor não foi vinculado a nota fiscal ao gerar o ajuste.\nQuando o fornecedor não está vinculado, por padrão é enviado \"EX\" no campo \"CODCIDORIGEM\", porém o Sankhya não aceita essa informação no campo.",
        "customFieldId": 206843
      },
      {
        "value": "Para liberação da NF, foi necessário realizar o vinculo do fornecedor via banco, sendo preenchido com o mesmo fornecedor presente na tabela \"NfeItem\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54089,
    "customFieldValues": [
      {
        "value": "200 - Código: Descrição: Por Favor, entre em contato com o suporte GIssOnline e informe o código de erro",
        "customFieldId": 206842
      },
      {
        "value": "Provável instabilidade",
        "customFieldId": 206843
      },
      {
        "value": "A solução é alterar o status da nota fiscal e enviar novamente a NF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54098,
    "customFieldValues": [
      {
        "value": "Erro de Autorização na API.",
        "customFieldId": 206842
      },
      {
        "value": "A partir de algumas versões, quando atualizado o ambiente está sendo removido as informações de autenticação da API, e atualmente não é mais possível utilizar a API sem autenticação.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustar o arquivo \"web.config\" da API, para a autenticação utilizada pelo cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54106,
    "customFieldValues": [
      {
        "value": "Enviar data de criação do título do contas a pagar para o Sankhya (campo Dt. Negociação",
        "customFieldId": 206842
      },
      {
        "value": "A Causa do problema era que a data do titulo não estava alimentando corretamente o Sankhya",
        "customFieldId": 206843
      },
      {
        "value": "Assim como ocorre para os números de títulos, a mesma variável de ambiente abrange o campo Data Negociação:\n\nQuando a variável de ambiente NWL_ENVOPERFINANESPECIFICADASANKHYA estiver marcada, essas são as regras:\n\n\n\nTítulos gerados por:\n\nNumerário: DT.Negociação = Data da geração da Parcela de Numerário;\n\nNota Fiscal de Despesa: DT.Negociação = Dt Emissão da nota de despesa;\n\nAdiantamento de Contrato de Cambio:  DT.Negociação = Dt. Criação do Contrato de Cambio;\n\nParcelas de Invoice: DT.Negociação = Dt.Emissão Invoice;\n\nFechamento Financeiro: DT.Negociação = Dt. Fechamento Financeiro.\n\n\n\nPara todos os casos, a data da negociação será a data do Pedido de Compra, lembrando que é a data da criação do pedido de compra gerado no Sankhya e, ainda, se para os tipos de títulos não for informado alguma data, será considerado a data do pedido de compra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54175,
    "customFieldValues": [
      {
        "value": "Valores dos impostos incorretos ao integrar o XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "A taxa ce Mercante é uma base de impostos, neste caso, ela estava sendo integrada com a taxa \"errada\", isso porque havia 3 TAGs dela no xml, as 3 estavam com taxas de conversão diferentes e estava puxando apenas a primeira taxa ",
        "customFieldId": 206843
      },
      {
        "value": "Solução contorno foi ajustar manualmente para os impostos ficarem de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54200,
    "customFieldValues": [
      {
        "value": "Não gera FAQ",
        "customFieldId": 206842
      },
      {
        "value": "Não gera FAQ",
        "customFieldId": 206843
      },
      {
        "value": "Não gera FAQ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54243,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF para SAP B1 \"CServiceData::SetPropertyValueString failed; Value too long in property 'PackDescription' of 'TaxExtension'\"",
        "customFieldId": 206842
      },
      {
        "value": "No SAP havia uma limitação de 10 caracteres para o campo 'PackDescription', como o conteudo enviado passa de 10 caracteres, acaba retornando erro.",
        "customFieldId": 206843
      },
      {
        "value": "Alterar a informação preenchida dentro da NF.\n\nCaminho: Nota Fiscal -> editar -> Transporte -> Volumes",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54308,
    "customFieldValues": [
      {
        "value": "Como editar um documento no processo ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Para isso basta selecionar o documento e clicar em excluir, isso fará que voce exclua o documento que necessita e não todos.\nSobre a parte de não salvar foi feito teste e continua salvando corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54310,
    "customFieldValues": [
      {
        "value": "Como funcionam os \"Indicadores por tempo\"?",
        "customFieldId": 206842
      },
      {
        "value": "Indicadores estão com valor zerado.",
        "customFieldId": 206843
      },
      {
        "value": "Os indicadores informam a diferença de dias entre duas datas, essas datas dependem de qual indicador está sendo avaliado. Dados do processo.\n\nExemplo. Indicador: Desembaraço X Emissão Nota\nCálculo: Diferença em dias entre a DataDesembaraço e a DataNotaFiscal ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54323,
    "customFieldValues": [
      {
        "value": "Taxas das moedas não atualizaram",
        "customFieldId": 206842
      },
      {
        "value": "Aplicativo que atualiza taxas não está funcionando.",
        "customFieldId": 206843
      },
      {
        "value": "Rodar o job para atualizar taxa ptax, manualmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54324,
    "customFieldValues": [
      {
        "value": "Envio NF para SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "Solucionado em versão posterior ",
        "customFieldId": 206843
      },
      {
        "value": "Ao enviar NF para SEFAZ está ocorrendo a mensagem em tela relacionada a 'gCred'.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54362,
    "customFieldValues": [
      {
        "value": "Agenda sobre RECOF-SPED Importação",
        "customFieldId": 206842
      },
      {
        "value": "Solicitação de agenda para tratar de RECOF-SPED Importação.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente/usuária entrou de férias. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54366,
    "customFieldValues": [
      {
        "value": "Por que o valor do ICMS não está fechando?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Podem haver diversas razões, a de chamado se enquadrada na variável NWL_PREPAIDICMS habilitada, fazendo com que a despesa base de imposto fosse descontada da base do ICMS.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54380,
    "customFieldValues": [
      {
        "value": "Operação incorreta do usuário.",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54393,
    "customFieldValues": [
      {
        "value": "Pedidos de Compra não estão integrando",
        "customFieldId": 206842
      },
      {
        "value": "Pedidos de Compra não estão integrando",
        "customFieldId": 206843
      },
      {
        "value": "Migrado integração de pedidos e custos para a fluid direto em PRD conforme alinhado com @Alessandro Rodrigues e desligado o integrador legado. Dessa forma os pedidos foram integrados.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54394,
    "customFieldValues": [
      {
        "value": "Integração Pedido de compra - Narwal x Sankhya",
        "customFieldId": 206842
      },
      {
        "value": "Integração Pedido de compra - Narwal x Sankhya\n",
        "customFieldId": 206843
      },
      {
        "value": "Integração de pedidos migrada para FLUID direto em PRD e desligado o integrador legado, conforme alinhado com @Alessandro Rodrigues, dessa forma foram integrado todos os pedidos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54398,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão geral em todos os campos do Narwal",
        "customFieldId": 206843
      },
      {
        "value": "Reinicialização do servidor de aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54400,
    "customFieldValues": [
      {
        "value": "Por que os valores da nota não batem com os valores da DI? ",
        "customFieldId": 206842
      },
      {
        "value": "Erro na integração por parte do cliente.",
        "customFieldId": 206843
      },
      {
        "value": "Tudo de acordo com o Narwal. Os valores não estavam de acordo pois a nota era de outro processo, no momento da integração acabaram não percebendo este fato.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54407,
    "customFieldValues": [
      {
        "value": "Fechamento financeiro com fornecedor incorrto",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Cliente precisa cadastrar o fornecedor dentro da rotina do cliente - Cliente > Configurações > Financeiro > Fornecedor. Após a criação do fornecedor, o método de importação do fornecedor foi ajustado na Operação Financeira. Passo a Passo anexado ao chamado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54408,
    "customFieldValues": [
      {
        "value": "Numeração duplicada",
        "customFieldId": 206842
      },
      {
        "value": "Enviado notas fiscais no mesmo momento",
        "customFieldId": 206843
      },
      {
        "value": "Ajustado internamente alterando a numeração para NULL.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54420,
    "customFieldValues": [
      {
        "value": "Como inserir moedas diferentes na Invoice?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Na aba valores do processo existe a opção de moedas diferentes para processos de multimoedas, ela precisa estar marcada.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54423,
    "customFieldValues": [
      {
        "value": "Valores divergente na NF ",
        "customFieldId": 206842
      },
      {
        "value": "calcular impostos ",
        "customFieldId": 206843
      },
      {
        "value": "Calcular imposto no processo antes de seguir para emissão da NF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54425,
    "customFieldValues": [
      {
        "value": "Lentidão geral.",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão geral no ambiente.",
        "customFieldId": 206843
      },
      {
        "value": "Reinicialização do servidor de aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54426,
    "customFieldValues": [
      {
        "value": "Por que os valores dos tributos está negativo na NF?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "A configuração do ICMS, consta alíquota 0, mesmo que seja diferido é importante inserir a alíquota e marcar a flag \"Diferimento sobre alíquota\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54428,
    "customFieldValues": [
      {
        "value": "Por que existe despesas que são criadas de forma automática no processo mesmo estando desabilitadas no Tipo despesa?",
        "customFieldId": 206842
      },
      {
        "value": "Ao realizar o fechamento financeiro gera uma despesa que, mesmo inativa no tipo despesa e excluída do processo, volta a aparecer após calcular os impostos.",
        "customFieldId": 206843
      },
      {
        "value": "Isso ocorre pois no contrato de comissão há uma despesa inclusa na aba \"Despesas\", puxando no momento de realizar o fechamento. O que pode ser feito é excluir esta despesa do contrato de comissão e salvar, após salvar, clicar no menu de ação e \"Replicar requisitos\", depois excluir a despesa no processo e ficará de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54471,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NFD para o Sênior \"A sequência não contém elementos\"",
        "customFieldId": 206842
      },
      {
        "value": "O erro ocorria pois a forma de pagamento de chave 000, informada no campo Condição Pagamento, dentro da Nota Fiscal de Despesa, estava desativada. Dessa forma, a variável \"forma\" estava vazia, portanto não tinha nenhuma lista de itens para ser acessada, gerando o erro.",
        "customFieldId": 206843
      },
      {
        "value": "Para solução é necessário ativar a forma de pagamento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54489,
    "customFieldValues": [
      {
        "value": "\"E-mail is already tanken\" ao criar um usuário, porém e-mail nunca foi utilizado.",
        "customFieldId": 206842
      },
      {
        "value": "O Narwal busca na tabela AspNetUsers se o e-mail já existe. Em alguns clientes, nesta tabela existe a informação de usuário, porém na tabela Usuário não tem nenhuma informação. Portanto, via tela não vai existir um usuário com este e-mail, porém via banco existe.",
        "customFieldId": 206843
      },
      {
        "value": "Deletar as informações do usuário na tabela AspNetUsers.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54545,
    "customFieldValues": [
      {
        "value": "Ordens de compra não integrando do Sênior para o Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Pedidos de compra criados no Sênior não estão chegando no Narwal",
        "customFieldId": 206843
      },
      {
        "value": "Verificar Web Service e caso esteja fora comunicar o cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54565,
    "customFieldValues": [
      {
        "value": "Anulação de Nota Fiscal",
        "customFieldId": 206842
      },
      {
        "value": "cFOP",
        "customFieldId": 206843
      },
      {
        "value": "Para anular a NF clicar no menu de ação da NF e clicar em Anulação. A opção anulação ficará disponível após expirar o prazo cancelamento do estado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54566,
    "customFieldValues": [
      {
        "value": "Shipstracking duvidas",
        "customFieldId": 206842
      },
      {
        "value": "Shipstracking duvidas",
        "customFieldId": 206843
      },
      {
        "value": "Cliente irá ter um treinamento, isso já esta Mapeado com o Glaucio e o Alexandre farias",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54577,
    "customFieldValues": [
      {
        "value": "Os pedidos do meu ERP não estão sendo integrados com o Narwal ",
        "customFieldId": 206842
      },
      {
        "value": "Os pedidos do meu ERP não estão sendo integrados com o Narwal ",
        "customFieldId": 206843
      },
      {
        "value": "Estávamos enfrentando erro porque estávamos rodando pela Fluid, já que o integrador legado não estava funcionando. Mas agora migramos para a Fluid e, além disso, foram feitas as configurações necessárias. Assim, os pedidos foram integrados normalmente\n ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54607,
    "customFieldValues": [
      {
        "value": "Código de autenticação não chega ao e-mail",
        "customFieldId": 206842
      },
      {
        "value": "O usuário relata que o código de verificação de autenticação não é entregue ao seu e-mail logo quando tenta realizar o login no narwal.",
        "customFieldId": 206843
      },
      {
        "value": "FAQ já criada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54617,
    "customFieldValues": [
      {
        "value": "Arro ao acessar o sistema",
        "customFieldId": 206842
      },
      {
        "value": "Após efetuar o login o erro http 500 e mostrado, erro relacionado com o usuário do banco",
        "customFieldId": 206843
      },
      {
        "value": "Após a criação do usuário novo com as permissões o mesmo conseguiu se conectar no ambiente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54625,
    "customFieldValues": [
      {
        "value": "Integração Pedido de compra - Narwal x Sankhya",
        "customFieldId": 206842
      },
      {
        "value": "Integração Pedido de compra - Narwal x Sankhya\n",
        "customFieldId": 206843
      },
      {
        "value": "Integração de pedidos migrada para FLUID direto em PRD e desligado o integrador legado, conforme alinhado com @Alessandro Rodrigues, dessa forma foram integrado todos os pedidos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54638,
    "customFieldValues": [
      {
        "value": "Erro ao redefinir senha",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54642,
    "customFieldValues": [
      {
        "value": " Nota cancelada no SAP e autorizada no Narwal",
        "customFieldId": 206842
      },
      {
        "value": " Nota cancelada no SAP e autorizada no Narwal\n",
        "customFieldId": 206843
      },
      {
        "value": "Cliente resolveu internamente, pois foi um erro de operação do usuario",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54644,
    "customFieldValues": [
      {
        "value": "Custos não integrando para o Sankhya.",
        "customFieldId": 206842
      },
      {
        "value": "Muitas requisições causadas por pedidos que já tiveram seus saldos consumidos e isso congestionou o integrador, causando muita lentidão na integração",
        "customFieldId": 206843
      },
      {
        "value": "Reiniciar o integrador Sankhya.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54645,
    "customFieldValues": [
      {
        "value": "Porque o botão \"Enviar Narwal\" não aparece no SAP B1?",
        "customFieldId": 206842
      },
      {
        "value": "O botão não aparece quando o código vinculado ao municipio/estado do Fornecedor é diferente de \"EX\".\n\nOBS: Cadastro do Fornecedor dentro do SAP.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário alterar e criar um novo municipio/estado para o Fornecedor com o código \"EX\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54666,
    "customFieldValues": [
      {
        "value": "Processo com PIS /COFINS alíquota zero, como deveria ficar processo para não puxar o valor do imposto.  ",
        "customFieldId": 206842
      },
      {
        "value": "Erro usuário",
        "customFieldId": 206843
      },
      {
        "value": "Produto com tributação de PIS/COFINS alíquota zero, porém dentro da aba produtos no processo estava informando a alíquota do imposto. \n\nDessa forma o sistema entende que o imposto teve a tributação, estava fazendo o calculo automático. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54668,
    "customFieldValues": [
      {
        "value": "Integração Pedido de compra - Narwal x Sankhya",
        "customFieldId": 206842
      },
      {
        "value": "Integração Pedido de compra - Narwal x Sankhya\n",
        "customFieldId": 206843
      },
      {
        "value": "Integração de pedidos migrada para FLUID direto em PRD e desligado o integrador legado, conforme alinhado com @Alessandro Rodrigues, dessa forma foram integrado todos os pedidos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54675,
    "customFieldValues": [
      {
        "value": "Como integrar DUIMP no Narwal, quando a empresa não é o importador. ",
        "customFieldId": 206842
      },
      {
        "value": "Ficamos com uma dúvida em relação a importação da DUIMP diretamente do siscomex, pela informação que temos a DUIMP não gerará XML então o narwal irá puxar as informações diretamente do siscomex. \n\n\n\nComo o sistema puxa essa informação? Ele precisa ter o certificado digital para acessar o radar? Penso nisso pois processos de importação direta, onde não envolve a City como importador, não temos acesso ao Siscomex do cliente.",
        "customFieldId": 206843
      },
      {
        "value": "A DUIMP no Narwal será integrada através da sua numeração, que corresponde ao registro da DUIMP. \n\nDessa forma, nos processos que não envolverem a City, não será necessário o uso do certificado digital. Basta preencher as informações que constam na imagem, pois a integração no Narwal ocorrerá diretamente pelo número.\n\nÉ importante ressaltar que a integração só ocorrerá com DUIMPs devidamente registradas",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54678,
    "customFieldValues": [
      {
        "value": "Erro de SMTP ao realizar o login no Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Após colocar o Login e Senha o mesmo trazia erro de SMTP",
        "customFieldId": 206843
      },
      {
        "value": "Senha expirada, após colocar a senha novamente o mesmo voltou a funcionar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54679,
    "customFieldValues": [
      {
        "value": "Informações complementares não puxaram na nota fiscal. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente informando que as informações adicionais da nota fiscal, não estava sendo preenchida na nota fiscal. ",
        "customFieldId": 206843
      },
      {
        "value": "Para que a informações complementares puxe automático na nota fiscal, dentro da rotina parametrização tem o campo de informações complementares, dessa forma pode deixar preenchido nesse campo, pois cada vez que o cliente gerar a nota com aquela parametrização a informação vai estar puxando automática na nota. \n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54689,
    "customFieldValues": [
      {
        "value": "E-mails / follow-ups não está chegando.",
        "customFieldId": 206842
      },
      {
        "value": "SMTP não está funcionando. Neste caso, está o relay.",
        "customFieldId": 206843
      },
      {
        "value": "Alterado para um SMTP ativo, funcionando.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54700,
    "customFieldValues": [
      {
        "value": "Por que se eu altero o processo a DI não é alterada?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "É necessário reprocessar a DI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54702,
    "customFieldValues": [
      {
        "value": "Lentidão",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão na impressão do rascunho da DI",
        "customFieldId": 206843
      },
      {
        "value": "Infra estava realizando uma limpeza no sistema, após a limpeza o mesmo retornou que o ambiente se estabilizou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54713,
    "customFieldValues": [
      {
        "value": "Por que os títulos do processo não estão aparecendo no contas a pagar?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Nesse caso, estava sendo inserido o numero do processo no campo \"Invoice\", ao invés de selecionar no campo \"processo\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54772,
    "customFieldValues": [
      {
        "value": "Bloqueio aba \"Comex\" no pedido SAP",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54789,
    "customFieldValues": [
      {
        "value": "Erro no envio de NF \"SAP B1 status 400: Estrutura inválida.\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro ocorre pois dentro da forma de pagamento, na invoice, não está informado a data de vencimento.",
        "customFieldId": 206843
      },
      {
        "value": "Informar a data de vencimento da parcela da invoice.\n\nCaminho: Editar processo -> invoice -> editar invoice -> Forma pagamento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53260,
    "customFieldValues": [
      {
        "value": "É possível alterar a informação que é integrada no centro de resultado?",
        "customFieldId": 206842
      },
      {
        "value": "O centro de resultado estava integrando para o Sankhya com uma informação diferente da informação desejada.",
        "customFieldId": 206843
      },
      {
        "value": "Para alterar a informação que é integrada, é necessário acessar a rotina \"Operação financeira\" dentro do Narwal. \n\nApós clicar para editar a operação desejada, ir na aba \"Sankhya\" e alterar a informação no campo \"Centro de custo\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53802,
    "customFieldValues": [
      {
        "value": "NF não integra para o SAP B1.",
        "customFieldId": 206842
      },
      {
        "value": "A NF não estava sendo integrada, pois no processo apenas 1 dos itens possuía vinculo com o pedido de compra.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário ajustar o pedido no SAP, e na nota fiscal editar e informar o pedido e a ordem ao qual o item pertencia.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54636,
    "customFieldValues": [
      {
        "value": "Como resolver o erro de base valorem incorreta na DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Podem ser várias questões, nesse caso foi verificado a unidade estatística da NCM e os pesos líquidos e brutos, como estavam incorretos, foram ajustados no cadastro/processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54562,
    "customFieldValues": [
      {
        "value": "Qual a regra utilizada para preencher o campo 'Local da condição' na adição?",
        "customFieldId": 206842
      },
      {
        "value": "O campo 'Local da condição' está preenchido com a informação 'incorreta'.",
        "customFieldId": 206843
      },
      {
        "value": "A informação será inserida de acordo com o Incoterm utilizado no processo:\nEXW → Informação vem do país do fornecedor.\nFCA, FAS, FOB → Informação vem da origem do processo.\nCFR, CIF, CPT, CIP → Informação vem do destino do processo.\nDES, DEQ, DDU, DDP, DAP, DAT → Informação vem do país do importador.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54357,
    "customFieldValues": [
      {
        "value": "Follows não são enviados e não apresentam erros. (Processo)",
        "customFieldId": 206842
      },
      {
        "value": "Follows não enviam e não acusam erro de SMTP ou configuração quando o cliente selecionado para o processo está com cadastro inativo. (Para follows de Processo)",
        "customFieldId": 206843
      },
      {
        "value": "Ativar o cadastro do cliente do processo ou alterar o cliente para um com cadastro ativo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54510,
    "customFieldValues": [
      {
        "value": "Erro na grid de consultas nos processos de exportação",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relatou problemas ao consultar processos na rotina de Processo (expo).",
        "customFieldId": 206843
      },
      {
        "value": "A solução deste caso foi orientar o cliente a resetar a grid de consulta. Após resetar, a consulta foi realizada e não gerou mais problemas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54613,
    "customFieldValues": [
      {
        "value": "Erro ao converter os dados para a entidade X",
        "customFieldId": 206842
      },
      {
        "value": "Integração via Planilha Excel. Algum campo está com o formato incorreto. (texto que era pra ser número, número que era pra ser data, etc...)",
        "customFieldId": 206843
      },
      {
        "value": "Avaliar cada campo da planilha e as configurações no Modelo de inserção.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54363,
    "customFieldValues": [
      {
        "value": "Valor dos impostos retidos não estão sendo destacados na Nota Fiscal de Serviço.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente PF",
        "customFieldId": 206843
      },
      {
        "value": "Quanto o tomador do serviço é P.F via de regra não tem retenção nos impostos. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54353,
    "customFieldValues": [
      {
        "value": "Por que meu título de previsão está com uma taxa moeda fixa?",
        "customFieldId": 206842
      },
      {
        "value": "Na rotina de contas a pagar, um título de previsão está vindo com uma taxa fixa, sem ser informada em nenhum lugar.",
        "customFieldId": 206843
      },
      {
        "value": "Dentro da rotina de cadastro de moeda, acessar o botão 'Previsão', e verificar se existe uma taxa informada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54560,
    "customFieldValues": [
      {
        "value": "Cadastros com pais do exterior com divergência na cidade",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relata que, ao realizar qualquer cadastro para países estrangeiros, o campo \"cidade\" está sendo preenchido automaticamente com \"Augsburgo\", cidade da Alemanha, independentemente do país selecionado.\n\nExemplo: em um cadastro de fornecedor com o país Argentina, o sistema atribui corretamente o estado como Exterior, porém a cidade \"Augsburgo\" é inserida automaticamente.",
        "customFieldId": 206843
      },
      {
        "value": "Isso ocorreu porque havia um cadastro para o estado \"Exterior\" com a cidade nomeada como \"Augsburgo\", fazendo com que essa cidade fosse atribuída automaticamente em qualquer país selecionado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54108,
    "customFieldValues": [
      {
        "value": "Por que os valores da nota fiscal não estão de acordo com a DI retificada?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Os valores do processo não estavam de acordo com a DI retificada, após ajustar ficou de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54518,
    "customFieldValues": [
      {
        "value": "Como insiro o certificado digital para NF de serviço.",
        "customFieldId": 206842
      },
      {
        "value": "Gateway",
        "customFieldId": 206843
      },
      {
        "value": "O cerificado digital deverá ser inserido na Filial e também no portal do E-notas.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54564,
    "customFieldValues": [
      {
        "value": "Onde cadastro nova natureza de operação para a Nota Fiscal? ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "A natureza de operação na Nota Fiscal é correspondente a Parametrização de NF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54427,
    "customFieldValues": [
      {
        "value": "Por que há duas despesas de ICMS geradas no processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Uma despesa foi criada pelo Narwal e a outra inserida de forma manual.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53178,
    "customFieldValues": [
      {
        "value": "Lentidão no sistema",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que, ao editar um processo e clicar em \"Salvar\", o Narwal apresentava uma demora de 2 a 3 minutos para efetuar a gravação das informações alteradas.",
        "customFieldId": 206843
      },
      {
        "value": "Após a atualização para a versão 2024.R6.5.0, a lentidão foi significativamente reduzida. Necessário reiniciar o servidor de aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54472,
    "customFieldValues": [
      {
        "value": "Por que o cliente não consegue emitir nota no Narwal?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Existe uma série de informações que deve ser configuradas, esse procedimento é realizado na implantação. Nesse caso, foi criada uma nova filial pelo cliente e não foi configurada, repassei para os responsáveis.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54399,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão em todas as rotinas.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário reiniciar o servidor de aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54401,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão em toda as rotinas.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário reiniciar o servidor de aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54554,
    "customFieldValues": [
      {
        "value": "Erro de permissão ao integrar a DI",
        "customFieldId": 206842
      },
      {
        "value": "O usuário relatou problemas na integração automática da DI.",
        "customFieldId": 206843
      },
      {
        "value": "O alerta exibido na tela estava relacionado à falta de permissão para o usuário. Após ligar para o cliente e  orienta-los para atribuir as permissões necessárias, o usuário conseguiu prosseguir com as operações de integração.\n\nA permissão mencionada deve ser atribuída ao grupo de usuários, conforme o grupo vinculado ao usuário do cliente.\n\nParâmetro: Integrar DI/DUIMP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54392,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão em todos os campos do Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário reiniciar o servidor da aplicação. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54504,
    "customFieldValues": [
      {
        "value": "Erro ao consultar pedido de compra ao realizar vinculo com uma Invoice",
        "customFieldId": 206842
      },
      {
        "value": "Cliente tentou realizar um vínculo de uma Invoice com um pedido de compra mas ao realizar a consulta constou um erro.",
        "customFieldId": 206843
      },
      {
        "value": "A variável MV_PRODDERAUTO está com valor que, aparentemente, não tem no Narwal, como ChaveDescricao. Ao mudar para Descricao a mensagem de erro parou de acontecer.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54109,
    "customFieldValues": [
      {
        "value": "Cadastro de usuário com e-mail já existente",
        "customFieldId": 206842
      },
      {
        "value": "Ocorre um erro ao criar um usuário com um e-mail previamente cadastrado em outro usuário.",
        "customFieldId": 206843
      },
      {
        "value": "Atuamente, não é possível criar dois ou mais usuários com o mesmo e-mail. Por este motivo, não aconselhamos utilizar e-mails genéricos na criação de usuários no Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54342,
    "customFieldValues": [
      {
        "value": "Filtro de gráfico do painel inicial",
        "customFieldId": 206842
      },
      {
        "value": "O usuário gostaria de saber se, no gráfico \"PROCESSOS POR ANO/MÊS/DIA DA SEMANA\", é possível aplicar simultaneamente os filtros para o mês de janeiro de 2024 e janeiro de 2025, sem considerar os meses intermediários.",
        "customFieldId": 206843
      },
      {
        "value": "Informamos ao usuário que não é possível aplicar o filtro sem considerar as datas dentro do intervalo entre janeiro de 2024 e janeiro de 2025. Foi oferecida a possibilidade de avaliação para criação de um filtro personalizado, porém o usuário optou por não seguir com a solicitação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54556,
    "customFieldValues": [
      {
        "value": "Na Nota Fiscal ao clicar em \"Novo(Importação)\" está ocorrendo a mensagem Saldo Insuficiente",
        "customFieldId": 206842
      },
      {
        "value": "Nota Fiscal já criada",
        "customFieldId": 206843
      },
      {
        "value": "Verificar na rotina Nota Fiscal se já existe Nota Fiscal para o processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54189,
    "customFieldValues": [
      {
        "value": "Erro na API ao tentar integrar pedido de compra \"Erro(s) de validação : O campo Nome é obrigatório.\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro ocorreu por conta que a chave do fornecedor foi informada de maneira vazia (\" \"), assim não sendo possível realizar o vinculo a um fornecedor.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário informar o Fornecedor para o item, dentro do pedido no ERP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53653,
    "customFieldValues": [
      {
        "value": "Regra de ordem dos itens no processo",
        "customFieldId": 206842
      },
      {
        "value": "O usuário tinha dúvidas sobre a regra que define a ordem dos itens vinculados ao processo.",
        "customFieldId": 206843
      },
      {
        "value": " ordem dos itens no processo pode ser alterada conforme as adições da DI vinculada. Qualquer modificação nas adições da DI impactará diretamente a sequência dos produtos no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54251,
    "customFieldValues": [
      {
        "value": "Erro ao enviar as despesas para SAP B1 \"540000062 - G/L account 4.01.01.05.98 needs DR assignment for dimension 1;  fill in DR-related fields.\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro ocorreu pois a NFD foi criada sem que a NF fosse enviada para o SAP.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário cancelar a NFD e realizar o envio da Nota Fiscal para o SAP. Após ter enviado a NF, criar a nota fiscal despesa novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54289,
    "customFieldValues": [
      {
        "value": "Como inserir automaticamente o campo \"Pagamento\" da NF?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Informar na parametrização a forma de pagamento, irá puxar de forma automática ao inserir a parametrização na NF.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54491,
    "customFieldValues": [
      {
        "value": "Usuário editando processo",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que alguns processos estavam bloqueados porque um usuário permanecia vinculado ao processo.",
        "customFieldId": 206843
      },
      {
        "value": "A solução foi ativar a variável NWL_HABILITABLOQUEIOUSUARIO, que controla a edição unificada de cada processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54515,
    "customFieldValues": [
      {
        "value": "Cliente não recebe e-mail de redefinição de senha",
        "customFieldId": 206842
      },
      {
        "value": "Falha de configuração do email do cliente",
        "customFieldId": 206843
      },
      {
        "value": "Acionamento TI do cliente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54480,
    "customFieldValues": [
      {
        "value": "Nota fiscal não estava trazendo a informação da unidade tributável ",
        "customFieldId": 206842
      },
      {
        "value": "Ao gerar a nota fiscal não estava puxando a unidade tributável no produto. ",
        "customFieldId": 206843
      },
      {
        "value": "Para o ajuste identificamos via auditoria que no cadastro do NCM a unidade de medida utilizada, estava como desativada no Narwal. \n\nAjustamos o NCM informando uma unidade de medida que estava ativa, a qual era a correta, após ajustes a nota saiu de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54499,
    "customFieldValues": [
      {
        "value": "Divergência no ICMS e BC icms ",
        "customFieldId": 206842
      },
      {
        "value": "Ao gerar a nota fiscal o valor do ICMS e a BC estava saindo com divergência, o processo estava trazendo um valor e a nota outro valor. ",
        "customFieldId": 206843
      },
      {
        "value": "Dentro da Parametrização o cliente no campo do ICMS informou a formula e o valor puxou de acordo. \n\n{ValorTotal}+{ValorFrete}+{ValorSeguro}+{Ii}+{Ipi}+{Pis}+{Cofins}+{DespesaBaseIcms}\n\nAjustou também a alíquota do ICMS. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54483,
    "customFieldValues": [
      {
        "value": "Erro emissão de NF - Numero Adição para courier",
        "customFieldId": 206842
      },
      {
        "value": "Erro emissão de NF - Numero Adição para courier\n",
        "customFieldId": 206843
      },
      {
        "value": "a nota fiscal já foi encaminhada, o que impossibilita, no sistema Narwal, a inclusão de adições no item da NF.\nPara realizar a alteração, será necessário proceder com o cancelamento do envio atual, incluir a adição no item (mesmo tratando-se de um envio via courier), e, em seguida, reenviar a nota fiscal corrigida para o Snakhya.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53795,
    "customFieldValues": [
      {
        "value": "O título do contrato de câmbio está sendo integrado com um valor de variação cambial",
        "customFieldId": 206842
      },
      {
        "value": "O título do contrato de câmbio está sendo integrado com um valor de variação cambial\n",
        "customFieldId": 206843
      },
      {
        "value": "Ao gerar o título no Sankhya, ele foi registrado corretamente com a mesma taxa de câmbio e baixado com sucesso, conforme o esperado.\n\nCabe ressaltar que a integração realiza a criação do título conforme a guia \"Lançamento\" do Sankhya, sem preencher informações na seção \"Outras Informações\". Dessa forma, não há nenhuma alteração ou envio adicional que possa gerar impactos nesse processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54418,
    "customFieldValues": [
      {
        "value": "lentidão ",
        "customFieldId": 206842
      },
      {
        "value": "lentidão",
        "customFieldId": 206843
      },
      {
        "value": "Reportado ao time infra",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54191,
    "customFieldValues": [
      {
        "value": "lentidão",
        "customFieldId": 206842
      },
      {
        "value": "lentidão",
        "customFieldId": 206843
      },
      {
        "value": "Equipe Infra analisando",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54486,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o narwal",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada em outros chamados.",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54473,
    "customFieldValues": [
      {
        "value": "Erro ao tentar enviar token de acesso ao ambiente",
        "customFieldId": 206842
      },
      {
        "value": "Necessário um cadastro válido de SMTP para envio dos tokens de acesso.",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso, foi removido a autenticação de dois fatores pois a Ventisol não utiliza sistema de e-mail dentro do Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54117,
    "customFieldValues": [
      {
        "value": "Erro ao enviar despesas para o SAP B1 \"Value too long in property 'LandedCostCode' of 'LandedCost_CostLine' \"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro ocorre quando uma despesa não está cadastrada no SAP, ou a chave da despesa está incorreta no Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Cadastrar a despesa no SAP, e informar a chave na rotina \"tipo despesa\" conforme cadastro no SAP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54304,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF para o SAP \"Chave da API inválida ou incorreta\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro é retornado quando não está sendo possível a comunicação com o endereço de envio, o endereço pode ser encontrado no web service.\n\nEssa falha de comunicação pode ser tanto do lado do cliente, como bloqueio de acesso do nosso lado.",
        "customFieldId": 206843
      },
      {
        "value": "Aberto chamado com a infra para liberação do endereço no firewall, após a liberação as integrações voltaram a ocorrer.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52868,
    "customFieldValues": [
      {
        "value": "Usuário editando processo",
        "customFieldId": 206842
      },
      {
        "value": "O usuário informou que estava com dificuldades para acessar alguns processos, pois eles apareciam como em edição por outros usuários, mesmo sem haver edição em andamento.",
        "customFieldId": 206843
      },
      {
        "value": "Orientamos o cliente a sempre utilizar a opção \"Salvar e sair\" ao deixar o processo, em vez de apenas fechar a aba do sistema ou da rotina, o que poderia manter o usuário preso na edição. Após essa orientação, o problema não voltou a ocorrer.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53442,
    "customFieldValues": [
      {
        "value": "Erro \"input string\" ao realizar baixa no contas a pagar/receber.",
        "customFieldId": 206842
      },
      {
        "value": "Usuário está utilizando grid de consulta no contas a pagar personalizada.",
        "customFieldId": 206843
      },
      {
        "value": "Resetar a grid de consulta.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54160,
    "customFieldValues": [
      {
        "value": "Taxa da moeda não atualizada",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada.",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54221,
    "customFieldValues": [
      {
        "value": "Sistema lento",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relata que o ambiente do narwal estava com extrema lentidão e algumas vezes saindo fora do ar.",
        "customFieldId": 206843
      },
      {
        "value": "FAQ já existente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54447,
    "customFieldValues": [
      {
        "value": "Erro de SMTP",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relata que estava com problemas de SMTP, impactando no login dos usuários.",
        "customFieldId": 206843
      },
      {
        "value": "O problema foi resolvido de forma interna pela própria infra do cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53650,
    "customFieldValues": [
      {
        "value": "Sistema solicitando informação já preenchida",
        "customFieldId": 206842
      },
      {
        "value": "O usuário informou que não conseguia realizar o fechamento financeiro, pois o sistema solicitava o preenchimento do campo \"Informe o valor despesa\".",
        "customFieldId": 206843
      },
      {
        "value": "Realizamos um teste com outro usuário e conseguimos salvar o fechamento financeiro com sucesso. Após isso, a mensagem de alerta deixou de ser exibida.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53631,
    "customFieldValues": [
      {
        "value": "Erro ao acessar o ambiente de homologação.",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relata que estava com impeditivos ao tentar acessar o ambiente de homologação",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53393,
    "customFieldValues": [
      {
        "value": "Grid de processo com divergência de informações",
        "customFieldId": 206842
      },
      {
        "value": "O usuário relatou que a grid de processos apresentava divergência nas informações exibidas entre a própria grid e os detalhes do processo.",
        "customFieldId": 206843
      },
      {
        "value": "Foi verificado que o usuário estava editando um processo, mas antes que este usuário tinha clicado em salvar pra de fato, aplicar as alterações realizada, a usuária que abriu o ticket estava vendo as informações antigas na grid. Após salvar e atualizar a grid de consulta, as informações ficaram de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54157,
    "customFieldValues": [
      {
        "value": "Taxa da moeda não atualizou",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já existente.",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53224,
    "customFieldValues": [
      {
        "value": "Relatório não sai informações",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relatou que o cadastro de uma das empresas no ambiente da Volk estava marcado como desativado.",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver este caso, orientamos o usuário a acessar o cadastro da empresa inativada e alterar o status para ativo, conforme a necessidade.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54429,
    "customFieldValues": [
      {
        "value": "Código: BHISS0003 Descrição: Essa prefeitura não suporta emissão de Nota Fiscal com tomador com end",
        "customFieldId": 206842
      },
      {
        "value": "Endereço cliente",
        "customFieldId": 206843
      },
      {
        "value": "Cadastro do Cliente está com o endereço diferente do cadastro no portal da pefeitura.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54068,
    "customFieldValues": [
      {
        "value": "Importar produtos via planilha",
        "customFieldId": 206842
      },
      {
        "value": "Erro de referencia de objeto no produto da planilha",
        "customFieldId": 206843
      },
      {
        "value": "Necessário informar a coluna E e O da planilha como obrigatória para a importação da planilha.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54359,
    "customFieldValues": [
      {
        "value": "Erro no acesso da API",
        "customFieldId": 206842
      },
      {
        "value": "Erro no acesso da API  - Erro 500",
        "customFieldId": 206843
      },
      {
        "value": "Foi validado que a pasta api.xml nao constava no servidor após adicionar o mesmo voltou a funcionar normalmente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53783,
    "customFieldValues": [
      {
        "value": "Cotação de frete internacional",
        "customFieldId": 206842
      },
      {
        "value": "Cliente com duvidas na rotina.",
        "customFieldId": 206843
      },
      {
        "value": "Foi repassada as informações e anexado documento para o cliente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54403,
    "customFieldValues": [
      {
        "value": "Nota fiscal de serviço para cliente do SN, com destaque de impostos federais.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente informa que a nota fiscal para o cliente do Simples nacional estava sendo destacado os impostos federais, porém deveria ser destacado apenas o IR. ",
        "customFieldId": 206843
      },
      {
        "value": "Dentro da rotina de cadastro do cliente estava com os impostos no financeiro flegados, esses impostos federais flegados eles estavam sendo levados para a nota fiscal.\n\nCliente fez o ajuste tirando as flags, e a nota saiu de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53872,
    "customFieldValues": [
      {
        "value": "Anexo e download de arquivos",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não estava conseguindo realizar o download de arquivos, apenas fazer o anexo deles.",
        "customFieldId": 206843
      },
      {
        "value": "Identificado que os usuários relatados estavam com o cache muito alto e foi necessário apagar, após isso download realizado com sucesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54385,
    "customFieldValues": [
      {
        "value": "Numeração NF",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "A numeração do sequencial da NF seguiu corretamente conforme definição da série.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53295,
    "customFieldValues": [
      {
        "value": "Erro ao acessar o ambiente do narwal",
        "customFieldId": 206842
      },
      {
        "value": "O usuário relatou que, ao acessar o Narwal e inserir os dados de login, recebia o erro \"HTTP ERROR 500\".",
        "customFieldId": 206843
      },
      {
        "value": "Para solucionar o problema, é necessário acessar a rotina de usuários e enviar o e-mail de redefinição de senha diretamente por essa funcionalidade. Após o usuário alterar a senha através do e-mail enviado, o acesso será restabelecido.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54367,
    "customFieldValues": [
      {
        "value": "Documentos no portal do cliente",
        "customFieldId": 206842
      },
      {
        "value": "Duvida de começar mostrar os arquivos para os clientes",
        "customFieldId": 206843
      },
      {
        "value": "Rotina de gestão de documentos e flegar os documentos que precisa ser visível para o cliente ou ao anexar os documentos no processo ativar a ultima flag mencionada no chamado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53869,
    "customFieldValues": [
      {
        "value": "Majoração COFINS",
        "customFieldId": 206842
      },
      {
        "value": "Direito a crédito Cofins",
        "customFieldId": 206843
      },
      {
        "value": "cadastro de NCM campo \"[ ] Não majora Cofins\".\n\nQuando a alíquota é superior a 10,65%, automaticamente 1% é considerado como custo do produto.\n\nCaso seu NCM não considere essa operação, você pode acessar o cadastro da NCM do respectivo item e marcar a flag \"Não Majora COFINS\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53885,
    "customFieldValues": [
      {
        "value": "Karsten - Recebimento 100% antecipado",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Precisou ser ativado a Variável mencionada ao chamado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54350,
    "customFieldValues": [
      {
        "value": "Por que o valor dos impostos estão incorretos?",
        "customFieldId": 206842
      },
      {
        "value": "Pode acontecer por diversos fatores, como:\nVMLD incorreto\nDespesa base de imposto faltando ou incorreta\nAlíquota incorreta",
        "customFieldId": 206843
      },
      {
        "value": "Realizar a revisão dos impostos acima.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54072,
    "customFieldValues": [
      {
        "value": "Serdia - Portal do narwal fora do ar",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que o portal de login no ambiente de produção estava indisponível.",
        "customFieldId": 206843
      },
      {
        "value": "A indisponibilidade foi causada por uma instabilidade no servidor onde a aplicação do cliente está hospedada. Após a reinicialização da pool de aplicação, o sistema voltou a operar normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54256,
    "customFieldValues": [
      {
        "value": "Diferença de ICMS nas adições da DI. ",
        "customFieldId": 206842
      },
      {
        "value": "Ao registrar a DI as informações adicionais da DI não estava trazendo o valor da AFRMM para o calculo da BC ICMS, sendo assim o valor estava divergente do processo. ",
        "customFieldId": 206843
      },
      {
        "value": "Ao fazer uma analise, identificamos que quando informado a despesa no processo, eles não estavam calculando os impostos, sendo assim o valor ia divergente do processo. \n\nFoi replicado o cenário em HML, no teste feito as adições puxou o mesmo valor de ICMS e BC das informações complementares. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53672,
    "customFieldValues": [
      {
        "value": "Como realizar pagamento de cambio antecipado?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Para realizar o adiantamento de câmbio, siga os seguintes passos:\nCom o pedido de compra criado, crie um contrato de câmbio e insira o valor referente ao adiantamento, lembrando de informar \"Sim\" no adiantamento.\nCom a invoice criada (refletindo uma proforma), faremos o fechamento deste adiantamento, onde será vinculada esta invoice e o contrato de câmbio.\nLembre-se de que um contrato de câmbio pode ter vários pedidos de compra vinculados, um pedido de compra pode gerar várias invoices e um processo pode ter várias invoices também. Tudo depende do saldo disponível. Se houver saldo, é possível dividir em quantas invoices forem necessárias.\nEm casos onde o valor da invoice final é menor do que o total do pedido de compra, pode-se criar a invoice e o processo com o valor menor e deixar o saldo no pedido, sem problemas (a não ser que seja utilizado algum relatório para controle de saldo, nesse caso, pode causar algumas divergências).\n\n\n\nEm casos onde o valor da invoice final é maior do que o do pedido de compra, é necessário gerar outro pedido de compra. Pode-se criar uma invoice a partir deste pedido e vinculá-la ao processo normalmente. Ou seja, podemos ter mais de um pedido de compra no processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53757,
    "customFieldValues": [
      {
        "value": "Desconto não aplicado corretamente na invoice.",
        "customFieldId": 206842
      },
      {
        "value": "Aplicado o desconto na invoice porém os valores não ficaram de acordo.",
        "customFieldId": 206843
      },
      {
        "value": "1. No Processo, guia Invoice manter o valor do desconto no campo \"Valor desconto\";\n2. Acessar a rotina Declaração Importação. Caso já tenha declaração gerada, cancelar;\n\n2.1 Na sequencia, na declaração importação clicar em Processar;\n2.2 Ainda na Declaração importação, clicar no menu de ação e clicar em \"Atualizar taxas\" e na sequencia apenas clique em Salvar (clicar em salvar para não atualizar a taxa, caso precise atualizar a taxa atual, deverá clicar em Atualizar);\n\n2.3 Editar a Declaração Importação, clicar em Acréscimo/Dedução;\n2.3.1 Clicar na guia Dedução e clicar em \"Nova Dedução\" e preencher os campos abaixo e clicar em Salvar;\n2.4. Clicar em Recalcular DI e clicar em Salvar(clicar em salvar para não atualizar a taxa, caso precise atualizar a taxa atual, deverá clicar em Atualizar);\n3.  Ainda da Declaração Importação clicar em Voltar e clicar em Salvar.\n4. Na rotina Processo clicar para editar. Acessar a guia Valores e no final da guia no grupo Valores verificar que o valor do VMLE/VMLD está considerando os descontos e na guia Despesas verificar que os valores dos impostos estão considerando o desconto. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52721,
    "customFieldValues": [
      {
        "value": "Visualização NCM na cotação de frete",
        "customFieldId": 206842
      },
      {
        "value": "Cliente relatou que aparece a descrição da NCM ao invés do número.",
        "customFieldId": 206843
      },
      {
        "value": "A visualização da NCM e Incoterm só aparece por extenso ao gerar a cotação, assim que salvar, já consta a sigla e os números da NCM.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54002,
    "customFieldValues": [
      {
        "value": "Por que as despesas do numerário estão duplicadas?",
        "customFieldId": 206842
      },
      {
        "value": "Quando clicar em \"processar impostos\" ou processar\" 2x no pré calculo, as despesa irão duplicar.",
        "customFieldId": 206843
      },
      {
        "value": "Caso seja necessário processar novamente o numerário, é preciso excluir as despesas do numerário antes.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53531,
    "customFieldValues": [
      {
        "value": "Como inserir a despesa de Armazenagem no numerário?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Processo> numerário> pré cálculo> calcular armazenagem",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53388,
    "customFieldValues": [
      {
        "value": "Quando uma despesa compõe o VMLD? ",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Compõe o valor do VMLD quando, na rotina \"Tipo despesa\", está marcada como \"base de imposto\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53551,
    "customFieldValues": [
      {
        "value": "Como cadastrar fórmulas no Narwal?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina \"Fórmula\" você pode realizar o cadastro/edição das fórmulas; Especificando o tipo; E para a composição, insira uma chave { e formule como gostaria que fosse calculado.\n\n\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54262,
    "customFieldValues": [
      {
        "value": "Como criar um usuário?",
        "customFieldId": 206842
      },
      {
        "value": "Cliente deseja cadastrar um novo usuário.",
        "customFieldId": 206843
      },
      {
        "value": "Rotina de cadastro 'Usuário' -> Novo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54062,
    "customFieldValues": [
      {
        "value": "Como inserir uma nova quebra de adição?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "A variável NWL_CMPDINAMICAGRUPADI  precisava ser habilitada.\nPode realizar a configuração da quebra das adição da seguinte forma:\n\nInserindo uma chave { e a TAG do beneficio fiscal. Dessa forma deve realizar a separação das adições. (Se faz necessário cancelar a DI e gerar novamente)\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54349,
    "customFieldValues": [
      {
        "value": "Envio NF para SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "Solucionado em versão posterior ",
        "customFieldId": 206843
      },
      {
        "value": "Ao enviar NF para SEFAZ está ocorrendo a mensagem em tela relacionada a 'gCred'.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54058,
    "customFieldValues": [
      {
        "value": "Taxa de Fechamento de Cambio",
        "customFieldId": 206842
      },
      {
        "value": "Taxa vindo zerada.",
        "customFieldId": 206843
      },
      {
        "value": "Resolução: Os titulos já estão sendo atualizados conforme o esperado, pela taxa fechamento.\n\nA correção ocorreu devido a ativação da variável de ambiente \"NWL_ATIVATAXAFECHAMENTOBAIXAMANUAL\" ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54096,
    "customFieldValues": [
      {
        "value": "Teste",
        "customFieldId": 206842
      },
      {
        "value": "-",
        "customFieldId": 206843
      },
      {
        "value": "-",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54300,
    "customFieldValues": [
      {
        "value": "Como anexar os documentos no processo via e-mail?",
        "customFieldId": 206842
      },
      {
        "value": "Cliente deseja realizar a inserção de documentos via e-mail.",
        "customFieldId": 206843
      },
      {
        "value": " Basta habilitar o campo 'Habilitar anexar e-mails' na rotina de cadastro de 'Empresa' -> aba 'Parâmetros', Logo após, irá ser habilitada a opção de copiar o endereço de e-mail do processo:\nProcesso -> Menu ação -> Copiar endereço de e-mail, ou, Processo -> Editar -> Copiar\nLogo após copiar o endereço de e-mail, basta informá-lo nos e-mails em cópia juntamente com os arquivos.\nO JOB responsável por anexar os documentos e e-mails no processo roda a cada 15 minutos.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54112,
    "customFieldValues": [
      {
        "value": "Estou com erro de atributo de acondicionamento ao enviar a DI para Registro",
        "customFieldId": 206842
      },
      {
        "value": "É necessário analisar se o atributo solicitado é do Catálogo (Produto) ou do NCM (DUIMP). O local de preenchimento são diferentes",
        "customFieldId": 206843
      },
      {
        "value": "Caso, ao enviar a DUIMP para registro, retorne mensagem impeditiva informando \"atributo adicional \"Acondicionamento\" do cadastro de atributos não informado no item, é necessário conferir, na DUIMP do erro, na aba de Produto, em Informações Complementares, se é necessario informar, por exemplo, o Acondicionamento",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54215,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Problemas Infra Narwal, necessário reiniciar o servidor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54233,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Problemas na Infra Narwal, necessário reiniciar o servidor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54263,
    "customFieldValues": [
      {
        "value": "Erro envio NF para o Sefaz",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Necessário reiniciar o Pool da aplicação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54316,
    "customFieldValues": [
      {
        "value": "Erro de objeto em base Produção recém criada",
        "customFieldId": 206842
      },
      {
        "value": "Causa foi o ID do usuário de administrador ter sido recadastrado na base de produção após ter sido excluído durante a fase de limpeza de base",
        "customFieldId": 206843
      },
      {
        "value": "Não se deve excluir, sob circunstância nenhuma, o usuário administrador do sistema.\nSe no cutover (limpeza de base) desejam excluir algum usuário, inativar o cadastro e colocar no checklist para excluir apenas os inativos, porém, o usuário administrador nunca deve ser inativado ou excluído.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54302,
    "customFieldValues": [
      {
        "value": "Duplicidade de processo.",
        "customFieldId": 206842
      },
      {
        "value": "Erro \"Informe o numero do processo\", cliente precisa preencher o numero manual.",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina sequencial o cliente pode informar a Filial e será anexar os prefixos de forma automatica.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54335,
    "customFieldValues": [
      {
        "value": "Campo obrigatório sem necessidade",
        "customFieldId": 206842
      },
      {
        "value": "Campo foi marcado como obrigatório por um usuário com a flag \"Permitir obrigar campos\" ativa no cadastro.",
        "customFieldId": 206843
      },
      {
        "value": "Desmarcar o campo como obrigatório.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54322,
    "customFieldValues": [
      {
        "value": "Sem acesso a uma rotina no Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Cadastro \"Grupo usuário\" não tem acesso à rotina desejada.",
        "customFieldId": 206843
      },
      {
        "value": "Liberar rotina no cadastro \"Grupo usuário\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53289,
    "customFieldValues": [
      {
        "value": "HTTP ERROR 500 ao tentar acessar o narwal",
        "customFieldId": 206842
      },
      {
        "value": "O usuário informou que, ao tentar realizar o login no Narwal, a mensagem \"HTTP ERROR 500\" era exibida.",
        "customFieldId": 206843
      },
      {
        "value": "Para contornar temporariamente esse problema, solicite a redefinição de senha diretamente pela rotina de usuário no Narwal. Após o usuário realizar o reset através do e-mail enviado, o acesso será restabelecido.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53245,
    "customFieldValues": [
      {
        "value": "Dúvida sobre ordem dos campos no processo de expo",
        "customFieldId": 206842
      },
      {
        "value": "O cliente estava com dúvidas relacionadas a ordem dos campos na rotina de processo (expo).",
        "customFieldId": 206843
      },
      {
        "value": "Foi feita a call com o cliente para melhor esclarecimento e foi visto que a ordem dos campos estava diferente dos demais usuários por conta da resolução do monitor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53941,
    "customFieldValues": [
      {
        "value": "Não é possível alterar a quantidade ao integrar XML da DI com item vinculado a invoice.",
        "customFieldId": 206842
      },
      {
        "value": "Ao integrar um XML da DI que esteja com quantidade de um ou mais itens diferentes e estes itens estejam vinculados a uma invoice, o sistema apresentará um alerta impeditivo.",
        "customFieldId": 206843
      },
      {
        "value": "Validar qual item (tabela itemprocesso) tem a mesma chave do alerta e verificar a quantidade.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54201,
    "customFieldValues": [
      {
        "value": "Como inserir uma despesa negativa no processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Pode inserir a despesa e salvar, depois inserir - (menos) na frente e salvar novamente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54212,
    "customFieldValues": [
      {
        "value": "Lentidão Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão geral!",
        "customFieldId": 206843
      },
      {
        "value": "Identificado que o servidor em que os clientes estavam hospedado estava passando por um cap de recurso, foi realizado a reinicialização da maquina.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54095,
    "customFieldValues": [
      {
        "value": "URL incorreta",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao tentar acessar o portal do cliente",
        "customFieldId": 206843
      },
      {
        "value": "o mesmo estava utilizando a URL errada para acesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54239,
    "customFieldValues": [
      {
        "value": "Pedido de login send solicitado repetidamente",
        "customFieldId": 206842
      },
      {
        "value": "O usuário informou que, ao acessar o Narwal, alguns minutos após realizar o login, o sistema solicita um novo login devido à perda de conexão.",
        "customFieldId": 206843
      },
      {
        "value": "A solução deste caso foi alcançada após a estabilização do ambiente da Nelson em termos de desempenho. Verificamos que o problema relatado estava sendo causado por lentidões e falta de otimização, o que também impactou a conexão de login do usuário.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53880,
    "customFieldValues": [
      {
        "value": "Não estou recebendo o token de acesso.",
        "customFieldId": 206842
      },
      {
        "value": "Usuário sem acesso ao e-mail da conta.",
        "customFieldId": 206843
      },
      {
        "value": "Verificar se o SMTP está funcionando corretamente e conseguir acessar a conta.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53923,
    "customFieldValues": [
      {
        "value": "Informe a sigla da Unidade de medida no item do Processo",
        "customFieldId": 206842
      },
      {
        "value": "Produto sem UN de medida",
        "customFieldId": 206843
      },
      {
        "value": "Acessar o Processo, guia Produto verificar se a UN de medida está informado. \nNo cadastro do Produto e/ou NCM é necessário informar a Unidade de Medida. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54295,
    "customFieldValues": [
      {
        "value": "Erro ao integrar pedido de venda ",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao integrar pedido de venda ",
        "customFieldId": 206843
      },
      {
        "value": "Cadastrado importador dessa forma foi corrigido o problema e colocado a inscrição Estadual que estava como nulo",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54297,
    "customFieldValues": [
      {
        "value": "Autorizar usuario criar resgistro de DU-e",
        "customFieldId": 206842
      },
      {
        "value": "Autorizar usuario criar resgistro de DU-e",
        "customFieldId": 206843
      },
      {
        "value": "usuario > editar > colocar as permissões segundo o grupo de usuário",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54004,
    "customFieldValues": [
      {
        "value": "Ambiente está dando erro 403",
        "customFieldId": 206842
      },
      {
        "value": "Angeloni possui um bloqueio, apenas a rede Narwal e a rede interna deles pode acessar o ambiente. Alguns usuários acessam via VPN, que precisa ser configurada corretamente por eles.",
        "customFieldId": 206843
      },
      {
        "value": "Configurar a VPN corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53626,
    "customFieldValues": [
      {
        "value": "Todos os campos do processo não estão editáveis",
        "customFieldId": 206842
      },
      {
        "value": "Outro usuário está editando o processo.",
        "customFieldId": 206843
      },
      {
        "value": "Apenas um usuário pode editar o processo por vez.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53541,
    "customFieldValues": [
      {
        "value": "ECarta de cambio envou porém não chega.",
        "customFieldId": 206842
      },
      {
        "value": "SMTP não está funcionando.",
        "customFieldId": 206843
      },
      {
        "value": "Testar SMTP pelo validador no cadastro da empresa.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53506,
    "customFieldValues": [
      {
        "value": "Campo obrigatório sem necessidade",
        "customFieldId": 206842
      },
      {
        "value": "Algum campo que o operacional não utiliza está marcado como obrigatório.",
        "customFieldId": 206843
      },
      {
        "value": "Remover permissão \"Permitir obrigar campos\" dos usuários, para evitar obrigatoriedade dos campo sem necessidade.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54158,
    "customFieldValues": [
      {
        "value": "Atualização da taxa do dólar",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada para este caso.",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53892,
    "customFieldValues": [
      {
        "value": "Alguns campos estão sumindo e outro estão como obrigatório",
        "customFieldId": 206842
      },
      {
        "value": "Flag no cadastro do usuário \"Permitir obrigar campos\"",
        "customFieldId": 206843
      },
      {
        "value": "Desmarcar flag \"Permitir obrigar campos\" dos usuários para que não ocultem ou obriguem os campo por engano.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53607,
    "customFieldValues": [
      {
        "value": "Semáforo \"numerário\" - regra para cor verde",
        "customFieldId": 206842
      },
      {
        "value": "O cliente abriu este ticket para que se possa entender a regra para quando o semáforo de numerário fica na cor verde.",
        "customFieldId": 206843
      },
      {
        "value": "O status \"Numerário nacionalização\" será verde se atender a qualquer uma das seguintes condições:\n\n- O campo \"Antecipa numerário\" estiver como \"Despachante cliente\" e \"Pagamento impostos NF saída\" estiver desmarcado.\n\n- \"Pagamento impostos NF saída\" estiver desmarcado e o despachante não for \"Despachante próprio\".\nO campo \"Numerário\" for igual a \"Sem antecipação\".\n\n- Os campos \"Data envio\" e \"Data depósito numerário\" estiverem preenchidos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53728,
    "customFieldValues": [
      {
        "value": "MENSAGEM DO SANKHYA: Campo não existe: Financeiro-> CustomFields",
        "customFieldId": 206842
      },
      {
        "value": "Variável de ambiebte",
        "customFieldId": 206843
      },
      {
        "value": "O erro ocorria pois no corpo da requisição estava sendo enviado um campo customizado que não existe na base da Texbrox HML: <CustomFields> <AD_VLRMOEDAIMP>517.13</AD_VLRMOEDAIMP> </CustomFields> \n\nO que define se esse campo será enviado ou não é a variável NWL_ENVIACAMPOSESPECIFICOSNFEQUALIMPOR. \nApós desativa-la, o título voltou a integrar:",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54282,
    "customFieldValues": [
      {
        "value": "Retorno de mensagem do SEFAZ ao enviar NF",
        "customFieldId": 206842
      },
      {
        "value": "FAQ já criada para este caso.",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53356,
    "customFieldValues": [
      {
        "value": "PROBLEMA EMISSÃO BORDERÔ",
        "customFieldId": 206842
      },
      {
        "value": "PROBLEMA EMISSÃO BORDERÔ",
        "customFieldId": 206843
      },
      {
        "value": "Verifiquei que as informações do relatório destacadas abaixo vem da rotina de Contas a Receber\n e quando e filtramos na rotina de contas a receber pelo processo que você informou, o Narwal não encontra nenhum resultado.\ndessa forma ela deve informar o valor no contas a receber e nao no processo",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53568,
    "customFieldValues": [
      {
        "value": "Integração com a Open retornando valores errados ou vazios dos impostos e despesas",
        "customFieldId": 206842
      },
      {
        "value": "Integração com a Open retornando valores errados ou vazios dos impostos e despesas",
        "customFieldId": 206843
      },
      {
        "value": "Esse problema é resolvido diretamente com o time da Open, foi passado o contato pois o mesmo resolve internamente sem passar a resolução",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53871,
    "customFieldValues": [
      {
        "value": "Erro ao gerar numerário 242636 - ROCRL",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao gerar numerário 242636 - ROCRL",
        "customFieldId": 206843
      },
      {
        "value": "Esse erro é direto do Totvs no qual o Jailton verifica e resolve, com base o que foi informado internamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54091,
    "customFieldValues": [
      {
        "value": "Lentidão",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão no sistema",
        "customFieldId": 206843
      },
      {
        "value": "Foi visto pelo time de infra no qual normalizou o sistema",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54163,
    "customFieldValues": [
      {
        "value": "Importação própria  nota não integrada",
        "customFieldId": 206842
      },
      {
        "value": "Importação própria - Integração das notas de trânsito\n\n",
        "customFieldId": 206843
      },
      {
        "value": "Nota não foi integrado pois o integrador estava fora, assim que o integrador voltou foi integrado a nota normalmente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54273,
    "customFieldValues": [
      {
        "value": "Erro 403 ao enviar NF para o SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "Certificado digital da Filial está com senha incorreta ou vencido.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente precisa validar se o certificado digital é válido.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53613,
    "customFieldValues": [
      {
        "value": "É possível alterar a configuração de débito dos impostos no processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "É possível realizar a alteração na aba DI/DA.Os débitos vem pagos pelo importador, se for necessário alterar, deve ser feito a cada novo processo, pois não conseguimos configurar para que venha sempre pelo despachante, por exemplo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54053,
    "customFieldValues": [
      {
        "value": "Por que os valores dos impostos não estão de acordo com a DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "O valor da taxa ce mercante, que é base de impostos e entra no valor aduaneiro, estava com o valor 288 (valor em dólar), quando na verdade o valor em reais era de 1.643,67.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52562,
    "customFieldValues": [
      {
        "value": "Integração entre ERP e Narwal não funciona",
        "customFieldId": 206842
      },
      {
        "value": "O certificado não havia sido atualizado, dessa forma no PI/PO estava retornando um erro no momento da autenticação.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário substituir o certificado para o ambiente de produção e homologação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54020,
    "customFieldValues": [
      {
        "value": "Parcela do numerário de câmbio não aparece para dar baixa.",
        "customFieldId": 206842
      },
      {
        "value": "Ao gerar o numerário de câmbio, a parcela não consta para dar baixa.",
        "customFieldId": 206843
      },
      {
        "value": "Operação financeira não cadastrada para a filial do processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53615,
    "customFieldValues": [
      {
        "value": "Invoice integrada para o SAP com valor incorreto.",
        "customFieldId": 206842
      },
      {
        "value": "A Invoice foi enviada para o SAP B1, porém a mesma integrou com o valor incorreto devido a uma alteração no schedule de envio.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário voltar para o fluxo antigo de envio, após essa alteração, os títulos voltaram a integrar com o valor correto.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54235,
    "customFieldValues": [
      {
        "value": "Rejeição Sefaz 549- CFOP de Saída pra NF de entrada. ",
        "customFieldId": 206842
      },
      {
        "value": "Ao emitir anulação de uma nota de saída, cliente informou o CFOP de saída, para nota de ajuste de entrada, com isso ocasionou o erro. ",
        "customFieldId": 206843
      },
      {
        "value": "Solução é ajustar manualmente o CFOP para o CFOP de entrada. \n\nPara notas de anulação geradas diretamente do menu de ação da NF o CFOP puxa de acordo com a operação. \n\nNessa situação a cliente gerou a nota divergente, cancelou e emitiu outra com o CFOP de acordo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54231,
    "customFieldValues": [
      {
        "value": "Taxa da moeda não atualizada",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que a taxa da moeda dólar não atualizou de forma automática.",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso, o cliente acabou ajustando de forma manual a taxa da moeda. Em outros casos, rodamos o job para que seja atualizado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53973,
    "customFieldValues": [
      {
        "value": "Ordem das informações ao exportar grid para excel",
        "customFieldId": 206842
      },
      {
        "value": "Ao exportar para excel uma grid, os campos estão vindo desordenados, dependendo da consulta realizada.",
        "customFieldId": 206843
      },
      {
        "value": "É possível ordenar os campos diretamente na grid (antes de exportar) para que, no momento da exportação para excel, as informações estejam ordenadas conforme necessidade.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53016,
    "customFieldValues": [
      {
        "value": "Preenchimento de DUIMP",
        "customFieldId": 206842
      },
      {
        "value": "Erro apresentado no preenchimento da DUIMP em ambientes de teste.",
        "customFieldId": 206843
      },
      {
        "value": "Erro em especifico na identificação de carga, o mesmo precisa terminar com estes seguintes números, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10 ou 11.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53208,
    "customFieldValues": [
      {
        "value": "Gestão de catalogo (Pais de origem - Fabricante/Produtor)",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava questionando o porque o mesmo não foi integrado para o portal único com as informações.",
        "customFieldId": 206843
      },
      {
        "value": "Instruído o cliente a criar um operador estrangeiro para os fabricantes e cadastrar diretamente no gestão de catalogo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53954,
    "customFieldValues": [
      {
        "value": "Cadastro do Cliente (Regime Tributação NFSe)",
        "customFieldId": 206842
      },
      {
        "value": "Cliente relata que após a atualização o campo está fazendo um autocomplete e gerando erro na NF",
        "customFieldId": 206843
      },
      {
        "value": "Informado que este campo sempre teve autocomplete e que não tem interferência na NF relatada por ela.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54081,
    "customFieldValues": [
      {
        "value": "Erro ao integrar NF ao processo",
        "customFieldId": 206842
      },
      {
        "value": "\"Erro no documento XML (1, 2)\" erro associado ao formato do arquivo incorreto.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustar o formado do arquivo XML.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53781,
    "customFieldValues": [
      {
        "value": "Arquivo txt de NF para envio ao sistema Object Data",
        "customFieldId": 206842
      },
      {
        "value": "Versão NFe",
        "customFieldId": 206843
      },
      {
        "value": "Acessar o cadastro da Filial ou Importador e alterar a versão NFe para 4.01.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54174,
    "customFieldValues": [
      {
        "value": "Atualização automática da taxa da moeda",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que a taxa da moeda estava com a vigência do dia 21/02, em vez da correta para o dia atual (24/02).",
        "customFieldId": 206843
      },
      {
        "value": "Este caso precisa ser revisado com o Igor para verificar se o arquivo da Convertec, que contém as taxas de cada moeda e é colocado no servidor, está vazio.\n\nCaso necessário, o job pode ser executado manualmente acessando este link. Em seguida, vá até \"Tarefas recorrentes\", localize o job chamado \"Job Atualizador de Taxa da Moeda\", marque a caixa ao lado dele e clique em \"Disparar agora\" no topo da página.\n\nApós alguns minutos, a taxa da moeda será atualizada, desde que o arquivo da Convertec esteja correto no servidor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53031,
    "customFieldValues": [
      {
        "value": "Como bloquear a integração de um XML com quantidades de produtos diferentes do processo?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Antes da validação o sistema faz alguns passos...\n\nRecupera o item da invoice a partir do item do pedido de compra.\nRecupera o item do processo que está vinculado ao item da invoice recuperada anteriormente.\nVerifica se existe realmente o item da invoice que foi tentado recuperar no passo 1.\nVerifica se existe o item do processo do processo vinculado no passo 2.\nA invoice precisa ter sido criada fora do processo.\nSe as etapas anteriores terem tido sucesso, ai sim ele valida a quantidade, e caso de falha retorna a mensagem da imagem na descrição.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53412,
    "customFieldValues": [
      {
        "value": "Desconto na rotina de Invoice no processo, seria apenas desconto financeiro. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente solicitou como deveria permanecer a Invoice, quando apenas possui desconto financeiro. ",
        "customFieldId": 206843
      },
      {
        "value": "\nDentro da rotina processo e aba de Invoice, tem o desconto financeiro, poderia estar informando nesse campo e verificar se vai ficar de acordo com o esperado. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53304,
    "customFieldValues": [
      {
        "value": "Vincular duas incoterm no processo DUE ",
        "customFieldId": 206842
      },
      {
        "value": "Como estar criando duas incoterm no processo de DUE. ",
        "customFieldId": 206843
      },
      {
        "value": "Para que consiga estar criando dois tipos de Incoterm no registro da DUE, vai precisar ativar a variável de ambiente NWL_INVOICEEXPO, essa variável ela vai permitir que você crie invoice no processo Expo. \n\n\n\nQuando você for registrar o processo DUE que tiver mais de uma incoterm, você vai criar a invoice selecionando os produtos que seria para Incoterm CFR E FOB. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53819,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF para o Sankhya \"Object reference not set to an instance of an object\"",
        "customFieldId": 206842
      },
      {
        "value": "A nota era enviada, porém no momento de enviar o vinculo entre pedido e nota estava retornando o erro, pois o processo foi realizado de maneira incorreta, assim nao possuindo vinculo com o pedido.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário cancelar os vinculos e ajustar o processo para que fosse possível o envio correto da nota.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54046,
    "customFieldValues": [
      {
        "value": "Solicitando o Fornecedor do Despachante ao gerar a parcela do Fechamento",
        "customFieldId": 206842
      },
      {
        "value": "Cadastro de Despachante não está informado o Fornecedor",
        "customFieldId": 206843
      },
      {
        "value": "Para todos os perfis de base Narwal, se algum titulo for gerado para um terceiro, é obrigatório que o mesmo esteja cadastrado como fornecedor.\n\nPara caso de Fornecedor do Despachante, Caso seu despachante não esteja cadastrado como fornecedor, será necessário gerar um novo cadastro e após, informá-lo na aba \"integração\" do cadastro de despachante.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54148,
    "customFieldValues": [
      {
        "value": "Código de verificação não chega ao e-mail",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que nenhum dos usuários estava recebendo o código de verificação de login no Narwal.\n",
        "customFieldId": 206843
      },
      {
        "value": "O erro foi causado por uma configuração incorreta no SMTP do próprio cliente. Após a correção feita pela infra do cliente, os usuários voltaram a receber normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53861,
    "customFieldValues": [
      {
        "value": "Documentos não aparece para o cliente",
        "customFieldId": 206842
      },
      {
        "value": "Cliente está relatando que o cliente não consegue visualizar os documentos anexados.",
        "customFieldId": 206843
      },
      {
        "value": "Ativar a flag para cada documento que será visto pelo cliente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53919,
    "customFieldValues": [
      {
        "value": "Lentidão geral",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão em todas as rotinas.",
        "customFieldId": 206843
      },
      {
        "value": "Cap de CPU e RAM.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52205,
    "customFieldValues": [
      {
        "value": "Follows enviados com informações incorretas.",
        "customFieldId": 206842
      },
      {
        "value": "Outro usuário estava alterando as informações do processo.",
        "customFieldId": 206843
      },
      {
        "value": "Verificar alterações nos campos de gatilho do follow, via auditoria.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54107,
    "customFieldValues": [
      {
        "value": "TAXA CE não estava somando ao valor dos produtos na NF.  ",
        "customFieldId": 206842
      },
      {
        "value": "A despesa de taxa CE não estava aparecendo no somatório a NF. ",
        "customFieldId": 206843
      },
      {
        "value": "Foi feito o ajustou da despesa na rotina tipo despesa, conforme as orientações que demos em outro chamado, colocando como base de imposto, também informou como outros acréscimos no campo do Siscomex. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53545,
    "customFieldValues": [
      {
        "value": "Código de verificação",
        "customFieldId": 206842
      },
      {
        "value": "O usuário reportou que, toda vez que o mesmo realizava o login no narwal, era enviado o código de verificação devo a autenticação de dois fatores.",
        "customFieldId": 206843
      },
      {
        "value": "Ao redefinir a senha, o parâmetro que controla a autenticação de dois fatores é ativada e um código é enviado para o e-mail do usuário toda vez que o mesmo realizar um novo login.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54143,
    "customFieldValues": [
      {
        "value": "Duplo fator de autenticação",
        "customFieldId": 206842
      },
      {
        "value": "Solicita um token a todo login no Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "A partir da versão 6.72.0, esta funcionalidade é obrigatória, em conformidade com a Lei Geral de Proteção de Dados Pessoais (LGPD).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54067,
    "customFieldValues": [
      {
        "value": "Como inserir um acréscimo na DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Precisa existir uma despesa base de imposto cadastrada no \"Tipo despesa\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54060,
    "customFieldValues": [
      {
        "value": "AJUDA PARA ALTERAR REFERÊNCIA NA ABA DE PROCESSOS",
        "customFieldId": 206842
      },
      {
        "value": "Cliente quer desmarcar o campo prefixo para alterar o numero do processo",
        "customFieldId": 206843
      },
      {
        "value": "A marcação desse campo está relacionada à integração da rotina sequencial com o número do processo informado no momento da criação. Como não é permitido alterar o número do processo após a criação, a alteração dessa configuração via banco de dados não afetará a informação do número do processo.\n\nPortanto, para realizar qualquer alteração, será necessário criar um novo processo, visto que, uma vez salvo, não será mais possível desmarcar essa opção.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53383,
    "customFieldValues": [
      {
        "value": "VALOR DO SERVIÇO SAINDO NA ABA DE NÃO INFORMADO",
        "customFieldId": 206842
      },
      {
        "value": "Poderiam nos ajudar a ajustar o valor do serviço para sair na aba de PAGO PELO DESPACHANTE, ao Invés de sair na aba de NÃO INFORMADO.",
        "customFieldId": 206843
      },
      {
        "value": "Atualmente somente colocando direto na despesa do processo e alterar o responsável do serviço",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54042,
    "customFieldValues": [
      {
        "value": "PEDIDO DE COMPRA - GERAR PROCESSO A PARTIR DO PEDIDO DE COMPRA",
        "customFieldId": 206842
      },
      {
        "value": "PEDIDO DE COMPRA - GERAR PROCESSO A PARTIR DO PEDIDO DE COMPRA",
        "customFieldId": 206843
      },
      {
        "value": "Cliente verificou que pode ter sido erro no computador deles, foi testado antes e estava funcionando normalmente, cliente retorno passando que o mesmo não esta mais divergente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54069,
    "customFieldValues": [
      {
        "value": "Como gerar a nota fiscal?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Nota gerada normalmente pelo cliente, tinha que ajustar a parametrização pois estava sem exceção.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53982,
    "customFieldValues": [
      {
        "value": "Erro ao emitir NF \"Informe a cidade do fornecedor da nota fiscal\"",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relata erros ao emitir a NF \"Informe a cidade do fornecedor da nota fiscal\".",
        "customFieldId": 206843
      },
      {
        "value": "Para corrigir este caso, é necessário verificar o fornecedor vinculado à nota fiscal. Em seguida, acesse o cadastro do fornecedor e atribua a cidade correspondente. Caso o fornecedor seja do exterior, basta preencher o campo 'País', e os campos 'Cidade' e 'Estado' serão preenchidos automaticamente com a opção 'Exterior'.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53601,
    "customFieldValues": [
      {
        "value": "Usuário não consegue baixar o XML da NF",
        "customFieldId": 206842
      },
      {
        "value": "O usuário relatou que, ao tentar baixar o XML da nota fiscal, não ocorre nenhuma ação de download ou exibido qualquer alerta.",
        "customFieldId": 206843
      },
      {
        "value": "Após análise, verificamos que o problema ao baixar o XML da nota fiscal ocorreu devido a um bloqueio no navegador. O Google Chrome do cliente estava impedindo o download dos arquivos",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54079,
    "customFieldValues": [
      {
        "value": "Taxa do dólar não atualizada",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que a taxa da moeda \"dólar\" não foi atualizada, o que impacta no cálculo correto dos impostos.",
        "customFieldId": 206843
      },
      {
        "value": "A atualização das taxas das moedas ocorre automaticamente todos os dias. Se a atualização não for realizada corretamente, verifique se o arquivo recebido do Banco Central contém as informações corretas. Caso necessário, o job pode ser executado manualmente seguindo os passos abaixo:\n\n1. Acesse https://cliente.narwalsistemas.com.br/jobs -> Tarefas recorrentes.\n\n2. Localize o job \"Job Atualizador de Taxa da Moeda\".\n\n3. Marque a checkbox correspondente e clique em \"Disparar agora\".\n\n4. Aguarde alguns minutos até que a taxa seja atualizada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53936,
    "customFieldValues": [
      {
        "value": "Colunas ocultadas ao integrar o XML de LI",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informou que teve dificuldades para visualizar as informações antes de integrar o XML da LI.",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver o problema, foi necessário que o usuário expandisse manualmente as colunas que são buscadas do XML. Após ajustar as colunas da LI em questão, as demais também foram impactadas, resolvendo o problema. A solução foi devidamente orientada ao cliente para que não seja necessário abrir novos chamados com o mesmo cenário.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54063,
    "customFieldValues": [
      {
        "value": "Erro ao tentar autorizar NF sefaz \"Array may not be empty or null. Parameter name: rawData\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro ocorreu por conta que foi removido o certificado de dentro do cadastro da filial, dessa forma não sendo possível autorizar no Sefaz.",
        "customFieldId": 206843
      },
      {
        "value": "Necessário anexar o certificado dentro do cadastro da Filial.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53747,
    "customFieldValues": [
      {
        "value": "Saldo insuficiente ao vincular pedido de compra a invoice.",
        "customFieldId": 206842
      },
      {
        "value": "Campo \"Quantidade a retirar\" tem quantidade maior que o saldo.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustar o campo Quantidade a retirar a quantidade de saldo existente no pedido de compra.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53750,
    "customFieldValues": [
      {
        "value": "Processo com taxa IPI onde não deveria ter",
        "customFieldId": 206842
      },
      {
        "value": "Estavam integrando a taxa IPI sem perceber.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustar diretamente no ERP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53948,
    "customFieldValues": [
      {
        "value": "Posição do processo não atualiza",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Cancelado/Rechaçado -> Status do processo é 'Cancelado' ou 'Rechaçado'.\nPré-Embarque -> Data de embarque do processo é nula e a Data de atracação do processo é nula.\nEm trânsito -> Data de embarque do processo não é nula e a Data de atracação do processo é nula.\nAtracados -> Data de embarque do processo não é nula, Data de atracação do processo não é nula e o campo Data de registro DI é nulo.\nRegistrados -> Data de embarque do processo não é nula, Data de atracação do processo não é nula, o campo Data de registro DI não é nulo e Data de desembaraço é nula.\nDesembaraçados -> Data de embarque do processo não é nula, Data de atracação do processo não é nula, o campo Data de registro DI não é nulo, Data de desembaraço não é nula e a Data de carregamento é nula.\nEntregues -> Data de embarque do processo não é nula, Data de atracação do processo não é nula, o campo Data de registro DI não é nulo, Data de desembaraço não é nula e a Data de carregamento não é nula.\nLocalização dos campos mencionados:\n\n\nStatus: Processo -> Editar -> Informações -> Principal -> Status.\nData de embarque: Processo -> Editar -> Informações -> Embarque -> Data embarque.\nData atracação: Processo -> Editar -> Informações -> Embarque -> Data atracação.\nData registro DI: Processo -> Editar -> Informações -> DI / DA -> Data registro.\nData desembaraço: Processo -> Editar -> Informações -> DI / DA -> Data desembaraço.\n\nData carregamento: Processo -> Editar -> Informações -> Transporte -> Containers -> Data carregamento.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53547,
    "customFieldValues": [
      {
        "value": "Como excluir/cancelar um pedido de compra.",
        "customFieldId": 206842
      },
      {
        "value": "Botão de cancelar o pedido de compra não fica disponível.",
        "customFieldId": 206843
      },
      {
        "value": "Para realizar a exclusão/cancelamento do pedido de compra, antes deve-se cancelar as invoices e processos vinculados ao mesmo, para que assim o saldo volte a ficar disponível e o botão de cancelar pedido de compra apareça.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53580,
    "customFieldValues": [
      {
        "value": "Como altero quem irá receber os follow-ups?",
        "customFieldId": 206842
      },
      {
        "value": "Desejo alterar quem irá receber os follow-ups cadastrados.",
        "customFieldId": 206843
      },
      {
        "value": "Deve-se entrar na rotina de cadastro de follow-up onde o mesmo está cadastrado, editar, e no campo 'Enviar', realizar a devida alteração nos e-mails.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54031,
    "customFieldValues": [
      {
        "value": "Não foi possivel alterar o valor das despesas pois o processo está fechado.",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Como havia uma parcela de fechamento financeiro, foi necessário excluir para prosseguir com a edição da despesa.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54027,
    "customFieldValues": [
      {
        "value": "Exceção Fiscal parametrização. ",
        "customFieldId": 206842
      },
      {
        "value": "Cliente solicita saber quando tem uma alíquota diferente de tributação do ICMS, como faz para configurar na parametrização.  ",
        "customFieldId": 206843
      },
      {
        "value": "Dentro da rotina parametrização, na aba de exceção fiscal vai criar as informações de tributação conforme o NCM. \n\nInformar também o tipo de produto e destino da mercadoria, conforme está no processo. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53995,
    "customFieldValues": [
      {
        "value": "Calcular impostos com erro",
        "customFieldId": 206842
      },
      {
        "value": "Quando o campo \"Taxa pagamento frete\" está preenchido, o sistema tenta gerar automaticamente uma despesa referente à diferença de frete. Para que isso ocorra corretamente, é necessário que, na rotina \"Tipo despesa\", exista uma despesa configurada com o tipo \"Diferença de frete\".\n\nCaso não haja essa despesa configurada, o erro será gerado.\n\nSe o campo \"Taxa pagamento frete\" estiver preenchido e a informação estiver correta, será preciso criar a despesa com o tipo correspondente. Caso contrário, basta remover o valor do campo.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente cadastrou esse frete incorretamente, ao apagar o mesmo funcionou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53987,
    "customFieldValues": [
      {
        "value": "Menu sumindo",
        "customFieldId": 206842
      },
      {
        "value": "Ao alterar o zoom da pagina o mesmo some",
        "customFieldId": 206843
      },
      {
        "value": "Alterar o zoom para 100%.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53992,
    "customFieldValues": [
      {
        "value": "HTTP Error 500 ",
        "customFieldId": 206842
      },
      {
        "value": "Conforme o relato do usuário, ao tentar acessar seu usuário no Narwal, era exibida uma página de erro com a mensagem \"HTTP Error 500\".",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver esse caso, é necessário realizar a redefinição de senha na rotina Usuário -> Redefinição de senha.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54005,
    "customFieldValues": [
      {
        "value": "Editar campo número",
        "customFieldId": 206842
      },
      {
        "value": "Campo número está bloqueado e não pode ser editado.",
        "customFieldId": 206843
      },
      {
        "value": "Este campo não é editável por padrão e atualmente não existe maneira nem é permitido alterar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53925,
    "customFieldValues": [
      {
        "value": "630 - Rejeicao: Valor do Produto difere do produto Valor Unitario de Tributacao e Quantidade Tributavel",
        "customFieldId": 206842
      },
      {
        "value": "Falta da informação da Unidade de medida",
        "customFieldId": 206843
      },
      {
        "value": "Na Nota Fiscal, guia Produto para determinada linha de produto falta a informação do \"valor unid. tributada\".\nIsso acontece pois a unidade informada no cadastro do Produto e NCM estão diferentes.\nQuando existe a diferença de unidade dos cadastros acima é necessário realizara a conversão da unidade de medida. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53939,
    "customFieldValues": [
      {
        "value": "Cliente havia se enganado, desconsiderar",
        "customFieldId": 206842
      },
      {
        "value": "Cliente havia se enganado, desconsiderar",
        "customFieldId": 206843
      },
      {
        "value": "Cliente havia se enganado, desconsiderar",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53167,
    "customFieldValues": [
      {
        "value": "Alteração de status do processo",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53515,
    "customFieldValues": [
      {
        "value": "Item não aparece para vincular a invoice",
        "customFieldId": 206842
      },
      {
        "value": "O pedido havia alguns itens, 1 desses itens não estava aparecendo para vincular a invoice. O item faltante estava vinculado a uma outra invoice, por esse motivo não aparecia.",
        "customFieldId": 206843
      },
      {
        "value": "Foi necessário excluir a invoice ao qual o item estava vinculado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53810,
    "customFieldValues": [
      {
        "value": "Erro na base de cálculo do ICMS",
        "customFieldId": 206842
      },
      {
        "value": "Frete não estava sendo considerado na parametrização da nota.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustada a parametrização de NF para que o Frete seja considerado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53879,
    "customFieldValues": [
      {
        "value": "Erro Apresentado: Falha de integração: { \"message\" : \"Authorization has been denied for this request.\" }",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar integrar os pedidos de compra do SAP para o Narwal, apresenta erro no momento da integração, Erro Apresentado: Falha de integração: { \"message\" : \"Authorization has been denied for this request.\" }",
        "customFieldId": 206843
      },
      {
        "value": "O problema era a questão de configuração de autenticação no SAP B1",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53497,
    "customFieldValues": [
      {
        "value": "Porque o crédito dos impostos não considera toda a alíquota do COFINS?",
        "customFieldId": 206842
      },
      {
        "value": "Quando a alqiuota do Cofins é superior a 10,25%, por padrão o sistema realiza o processo de majoração do COFINS o que faz com que um percentual dos 10,25% sejão considerados como custo do produto e não sejam creditados do valor.",
        "customFieldId": 206843
      },
      {
        "value": "Quando a alqiuota do Cofins é superior a 10,25%, por padrão o sistema realiza o processo de majoração do COFINS o que faz com que um percentual dos 10,25% sejão considerados como custo do produto e não sejam creditados do valor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53724,
    "customFieldValues": [
      {
        "value": "Follows não estão sendo enviados em HML",
        "customFieldId": 206842
      },
      {
        "value": "Por padrão os follows em HML são desativados.",
        "customFieldId": 206843
      },
      {
        "value": "Ativar os follows sob demanda e cuidar para quem são enviados.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53838,
    "customFieldValues": [
      {
        "value": "Erro ao consultar siscarga.",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao clicar no botão de consultar siscarga na aba embarque do processo.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente estava inserindo a senha de assinatura do certificado digital, o correto é inserir a senha de instalação.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53758,
    "customFieldValues": [
      {
        "value": "Erro ao emitir LI substitutiva",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar emitir a LI substitutiva de um processo, o Narwal exibe o seguinte alerta:\n\n\"O(s) campo(s) [Fabricante] descaracteriza(m) a LI original em caso de substituição e não pode(m) ser alterado(s).\"\n\nRotina: SISCOMEX → Licença de Importação → Emitir LI Substitutiva.",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver esse caso específico, foi necessário analisar o banco de dados, verificando a tabela LicencaImportacao. O objetivo era confirmar se a LI que o cliente estava tentando emitir possuía o fabricante dos produtos vinculado à mesma LI.\n\nComo se tratava de uma LI substitutiva, o fabricante deveria ser o mesmo dos produtos integrados ao processo. Durante a análise, foi identificado que o campo FabricanteId estava como NULL na LI.\n\nA orientação foi repassada ao cliente via call, instruindo-o a atribuir o fabricante diretamente na rotina LI → Aba Fornecedor → Campo Fabricante. Após essa ação, a LI foi emitida com sucesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53761,
    "customFieldValues": [
      {
        "value": "Erro ao enviar pedido do SAP : Inform country in the bank",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao enviar pedido do SAP : Inform country in the bank",
        "customFieldId": 206843
      },
      {
        "value": "Informado o o país no pedido de compra  logo ao enviar foi integrado normalmente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53887,
    "customFieldValues": [
      {
        "value": "Erro ao acessar o ambiente de homologação",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relatou dificuldades para acessar o ambiente de homologação. Pelo print anexado, é possível identificar que o erro pode estar relacionado a uma falha, expiração de senha ou configuração incorreta do SMTP.",
        "customFieldId": 206843
      },
      {
        "value": "O problema foi resolvido após atualizar a senha do SMTP, localizada na rotina:\n\nEmpresa → Edição → Aba \"Parâmetros\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53863,
    "customFieldValues": [
      {
        "value": "Erro ao integrar NF no processo expo",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Erro na sigla da unidade de medida, como o despachante alterou a sigla da unidade no xml, foi necessário alterar no Narwal também.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53840,
    "customFieldValues": [
      {
        "value": "Arquivo TXT está apresentando vários erros ao integrar",
        "customFieldId": 206842
      },
      {
        "value": "Sistema onde o arquivo estava sendo integrado estava com a Versão NFe diferente do arquivo gerado no Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Alterar a versão do sistema onde o arquivo precisa ser integrado para a versão igual ao arquivo gerado no Narwal. Versão correta pode ser encontrada na filial do processo, aba Nota Fiscal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53849,
    "customFieldValues": [
      {
        "value": "Erro 500 no login",
        "customFieldId": 206842
      },
      {
        "value": "Ao realizar o login no Narwal aparece erro de http 500",
        "customFieldId": 206843
      },
      {
        "value": "Realizado o ajuste no usuário de audit.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53675,
    "customFieldValues": [
      {
        "value": "Divergência Impostos Fechamento financeiro ",
        "customFieldId": 206842
      },
      {
        "value": "Erro dos impostos para o fechamento financeiro, o valor que está puxando no processo difere do que está na DI. \n\nPara o fechamento financeiro os impostos precisam estar o mesmo. \n",
        "customFieldId": 206843
      },
      {
        "value": "Solução para o erro importar o XML da DI, no processo e na rotina declaração de importação, vai acessar o menu de ação, enviar o fechamento. \n\nEnviando o fechamento os valores vão de acordo com o Siscomex ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52271,
    "customFieldValues": [
      {
        "value": "Erro vinculação de importador X Exportador",
        "customFieldId": 206842
      },
      {
        "value": "Erro vinculação de importador X Exportador DI",
        "customFieldId": 206843
      },
      {
        "value": "o vínculo não estava sendo exibido devido ao fato de o nome do cliente estar em maiúsculas. Realizamos o ajuste para a forma minúscula, e o vínculo foi corretamente exibido na Declaração de Importação (DI).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53363,
    "customFieldValues": [
      {
        "value": "RELATÓRIO - CONTA CORRENTE CLIENTE - SALDO SEM UTILIZAÇÃO",
        "customFieldId": 206842
      },
      {
        "value": "Cliente solicitou um relatorio de saldo,",
        "customFieldId": 206843
      },
      {
        "value": "Não consegui contato com o cliente para entender o que precisa e validar se realmente tem no narwal ou teria que ser melhoria.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53598,
    "customFieldValues": [
      {
        "value": "Divergência no valor/base de cálculo do ICMS.",
        "customFieldId": 206842
      },
      {
        "value": "Valor/Base de cálculo do ICMS divergente.",
        "customFieldId": 206843
      },
      {
        "value": "Valor está divergente, devido a variável de ambiente 'NWL_PREPAIDICMS' ativa. A despesa base imposto está diminuindo na base do ICMS.\nCom a mesma desativada, o valor fica de acordo com o cálculo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53831,
    "customFieldValues": [
      {
        "value": "E-mail de token não chega, quando solicitado",
        "customFieldId": 206842
      },
      {
        "value": "Falha na infra do cliente, ao testar em nossa infra os e-mail chegam normalmente.",
        "customFieldId": 206843
      },
      {
        "value": "TI do cliente deve analisar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53686,
    "customFieldValues": [
      {
        "value": "Ordens de Compra Não Estão integrando após atualização do Sênior",
        "customFieldId": 206842
      },
      {
        "value": "Mudança das referências de integração devido a atualização do ERP",
        "customFieldId": 206843
      },
      {
        "value": "Reinstalar o pacote do integrador e atualizar as referências do nosso lado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53522,
    "customFieldValues": [
      {
        "value": "Incluir casas decimais - NF",
        "customFieldId": 206842
      },
      {
        "value": "Incluir casas decimais - NF\n",
        "customFieldId": 206843
      },
      {
        "value": ", atualmente, o sistema não possui uma configuração padrão para enviar o valor com 6 casas decimais diretamente ao SAP, pois está perante ao que é pedido pelo SEFAZ com 10 casas decimais.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53272,
    "customFieldValues": [
      {
        "value": "Relatório de ordem de compra enviado ao fornecedor",
        "customFieldId": 206842
      },
      {
        "value": "Relatório de ordem de compra enviado ao fornecedor",
        "customFieldId": 206843
      },
      {
        "value": "Foi identificado que alguns fornecedores estavam recebendo e-mails de relatórios de ordens de compra de forma indevida. Após análise, verificamos que a regra para o envio desses e-mails estava habilitada na gestão de follow-up, o que permitia que os fornecedores recebessem as informações.\n\nPara corrigir isso, removemos os fornecedores dessa distribuição específica de relatórios, garantindo que não recebam mais os e-mails de forma indevida.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53428,
    "customFieldValues": [
      {
        "value": "Divergencia ICMS",
        "customFieldId": 206842
      },
      {
        "value": "Falta de informação na planilha do cliente",
        "customFieldId": 206843
      },
      {
        "value": "Validado a planilha com os valores do cliente. Foi confirmado que na planilha está faltando somar o valor do IPI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53843,
    "customFieldValues": [
      {
        "value": "Porque minha base de Exportador está com Power BI de Importador?",
        "customFieldId": 206842
      },
      {
        "value": "Time que solicitou abertura da base, solicitou para Importador.\n",
        "customFieldId": 206843
      },
      {
        "value": "Na solicitação da criação de uma nova base, deve ser informado o perfil do cliente, pois o BI é instalado de acordo com o Perfil.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53824,
    "customFieldValues": [
      {
        "value": "Erro na visualização do BI",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não consegue visualizar informações no painel do BI",
        "customFieldId": 206843
      },
      {
        "value": "Ajustar o filtro de data no BI e também colocar as informações como data ETA, Data nota fiscal, Data registro da DI, dessa forma irá aparecer de forma clara no BI as informações do processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53827,
    "customFieldValues": [
      {
        "value": "erro nas integrações de numerário e titulos financeiros do narwal para o sankhya",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava com erro nas integrações de numerário e titulos financeiros do narwal para o sankhya",
        "customFieldId": 206843
      },
      {
        "value": "A análise dos títulos enviados revelou os seguintes problemas e suas respectivas soluções:\n\nTítulos 4663, 4667, 4649: A TOP (Tabela de Operações Padrão) não estava parametrizada para as funções financeiras específicas requeridas. A parametrização foi ajustada para permitir o processamento correto desses títulos.\n\nTítulo 4646: A natureza de operação 4020900 utilizada no sistema Narwal não estava ativa ou não foi configurada como analítica no Sankhya. Foi realizada a ativação e a configuração necessária para garantir a integração entre os sistemas.\n\nTítulos 4648, 4650: Estes títulos não foram enviados para integração, o que impediu que chegassem à camada de integração da FLUID. Foi verificado e corrigido o processo de envio para garantir que os títulos sejam integrados corretamente.\n\nTítulo 4651: Foi identificado que a Natureza de Operação não foi informada. A natureza de operação foi devidamente atualizada para garantir o processamento adequado.\n\nObservação: As TOPs não parametrizadas foram ajustadas conforme necessário e todas as parametrizações de títulos foram revisadas com base na planilha fornecida pela Leila via Teams, garantindo a correção de todos os parâmetros.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53656,
    "customFieldValues": [
      {
        "value": "Erro na fluid ao enviar NF para o SAP B1",
        "customFieldId": 206842
      },
      {
        "value": "Estava sendo retornado erro na fluid no passo \"envianotainvent\" pois o Token havia sido alterado.",
        "customFieldId": 206843
      },
      {
        "value": "Solicitar a fluid a alteração do Token que permite a comunicação com a Invent.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53330,
    "customFieldValues": [
      {
        "value": "Como realizar uma substituição de NF?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Cliente fez pela prefeitura.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53371,
    "customFieldValues": [
      {
        "value": "Usuário editando processo",
        "customFieldId": 206842
      },
      {
        "value": "Alguns usuários estavam ficando \"presos\" na edição do processo, mesmo sem o Narwal estar aberto.",
        "customFieldId": 206843
      },
      {
        "value": "A solução foi ativar a variável NWL_HABILITABLOQUEIOUSUARIO, permitindo o bloqueio de acesso à edição de um processo ou DI. Após ativar a variável, o cliente confirmou que o problema foi resolvido.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53274,
    "customFieldValues": [
      {
        "value": "Como realizar a alteração de alíquotas?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Acessando a rotina \"NCM\", pesquisar pela NCM corresponde, editar e ajustar.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53544,
    "customFieldValues": [
      {
        "value": "Despesa não está compondo o cálculo do ICMS",
        "customFieldId": 206842
      },
      {
        "value": "Cadastro Tipo Despesa ",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro do Tipo despesa o campo \"Importação própria\" ou \"Encomenda\" ou \"Conta e ordem\" não está configurado para \"Base ICMS\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53516,
    "customFieldValues": [
      {
        "value": "Descrição do Importador em inglês  no rascunho da DU-e ",
        "customFieldId": 206842
      },
      {
        "value": "Navegador estava traduzindo",
        "customFieldId": 206843
      },
      {
        "value": "A descrição do nome do Importador na DU-e está sendo traduzida para idioma inglês. Confirmado que é o navegador utilizado pelo cliente. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53787,
    "customFieldValues": [
      {
        "value": "Porque minha nota fiscal está sem o peso bruto informado?",
        "customFieldId": 206842
      },
      {
        "value": "Não foi informado peso bruto nos itens do Processo",
        "customFieldId": 206843
      },
      {
        "value": "È necessário preencher, por linha de produto do processo, o peso bruto total de cada item, de acordo com o packing list.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53798,
    "customFieldValues": [
      {
        "value": "Contas a pagar no Sankhya não integrando ao narwal",
        "customFieldId": 206842
      },
      {
        "value": "Contas a pagar no Sankhya não estavam correto ",
        "customFieldId": 206843
      },
      {
        "value": "garantimos no sankhya que os lançamentos de crédito e débito fossem processados corretamente, alinhando a baixa da despesa com a receita, conforme esperado.\n\nAlém disso, as configurações relativas à integração com o ERP foram ajustadas para que o desconto atribuído no contas a pagar fosse refletido corretamente no sistema, resolvendo o problema de valores inconsistentes.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53741,
    "customFieldValues": [
      {
        "value": "Código de acesso não chega ao e-mail",
        "customFieldId": 206842
      },
      {
        "value": "O cliente informa que, ao tentar fazer login no Narwal, não está recebendo o código de acesso em seu e-mail.",
        "customFieldId": 206843
      },
      {
        "value": "Para este caso foi apenas um atraso na entrega do e-mail. Após alguns minutos, o usuário recebeu o código e conseguiu realizar o login.\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53619,
    "customFieldValues": [
      {
        "value": "Para que serve o filtro de Fornecedor no cadastro de Produto",
        "customFieldId": 206842
      },
      {
        "value": "Cadastro de Produto não tem vínculo com os Fornecedores.",
        "customFieldId": 206843
      },
      {
        "value": "O filtro recupera todos os Produtos que, dentro de um Processo, tem o mesmo Fornecedor informado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52077,
    "customFieldValues": [
      {
        "value": "Quantidade de embalagens diferente do pedido de compra",
        "customFieldId": 206842
      },
      {
        "value": "Quantidade de embalagens diferente do pedido de compra",
        "customFieldId": 206843
      },
      {
        "value": "\nDentro do cadastro de produtos, há uma aba específica chamada \"Embalagens\", onde é possível preencher um campo referente à quantidade de unidades por embalagem. Caso este campo esteja preenchido, o sistema utilizará essa informação para realizar o cálculo e determinar a quantidade de embalagens necessárias.\n\n\n\nPara exemplificar, no processo 212177 mencionado, o produto com a chave 3.650.8250 possui uma quantidade total de 53.000 unidades. No cadastro de produto, na aba \"Embalagens\", consta que cada embalagem comporta 20 unidades. Portanto, o sistema calcula a quantidade de embalagens necessárias dividindo a quantidade total de unidades pela quantidade de unidades por embalagem, ou seja, 53.000 / 20 = 2.650 embalagens.\n\n\n\nEm resumo, o sistema irá considerar as informações preenchidas no campo \"Quantidade de Produto na Embalagem\" para calcular automaticamente o número de embalagens necessárias.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53714,
    "customFieldValues": [
      {
        "value": "Gestão de Eventos - Evento",
        "customFieldId": 206842
      },
      {
        "value": "Duvida referente ao campo 'Evento'",
        "customFieldId": 206843
      },
      {
        "value": "Instruído o cliente que este campo contra o evento, abrindo uma chave '{' ele lista os campos",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53799,
    "customFieldValues": [
      {
        "value": "Erro registro de LI",
        "customFieldId": 206842
      },
      {
        "value": "Erro informa que o usuário não tem permissão para registrar a LI.",
        "customFieldId": 206843
      },
      {
        "value": "Identificado que dentro da LI havia alguns campos obrigatórios que estavam em branco, após fazer o preenchimento do mesmo a LI registrou. Sem a necessidade de alterar quaisquer modificação dentro do usuário.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53585,
    "customFieldValues": [
      {
        "value": "Porque não puxa o processo no BI",
        "customFieldId": 206842
      },
      {
        "value": "Esperávamos que o BI mostrasse todos os processos, contudo ele só mostra 1. / 2- dentro do BI a moeda do processo está vindo errada, era para ser Dolar e está vindo em Real.",
        "customFieldId": 206843
      },
      {
        "value": " comum ocorrer no inicio das novas bases, uma vez que a regra do Power BI do Narwal, tem uma premissa: possuir uma das 3 datas preenchidas num processo:\n\nData ETA; Data Registro DI; Data Entrega (emissão NF).\n\nNote, que na base da Vimacedo, não temos processo com nenhuma dessas 3 datas preenchidas.\n\nA partir do momento que for preenchido uma dessas datas, no dia seguinte, podemos fazer um update para atualizar os dados do BI",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52011,
    "customFieldValues": [
      {
        "value": "Porque meu titulo efetivo de câmbio não integra ao Sankhya?",
        "customFieldId": 206842
      },
      {
        "value": "Após emissão da Nota Fiscal de Nacionalização, caso ainda haja títulos de câmbio á prazo abertos, o Narwal automaticamente irá converter o titulo de previsão invoice, para o titulo efetivo invoice, para que possa ser atualizado no ERP, também, o valor do titulo já convertido pela taxa da DI, para posterior calculo da variação cambial.",
        "customFieldId": 206843
      },
      {
        "value": "Após ajuste de uma variável de ambiente: NWL_DESABILITAENVCANCEAUTOMATICENVICANCENFE = FALSE O título passou a integrar corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53357,
    "customFieldValues": [
      {
        "value": "Processo com DI registrada por fora",
        "customFieldId": 206842
      },
      {
        "value": "Cliente registrou a DI por fora e precisa integrar no Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Instruído o cliente que em versões mais recente temos a rotina \"Integrar DI/DUIMP\" que traz a DI registrada por fora.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53232,
    "customFieldValues": [
      {
        "value": "Configuração/parametrização do add-on, validar liberação de IPs e portas externas do add-on fiscal e Service Layer",
        "customFieldId": 206842
      },
      {
        "value": "Liberação de IPs e portas externas do add-on fiscal e Service Layer.",
        "customFieldId": 206843
      },
      {
        "value": "Configuração  técnica com cliente para validar liberação de IPs e portas externas do add-on fiscal e Service Layer.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53793,
    "customFieldValues": [
      {
        "value": "SAP B1 status 400: Estrutura inválida.",
        "customFieldId": 206842
      },
      {
        "value": "Erro ao enviar NF para o ERP.",
        "customFieldId": 206843
      },
      {
        "value": "É necessário que todas as invoices do processo contenham uma data de vencimento na aba \"Forma Pagamento.\"",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53777,
    "customFieldValues": [
      {
        "value": "Grid Pedido de Compra sem a opção de edição.",
        "customFieldId": 206842
      },
      {
        "value": "Grid estava toda alterada.",
        "customFieldId": 206843
      },
      {
        "value": "Reset de grid",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53763,
    "customFieldValues": [
      {
        "value": "Cancelamento de LI no Narwal, sem cancelar no siscomex. ",
        "customFieldId": 206842
      },
      {
        "value": "Possibilidade de cancelamento de uma LI no Narwal e reimportar o arquivo, sem que seja cancelada ao Siscomex. ",
        "customFieldId": 206843
      },
      {
        "value": "Para essa solicitação existe uma Variável, quando habilitada ela cancela a LI no Siscomex, quando desabilitada ela não permite o cancelamento no Siscomex apenas no Narwal.  \n\nVariável-  NWL-CANCLINTEGRADA \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53362,
    "customFieldValues": [
      {
        "value": "Custo unitário na Simulação de Importação",
        "customFieldId": 206842
      },
      {
        "value": "Exceção Fiscal informado na guia Produtos",
        "customFieldId": 206843
      },
      {
        "value": "Na Simulação de Importação, na guia Produtos estava sendo informado a Exceção Fiscal. Porém o ideal é informar a parametrização NF na guia Impostos(Simulação).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53746,
    "customFieldValues": [
      {
        "value": "Erro ao gerar DI",
        "customFieldId": 206842
      },
      {
        "value": "Ao registrar a DI retorna um erro que o Fabricante precisa ser informado o País",
        "customFieldId": 206843
      },
      {
        "value": "Cadastrado o País no Fabricante.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53127,
    "customFieldValues": [
      {
        "value": "Gerando contas a receber para um pedido de serviço",
        "customFieldId": 206842
      },
      {
        "value": "O cliente está enfrentando um problema no processo de emissão de pedidos de serviço. Embora o pedido devesse ser gerado sem a criação de parcelas, o sistema está automaticamente gerando essas parcelas, o que não é o comportamento esperado.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustado a forma de pagamento \"sem pagamento\" para não gerar parcela e apagamos a linha de pagamentos que estava cadastrada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53739,
    "customFieldValues": [
      {
        "value": "Link de redefinição de senha",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não esta recebendo o link de redefinição de senha",
        "customFieldId": 206843
      },
      {
        "value": "Foi feito o envio pela rotina usuário dentro do narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53419,
    "customFieldValues": [
      {
        "value": "Como reter ISS na NFSe?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Dentro do cadastro do cliente> configurações> faturamento a \"natureza operação serviço\"  precisa estar como \"ISS RETIDO PELO TOMADOR OU INTERMEDIARIO\" e a flag \"Recolhe ISS\" deve estar ativa.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53754,
    "customFieldValues": [
      {
        "value": "Sem acesso a uma rotina",
        "customFieldId": 206842
      },
      {
        "value": "Grupo Usuário sem acesso a rotina desejada.",
        "customFieldId": 206843
      },
      {
        "value": "Liberar rotina no cadastro de Grupo Usuário ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53270,
    "customFieldValues": [
      {
        "value": "Por que os valores de impostos não estão de acordo com a DI?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Podem existir diversas causas, mas neste caso havia uma despesa sendo informada erroneamente como \"base de imposto\", alterando a base do calculo dos impostos. Assim que a despesa foi alterada no \"tipo despesa\", os valores ficaram de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53188,
    "customFieldValues": [
      {
        "value": "DIME SC | NOTAS COM SÉRIE 2",
        "customFieldId": 206842
      },
      {
        "value": "As notas que são integradas do Narwal não estão levando para o registro 50 da DIME - SC",
        "customFieldId": 206843
      },
      {
        "value": "Validado que nunca emitiram uma DIme no narwal, e o campo ibge ja tem no envio do narwal, porém verificaram que é uma melhoria será realizado no ERP do cliente pela BM3",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53381,
    "customFieldValues": [
      {
        "value": "Taxa da moeda na criação da invoice",
        "customFieldId": 206842
      },
      {
        "value": "Alterar a taxa da moeda de acordo com uma data específica na criação da invoice.",
        "customFieldId": 206843
      },
      {
        "value": "Não é possível selecionar uma data para que o Narwal informe a taxa da moeda na invoice, apenas alterando manualmente, ou utilizando a taxa do dia.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53744,
    "customFieldValues": [
      {
        "value": "Problemas ao acessar o link do portal",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relata que todos os usuários estavam com problemas ao acessar o link do Narwal. \n\nErro: ERR_CONECTION_TIMED_OUT",
        "customFieldId": 206843
      },
      {
        "value": "Verificado com o cliente por call que a instabilidade foi causada por uma queda na internet interna. Após alguns minutos, o acesso ao narwal foi restabelecido.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53618,
    "customFieldValues": [
      {
        "value": "Dúvida sobre integração do XML da DI no processo",
        "customFieldId": 206842
      },
      {
        "value": "O cliente tinha dúvidas sobre a parametrização usada para integrar o XML da DI.",
        "customFieldId": 206843
      },
      {
        "value": "A parametrização pode variar conforme a necessidade do usuário. Neste caso, a melhor opção é usar \"Associar item a processo existente\" para manter as informações já presentes no processo e atualizá-las conforme a DI integrada.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52934,
    "customFieldValues": [
      {
        "value": "Erro de token ao logar no portal do cliente.",
        "customFieldId": 206842
      },
      {
        "value": "Ao tentar realizar login no portal do cliente, fica em looping, o erro é disparado no devtools informando que não foi possível autenticar o token.",
        "customFieldId": 206843
      },
      {
        "value": "Foi verificado que a URL do portal do cliente da ormac estava fora do padrão Narwal, após realizar os ajustes para o padrão, foi possível realizar o login.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53727,
    "customFieldValues": [
      {
        "value": "Por qual motivo não estou identificando meu título de fechamento no contas á pagar?",
        "customFieldId": 206842
      },
      {
        "value": "Causas possíveis:\n-Incorreto cadastro da Operação Financeira\n-Entendimento de contas á pagar/receber",
        "customFieldId": 206843
      },
      {
        "value": "Ao gerar a parcela, é importante verificar duas situações:\n1. Se a variável de ambiente  NWL_ENVIAFECHAMENTORESULTANTE está habilitada, pois ela considera que o Narwal é integrado com um ERP aonde é necessário enviar o valor total do Fechamento do Despachante, não apenas a resultante do valor adiantado x efetivo.\n2- Ao gerar a parcela, identificar na linha da parcela criada, se gerou um contas á pagar ou a receber, pois a resultante de dois valores pode gerar duas situações de movimentação de valores.\n3 - Se a Operação Financeira \"Fechamento Financeiro á Pagar\" e \"Fechamento Financeiro Á Receber\" está corretamente criada, para a filial do Processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53374,
    "customFieldValues": [
      {
        "value": "Como habilitar botão de \"Enviar p/ Narwal\" no SAP.",
        "customFieldId": 206842
      },
      {
        "value": "O botão não estava habilitado por conta de uma regra, para que seja possível o envio para o Narwal, o Fornecedor precisa ser estrangeiro.",
        "customFieldId": 206843
      },
      {
        "value": "Alterado o cadastro do Fornecedor no SAP, e informado o estado como \"EXTERIOR\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53737,
    "customFieldValues": [
      {
        "value": "Site não está carregando (on premise).",
        "customFieldId": 206842
      },
      {
        "value": "Falha na comunicação externa com o servidor. Acessando diretamente pelo servidor o ambiente está funcionando corretamente.",
        "customFieldId": 206843
      },
      {
        "value": "Time de infraestrutura do cliente deve atuar neste caso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53704,
    "customFieldValues": [
      {
        "value": "Grid gerando erro ao consultar o processo",
        "customFieldId": 206842
      },
      {
        "value": "Após alterar algumas colunas da grid do processo o mesmo gerava erro ao consultar.",
        "customFieldId": 206843
      },
      {
        "value": "Resetar a grid.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52638,
    "customFieldValues": [
      {
        "value": "Lentidão no portal do cliente",
        "customFieldId": 206842
      },
      {
        "value": "Cliente relatava bastante lentidão no portal do cliente.",
        "customFieldId": 206843
      },
      {
        "value": "Foi identificado que o sistema estava realizando o reciclo do pool de forma contínua, o que causava um tempo de carregamento elevado quando o cliente tentava acessar o sistema. O ajuste foi feito para que o pool seja reiniciado uma vez por mês, melhorando a performance e diminuindo o tempo de espera.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53740,
    "customFieldValues": [
      {
        "value": "Código de autenticação não chega no e-mail",
        "customFieldId": 206842
      },
      {
        "value": "O usuário relatou que não estava recebendo o código de autenticação de dois fatores, que é enviado automaticamente para o e-mail ao realizar o login.",
        "customFieldId": 206843
      },
      {
        "value": "Em call com o cliente, identificamos que a demora na entrega do código foi causada por uma instabilidade na rede interna do próprio cliente. Após analisar o SMTP e confirmar que estava configurado corretamente, o código foi entregue no e-mail do usuário após 4 minutos.\n\nSe esse problema ocorrer com outros clientes ou usuários, é importante verificar se a senha SMTP não está expirada ou foi alterada/inserida com os dados incorretos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53611,
    "customFieldValues": [
      {
        "value": "Consulta shipstracking",
        "customFieldId": 206842
      },
      {
        "value": "Em consulta o Shipstracking na aba Tracking os campos com datas abaixo não são preenchidos automaticamente ?\n\nGostaria de informar também que o ShisTracking ficou disponível somente para consulta no Booking, contêiner e nos dados do BL não ficará disponível ?",
        "customFieldId": 206843
      },
      {
        "value": "Com relação às informações necessárias, posso confirmar com certeza os seguintes campos que devem ser preenchidos:\n\nNavio\nOrigem\nDestino\nData ETA (Estimated Time of Arrival)\nData ETD (Estimated Time of Departure)\nData de embarque\nData de atracação\nAlém disso, gostaria de salientar que o botão de ação está disponível apenas quando o tipo de transporte é aéreo. No caso de transporte marítimo, ele está sempre localizado nos dados do container ou no booking.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53669,
    "customFieldValues": [
      {
        "value": "Títulos de Importação no Contas a pagar",
        "customFieldId": 206842
      },
      {
        "value": "No Processo não foi calculados os impostos",
        "customFieldId": 206843
      },
      {
        "value": "Na rotina Operação financeira deverá ter criado a operação com o tipo \"Importação despesas a pagar\";\nNa rotina \"Variáveis ambiente\" a variável NWL_AGRUPARIMPOSTOSDI deverá estar ativo para gerar um unico titulo para os impostos da DI.\nNo Processo, obrigatoriamente deverá ser calculados os impostos do processo;\nApós acessar a Declaração de importação e confirmar se na guia Pagamentos consta as despesas dos impostos. Os impostos serão gerados automaticamente ao calcular os impostos no processo.\nQuando as despesas estão na guia mencionada acima, basta acessar o menu de ação da Declaração e clicar em Enviar impostos.\nSerá gerado no Contas a pagar o título com os impostos.     \t   ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52942,
    "customFieldValues": [
      {
        "value": "Despesas não aparecem no Fechamento Financeiro",
        "customFieldId": 206842
      },
      {
        "value": "Impostos não haviam sido calculados.",
        "customFieldId": 206843
      },
      {
        "value": "Calcular impostos.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53730,
    "customFieldValues": [
      {
        "value": "Erro 500 ao acessar o narwal",
        "customFieldId": 206842
      },
      {
        "value": "Ao inserir os dados de login no narwal, era exibido a mensagem \"HTTP ERROR 500\".",
        "customFieldId": 206843
      },
      {
        "value": "A solução para resolver o problema de login envolve duas etapas:\n\n1° Verificação de bloqueio no banco de dados:\n\nAcesse a tabela AspNetUsers e verifique a coluna LockoutEndDateUtc.\n\nSe houver uma data registrada para o ID do usuário, realize um UPDATE para NULL, removendo o bloqueio gerado após três tentativas de acesso sem sucesso.\nRedefinição de senha:\n\n2° Redefinição de senha:\n\nEnvie um link de redefinição de senha para o usuário que está com o erro citado. O envio do link ao e-mail deve ser enviado diretamente pela rotina \"Usuário\".\n\nApós essas etapas, o usuário poderá tentar o login novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53735,
    "customFieldValues": [
      {
        "value": "Relatório de Acompanhamento de Pedido indisponível",
        "customFieldId": 206842
      },
      {
        "value": "O cliente relatou que a rotina \"Acompanhamento de Pedido\" não estava aparecendo na listagem das rotinas.\n\nRotina: Relatórios → Gerais → Acompanhamento de Pedido.",
        "customFieldId": 206843
      },
      {
        "value": "Foi validado que a instabilidade ocorreu na infraestrutura do cliente. O problema foi solucionado após o cliente deslogar e acessar novamente o Narwal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53474,
    "customFieldValues": [
      {
        "value": "Duvida versão da nota",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "Foi instruído ao parceiro que a versão 4.00 e 4.01 tem diferenças de layout, dito isso para algumas notas o narwal não autoriza a emissão com a versão 4.01,",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53710,
    "customFieldValues": [
      {
        "value": "Despesas incorretas",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "O cliente encontrou a divergência e alterou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53633,
    "customFieldValues": [
      {
        "value": "(Informativo) Mudanças sobre emissão de NF - Brusque",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53609,
    "customFieldValues": [
      {
        "value": "Valores dos impostos divergentes da DI",
        "customFieldId": 206842
      },
      {
        "value": "XML da DI",
        "customFieldId": 206843
      },
      {
        "value": "Integrado o xml da DI no processo e alterado a taxa do seguro conforme DI.\nCalcular os impostos(no Processo).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53671,
    "customFieldValues": [
      {
        "value": "Erro ao enviar NF para o SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "O erro ao enviar duas notas fiscais para o SEFAZ ocorreu devido à adição de produtos que não foram migrados para a NF. Após análise, foi identificado que se tratava de um erro operacional, pois os produtos na aba Processo → Produtos não estavam com a adição preenchida.",
        "customFieldId": 206843
      },
      {
        "value": "A solução foi adicionar manualmente as adições em cada produto diretamente na rotina de NF:\n\nNota Fiscal → Produto → Edição do Produto → Importação → Campo Adição.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53614,
    "customFieldValues": [
      {
        "value": "Valor incorreto de frete no processo",
        "customFieldId": 206842
      },
      {
        "value": "Usuário informou o valor do frete na moeda errada dentro da invoice.",
        "customFieldId": 206843
      },
      {
        "value": "Ajustar o valor do frete na invoice para o valor na moeda original.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53662,
    "customFieldValues": [
      {
        "value": "Erro Integração XML de DI",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53674,
    "customFieldValues": [
      {
        "value": "Porque meus impostos do Numerário Processo Impo estão com diferença?",
        "customFieldId": 206842
      },
      {
        "value": "Foi analisado que neste caso, o consultor possuia um acrescimo (Taxa CE Mercante) com rateio pelo peso liquido da mercadoria.\nConstatado (com o documento DI - PDF) que o peso liquido tanto das adições quanto total do processo, estavam divergentes dos pesos da DI. Por isso, o Narwal calculou o acréscimo de acordo com os pesos errados, consequentemente, trazendo divergência ao calculo dos impostos",
        "customFieldId": 206843
      },
      {
        "value": "Analisar:\n-Se há acréscimo no pré calculo\n-Se o acréscimo tem rateio por peso liquido ou valor\n-Se o peso liquido e valor da mercadoria estão de acordo com a DI",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53323,
    "customFieldValues": [
      {
        "value": "Nota Fiscal Denegada",
        "customFieldId": 206842
      },
      {
        "value": "Falha do cliente.",
        "customFieldId": 206843
      },
      {
        "value": "Não houve solução, pois o cliente se equivocou com status da Nota Fiscal no ERP. O mesmo queria realizar no Narwal a Anulação de uma NF afirmando que a mesma estava Denegada, sendo que a NF constava como Autorizada no SEFAZ .",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53641,
    "customFieldValues": [
      {
        "value": "Sistema fora do ar",
        "customFieldId": 206842
      },
      {
        "value": "Instabilidade ao acessar o narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Verificado que não houve instabilidade ou impeditivos para acesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53407,
    "customFieldValues": [
      {
        "value": "Erro retorno do Senior ao enviar nota fiscal de despesa",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro é gerado através de uma configuração do CFOP no próprio Sênior.",
        "customFieldId": 206843
      },
      {
        "value": "Para corrigir esse problema basta seguir os passos deste fórum do próprio Sênior exemplificando como resolver o problema.\nhttps://suporte.senior.com.br/hc/pt-br/articles/4408641549332-ERP-Webservice-O-rateio-da-transa%C3%A7%C3%A3o-XX-para-execu%C3%A7%C3%A3o-atrav%C3%A9s-de-servi%C3%A7os-deve-ser-sem-confirma%C3%A7%C3%A3o-ou-sem-rateio",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53655,
    "customFieldValues": [
      {
        "value": "E-mail de redefinição de senha não entregue",
        "customFieldId": 206842
      },
      {
        "value": "Foi identificado que a senha SMTP do cliente estava expirada.",
        "customFieldId": 206843
      },
      {
        "value": "A solução foi atualizar a senha SMTP diretamente na rotina:\n\nEmpresa → Parâmetros → Configuração de E-mail\n\nApós atualizar a senha, os e-mails de redefinição de senha foram entregues corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53593,
    "customFieldValues": [
      {
        "value": "Quantidade, peso líquido e peso bruto não migrados para a NF",
        "customFieldId": 206842
      },
      {
        "value": "O erro ocorreu devido a um erro operacional do cliente. Ao gerar a nota fiscal, as informações de quantidade, peso líquido e peso bruto do processo não estavam sendo migradas.\n\nRotina: Nota Fiscal → Transporte → Volumes",
        "customFieldId": 206843
      },
      {
        "value": "Para que as informações sejam migradas corretamente, é necessário preenchê-las na rotina:\n\nProcesso → Embalagens.\n\nApós a inserção das embalagens, os dados foram vinculados corretamente, com exceção da Quantidade, que precisou ser atribuída manualmente na rotina Nota Fiscal → Transporte → Volumes.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53078,
    "customFieldValues": [
      {
        "value": "Erro no retorno da API",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava com erro na API do pedido 251328 ",
        "customFieldId": 206843
      },
      {
        "value": "O pedido tem 2 itens, mas o processo está vinculado apenas a 1 item. A nota é gerada de acordo com os itens do processo.\nNo momento de integrar o XML da DI, é marcado a opção para associar com os itens existentes no processo\nComo no processo havia 1 item, ele vinculou apenas esse item, tanto que na rotina \"Declaração importação\" na aba \"Adição\" consta apenas esse item",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53647,
    "customFieldValues": [
      {
        "value": "Rejeição 630 SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "Rejeição 630: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável",
        "customFieldId": 206843
      },
      {
        "value": "Cliente não havia cadastrado a conversão de unidade de medida para os itens do processo, fazendo com que o valor e a quantidade unidade tributada ficasse zerada na nota fiscal.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53327,
    "customFieldValues": [
      {
        "value": "Problema visualização cadastro fornecedor",
        "customFieldId": 206842
      },
      {
        "value": "Cliente pontuo problema de renderização no narwal ao acessar a rotina de fornecedor",
        "customFieldId": 206843
      },
      {
        "value": "O cliente informou que o sistema Narwal não estava renderizando corretamente. Realizamos diversos testes, inclusive em outras máquinas, e não conseguimos reproduzir o problema relatado. Além disso, não obtivemos retorno adicional do cliente após nossa investigação.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53542,
    "customFieldValues": [
      {
        "value": "Imagens do template do follow up não carregam ",
        "customFieldId": 206842
      },
      {
        "value": "Extensão das imagens no template está diferente da extensão dos arquivos no servidor.",
        "customFieldId": 206843
      },
      {
        "value": "Editar o template e alterar a extensão das imagens conforme está nos arquivos do servidor.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53637,
    "customFieldValues": [
      {
        "value": "Exportador na grid do processo",
        "customFieldId": 206842
      },
      {
        "value": "Falta da informação exportador na grid do processo",
        "customFieldId": 206843
      },
      {
        "value": "Para que a coluna Exportador seja informada na grid dos Processos é necessário informar o campo \"Fornecedor\" no Processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53430,
    "customFieldValues": [
      {
        "value": "Como configurar usuários dentro do Narwal? ",
        "customFieldId": 206842
      },
      {
        "value": "Configuração Usuários,  em algumas rotinas dentro do Narwal. ",
        "customFieldId": 206843
      },
      {
        "value": "Para que seja configurado o usuário dentro do Narwal. \n\nAcessar a rotina de usuário, verificar o grupo que se enquadra esse usuário. \n\nPara dar acesso a algumas rotinas do narwal, é apenas os Administradores vão poder dar acesso aos funcionários, conforme o seu grupo de usuário. \n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53594,
    "customFieldValues": [
      {
        "value": "Porque o título de numerário não foi criado?",
        "customFieldId": 206842
      },
      {
        "value": "Causa 1 - a Filial do Processo nao estava com as Operações Financeiras cadastradas corretamente\nCausa 2 - Na aba Numerário, não tinhamos despesas lançadas contra o Despachante",
        "customFieldId": 206843
      },
      {
        "value": "Foi analisado:\nOperações Financeiras criadas para a Filial\nCadastro do Despachante - Fornecedor Informado\nDespesas pagas por - despachante - na aba Numerário",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53536,
    "customFieldValues": [
      {
        "value": "Erro ao vincular DI",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não estava conseguindo  fazer vinculação da DI no narwal:\n\nRetorno do erro : A cadeia de caracteres de entrada não estava em um fomato correto",
        "customFieldId": 206843
      },
      {
        "value": "DI reintegrada no processo.\n\nTentei puxar novamente o XML via siscomex e apareceu um erro \"da invoice já baixada que não pode ser alterada\"\n\nQuando é integrado o XML ele atualiza a invoice por isso os valores precisam estar em aberto.\n\nCancelei o fechamento de cambio do contrato 446800385.\n\nReintegrei a DI e deu certo.\n\nRefiz o fechamento de cambio novamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53621,
    "customFieldValues": [
      {
        "value": "Envio de NF para SEFAZ",
        "customFieldId": 206842
      },
      {
        "value": "No momento do envio  da NF para o SEFAZ\n",
        "customFieldId": 206843
      },
      {
        "value": "No momento do Envio da NF para o SEFAZ em tela aparece uma mensagem extensa em amarelo. Para liberar acessar o NC e reiniciar pool de aplicação.\nImportante: Quando ocorrer deverá chamar o Lucas santanna ou Wellington para que analisem.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53355,
    "customFieldValues": [
      {
        "value": "Input Massivo de Processo por e-mail no Módulo Logístico.",
        "customFieldId": 206842
      },
      {
        "value": "O cliente GM, usa o input de informações via o envio de um e-mail padrão (anexo) e o cliente está dizendo que existem processos que não estão sendo criado, ou com  duplicidade.\n",
        "customFieldId": 206843
      },
      {
        "value": "Ajuste na API, e inclusão do limite de 300 processos por vez (linha do excel) ao encaminhar o e-mail.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53491,
    "customFieldValues": [
      {
        "value": "Como criar Portal do Cliente?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Informações disponibilizadas no link contendo o passo a passo.\n\nhttps://portal.narwalsistemas.com.br/wiki/usuario-portal-do-cliente/",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53254,
    "customFieldValues": [
      {
        "value": "Envio de NF para o Sankhya gera erro \"MENSAGEM DO SANKHYA: Tipo de Movimento inválido nesta opção.\"",
        "customFieldId": 206842
      },
      {
        "value": "Esse erro é retornado quando o campo \"TIPMOV\" é enviado como \"C\" e a TOP no Sankhya não está parametrizada para receber movimentação de compra.\n\nO contrario também ocorre.",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver é necessário ajustar a TOP no Sankhya, ou alterar a TOP que é utilizada para envio.\n\nNa rotina \"Parametrização NF\", quando editamos a parametrização há uma aba \"Sankhya\", lá é possível ajustar a TOP.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53467,
    "customFieldValues": [
      {
        "value": "Conversão do valor Antidumping",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida sobre valor calculado de antidumping na adição, dentro da Declaração de importação.",
        "customFieldId": 206843
      },
      {
        "value": "Valor que está em tela no Narwal já está convertido para BRL.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53436,
    "customFieldValues": [
      {
        "value": "Aba produtos vindo em branco",
        "customFieldId": 206842
      },
      {
        "value": "Operação incorreta do Usuário.",
        "customFieldId": 206843
      },
      {
        "value": "Operação incorreta do Usuário. Cliente trouxe as informações para o Narwal com conteúdos faltantes",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53549,
    "customFieldValues": [
      {
        "value": "Processo precisar estar aberto",
        "customFieldId": 206842
      },
      {
        "value": "Está ocorrendo a mensagem Processo precisa estar aberto. ao criar a nota fiscal. ",
        "customFieldId": 206843
      },
      {
        "value": "Quando a variável NWL_ENCERRAPROCESSO está com valor SIM, o processo é encerrado, ou seja, o status é alterado automaticamente para Fechado no momento da criação da Nota Fiscal.\n\nE possível reabrir o status da NF, para isso o usuário deverá ter a permissão para \"Permite reabrir processo\"; ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53586,
    "customFieldValues": [
      {
        "value": " tag cprod incorreta no xml da nota fiscal",
        "customFieldId": 206842
      },
      {
        "value": "Cliente está com a tag cprod incorreta no xml da nota fiscal",
        "customFieldId": 206843
      },
      {
        "value": "Identificamos que o problema que você está enfrentando com a tag <cprod> no XML ocorre devido a uma duplicação na chave de produto no sistema. O código 061005501 está associado a dois produtos, sendo que um deles, o produto de código 4446, possui a mesma chave, mas com aspas adicionais. Nesse caso foi passado para que fosse verificado o valor correto da chave do produto assim emitindo a nota fiscal corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53128,
    "customFieldValues": [
      {
        "value": "Dúvidas sobre DUIMP - XML e dúvidas gerais",
        "customFieldId": 206842
      },
      {
        "value": "N/A",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53548,
    "customFieldValues": [
      {
        "value": "Despesas Taxa Sicomex e THC não estão sendo calculadas",
        "customFieldId": 206842
      },
      {
        "value": "Copar despesas do numerário para despesas do processo",
        "customFieldId": 206843
      },
      {
        "value": "Cliente Natura realiza a cópia das despesas do Numerário para Processo. \nApós copiar as despesas do Numerário para Processo, as despesas refletiram corretamente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53553,
    "customFieldValues": [
      {
        "value": "Erro \"Invalid character found at position\" ao integrar pedido de compra.",
        "customFieldId": 206842
      },
      {
        "value": "O problema ocorreu por conta de caracteres invalidos informado na descrição do produto no ERP.",
        "customFieldId": 206843
      },
      {
        "value": "Para solucionar o problema, foi necessário alterar a descrição, após alteração a integração ocorreu normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53571,
    "customFieldValues": [
      {
        "value": "ICMS que deveria ser imune está sendo inserido automático ao calcular impostos",
        "customFieldId": 206842
      },
      {
        "value": "O valor do ICMS está sendo inserido de forma automática ao calcular os impostos, mesmo sendo imune (não deve ser sobrado)",
        "customFieldId": 206843
      },
      {
        "value": "O cliente deve informar a parametrização onde consta a isenção deste imposto.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53575,
    "customFieldValues": [
      {
        "value": "\"Erro de Servidor no Aplicativo\" ao iniciar o ambiente.",
        "customFieldId": 206842
      },
      {
        "value": "Falha na inicialização de um <dependentAssembly> no webconfig do portal.",
        "customFieldId": 206843
      },
      {
        "value": "Acessar o ambiente em localhost (localhost detalha melhor o erro, em alguns casos), verificar qual <dependentAssembly> está causando a falha e apaga-lo do WebConfig (vide tramite 4 do atendimento).",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53524,
    "customFieldValues": [
      {
        "value": " ERRO AO TENTAR FAZER O CADASTRO DE PRODUTO VIA PLANILHA",
        "customFieldId": 206842
      },
      {
        "value": "Erro Carregue NCM Conversão Inválida. \nNotei que a coluna \"NCM\" não está disponível no modelo padrão, apenas o \"NCMID\". ",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver isso, removi a coluna \"NCM\" da planilha e consegui avançar com a integração.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52484,
    "customFieldValues": [
      {
        "value": "Erro ao enviar pedido de compra ao narwal",
        "customFieldId": 206842
      },
      {
        "value": "Cliente não conseguia enviar os pedidos ao narwal por falha de comunicação com o Banco de dados",
        "customFieldId": 206843
      },
      {
        "value": "validamos o IP utilizado para o envio dos pedidos e comparamo-lo com o IP registrado em nosso servidor. Identificamos que os IPs não eram os mesmos. Após o ajuste no IP na connectionString e a reinicialização do serviço, os pedidos foram integrados com sucesso.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53446,
    "customFieldValues": [
      {
        "value": "Informação \"Total\" não aparece na baixa de lote do contas a pagar",
        "customFieldId": 206842
      },
      {
        "value": "A informação do total ao clicar em \"Baixar lote\" não é exibida.",
        "customFieldId": 206843
      },
      {
        "value": "O valor da coluna \"Total\", que deveria exibir o total dos lançamentos selecionados, estava sendo mostrado na coluna \"Valor saldo (USD)\". Verifiquei que a coluna estava oculta. Após reexibi-la, a informação voltou a aparecer normalmente.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53287,
    "customFieldValues": [
      {
        "value": "Rejeição 610 SEFAZ.",
        "customFieldId": 206842
      },
      {
        "value": "Erro Rejeição 610: Total da NF difere do somatório dos Valores compõe o valor Total da NF, quando realizado o envio da NFe para o SEFAZ.",
        "customFieldId": 206843
      },
      {
        "value": "O cálculo realizado pelo SEFAZ foi verificado e analisado no XML da NF-e. Para mais informações sobre a rejeição 610 e como resolvê-la, está disponível no link:\nhttps://oobj.com.br/bc/rejeicao-610-como-resolver/\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53314,
    "customFieldValues": [
      {
        "value": "Por que há diferença nos valores do processo para a Invoice?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Por conta do arredondamento houve uma pequena diferença no valor do processo para o valor da Invoice, já que Invoice tem apenas duas casas decimais.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53520,
    "customFieldValues": [
      {
        "value": "Aba de exceção fiscal oculta",
        "customFieldId": 206842
      },
      {
        "value": "Aba não aparece na rotina de exceção fiscal.",
        "customFieldId": 206843
      },
      {
        "value": "Acessar a rotina com a flag \"Permite obrigar campos\" habilitada no cadastro de usuário, e clicar no botão para habilitar a aba.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53543,
    "customFieldValues": [
      {
        "value": "Erro ao transmitir NF",
        "customFieldId": 206842
      },
      {
        "value": "Cliente resolveu internamente",
        "customFieldId": 206843
      },
      {
        "value": "Cliente resolveu internamente",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53276,
    "customFieldValues": [
      {
        "value": "Duvida referente a Sigla da Moeda no contas a pagar",
        "customFieldId": 206842
      },
      {
        "value": "O mesmo está aparecendo em forma de numero.",
        "customFieldId": 206843
      },
      {
        "value": "Identificado que na rotina de Moeda o mesmo puxa a informação no campo 'chave', dito isso o cliente precisa configurar a maneira que deve aparecer, pois pode ter conflitos com ERP's.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53525,
    "customFieldValues": [
      {
        "value": "Erro ao registrar DI \"A cadeia de caracteres de entrada não estava em um formato correto\"",
        "customFieldId": 206842
      },
      {
        "value": "Dentro da DI, há um campo onde podemos colocar informações complementares, informações como: nome do navio, data embarque, etc...\n\nEssas informações são colocadas entre chaves, exemplo \"{NOME.DO.NAVIO}\" toda chave deve ter um ponto onde é aberta e fechada, caso feito de maneira errada, é retornado o erro.",
        "customFieldId": 206843
      },
      {
        "value": "Para solucionar o problema, basta achar qual das informações está com erro, e corrigir.\n\nExemplo erro: {NOME.DO.NAVIO}}\n\nExemplo de correção: {NOME.DO.NAVIO}, sem a chave \"}\" a mais que foi colocada ao fechar a informação",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53502,
    "customFieldValues": [
      {
        "value": "Como cadastrar o \"Setor aduaneiro\" e \"Recinto alfandegado\"",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "O cadastro é realizado dentro das devidas rotinas: \"Setor aduaneiro\" e \"Recinto alfandegado\".",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53501,
    "customFieldValues": [
      {
        "value": "Despesas duplicadas no Numerário",
        "customFieldId": 206842
      },
      {
        "value": "Quando a parcela do Numerário está criada, e é colocado para processar novamente o pré-calculo, todas as despesas que constam no mesmo, serão duplicadas.",
        "customFieldId": 206843
      },
      {
        "value": "Caso seja necessário processar a mesma tabela pré calculo para atualização de valores, será necessário:\n\n1. ou excluir a parcela de numerário ou\n\n2. remover manualmente as despesas, pois serão lançadas em duplicidade.\n\nEsse é um método de segurança do sistema afim de que a partir do momento que há uma parcela gerada no contas á pagar, não sofra ajuste de valores.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53507,
    "customFieldValues": [
      {
        "value": "Power BI apresentando dados inexistentes no ambiente PRD",
        "customFieldId": 206842
      },
      {
        "value": "Ambiente PRD foi copiado do HML e teve uma limpeza na base. Porém o BI não remove as informações, sendo necessário atualizar manualmente.",
        "customFieldId": 206843
      },
      {
        "value": "Abrir SDK para o TI para atualizarem o BI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53475,
    "customFieldValues": [
      {
        "value": "Valores não batendo na Nota Fiscal",
        "customFieldId": 206842
      },
      {
        "value": "Cliente gerou os itens a partir do pedido de compra sem integrar o XML da DI. E realizou atualizações manuais.",
        "customFieldId": 206843
      },
      {
        "value": "Identificado que o cliente não integrou o XML da DI, dito isso o mesmo não puxou certo os valores da despesas/taxas/frete, por esse motivo os valores não estavam batendo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53415,
    "customFieldValues": [
      {
        "value": "Erro ao integrar o XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava com erro ao integrar o XML da DI, este erro está sendo causado por conta dos itens já estarem com vinculo no lançamento fiscal.",
        "customFieldId": 206843
      },
      {
        "value": "Neste caso o cliente teve que apagar a invoice e excluir os itens já lançados para poder integrar o XML da DI.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53306,
    "customFieldValues": [
      {
        "value": "Erro ao integrar XML da DI",
        "customFieldId": 206842
      },
      {
        "value": "O XML fornecido pelo usuário apresentava divergências nas quantidades de alguns itens em relação às quantidades registradas no processo.",
        "customFieldId": 206843
      },
      {
        "value": "Para resolver esse caso, é necessário pegar a chave do item exibida no alerta e consultá-la via banco na tabela \"ItemProcesso\" para identificar a ordem do item. Com essa informação, deve-se verificar a quantidade registrada no processo e compará-la com a quantidade do mesmo produto no XML. Para localizar o item no XML, é possível buscar pela descrição do produto, que será a mesma tanto no processo quanto no XML.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53230,
    "customFieldValues": [
      {
        "value": "Valor da parcela diferente da informada no fechamento financeiro.",
        "customFieldId": 206842
      },
      {
        "value": "Valor informado da parcela não condiz com o apresentado antes de gerá-la",
        "customFieldId": 206843
      },
      {
        "value": "Verificamos que a divergência ocorreu por conta do acréscimo inserido no título de contas a receber, o valor de acréscimo não faz parte da parcela.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53503,
    "customFieldValues": [
      {
        "value": "Usuário informa que a base de cálculo do ICMS incorreta",
        "customFieldId": 206842
      },
      {
        "value": "A taxa estava incorreta devido a uma alteração manual na taxa moeda dentro do processo. ",
        "customFieldId": 206843
      },
      {
        "value": "Após alterar a taxa (a pedido da cliente) para o valor correto, a base de calculo ficou de acordo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53482,
    "customFieldValues": [
      {
        "value": "Alteração do numero do processo.",
        "customFieldId": 206842
      },
      {
        "value": "O motivo da causa foi devido a erros de digitação pelo usuário.",
        "customFieldId": 206843
      },
      {
        "value": "Realizar o cancelamento do processo e a abertura de um novo, para que seja criado com a numeração correta.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52273,
    "customFieldValues": [
      {
        "value": "Lentidão",
        "customFieldId": 206842
      },
      {
        "value": "Lentidão ao executar fluxo.",
        "customFieldId": 206843
      },
      {
        "value": "Atualização de versão.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53444,
    "customFieldValues": [
      {
        "value": "NOTA FISCAL REJEITADA - CÓDIGO 539 - STATUS Duplicidade de NF-e, com diferença na Chave de Acesso",
        "customFieldId": 206842
      },
      {
        "value": "No SEFAZ a numeração da Nota fiscal que está sendo enviada já está autorizada.  ",
        "customFieldId": 206843
      },
      {
        "value": "No SEFAZ a numeração da Nota fiscal que está sendo enviada já está autorizada.  ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53490,
    "customFieldValues": [
      {
        "value": "Como habilitar aba dentro do sistema?",
        "customFieldId": 206842
      },
      {
        "value": "A aba foi desabilitada sem querer por alguém que tem permissão para obrigar campos (Permissão alterável no cadastro do cliente).",
        "customFieldId": 206843
      },
      {
        "value": "Quando o usuário tem essa permissão, aparece uma bolinha azul em cima do campo, quando o azul está forte, é porque a aba está habilitada. Quando o azul está com uma cor mais fraca, é porque a aba está desabilitada. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53449,
    "customFieldValues": [
      {
        "value": "Pedido excluído do Narwal mas aparecendo no BI",
        "customFieldId": 206842
      },
      {
        "value": "Pedido foi cancelado e encerrado no Narwal, e está aparecendo no BI.",
        "customFieldId": 206843
      },
      {
        "value": "Feito a exclusão via banco para este pedido, liberado pela Camila Ribeiro.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53174,
    "customFieldValues": [
      {
        "value": "Dúvidas sobre o modulo Proposta comercial",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "N/A",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53423,
    "customFieldValues": [
      {
        "value": "Como é calculada a taxa moeda?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "Primeiro, divide-se o valor de venda em reais pelo valor da moeda correspondente (os dados estão no XML), soma a taxa de todas adições e divide pela quantidade total de adição.\n\n",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53308,
    "customFieldValues": [
      {
        "value": "Acesso a rotina LPCO",
        "customFieldId": 206842
      },
      {
        "value": "Cliente estava sem acesso a rotina LPCO, ",
        "customFieldId": 206843
      },
      {
        "value": "Fui em usuário verifiquei qual era o grupo , e coloquei a perissão",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53286,
    "customFieldValues": [
      {
        "value": "Duvida - Abertura Duimp",
        "customFieldId": 206842
      },
      {
        "value": "Consultor tentou criar uma DUIMP sem ter um processo, pela rotina \"Integrar DUIMP\"",
        "customFieldId": 206843
      },
      {
        "value": "Já temos a instrução da solução em https://portal.narwalsistemas.com.br/documentacao/narwal/novo-processo-importacao/duimp/material/",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53433,
    "customFieldValues": [
      {
        "value": "Valor da mercadoria só aparece em dólar nas informações complementares da DI.",
        "customFieldId": 206842
      },
      {
        "value": "Cliente imputou diretamente a sigla do dólar nas informações complementares",
        "customFieldId": 206843
      },
      {
        "value": "Opção correta seria utilizar a tag '{MOEDA.MERCADORIA.SIGLA}' na rotina 'Informações complementares SISCOMEX' ao invés de inputar diretamente a sigla do dólar nas informações complementares.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 53334,
    "customFieldValues": [
      {
        "value": "Pedido não integra Sênior -> Narwal",
        "customFieldId": 206842
      },
      {
        "value": "Alguns pedidos não estavam integrando do Sênior para o Narwal.",
        "customFieldId": 206843
      },
      {
        "value": "Foi identificado que quando o integrador buscava os pedidos mencionados, no log era retornado os seguintes erros: \n\n1° \"Inform NCM or HS Code\": Para esse caso, o produto foi cadastrado no Narwal, porém estava sem a informação do NCM preenchida.\n\n2° \"Informe a descrição da moeda para:\" Para esse caso, a chave que estava sendo enviada da moeda, não estava parametrizada dentro do Narwal, sendo necessário identificar com o cliente qual moeda se tratava para poder alterar do nosso lado.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 52680,
    "customFieldValues": [
      {
        "value": "BUG - Erro ao importar catálogo de produto",
        "customFieldId": 206842
      },
      {
        "value": "Alterações no cadastro de produtos entre versões. O método de importação do catálogo de produtos por planilha foi afetado.",
        "customFieldId": 206843
      },
      {
        "value": "Atualizar versão.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54563,
    "customFieldValues": [
      {
        "value": "Ao salvar NF está com a mensagem: O campo DescricaoCompletaDi deve ser uma cadeia de caracteres ou tipo de matriz com comprimento máximo de '500'",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida",
        "customFieldId": 206843
      },
      {
        "value": "No cadastro do produto o campo Descrição Completa Di deve estar limitado a 500 caracteres. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54598,
    "customFieldValues": [
      {
        "value": "Alíquotas PIS/COFINS NCMs",
        "customFieldId": 206842
      },
      {
        "value": "Incidente",
        "customFieldId": 206843
      },
      {
        "value": "O Narwal disponibiliza ferramenta para a atualização automática de NCMs, simplificando a gestão dos processos. No entanto, podem ocorrer falhas pontuais nesse processo. Por isso, recomendamos que, seja realizada a validação dos NCMs, garantindo que estejam devidamente atualizadas.\n\nCaso identifiquem alguma discrepância, a atualização pode ser feita manualmente. Para isso, basta editar o NCM e ajustar os percentuais conforme necessário.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 54824,
    "customFieldValues": [
      {
        "value": "Cliente gostaria de saber como que funciona a rotina de Calculo de armazenagem? ",
        "customFieldId": 206842
      },
      {
        "value": "Duvida ",
        "customFieldId": 206843
      },
      {
        "value": "Cliente nunca utilizou, dessa forma seguimos com a solicitação de treinamento ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55021,
    "customFieldValues": [
      {
        "value": "Por que está duplicando o ICMS?",
        "customFieldId": 206842
      },
      {
        "value": "Dúvida.",
        "customFieldId": 206843
      },
      {
        "value": "Uma das despesas foi inserida manualmente e a outra o Narwal calculou.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55396,
    "customFieldValues": [
      {
        "value": "PERGUNTA",
        "customFieldId": 206842
      },
      {
        "value": "CAUSA",
        "customFieldId": 206843
      },
      {
        "value": "SOLUCAO",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 55720,
    "customFieldValues": [
      {
        "value": "Onde ficam os acréscimos vindos da consulta SISCARGA?",
        "customFieldId": 206842
      },
      {
        "value": "Cliente deseja saber onde fica informado os acréscimos após aprovar a consulta SISCARGA no processo.",
        "customFieldId": 206843
      },
      {
        "value": "Os acréscimos ficam dentro da rotina 'Declaração importação' -> Atualizar taxas.\nObs: A aba 'SISCARGA/Frete' só aparecerá para os processos que contenham a consulta siscarga aprovada dentro do processo.",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 56172,
    "customFieldValues": [
      {
        "value": "Nota de nacionalização não estava trazendo a base de calculo do ICMS, quando o CST de diferimento? ",
        "customFieldId": 206842
      },
      {
        "value": "Erro do usuário ao configurar parametrização ",
        "customFieldId": 206843
      },
      {
        "value": "Foi orientado que ajustasse a parametrização informando na parte do icms para destacar a flag de Base de calculo destacada. \n\nNo valor total dos produtos, foi solicitado que alterasse a formula, pois estava divergente. ",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57031,
    "customFieldValues": [
      {
        "value": "Numeração ",
        "customFieldId": 206842
      }
    ]
  },
  {
    "id": 57289,
    "customFieldValues": [
      {
        "value": "como criar parametrização quando o ICMS possui um acréscimo de 40% ?",
        "customFieldId": 206842
      },
      {
        "value": "Duvida",
        "customFieldId": 206843
      },
      {
        "value": "Para que o valor seja somasse a base de ICMS, precisamos ajustar a fórmula na parametrização da nota fiscal. A fórmula deve incluir a seguinte informações para o cálculo da base de ICMS. \n\n((({valortotal}+{despesabasedeicms}+{ipi}+{pis}+{cofins}{ii})+(({valortotal}+{despesabasedeicms}+{ipi}+{pis}+{cofins}{ii})*0.40))*0.80",
        "customFieldId": 206844
      }
    ]
  },
  {
    "id": 57770,
    "customFieldValues": [
      {
        "value": "Inserção de pedido de compra atualiza se o pedido ja existe",
        "customFieldId": 206842
      },
      {
        "value": "O parceiro questionou se ao integrar uma planilha de pedido de compra com um pedido que ja existe se atualizaria o pedido do Narwal",
        "customFieldId": 206843
      },
      {
        "value": "o Modelo de Inserção de Pedido de compra, não atualiza os pedidos ja existentes, apenas cria novos pedidos.",
        "customFieldId": 206844
      }
    ]
  }
]

formatted_data = []

for item in all_data:
    campos = {cf["customFieldId"]: cf["value"] for cf in item.get("customFieldValues", [])}
    formatted_data.append({
        "id": item.get("id"),
        "pergunta": campos.get(206842, ""),
        "causa": campos.get(206843, ""),
        "solucao": campos.get(206844, "")
    })

# Salvar o novo formato
final_output_path = "faq.json"
with open(final_output_path, "w", encoding="utf-8") as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=2)

final_output_path