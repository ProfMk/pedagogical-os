import { useEffect, useState } from 'react';

import { getTeacherDashboard } from '../api/teacherDashboardApi';
import { TeacherDashboardResponse } from '../types/teacherDashboard';

const INSTITUTION_ID = '11111111-1111-1111-1111-111111111111';
const ACADEMIC_YEAR_ID = '22222222-2222-2222-2222-222222222222';
const TEACHER_ID = '33333333-3333-3333-3333-333333333333';

export function useTeacherDashboard(): {
  data: TeacherDashboardResponse | null;
  loading: boolean;
  error: string | null;
} {
  const [data, setData] = useState<TeacherDashboardResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load(): Promise<void> {
      try {
        const result = await getTeacherDashboard(INSTITUTION_ID, ACADEMIC_YEAR_ID, TEACHER_ID);
        setData(result);
      } catch {
        setError('Failed to load dashboard');
      } finally {
        setLoading(false);
      }
    }

    void load();
  }, []);

  return { data, loading, error };
}
