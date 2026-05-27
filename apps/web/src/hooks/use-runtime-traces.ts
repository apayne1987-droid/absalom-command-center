"use client";

import { useQuery } from "@tanstack/react-query";

import { api } from "@/lib/api";

import type { RuntimeTrace } from "@/types/runtime-trace";


export function useRuntimeTraces() {

  return useQuery<RuntimeTrace[]>({
    queryKey: ["runtime-traces"],

    queryFn: async () => {

      const response = await api.get(
        "/autonomy/traces"
      );

      return response.data;
    },

    refetchInterval: 4000,
  });
}
