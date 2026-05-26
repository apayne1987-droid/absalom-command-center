"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import {
  Activity,
  Brain,
  CheckCircle,
  ChevronRight,
  ClipboardList,
  Cpu,
  DollarSign,
  Layers3,
  LogOut,
  RefreshCw,
  Shield,
  Workflow,
  XCircle,
} from "lucide-react";

import { api } from "@/lib/api";
import { ExecutiveCopilotPanel } from "@/components/copilot/executive-copilot-panel";

type RuntimeMetrics = {
  workflows: number;
  tasks: number;
  execution_logs: number;
  completed_tasks: number;
  failed_tasks: number;
  active_tasks: number;
};

type ExecutivePriority = {
  id: number;
  title: string;
  bottleneck: string | null;
  priority_score: number;
  status: string;
};

type CurrentUser = {
  id: number;
  email: string;
};

type Workspace =
  | "Executive Core"
  | "Execution OS"
  | "AI Systems"
  | "Revenue Engine"
  | "Dev Forge"
  | "Infrastructure";

const navigation = [
  {
    title: "Executive Core" as Workspace,
    icon: Brain,
  },
  {
    title: "Execution OS" as Workspace,
    icon: ClipboardList,
  },
  {
    title: "AI Systems" as Workspace,
    icon: Cpu,
  },
  {
    title: "Revenue Engine" as Workspace,
    icon: DollarSign,
  },
  {
    title: "Dev Forge" as Workspace,
    icon: Layers3,
  },
  {
    title: "Infrastructure" as Workspace,
    icon: Shield,
  },
];

