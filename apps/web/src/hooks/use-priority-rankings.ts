"use client";

import { useQuery } from "@tanstack/react-query";

import { api } from "@/lib/api";
import type { PriorityItem } from "@/types/priority";


export function usePriorityRankings() {
  return useQuery<PriorityItem[]>({
    queryKey: ["priority-rankings"],

    queryFn: async () => {
      const response = await api.get("/priority/rankings");

      return response.data;
    },
  });
}
