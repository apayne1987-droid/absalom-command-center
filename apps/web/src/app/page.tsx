"use client";

import { useEffect, useState } from "react";
import { Activity, CheckCircle, ClipboardList, Workflow } from "lucide-react";

import { api } from "@/lib/api";

type RuntimeMetrics = {
  workflows: number;
  tasks: number;
  execution_logs: number;
  completed_tasks: number;
  failed_tasks: number;
  active_tasks: number;
};

export default function Home() {
  const [metrics, setMetrics] = useState<RuntimeMetrics | null>(null);

  useEffect(() => {
    async function loadMetrics() {
      const response = await api.get("/metrics/runtime");

      setMetrics(response.data);
    }

    loadMetrics();
  }, []);

  return (
    <main className="min-h-screen bg-black text-white p-10">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-5xl font-bold mb-10">
          ABSALOM COMMAND CENTER
        </h1>

        {!metrics ? (
          <div className="text-xl">Loading runtime telemetry...</div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <MetricCard
              title="Workflows"
              value={metrics.workflows}
              icon={<Workflow size={28} />}
            />

            <MetricCard
              title="Tasks"
              value={metrics.tasks}
              icon={<ClipboardList size={28} />}
            />

            <MetricCard
              title="Execution Logs"
              value={metrics.execution_logs}
              icon={<Activity size={28} />}
            />

            <MetricCard
              title="Completed Tasks"
              value={metrics.completed_tasks}
              icon={<CheckCircle size={28} />}
            />

            <MetricCard
              title="Failed Tasks"
              value={metrics.failed_tasks}
              icon={<Activity size={28} />}
            />

            <MetricCard
              title="Active Tasks"
              value={metrics.active_tasks}
              icon={<Activity size={28} />}
            />
          </div>
        )}
      </div>
    </main>
  );
}

function MetricCard({
  title,
  value,
  icon,
}: {
  title: string;
  value: number;
  icon: React.ReactNode;
}) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">
      <div className="flex items-center justify-between mb-4">
        <div className="text-zinc-400">{title}</div>

        <div className="text-zinc-500">
          {icon}
        </div>
      </div>

      <div className="text-5xl font-bold">
        {value}
      </div>
    </div>
  );
}
