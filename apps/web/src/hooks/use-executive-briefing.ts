"use client";

import { useQuery } from "@tanstack/react-query";

import { api } from "@/lib/api";
import type { ExecutiveBriefing } from "@/types/copilot";


export function useExecutiveBriefing() {
  return useQuery<ExecutiveBriefing>({
    queryKey: ["executive-briefing"],

    queryFn: async () => {
      const response = await api.get("/copilot/briefing");

      return response.data;
    },
  });
}
