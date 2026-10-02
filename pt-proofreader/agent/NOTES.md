# Notes

- https://mastra.ai/reference/file-based-agents/config
- https://mastra.ai/docs/agents/overview#expand-your-agent
- https://mastra.ai/docs/harness/durable-agents
- https://github.com/mastra-ai/mastra/blob/9a3513c18ec2d8b12174620a2a6db968760b9141/packages/create-mastra/package.json
- https://huggingface.co/amalia-llm/AMALIA-9B-0626-DPO/blob/c4614b9b5c7b4fe303fa20902e692fc7dface640/chat_template.jinja: "O teu nome é Amália, e és um modelo avançado de linguagem útil. Responde sempre na língua do utilizador, a menos que sejas instruído em contrário, e lembra-te que a tua língua principal é o português europeu."
- https://letraaletra.pt/: "Além da revisão da ortografia, gramática, clareza e coerência de qualquer texto escrito em português, dependendo do tipo de documento ou da necessidade, podem ser revistos outros aspectos."
- https://www.apportugal.com/servicos/revisao-de-textos/: "A AP|PORTUGAL coloca à sua disposição o serviço de revisão de textos nas mais variadas línguas. A nossa equipa de revisores especializados dispõe de ferramentas e metodologias, que permitem uma revisão eficaz e sem erros, tanto a nível gramatical, sintática, semântica e terminológica, ortográfica e da pontuação, assim como da formatação e paginação."
- https://pt.wikipedia.org/wiki/Revisor_de_textos
- https://mastra.ai/models#select-the-openai-responses-api
- https://mastra.ai/models#example-lmstudio: `id: "lmstudio/qwen/qwen3-30b-a3b-2507"`
- https://docs.vllm.ai/projects/vllm-omni/en/latest/serving/chat_completions_api/: `/v1/chat/completions`
- https://languagetool.org/pt/verificacao-ortografica-portugues: "Cole aqui seu texto...ou verifique esta texto, afim de revelar alguns dos dos problemas que o LanguageTool consegue detectar. Isto tal vez permita corrigir os seus erro. Nós prometo ajudá-lo. para testar a grafia e as regrs do antigo) Acordo Ortográfico,, verifique o mesmo texto mesmo texto em Português de Angola ou Português do Moçambique e faça a analise dos resultados.. Nossa equipe anuncia a versão 4.5, que será lançada sexta-feira, 26 de março de 2019."
- https://amalia-llm.github.io/intro.html#servir-uma-api-localmente: "Para servir localmente o AMALIA, o hardware mínimo é de uma GPU NVIDIA A100 40GB, sendo que para aplicações com vários clientes é recomendado um mínimo de 4 destas GPUs. O software recomendado é o vLLM instalado em ambiente conda com Python 3.12+:"
- https://aclanthology.org/2026.propor-1.38.pdf: "Expanding multilingual capabilities and introducing tool-calling functionality are other priorities for future iterations."

## Commands

```bash
npm install @mastra/core && npm install -D mastra
```

```bash
npm create mastra@latest -- --no-install
```
