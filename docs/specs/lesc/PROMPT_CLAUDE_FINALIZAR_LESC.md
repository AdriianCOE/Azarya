# Prompt para Claude — finalizar Lesc/CZL no repositório Azarya

Você está trabalhando no repositório do mod total conversion **Azarya** para Hearts of Iron IV. Sua tarefa é transformar a nova árvore nacional de Lesc em conteúdo jogável completo, coerente e auditável, **sem inventar relações que contradigam o cânone atual**.

## Arquivo de entrada obrigatório

Use como especificação principal:

```text
LSC_Lesc_focus_tree_reformulada.txt
```

A árvore contém focos, coordenadas, flags, variáveis, ideias e eventos que formam um contrato de implementação. Você pode corrigir sintaxe, balanceamento e integração, mas não deve descaracterizar a estrutura narrativa sem explicar a necessidade.

## Cânone obrigatório

- A tag real do país é **CZL**. O namespace `LSC_` pode ser mantido para focos, eventos, ideias, variáveis e decisões porque já aparece no esqueleto original. Não renomeie a tag do país.
- O cenário único começa em **1º de janeiro de 1924**.
- O Czariado de Lesc nasceu quando famílias oligárquicas ricas do sul financiaram e conduziram a conquista do norte empobrecido.
- O sul concentra indústria, portos, burocracia, academias militares e cultura dominante.
- O norte é administrado como território colonial: repressão, recrutamento forçado e extração de recursos.
- O governante inicial é **Czar Viktor IV Vorenkov**.
- A modernização militar de Viktor segue uma doutrina inspirada em **Gydian**, sem tornar Lesc automaticamente fantoche ou principal rival de Gydian.
- Gydian busca influência por empréstimos, assessores, tratados, armas, garantias e golpes, preferindo pressão indireta à guerra aberta.
- Lesc pode sofrer guerra civil, mas não existe vencedor histórico único fixado.
- Os três futuros centrais são:
  - **Kael Vorenkov**: continuidade e radicalização imperial; Coroa, Exército e oligarcas do sul; autoritarismo expansionista.
  - **Álvaro Vorenkov**: revolta do norte, fim da administração militar e solução revolucionária/federal; não deve virar apenas “comunismo genérico”.
  - **Selene Vorenkov**, a **Princesa de Mármore**: equilíbrio ambíguo entre facções, intriga palaciana, legitimidade própria e possibilidade de monarquia reformada ou autocracia silenciosa.
- Lesc e Thiryn não possuem rivalidade, aliança ou passado compartilhado definidos. Não crie conteúdo bilateral entre CZL e THK.
- Uma Helvaria reunificada é o principal rival continental anti-gydiano futuro. Lesc pode tratá-la como contrapeso, mas não deve substituí-la nesse papel.
- O país possui 14 estados, capital no estado 335, grande exército e a maior contagem de navios do cenário atual. Preserve essa identidade militar e naval.

## Antes de editar

1. Audite o repositório e descubra o estado real de:
   - `common/national_focus/Lesc.txt`
   - `history/countries/CZL - Czariado de Lesc.txt`
   - arquivos de personagens de CZL
   - ideias atuais de CZL
   - eventos e decisões existentes de Lesc
   - localisation relacionada a `CZL_` e `LSC_`
   - sprites/ícones disponíveis
   - estados pertencentes a CZL, distinguindo norte e sul por localização real no mapa
2. Confirme se o arquivo usa replace paths relevantes. Não reintroduza conteúdo vanilla órfão.
3. Preserve conteúdo autoral válido. Remova o esqueleto antigo somente quando a substituição estiver completa.
4. Não faça commit, push, merge ou deploy.

## Arquitetura obrigatória

Implemente **uma única árvore `LSC_focus` atribuída à tag CZL**. Não use três árvores carregadas dinamicamente. Motivos:

- reduz dependências cruzadas frágeis;
- facilita auditoria de IDs e coordenadas;
- mantém os três caminhos visíveis e mutuamente exclusivos;
- evita perda de focos concluídos em trocas de árvore.

Respeite a semântica de pré-requisitos do HOI4:

- blocos `prerequisite` separados = requisitos cumulativos;
- vários `focus = ...` dentro do mesmo bloco = alternativas;
- `mutually_exclusive` deve listar IDs de focos, nunca `mutually_exclusive = yes`.

## Sistemas a implementar

### 1. Crise imperial pré-guerra

Crie uma categoria de decisões para a **Fratura Imperial**, ativada pelo primeiro foco. Ela deve exibir e alterar, de forma legível:

