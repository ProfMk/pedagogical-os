import { useEffect, useState } from "react";

import { getTeacherDashboard } from "../api/teacherDashboardApi";
import { TeacherDashboardResponse } from "../types/teacherDashboard";

export function useTeacherDashboard() {
  const [data, setData] = useState<TeacherDashboardResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      try {

        const result = await getTeacherDashboard(
        "11111111-1111-1111-1111-111111111111",
        "22222222-2222-2222-2222-222222222222"
        );

        setData(result);

      } catch (err) {
        setError("Failed to load dashboard");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  return { data, loading, error };
}