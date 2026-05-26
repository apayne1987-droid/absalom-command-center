"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import {
  Activity,
  CheckCircle,
  ClipboardList,
  LogOut,
  RefreshCw,
  Workflow,
  XCircle,
} from "lucide-react";

import { api } from "@/lib/api";

type RuntimeMetrics = {
  workflows: number;
  tasks: number;
  execution_logs: number;
  completed_tasks: number;
  failed_tasks: number;
  active_tasks: number;
};

type WorkflowItem = {
  id: number;
  name: string;
  state: string;
};

type TaskItem = {
  id: number;
  workflow_id: number;
  name: string;
  state: string;
};

type ExecutionLogItem = {
  id: number;
  task_id: number;
  event_type: string;
  message: string;
};

type CurrentUser = {
  id: number;
  email: string;
  is_active: boolean;
  is_superuser: boolean;
};

export default function Home() {
  const router = useRouter();

  const [user, setUser] = useState<CurrentUser | null>(null);
  const [metrics, setMetrics] = useState<RuntimeMetrics | null>(null);
  const [workflows, setWorkflows] = useState<WorkflowItem[]>([]);
  const [tasks, setTasks] = useState<TaskItem[]>([]);
  const [logs, setLogs] = useState<ExecutionLogItem[]>([]);
  const [loading, setLoading] = useState(true);

  async function loadDashboard() {
    const [userResponse, metricsResponse, workflowsResponse, tasksResponse, logsResponse] =
      await Promise.all([
        api.get("/protected/me"),
        api.get("/metrics/runtime"),
        api.get("/workflows"),
        api.get("/tasks"),
        api.get("/execution-logs"),
      ]);

    setUser(userResponse.data);
    setMetrics(metricsResponse.data);
    setWorkflows(workflowsResponse.data);
    setTasks(tasksResponse.data);
    setLogs(logsResponse.data);
    setLoading(false);
  }

  function logout() {
    localStorage.removeItem("access_token");
    router.push("/login");
  }

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      router.push("/login");
      return;
    }

    loadDashboard().catch(() => {
      localStorage.removeItem("access_token");
      router.push("/login");
    });

    const interval = setInterval(() => {
      loadDashboard().catch(() => {
        localStorage.removeItem("access_token");
        router.push("/login");
      });
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <main className="min-h-screen bg-black text-white p-8">
      <div className="max-w-7xl mx-auto space-y-8">
        <header className="flex items-center justify-between">
          <div>
            <h1 className="text-5xl font-bold tracking-tight">
              ABSALOM COMMAND CENTER
            </h1>
            <p className="text-zinc-400 mt-2">
              Authenticated runtime orchestration and operational telemetry.
            </p>
            {user && (
              <p className="text-zinc-500 mt-1 text-sm">
                Logged in as {user.email}
              </p>
            )}
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={loadDashboard}
              className="flex items-center gap-2 bg-white text-black px-4 py-2 rounded-xl font-semibold"
            >
              <RefreshCw size={18} />
              Refresh
            </button>

            <button
              onClick={logout}
              className="flex items-center gap-2 bg-zinc-800 text-white px-4 py-2 rounded-xl font-semibold"
            >
              <LogOut size={18} />
              Logout
            </button>
          </div>
        </header>

        {loading || !metrics ? (
          <div className="text-xl text-zinc-400">
            Loading authenticated runtime telemetry...
          </div>
        ) : (
          <>
            <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <MetricCard title="Workflows" value={metrics.workflows} icon={<Workflow size={28} />} />
              <MetricCard title="Tasks" value={metrics.tasks} icon={<ClipboardList size={28} />} />
              <MetricCard title="Execution Logs" value={metrics.execution_logs} icon={<Activity size={28} />} />
              <MetricCard title="Completed" value={metrics.completed_tasks} icon={<CheckCircle size={28} />} />
              <MetricCard title="Failed" value={metrics.failed_tasks} icon={<XCircle size={28} />} />
              <MetricCard title="Active" value={metrics.active_tasks} icon={<Activity size={28} />} />
            </section>

            <section className="grid grid-cols-1 xl:grid-cols-2 gap-6">
              <Panel title="Workflows">
                <DataTable
                  headers={["ID", "Name", "State"]}
                  rows={workflows.map((workflow) => [
                    workflow.id,
                    workflow.name,
                    <StatusBadge key={workflow.id} state={workflow.state} />,
                  ])}
                />
              </Panel>

              <Panel title="Tasks">
                <DataTable
                  headers={["ID", "Workflow", "Name", "State"]}
                  rows={tasks.map((task) => [
                    task.id,
                    task.workflow_id,
                    task.name,
                    <StatusBadge key={task.id} state={task.state} />,
                  ])}
                />
              </Panel>
            </section>

            <Panel title="Execution Log Feed">
              <div className="space-y-3 max-h-[420px] overflow-y-auto pr-2">
                {logs
                  .slice()
                  .reverse()
                  .map((log) => (
                    <div key={log.id} className="border border-zinc-800 bg-zinc-950 rounded-xl p-4">
                      <div className="flex items-center justify-between mb-2">
                        <div className="font-semibold text-sm text-zinc-300">{log.event_type}</div>
                        <div className="text-xs text-zinc-500">Task #{log.task_id}</div>
                      </div>
                      <p className="text-zinc-400 text-sm">{log.message}</p>
                    </div>
                  ))}
              </div>
            </Panel>
          </>
        )}
      </div>
    </main>
  );
}

function MetricCard({ title, value, icon }: { title: string; value: number; icon: React.ReactNode }) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">
      <div className="flex items-center justify-between mb-4">
        <div className="text-zinc-400">{title}</div>
        <div className="text-zinc-500">{icon}</div>
      </div>
      <div className="text-5xl font-bold">{value}</div>
    </div>
  );
}

function Panel({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">
      <h2 className="text-2xl font-bold mb-5">{title}</h2>
      {children}
    </section>
  );
}

function DataTable({ headers, rows }: { headers: string[]; rows: React.ReactNode[][] }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-zinc-800 text-zinc-500">
            {headers.map((header) => (
              <th key={header} className="text-left py-3 pr-4">
                {header}
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {rows.map((row, index) => (
            <tr key={index} className="border-b border-zinc-800">
              {row.map((cell, cellIndex) => (
                <td key={cellIndex} className="py-3 pr-4 text-zinc-300">
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function StatusBadge({ state }: { state: string }) {
  const styles: Record<string, string> = {
    CREATED: "bg-zinc-800 text-zinc-300",
    QUEUED: "bg-blue-950 text-blue-300",
    ACTIVE: "bg-yellow-950 text-yellow-300",
    COMPLETED: "bg-green-950 text-green-300",
    FAILED: "bg-red-950 text-red-300",
    PAUSED: "bg-purple-950 text-purple-300",
    ARCHIVED: "bg-zinc-800 text-zinc-500",
  };

  return (
    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${styles[state] ?? "bg-zinc-800 text-zinc-300"}`}>
      {state}
    </span>
  );
}