- `LSC_northern_unrest`
- `LSC_army_loyalty`
- `LSC_oligarch_influence`
- `LSC_gydian_influence`
- `LSC_selene_legitimacy`
- `LSC_revolutionary_strength`

Use valores entre 0 e 100 e sempre aplique clamp. Adicione decisões com custos, cooldowns e consequências reais; nada de botões gratuitos repetíveis.

Exemplos de decisões:

- reforçar guarnições do norte;
- negociar com industriais do sul;
- substituir oficiais suspeitos;
- aceitar assessores gydianos;
- censurar jornais do norte;
- financiar redes de auxílio de Selene;
- esconder armas nos vales para Álvaro;
- organizar ligas de veteranos para Kael.

Cada decisão deve mover pelo menos duas variáveis, criando trade-offs.

### 2. Sucessão de Viktor IV

Crie uma cadeia de eventos `LSC_succession` que apresente:

- declínio físico/político de Viktor IV;
- disputa entre os três filhos;
- reação do Exército, oligarcas, burocratas do sul e províncias do norte;
- influência indireta gydiana;
- escolha do jogador representada pelos três focos mutuamente exclusivos.

Viktor não precisa morrer obrigatoriamente da mesma forma em todas as rotas. Evite repetir “um filho mata o pai” três vezes. Dê identidades distintas:

- Kael pode fabricar uma crise, prender ou eliminar Viktor e incriminar Álvaro;
- Álvaro pode transformar uma repressão ou massacre em levante nacional;
- Selene pode forçar abdicação, regência ou acordo palaciano, com risco de guerra caso sua legitimidade seja baixa.

### 3. Guerra civil dinâmica

Implemente os eventos `LSC_civil_war.10`, `.20` e `.30` usando as variáveis anteriores.

Requisitos:

- a força territorial, unidades, generais, equipamentos e ideias de cada lado devem depender das preparações feitas;
- norte e sul devem usar estados reais de CZL, auditados no mapa;
- evite hardcode de províncias sem confirmar propriedade e localização;
- crie tags dinâmicas ou países de guerra civil somente se necessário e de acordo com os padrões existentes no mod;
- não duplique personagens entre lados incompatíveis;
- use OOBs válidos e templates existentes;
- não crie divisões com templates inexistentes;
- a guerra precisa ter mecanismo anti-softlock e conclusão confiável;
- ao terminar, defina exatamente uma flag de vitória: `LSC_kael_victory`, `LSC_selene_victory` ou `LSC_alvaro_victory`;
- limpe flags temporárias, decisões da crise e ideias de guerra;
- trate capitulação, vitória por anexação e casos em que um lado desapareça inesperadamente.

A rota de Selene deve poder evitar uma guerra civil total apenas quando legitimidade, estabilidade e apoio institucional forem suficientemente altos. Caso contrário, ela enfrenta guerra curta, golpe ou conflito de três lados. Não transforme essa rota em vitória gratuita.

### 4. Personagens

Audite personagens existentes e implemente, no mínimo:

- Viktor IV Vorenkov — líder inicial;
- Kael Vorenkov — líder político e possível comandante;
- Álvaro Vorenkov — líder revolucionário;
- Selene Vorenkov — líder política, Princesa de Mármore;
- 2 oficiais do alto comando ligados à doutrina gydiana;
- 2 oligarcas/industriais do sul;
- 2 lideranças civis ou militares do norte;
- 1 diplomata ou assessor gydiano em Lesc;
- 1 figura burocrática/palaciana ligada a Selene.

Novos personagens secundários podem receber nomes originais, mas devem ter:

- região/facção de origem;
- objetivo político;
- lealdades e rivalidades;
- papel jogável claro;
- traços balanceados;
- disponibilidade condicional por rota;
- destino coerente durante a guerra civil.

Não reutilize nomes vanilla nem personagens de outros países de Azarya.

### 5. Ideias nacionais e dynamic modifiers

Implemente todos os IDs de ideias referenciados pela árvore. Consolide ideias redundantes e prefira modificadores dinâmicos para sistemas graduais.

Princípios de balanceamento:

- o norte deve produzir recursos e homens, mas pagar o custo da exploração;
- o sul deve concentrar indústria e poder político, mas depender de estabilidade e mão de obra do norte;
- Kael recebe mobilização, indústria militar e comando, pagando com resistência, estabilidade e dependência oligárquica;
- Álvaro recebe estabilidade de longo prazo, manpower e integração do norte, pagando com ruptura industrial, expurgos ou reconstrução lenta;
- Selene recebe flexibilidade, legitimidade e diplomacia, mas precisa equilibrar facções e não deve superar as outras rotas em tudo;
- influência gydiana alta deve conceder benefícios militares/econômicos acompanhados de autonomia reduzida, obrigações ou eventos de pressão;
- não conceda fábricas, slots e recursos sem verificar o tamanho real da economia de CZL.

