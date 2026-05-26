"use client";

import { Brain, Sparkles } from "lucide-react";

import { useExecutiveBriefing } from "@/hooks/use-executive-briefing";


export function ExecutiveCopilotPanel() {
  const { data, isLoading } = useExecutiveBriefing();

  return (
    <div className="bg-[#111113] border border-zinc-900 rounded-[32px] p-8 overflow-hidden relative">
      <div className="absolute inset-0 bg-gradient-to-br from-white/[0.03] via-transparent to-transparent pointer-events-none" />

      <div className="relative z-10">
        <div className="flex items-center justify-between mb-8">
          <div>
            <div className="text-xs uppercase tracking-[0.3em] text-zinc-500 mb-3">
              AI Executive Copilot
            </div>

            <h3 className="text-3xl font-semibold tracking-tight">
              Operational Briefing
            </h3>
          </div>

          <div className="h-14 w-14 rounded-2xl bg-white text-black flex items-center justify-center shadow-2xl">
            <Brain size={24} />
          </div>
        </div>

        {isLoading ? (
          <div className="space-y-4 animate-pulse">
            <div className="h-4 bg-zinc-800 rounded w-full" />
            <div className="h-4 bg-zinc-800 rounded w-5/6" />
            <div className="h-4 bg-zinc-800 rounded w-4/6" />
          </div>
        ) : (
          <div className="space-y-6">
            <div className="flex items-center gap-2 text-sm text-emerald-400">
              <Sparkles size={16} />
              AI operational analysis active
            </div>

            <div className="text-zinc-300 leading-8 text-[15px] whitespace-pre-wrap">
              {data?.summary}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
