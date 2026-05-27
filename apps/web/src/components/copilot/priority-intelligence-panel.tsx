"use client";

import { ArrowUpRight, BrainCircuit } from "lucide-react";

import { usePriorityRankings } from "@/hooks/use-priority-rankings";


export function PriorityIntelligencePanel() {

  const { data, isLoading } = usePriorityRankings();

  return (
    <div className="bg-[#111113] border border-zinc-900 rounded-[32px] p-8 mt-8">

      <div className="flex items-center justify-between mb-8">

        <div>
          <div className="text-xs uppercase tracking-[0.3em] text-zinc-500 mb-3">
            Priority Intelligence Engine
          </div>

          <h3 className="text-3xl font-semibold tracking-tight">
            Strategic Priority Rankings
          </h3>
        </div>

        <div className="h-14 w-14 rounded-2xl bg-white text-black flex items-center justify-center">
          <BrainCircuit size={24} />
        </div>
      </div>

      {isLoading ? (

        <div className="space-y-4 animate-pulse">
          <div className="h-4 bg-zinc-800 rounded w-full" />
          <div className="h-4 bg-zinc-800 rounded w-5/6" />
          <div className="h-4 bg-zinc-800 rounded w-4/6" />
        </div>

      ) : (

        <div className="space-y-4">

          {data?.map((item, index) => (

            <div
              key={item.title}
              className="bg-zinc-950/70 border border-zinc-900 rounded-2xl p-5 flex items-center justify-between"
            >

              <div>

                <div className="flex items-center gap-3 mb-2">

                  <div className="h-8 w-8 rounded-full bg-white text-black flex items-center justify-center text-sm font-semibold">
                    {index + 1}
                  </div>

                  <div className="text-lg font-medium text-white">
                    {item.title}
                  </div>

                </div>

                <div className="flex items-center gap-6 text-sm text-zinc-500">

                  <span>ROI: {item.roi_score}</span>

                  <span>Leverage: {item.leverage_score}</span>

                  <span>Automation: {item.automation_score}</span>

                  <span>Alignment: {item.strategic_alignment_score}</span>

                  <span>Difficulty: {item.difficulty_score}</span>

                </div>

              </div>

              <div className="flex items-center gap-3">

                <div className="text-right">

                  <div className="text-xs uppercase tracking-[0.2em] text-zinc-500 mb-1">
                    Priority Score
                  </div>

                  <div className="text-3xl font-semibold">
                    {item.priority_score}
                  </div>

                </div>

                <ArrowUpRight className="text-emerald-400" />

              </div>

            </div>
          ))}

        </div>
      )}
    </div>
  );
}
