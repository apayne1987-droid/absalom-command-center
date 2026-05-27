export type RuntimeTrace = {
  id: number | null;
  objective: string;
  current_step: string;
  status: string;
  result: string;
  validation_status: string;
  retry_count: number;
  created_at: string | null;
};
