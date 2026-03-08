import { useEffect, useState } from 'react';

import { getStudents } from '../api/studentApi';
import { StudentApiResponse } from '../types/apiTypes';

export const useStudents = (): {
  data: StudentApiResponse | null;
  loading: boolean;
  error: string | null;
} => {
  const [data, setData] = useState<StudentApiResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const load = async (): Promise<void> => {
      try {
        setLoading(true);
        const response = await getStudents();
        setData(response);
      } catch {
        setError('Failed to load students.');
      } finally {
        setLoading(false);
      }
    };

    void load();
  }, []);

  return { data, loading, error };
};
