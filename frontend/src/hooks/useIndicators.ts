import { useEffect, useState } from 'react';

import { getIndicators } from '../api/indicatorApi';
import { IndicatorApiResponse } from '../types/apiTypes';

export const useIndicators = (): {
  data: IndicatorApiResponse | null;
  loading: boolean;
  error: string | null;
} => {
  const [data, setData] = useState<IndicatorApiResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const load = async (): Promise<void> => {
      try {
        setLoading(true);
        const response = await getIndicators();
        setData(response);
      } catch {
        setError('Failed to load indicators.');
      } finally {
        setLoading(false);
      }
    };

    void load();
  }, []);

  return { data, loading, error };
};
