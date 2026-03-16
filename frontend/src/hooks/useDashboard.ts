import { useEffect, useState } from 'react';

import { getDashboardSummary } from '../api/dashboardApi';
import { DashboardApiResponse } from '../types/apiTypes';

export const useDashboard = (): {
  data: DashboardApiResponse | null;
  loading: boolean;
  error: string | null;
} => {
  const [data, setData] = useState<DashboardApiResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const load = async (): Promise<void> => {
      try {
        setLoading(true);
        try {
    const response = await getDashboardSummary();
    setData(response);
}     catch {
    // dashboard summary optional
}
      } catch {
      console.warn('Dashboard endpoint not implemented yet');
      } finally {
        setLoading(false);
      }
    };

    void load();
  }, []);

  return { data, loading, error };
};
