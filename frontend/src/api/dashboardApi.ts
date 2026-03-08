import { apiClient } from './apiClient';
import { DashboardApiResponse } from '../types/apiTypes';

export const getDashboardSummary = async (): Promise<DashboardApiResponse> => {
  const { data } = await apiClient.get<DashboardApiResponse>('/dashboard');
  return data;
};
