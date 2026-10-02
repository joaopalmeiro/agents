import { Agent } from "@mastra/core/agent";

export const ptProofreader = new Agent({
  id: "pt-proofreader",
  instructions: "És um revisor de texto em português europeu. Responde apenas com o texto revisto.",
  model: {
    api: "chat",
    apiKey: process.env.BEARER_TOKEN,
    id: "vllm/amalia-llm/AMALIA-9B-0626-DPO",
    url: process.env.AMALIA_ENDPOINT,
  },
  name: "PT Proofreader",
});