### 6. Pós-guerra e decisões de integração

Crie categorias pós-guerra para:

- desmobilização e veteranos;
- reconstrução de ferrovias entre norte e sul;
- julgamento, cooptação ou preservação dos oligarcas;
- integração/autonomia das províncias do norte;
- reforma do corpo de oficiais;
- remoção gradual das penalidades da guerra;
- reconstrução da frota e dos estaleiros.

Use missões temporizadas para evitar que o jogador remova todas as penalidades instantaneamente.

### 7. Política externa

Implemente a cadeia `LSC_foreign` sem inventar relações com THK.

Rotas:

- Kael pode aceitar missão gydiana ou tentar criar uma via imperial independente;
- Selene pode praticar diplomacia de equilíbrio e tratar Helvaria como contrapeso futuro;
- Álvaro pode apoiar movimentos anticoloniais e redes revolucionárias, sem automaticamente dominar países estrangeiros;
- influência gydiana deve reagir às escolhas internas de Lesc.

Não crie facção global ou guerras gratuitas nesta rodada. Foque em opiniões, acordos, assessores, comércio, garantias condicionais, decisões e preparação futura.

### 8. Localisation e narrativa

Crie localisation completa em inglês para:

- todos os focos;
- descrições de foco;
- tooltips;
- ideias;
- decisões;
- missões;
- eventos e opções;
- personagens e traços;
- nomes de países de guerra civil, se houver.

Tom:

- início do século XX;
- linguagem imperial, burocrática e militar;
- contraste entre riqueza meridional e exploração setentrional;
- sem referências a países reais;
- sem texto genérico de “árvore comunista/fascista”; cada descrição deve falar de Lesc.

As opções de evento devem mostrar consequências previsíveis sem revelar números secretos desnecessários.

### 9. IA

Implemente IA funcional para os três caminhos, sem vencedor canônico obrigatório.

- use pesos iniciais próximos, ajustados por estabilidade, apoio de guerra, popularidade ideológica e estado das variáveis;
- a IA deve usar as decisões de preparação;
- evite que selecione decisões contraditórias com sua rota;
- durante a guerra civil, defina prioridades defensivas/ofensivas razoáveis;
- após a guerra, priorize remoção de penalidades antes de política externa ambiciosa.

### 10. Ícones e assets

- Reutilize apenas ícones já existentes e semanticamente adequados como fallback.
- Não copie assets de outros mods.
- Liste os focos/personagens que precisam de arte original futura.
- Não bloqueie a implementação por falta de portrait: use fallback válido e documente.

## Validação obrigatória

Execute uma auditoria estática antes de testar:

- chaves balanceadas;
- IDs de foco únicos;
- zero prerequisite órfão;
- zero mutually exclusive órfão;
- zero colisão de coordenadas;
- nenhuma dependência posicionada acima do pai;
- todas as ideias referenciadas existem;
- todos os eventos referenciados existem;
- todas as decisões e categorias referenciadas existem;
- todos os personagens usados existem;
- todos os estados e tags usados existem;
- nenhum template de divisão inexistente;
- localisation para cada chave visível;
- ausência de referências vanilla indevidas.

Depois rode, na ordem disponível no ambiente:

1. parser/validator local do mod;
2. inicialização do jogo no cenário de 1924 com CZL;
3. inspeção de `error.log`, `game.log` e `setup.log`;
4. `Focus.AutoComplete` e `Focus.NoChecks` apenas para smoke test de cada ramo;
5. uma simulação curta de cada guerra civil;
6. teste de conclusão e desbloqueio dos focos pós-guerra;
7. teste da IA por pelo menos uma rota completa, quando viável.

Não declare sucesso apenas porque o arquivo faz parse. Diferencie:

- validação estática;
- carregamento sem erro;
- fluxo jogável;
- balanceamento ainda não comprovado.

## Entregáveis

Ao terminar, forneça:

1. resumo da lore implementada;
2. lista de arquivos criados/alterados;
3. tabela dos três caminhos e suas mecânicas;
4. personagens criados e seus papéis;
5. decisões/eventos implementados;
6. resultados de cada validação/teste;
7. erros ou bloqueadores restantes;
8. lista de assets originais ainda necessários;
9. diff resumido, sem colar arquivos gigantes completos;
10. confirmação explícita de que não houve commit, push, merge ou deploy.
