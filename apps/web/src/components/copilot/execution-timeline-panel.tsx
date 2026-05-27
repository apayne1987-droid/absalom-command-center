"use client";

import {
  Activity,
  CheckCircle2,
  Clock3,
  Workflow,
} from "lucide-react";

import { useRuntimeTraces } from "@/hooks/use-runtime-traces";


export function ExecutionTimelinePanel() {

  const { data, isLoading } = useRuntimeTraces();

  return (
    <div className="bg-[#111113] border border-zinc-900 rounded-[32px] p-8 mt-8">

      <div className="flex items-center justify-between mb-8">

        <div>

          <div className="text-xs uppercase tracking-[0.3em] text-zinc-500 mb-3">
            Runtime Observability
          </div>

          <h3 className="text-3xl font-semibold tracking-tight">
            Execution Timeline
          </h3>

        </div>

        <div className="h-14 w-14 rounded-2xl bg-white text-black flex items-center justify-center">
          <Workflow size={24} />
        </div>

      </div>

      {isLoading ? (

        <div className="space-y-4 animate-pulse">
          <div className="h-4 bg-zinc-800 rounded w-full" />
          <div className="h-4 bg-zinc-800 rounded w-5/6" />
          <div className="h-4 bg-zinc-800 rounded w-4/6" />
        </div>

      ) : (

        <div className="space-y-5">

          {data?.length === 0 && (

            <div className="text-zinc-500 text-sm">
              No execution traces yet.
            </div>

          )}

          {data?.map((trace, index) => (

            <div
              key={index}
              className="bg-zinc-950/70 border border-zinc-900 rounded-2xl p-5"
            >

              <div className="flex items-center justify-between mb-4">

                <div className="flex items-center gap-3">

                  <div className="h-10 w-10 rounded-full bg-emerald-500/15 text-emerald-400 flex items-center justify-center">
                    <Activity size={18} />
                  </div>

                  <div>

                    <div className="text-white font-medium">
                      {trace.objective}
                    </div>

                    <div className="text-xs text-zinc-500 mt-1">
                      Current Step: {trace.current_step}
                    </div>

                  </div>

                </div>

                <div className="flex items-center gap-2 text-emerald-400 text-sm">
                  <CheckCircle2 size={16} />
                  {trace.status}
                </div>

              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

                <div className="bg-black/30 rounded-xl p-4">

                  <div className="text-xs uppercase tracking-[0.2em] text-zinc-500 mb-2">
                    Validation
                  </div>

                  <div className="text-zinc-300 text-sm">
                    {trace.validation_status}
                  </div>

                </div>

                <div className="bg-black/30 rounded-xl p-4">

                  <div className="text-xs uppercase tracking-[0.2em] text-zinc-500 mb-2">
                    Retry Count
                  </div>

                  <div className="text-zinc-300 text-sm">
                    {trace.retry_count}
                  </div>

                </div>

                <div className="bg-black/30 rounded-xl p-4">

                  <div className="text-xs uppercase tracking-[0.2em] text-zinc-500 mb-2">
                    Result
                  </div>

                  <div className="text-zinc-300 text-sm">
                    {trace.result}
                  </div>

                </div>

              </div>

              <div className="flex items-center gap-2 mt-5 text-xs text-zinc-500">
                <Clock3 size={14} />
                Runtime execution recorded
              </div>

            </div>
          ))}

        </div>
      )}
    </div>
  );
}
