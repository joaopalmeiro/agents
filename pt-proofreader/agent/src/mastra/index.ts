import { Mastra } from "@mastra/core";

import { ptProofreader } from "./agents/pt-proofreader";

export const mastra = new Mastra({
  agents: { ptProofreader },
});
