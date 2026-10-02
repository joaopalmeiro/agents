import { Agent } from "@mastra/core/agent";

export const ptProofreader = new Agent({
  id: "pt-proofreader",
  instructions: "You are a helpful assistant.",
  model: "openai/gpt-5.6-sol",
  name: "PT Proofreader",
});
