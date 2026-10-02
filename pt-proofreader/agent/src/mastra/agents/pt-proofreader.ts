import { Agent } from "@mastra/core/agent";

export const ptProofreader = new Agent({
  id: "pt-proofreader",
  instructions: "És um revisor de texto em português europeu. Responde apenas com o texto revisto.",
  model: "openai/gpt-5.6-sol",
  name: "PT Proofreader",
});
