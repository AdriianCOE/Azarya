# Revisão do Pack 1 — Documentação-base

## Veredito

O pack estava útil, mas misturava três camadas:

1. snapshot técnico antigo;
2. decisões canônicas mais recentes;
3. propostas ainda não aprovadas.

Os arquivos corrigidos separam essas camadas e atualizam o núcleo documental para o canon discutido até 2026-07-17.

## Correções principais

- Durnstad (`DUH`) e Durtenbach (`DTB`) foram desambiguados.
- A garantia gydiana a Durnstad deixou de ser tratada como contradição.
- A Crise de Astravern em 1927 foi registrada como estopim histórico da Grande Guerra.
- A vitória histórica de Durtenbach e a Helvaria reunificada foram consolidadas.
- Gengen foi registrado como inclinado ao bloco gydiano.
- Sithius recebeu seu papel histórico de aliado oportunista e sua decadência territorial foi explicada.
- Orvena, Karyō e Liangor passaram de PROPOSTA para CANON/IMPLEMENTAÇÃO EM ANDAMENTO.
- O terremoto deixou de afirmar Eldoria como epicentro geológico sem prova direta.
- Bases aéreas e navais foram separadas de força aérea e marinha.
- Rankings militares foram corrigidos.
- Declarações `declare_war_on` passaram a exigir validação runtime antes de serem chamadas de guerras ativas.
- A contradição entre notícia própria de Great Thiryn e `news.59` foi registrada para revalidação.
- O namespace genérico `news` foi rejeitado para conteúdo novo; foi proposto `az_news`.
- IDs, flags, variáveis, decisões e localisation receberam um padrão único.
- A matriz ganhou regras de idempotência, save/load e fallback para tags anexadas.
- Os números 57 tags/506 estados foram marcados como snapshot anterior à expansão oriental.

## Arquivos

- `AZARYA_WORLD_CONTEXT_AUDIT.md` — snapshot histórico corrigido.
- `00_CANON_RULES.md` — fonte principal de regras.
- `01_WORLD_OVERVIEW.md` — visão geopolítica atual.
- `02_MASTER_TIMELINE.md` — timeline consolidada até a guerra mundial.
- `03_GEOPOLITICAL_BLOCKS.md` — blocos históricos e alternativas.
- `04_CONTENT_IMPLEMENTATION_MATRIX.md` — ordem e dependências técnicas.
- `05_ID_AND_FLAG_REGISTRY.md` — padrão técnico proposto.

## Pendências que não podem ser resolvidas só com este pack

- confirmar contagem atual de tags e estados após ORV/KAR/LIA;
- validar se Eldoria é explicitamente chamada de epicentro;
- confirmar o wiring atual de Great Thiryn e remover `news.59` se ainda existir;
- executar runtime das guerras KOZ→TOL e ELD/GET→SVD;
- identificar definitivamente os Estados-bandidos ligados à oferta de Nirisia;
- confirmar nomes finais dos continentes e penínsulas;
- validar tags, capitais e fronteiras orientais no repositório atual.
