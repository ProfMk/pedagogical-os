import { apiClient } from './apiClient';
import { IndicatorApiResponse } from '../types/apiTypes';

export const getIndicators = async (): Promise<IndicatorApiResponse> => {
  const { data } = await apiClient.get<IndicatorApiResponse>('/indicators');
  return data;
};
