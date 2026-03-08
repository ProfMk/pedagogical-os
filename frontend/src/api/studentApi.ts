import { apiClient } from './apiClient';
import { StudentApiResponse } from '../types/apiTypes';

export const getStudents = async (): Promise<StudentApiResponse> => {
  const { data } = await apiClient.get<StudentApiResponse>('/students');
  return data;
};
