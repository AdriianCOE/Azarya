# Sistema: Doutrina de Expansão Gydiana

*Ver `00_CANON_RULES.md`, `03_GEOPOLITICAL_BLOCKS.md` e `04_CONTENT_IMPLEMENTATION_MATRIX.md`.*

## Conceito [CANON]

O Gydian Empire busca hegemonia continental e posteriormente global.

Sua preferência é obter território, bases, influência ou submissão **sem iniciar uma guerra aberta**, usando:

- empréstimos;
- armamentos;
- assessores;
- influência política;
- golpes;
- garantias;
- tratados;
- plebiscitos;
- controle de ferrovias, alfândegas, portos e defesa.

A propaganda apresenta esse processo como integração, proteção, pacificação ou correção territorial.

Os adversários podem chamá-lo de:

> **Anexações de Veludo**

Esse nome permanece proposta até aprovação formal.

## Arquitetura recomendada [PROPOSTA TÉCNICA]

Não usar um único sistema totalmente genérico capaz de anexar qualquer país automaticamente.

Isso deixaria:

- triggers difíceis de ler;
- efeitos opacos;
- IA imprevisível;
- localisation excessivamente genérica;
- maior risco de transferir estados errados.

Também não duplicar toda a lógica à mão em cada país.

A solução recomendada é **híbrida**:

### Núcleo compartilhado

Scripted effects e triggers reutilizáveis para:

- aumentar ou reduzir influência;
- registrar dívida;
- verificar dependência;
- transferir estado com segurança;
- transformar país em fantoche;
- remover garantia antes de guerra;
- disparar notícia depois do efeito;
- impedir repetição;
- aplicar reação internacional.

### Cadeias específicas

Cada alvo recebe:

- eventos próprios;
- localisation própria;
- exigências próprias;
- alternativas próprias;
- consequências próprias.

## Variáveis propostas

Variáveis separadas por alvo:

```text
az_gye_influence_fvi
az_gye_influence_duh
az_gye_influence_atv
az_gye_influence_koz
az_gye_influence_nir
az_gye_influence_upg
az_gye_influence_thk
az_gye_influence_sit
```

Faixa recomendada: `0–100`, sempre limitada por scripted effect.

Faixas conceituais:

| Nível | Situação |
|---:|---|
| 0–24 | influência limitada |
| 25–49 | dependência inicial |
| 50–74 | alinhamento profundo |
| 75–99 | soberania comprometida |
| 100 | integração, submissão ou crise final disponível |

Os limiares podem variar por país. Não usar a mesma consequência automática para todos.

## Reação continental [PROPOSTA]

Adicionar uma variável global ou nacional gydiana de **alarme continental**:

```text
az_gye_continental_alarm
```

Ela aumenta com:

- anexação de Fervonia;
- submissão de Astravern;
- cessão de Karleston;
- cessão de Celest;
- guerra de Durnstad;
- revelação dos crimes em Durnstad;
- tentativa de absorção de Sithius;
- pressão simultânea sobre Thiryn e Gengen.

Ela pode:

- acelerar garantias anti-gydianas;
- aumentar apoio a Helvaria;
- tornar países pequenos mais propensos a recusar;
- antecipar a Crise de Astravern;
- prejudicar relações diplomáticas;
- desbloquear coalizões defensivas.

Não deve iniciar automaticamente a Grande Guerra antes de 1927 sem uma cadeia específica.

## Casos nacionais

### Zauern

Gydian apoia a guerra contra Torronese com:

- equipamentos;
- crédito;
- trabalhadores;
- assessores;
- logística.

Em troca, Zauern promete Karleston (361).

A transferência só ocorre se:

- Zauern aceitar o acordo;
- Karleston ainda estiver sob controle adequado;
- a condição de guerra prevista for cumprida;
- a transferência ainda não tiver sido executada.

### Nirisia

Gydian oferece eliminar ou neutralizar Estados-bandidos em troca de Celest (462).

Opções:

- aceitar;
- recusar;
- renegociar.

A cadeia depende da identificação definitiva das tags e estados bandidos.

### Fervonia

Progressão histórica:

1. garantia;
2. crédito;
3. conselheiros;
4. controle alfandegário ou defensivo;
5. união política, fantoche ou integração.

A rota histórica evita guerra ampla.

### Astravern

Gydian suborna a monarquia e protege o governo contra opositores.

Progressão:

1. empréstimos;
2. apoio ao regime;
3. presença militar;
4. alinhamento externo;
5. fantoche ou aliado subordinado.

Astravern torna-se peça central do estopim de 1927.

### Sithius

Gydian usa:

- dívida;
- compra de concessões;
- arrendamento de portos;
- modernização naval;
- promessa de recuperar antigas possessões.

Resultados:

- aliado menor histórico;
- resistência;
- anexação;
- restauração independente.

### Thiryn e Gengen

Gydian joga com os dois lados:

- oferece proteção a Gengen;
- vende armas e exige bases;
- sugere a Thiryn que os territórios perdidos poderão ser devolvidos;
- impede reconciliação enquanto ambos forem úteis.

### Junta Helvariana

Recebe armas, crédito e assessores durante a Guerra das Três Bandeiras.

Gydian espera criar um Estado reunificado subordinado, mas pode acabar fortalecendo um rival.

## Durnstad — exceção armada [CANON]

Durnstad é a única anexação gydiana anterior à Grande Guerra que exige uma campanha militar real.

A garantia inicial é parte da armadilha:

1. Gydian protege Durnstad;
2. cria dependência;
3. exige controle político e militar;
4. Durnstad tenta romper;
5. Gydian acusa o governo de violar o acordo;
6. remove ou trai a garantia;
7. invade;
8. ocupa e encobre os crimes.

A ocupação inclui genocídio ocultado por:

- censura;
- deportações;
- desaparecimentos;
- destruição de registros;
- falsificação de relatórios;
- propaganda de “pacificação”.

Não produzir descrições gráficas.

## Contabilidade de concessões

Cada ganho deve ser registrado separadamente:

```text
az_koz_karleston_ceded
az_nir_celest_ceded
az_fvi_integration_completed
az_atv_subordination_completed
az_duh_occupation_completed
az_sit_concession_<id>
```

Não usar apenas uma flag genérica como `GYE_expansion_complete`.

## Regra de notícia

A ordem correta é:

1. aplicar efeito;
2. registrar flag;
3. recalcular influência/alarme;
4. disparar `az_news`;
5. habilitar reações estrangeiras.

## Falhas e alternativas

Toda cadeia precisa funcionar quando:

- o alvo foi anexado por terceiro;
- Gydian mudou de governo;
- o alvo recusou;
- a guerra regional terminou de modo alternativo;
- o estado prometido mudou de dono;
- a Grande Guerra começou antes da cadeia terminar.

## Testes mínimos

- nenhuma anexação duplicada;
- nenhuma transferência de capital não planejada;
- garantia removida antes da guerra de Durnstad;
- influência limitada a 0–100;
- IA histórica não força escolha do jogador;
- save/load preserva estágio;
- recusa não trava 1927;
- notícias não controlam efeitos;
- tags mortas possuem fallback.
