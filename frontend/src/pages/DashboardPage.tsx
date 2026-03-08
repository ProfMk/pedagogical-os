import { Card } from '../components/ui/Card';
import { useDashboard } from '../hooks/useDashboard';

export const DashboardPage = (): JSX.Element => {
  const { data, loading, error } = useDashboard();

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: 24 }}>
      <h1>Teacher Dashboard Page</h1>
      <Card>
        <p>Dashboard overview placeholder.</p>
        {loading && <p>Loading dashboard data...</p>}
        {error && <p>{error}</p>}
        {data && <p>API summary: {data.summary}</p>}
      </Card>
    </main>
  );
};
