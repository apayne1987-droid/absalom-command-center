import { create } from "zustand";

type Workspace =
  | "Executive Core"
  | "Execution OS"
  | "AI Systems"
  | "Revenue Engine"
  | "Dev Forge"
  | "Infrastructure";

type AppState = {
  activeWorkspace: Workspace;
  setWorkspace: (workspace: Workspace) => void;
};

export const useAppStore = create<AppState>((set) => ({
  activeWorkspace: "Executive Core",

  setWorkspace: (workspace) =>
    set({
      activeWorkspace: workspace,
    }),
}));