export default function Home() {
  const router = useRouter();

  const [activeWorkspace, setActiveWorkspace] =
    useState<Workspace>("Executive Core");

  const [user, setUser] = useState<CurrentUser | null>(null);
  const [metrics, setMetrics] = useState<RuntimeMetrics | null>(null);
  const [priorities, setPriorities] = useState<ExecutivePriority[]>([]);
  const [loading, setLoading] = useState(true);

  async function loadDashboard() {
    const [
      userResponse,
      metricsResponse,
      prioritiesResponse,
    ] = await Promise.all([
      api.get("/protected/me"),
      api.get("/metrics/runtime"),
      api.get("/executive/priorities"),
    ]);

    setUser(userResponse.data);
    setMetrics(metricsResponse.data);
    setPriorities(prioritiesResponse.data);
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
  }, []);

  if (loading || !metrics) {
    return (
      <main className="min-h-screen bg-[#09090B] text-white flex items-center justify-center">
        <div className="text-zinc-500 text-lg">
          Initializing Executive Runtime...
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-[#09090B] text-white flex">
      <aside className="w-[290px] border-r border-zinc-900 bg-black/40 backdrop-blur-xl p-6 flex flex-col">
        <div>
          <div className="text-xs uppercase tracking-[0.25em] text-zinc-500 mb-3">
            ABSALOM OS
          </div>

          <h1 className="text-2xl font-semibold tracking-tight">
            Executive Command
          </h1>

          <p className="text-sm text-zinc-500 mt-3 leading-relaxed">
            AI-native leverage infrastructure for operational execution,
            prioritization, automation, and intelligence.
          </p>
        </div>

        <nav className="mt-10 flex-1 space-y-2">
          {navigation.map((item) => {
            const Icon = item.icon;

            const active = activeWorkspace === item.title;

            return (
              <button
                key={item.title}
                onClick={() => setActiveWorkspace(item.title)}
                className={`w-full flex items-center justify-between rounded-2xl px-4 py-3 transition border ${
                  active
                    ? "bg-white text-black border-white"
                    : "hover:bg-zinc-900 border-transparent hover:border-zinc-800"
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon
                    size={18}
                    className={active ? "text-black" : "text-zinc-400"}
                  />

                  <span
                    className={`text-sm font-medium ${
                      active ? "text-black" : "text-zinc-200"
                    }`}
                  >
                    {item.title}
                  </span>
                </div>

                <ChevronRight
                  size={16}
                  className={active ? "text-black" : "text-zinc-600"}
                />
              </button>
            );
          })}
        </nav>

        <div className="border-t border-zinc-900 pt-5">
          <div className="text-sm text-zinc-400 mb-3">
            {user?.email}
          </div>

          <button
            onClick={logout}
            className="w-full bg-zinc-900 hover:bg-zinc-800 transition rounded-2xl py-3 text-sm font-semibold"
          >
            Logout
          </button>
        </div>
      </aside>

      <section className="flex-1 p-10 overflow-auto">
        <header className="flex items-start justify-between mb-10">
          <div>
            <div className="text-xs uppercase tracking-[0.3em] text-zinc-500 mb-4">
              {activeWorkspace}
            </div>

            <h2 className="text-5xl font-semibold tracking-tight leading-none">
              {workspaceTitle(activeWorkspace)}
            </h2>

            <p className="text-zinc-500 mt-5 max-w-2xl text-lg leading-relaxed">
              {workspaceDescription(activeWorkspace)}
            </p>
          </div>

          <button
            onClick={loadDashboard}
            className="bg-white text-black px-5 py-3 rounded-2xl font-semibold flex items-center gap-2 shadow-2xl"
          >
            <RefreshCw size={18} />
            Refresh Runtime
          </button>
        </header>

        {activeWorkspace === "Executive Core" && (
          <>
            <div className="mb-8">
              <ExecutiveCopilotPanel />
            </div>
<section className="grid grid-cols-2 xl:grid-cols-6 gap-5 mb-10">
              <MetricCard
                title="Workflows"
                value={metrics.workflows}
                icon={<Workflow size={20} />}
              />

              <MetricCard
                title="Tasks"
                value={metrics.tasks}
                icon={<ClipboardList size={20} />}
              />

              <MetricCard
                title="Execution Logs"
                value={metrics.execution_logs}
                icon={<Activity size={20} />}
              />

              <MetricCard
                title="Completed"
                value={metrics.completed_tasks}
                icon={<CheckCircle size={20} />}
              />

              <MetricCard
                title="Failed"
                value={metrics.failed_tasks}
                icon={<XCircle size={20} />}
              />

              <MetricCard
                title="Active"
                value={metrics.active_tasks}
                icon={<Cpu size={20} />}
              />
            </section>

            <section className="grid grid-cols-1 xl:grid-cols-[1.2fr_0.8fr] gap-8">
              <div className="bg-[#111113] border border-zinc-900 rounded-[28px] p-8">
                <div className="flex items-center justify-between mb-8">
                  <div>
                    <div className="text-xs uppercase tracking-[0.25em] text-zinc-500 mb-3">
                      Priority Engine
                    </div>

                    <h3 className="text-3xl font-semibold">
                      Top Strategic Priorities
                    </h3>
                  </div>

                  <div className="text-sm text-zinc-500">
                    Leverage-ranked operational targets
                  </div>
                </div>

                <div className="space-y-5">
                  {priorities.map((priority) => (
                    <div
                      key={priority.id}
                      className="rounded-3xl border border-zinc-900 bg-black/40 p-6 hover:border-zinc-700 transition"
                    >
                      <div className="flex items-start justify-between mb-5">
                        <div>
                          <div className="text-xs uppercase tracking-[0.25em] text-zinc-500 mb-3">
                            Priority #{priority.id}
                          </div>

                          <h4 className="text-2xl font-semibold leading-tight max-w-3xl">
                            {priority.title}
                          </h4>
                        </div>

                        <div className="bg-white text-black px-4 py-2 rounded-2xl font-bold text-lg">
                          {priority.priority_score}
                        </div>
                      </div>

                      <div className="grid grid-cols-1 xl:grid-cols-[1fr_auto] gap-6 items-end">
                        <div>
                          <div className="text-sm text-zinc-500 mb-2">
                            Current Bottleneck
                          </div>

                          <p className="text-zinc-300 leading-relaxed">
                            {priority.bottleneck ?? "No bottleneck recorded."}
                          </p>
                        </div>

                        <div className="text-xs uppercase tracking-[0.2em] text-emerald-400">
                          {priority.status}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="space-y-8">
                <SystemPanel
                  title="Runtime Status"
                  value="Operational"
                  subtitle="Core systems online and authenticated."
                />

                <SystemPanel
                  title="Execution Velocity"
                  value={`${metrics.completed_tasks}`}
                  subtitle="Completed operational tasks."
                />

                <SystemPanel
                  title="Failure Load"
                  value={`${metrics.failed_tasks}`}
                  subtitle="Runtime execution failures detected."
                />

                <SystemPanel
                  title="Operational Principle"
                  value="Compression > Expansion"
                  subtitle="Focused leverage beats conceptual complexity."
                />
              </div>
            </section>
          </>
        )}

        {activeWorkspace !== "Executive Core" && (
          <WorkspacePlaceholder workspace={activeWorkspace} />
        )}
      </section>
    </main>
  );
}

function workspaceTitle(workspace: Workspace) {
  const map: Record<Workspace, string> = {
    "Executive Core": "Operational Intelligence",
    "Execution OS": "Execution Infrastructure",
    "AI Systems": "AI-Native Leverage Systems",
    "Revenue Engine": "Revenue Intelligence",
    "Dev Forge": "Engineering Systems",
    "Infrastructure": "Runtime Resilience",
  };

  return map[workspace];
}

function workspaceDescription(workspace: Workspace) {
  const map: Record<Workspace, string> = {
    "Executive Core":
      "Focused leverage infrastructure designed to compress cognition and improve prioritization.",
    "Execution OS":
      "Operational execution systems focused on workflows, outputs, and execution velocity.",
    "AI Systems":
      "AI-native operational systems built to automate workflows and reduce cognitive load.",
    "Revenue Engine":
      "Recurring revenue infrastructure, monetization systems, and conversion analytics.",
    "Dev Forge":
      "Engineering systems, observability, scalability, and infrastructure tooling.",
    "Infrastructure":
      "Reliability engineering, runtime resilience, operational continuity, and security.",
  };

  return map[workspace];
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
    <div className="bg-[#111113] border border-zinc-900 rounded-[24px] p-5">
      <div className="flex items-center justify-between mb-5">
        <div className="text-zinc-500 text-sm">{title}</div>

        <div className="text-zinc-600">{icon}</div>
      </div>

      <div className="text-4xl font-semibold tracking-tight">
        {value}
      </div>
    </div>
  );
}

function SystemPanel({
  title,
  value,
  subtitle,
}: {
  title: string;
  value: string;
  subtitle: string;
}) {
  return (
    <div className="bg-[#111113] border border-zinc-900 rounded-[28px] p-7">
      <div className="text-xs uppercase tracking-[0.25em] text-zinc-500 mb-3">
        {title}
      </div>

      <div className="text-3xl font-semibold leading-tight mb-4">
        {value}
      </div>

      <p className="text-zinc-500 leading-relaxed">
        {subtitle}
      </p>
    </div>
  );
}

function WorkspacePlaceholder({
  workspace,
}: {
  workspace: Workspace;
}) {
  return (
    <div className="bg-[#111113] border border-zinc-900 rounded-[28px] p-10">
      <div className="text-xs uppercase tracking-[0.25em] text-zinc-500 mb-4">
        {workspace}
      </div>

      <h3 className="text-4xl font-semibold mb-6">
        Workspace Architecture Initialized
      </h3>

      <p className="text-zinc-500 text-lg leading-relaxed max-w-3xl">
        This workspace is now connected to the executive navigation system and
        ready for operational module expansion.
      </p>
    </div>
  );
}


