"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { api } from "@/lib/api";

export default function LoginPage() {
  const router = useRouter();

  const [email, setEmail] = useState("admin@test.com");
  const [password, setPassword] = useState("Strong123!");
  const [error, setError] = useState("");

  async function handleLogin() {
    setError("");

    try {
      const response = await api.post("/auth/login", {
        email,
        password,
      });

      localStorage.setItem("access_token", response.data.access_token);

      router.push("/");
    } catch {
      setError("Invalid login credentials.");
    }
  }

  return (
    <main className="min-h-screen bg-black text-white flex items-center justify-center p-8">
      <div className="w-full max-w-md bg-zinc-900 border border-zinc-800 rounded-2xl p-8 space-y-6">
        <div>
          <h1 className="text-3xl font-bold">Command Center Login</h1>
          <p className="text-zinc-400 mt-2">
            Authenticate to access the operational dashboard.
          </p>
        </div>

        <div className="space-y-4">
          <input
            className="w-full bg-black border border-zinc-700 rounded-xl px-4 py-3"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            placeholder="Email"
          />

          <input
            className="w-full bg-black border border-zinc-700 rounded-xl px-4 py-3"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Password"
            type="password"
          />

          {error && <p className="text-red-400 text-sm">{error}</p>}

          <button
            onClick={handleLogin}
            className="w-full bg-white text-black rounded-xl py-3 font-semibold"
          >
            Login
          </button>
        </div>
      </div>
    </main>
  );
}
