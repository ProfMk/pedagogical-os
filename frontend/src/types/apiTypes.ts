export type DashboardApiResponse = {
  summary: string;
};

export type StudentApiResponse = {
  students: Array<{ id: string; name: string }>;
};

export type IndicatorApiResponse = {
  indicators: Array<{ id: string; label: string }>;
};
