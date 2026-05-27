"use client";

import { useState } from "react";

import axios from "axios";

import { Bot } from "lucide-react";


export function AutonomousExecutionPanel() {

  const [objective, setObjective] = useState("");

  const [result, setResult] = useState<any>(null);

  const [loading, setLoading] = useState(false);

  async function executeObjective() {

    try {

      setLoading(true);

      const response = await axios.post(
        "http://localhost:8000/autonomy/execute",
        {
          objective,
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }
  }

  return (
    <div className="bg-[#111113] border border-zinc-900 rounded-[32px] p-8 mt-8">

      <div className="flex items-center justify-between mb-8">

        <div>

          <div className="text-xs uppercase tracking-[0.3em] text-zinc-500 mb-3">
            Autonomous Runtime
          </div>

          <h3 className="text-3xl font-semibold tracking-tight">
            Autonomous Objective Execution
          </h3>

        </div>

        <div className="h-14 w-14 rounded-2xl bg-white text-black flex items-center justify-center">
          <Bot size={24} />
        </div>

      </div>

      <div className="space-y-4">

        <input
          value={objective}
          onChange={(e) => setObjective(e.target.value)}
          placeholder="Enter operational objective..."
          className="w-full bg-zinc-950 border border-zinc-900 rounded-2xl px-5 py-4 outline-none"
        />

        <button
          onClick={executeObjective}
          disabled={loading}
          className="bg-white text-black px-6 py-3 rounded-2xl font-medium"
        >
          {loading ? "Executing..." : "Execute Objective"}
        </button>

        {result && (

          <div className="bg-zinc-950 border border-zinc-900 rounded-2xl p-5 mt-6">

            <pre className="text-sm text-zinc-300 whitespace-pre-wrap">
              {JSON.stringify(result, null, 2)}
            </pre>

          </div>
        )}

      </div>
    </div>
  );
}
