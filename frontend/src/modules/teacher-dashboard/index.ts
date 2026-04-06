export type AcademicPeriodOption = {
  id: string;
  name: string;
  status: string;
};

export const getOpenPeriods = (period: unknown): AcademicPeriodOption[] => {
  const rows = Array.isArray(period)
    ? period
    : period && typeof period === 'object' && 'periods' in period && Array.isArray((period as { periods: unknown[] }).periods)
      ? (period as { periods: unknown[] }).periods
      : [];

  return rows
    .filter((row): row is AcademicPeriodOption => {
      return Boolean(
        row &&
          typeof row === 'object' &&
          'id' in row &&
          'name' in row &&
          'status' in row &&
          typeof (row as { id: unknown }).id === 'string' &&
          typeof (row as { name: unknown }).name === 'string' &&
          typeof (row as { status: unknown }).status === 'string'
      );
    })
    .filter((row) => row.status.toUpperCase() === 'OPEN');
};