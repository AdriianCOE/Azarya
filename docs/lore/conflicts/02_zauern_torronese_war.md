# Guerra Zauern–Torronese

*Ver `00_CANON_RULES.md`, `02_MASTER_TIMELINE.md` e `gydian_expansion_doctrine.md`.*

## Resumo [CANON]

Gydian apoia Zauern (`KOZ`) contra a Liga Torronese (`TOL`) com:

- equipamentos;
- armas;
- crédito;
- trabalhadores;
- assessores;
- inteligência;
- logística.

Em troca, Zauern promete entregar **Karleston, estado 361**, a Gydian.

A guerra permite que Gydian obtenha território por meio de um conflito travado por outro país.

## Estado técnico atual [IMPLEMENTADO PARCIAL]

Foi encontrado em:

```text
history/countries/KOZ - Kingdom of Zauern.txt
```

um efeito:

```text
declare_war_on = {
    target = TOL
    type = annex_everything
}
```

Karleston (361) pertence tecnicamente a KOZ no ponto de partida auditado.

### Limite da confirmação

A presença de `declare_war_on` no history indica intenção de começar a guerra no cenário, mas ainda precisa ser validada em runtime:

- a guerra inicia corretamente em 1º de janeiro?
- o efeito é executado na ordem esperada?
- existe erro de setup?
- a guerra total é realmente o tipo de conflito desejado?
- a IA consegue sustentar a guerra?

Portanto, não afirmar que a mecânica está concluída.

## Cronologia

O canon ainda não fixou com absoluta precisão se a guerra deve:

- já existir em 1º de janeiro de 1924;
- começar durante os primeiros meses;
- começar somente depois de uma oferta gydiana.

A implementação atual favorece guerra ativa desde o início. A decisão narrativa deve ser confirmada antes de mover ou remover o `declare_war_on`.

## Acordo de Karleston

Antes ou durante a guerra, Gydian e Zauern firmam um acordo secreto ou reservado.

### Obrigações de Gydian

- fornecer material;
- ampliar capacidade logística;
- reparar ou construir ferrovias;
- apoiar crédito de guerra;
- treinar oficiais;
- reconhecer objetivos de Zauern.

### Obrigações de Zauern

- entregar Karleston (361);
- alinhar compras militares;
- conceder acesso ferroviário;
- aproximar política externa de Gydian;
- aceitar futura pressão para entrar na facção.

## Rota histórica [CANON]

1. Zauern recebe apoio gydiano.
2. Zauern vence ou obtém o resultado necessário.
3. Karleston é cedida a Gydian.
4. Zauern torna-se econômica e militarmente dependente.
5. posteriormente pode entrar no bloco gydiano sob pressão.

A cessão deve ser apresentada como acordo legal, não anexação aberta.

## Resultados alternativos

### Torronese resiste ou vence

Possíveis consequências:

- Gydian perde prestígio;
- Zauern sofre crise política;
- a cessão de Karleston não ocorre;
- Gydian pode exigir compensação financeira;
- Torronese aproxima-se de Helvaria ou de outra potência;
- a guerra pode terminar em paz limitada.

Os efeitos finais permanecem TBD.

### Zauern vence, mas recusa a cessão

- ruptura com Gydian;
- ultimato;
- embargo;
- golpe pró-Gydian;
- pressão para entrega posterior.

### Gydian retira apoio

- queda do desempenho militar de Zauern;
- perda de influência;
- busca de patrocinador alternativo.

## Implementação recomendada

A transferência de Karleston deve ocorrer por evento ou scripted effect seguro após a condição de vitória.

Não colocar a transferência dentro de uma notícia.

### Condições mínimas

- KOZ aceitou o acordo;
- estado 361 ainda existe e possui owner válido;
- resultado militar exigido foi alcançado;
- Karleston ainda não foi cedida;
- GYE existe;
- a Grande Guerra não tornou o acordo impossível.

## Flags conceituais

```text
az_koz_gydian_support_accepted
az_koz_karleston_promised
az_koz_karleston_ceded
az_koz_joined_gydian_sphere
```

## Testes obrigatórios

- validar guerra no boot;
- impedir cessão duplicada;
- não transferir Karleston se TOL vencer;
- comportamento se KOZ for anexado;
- comportamento se GYE não existir;
- save/load antes e depois da paz;
- confirmar que `annex_everything` não produz resultado narrativamente inadequado;
- garantir que Karleston não seja capital ou estado essencial cuja transferência quebre KOZ.
