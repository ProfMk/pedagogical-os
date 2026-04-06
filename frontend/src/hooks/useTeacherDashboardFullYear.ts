import { useEffect, useState } from 'react';
import { TeacherDashboardResponse } from '../types/teacherDashboard';
import { apiGet } from '../api/client';

const INSTITUTION_ID = 'b1c31b99-f597-48fb-af2d-ad8fcbddc9bb';
const ACADEMIC_YEAR_ID = 'd3d61e45-e5a7-4f22-9860-811e73201326';
const TEACHER_ID = '11111111-1111-1111-1111-111111111111';

export function useTeacherDashboardFullYear(): {
  data: TeacherDashboardResponse | null;
  loading: boolean;
  error: string | null;
} {
  const [data, setData] = useState<TeacherDashboardResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load(): Promise<void> {
      setLoading(true);
      setError(null);

      try {
        const result = await apiGet<TeacherDashboardResponse>(
          `/teacher/dashboard-full-year?institution_id=${INSTITUTION_ID}&academic_year_id=${ACADEMIC_YEAR_ID}&teacher_id=${TEACHER_ID}`
        );

        setData(result);
      } catch {
        setError('Failed to load full year dashboard');
      } finally {
        setLoading(false);
      }
    }

    void load();
  }, []);

  return { data, loading, error };
}