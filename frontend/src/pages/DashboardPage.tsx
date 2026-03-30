import { useNavigate } from 'react-router-dom';
import { Card } from '../components/ui/Card';
import { useDashboard } from '../hooks/useDashboard';

export const DashboardPage = (): JSX.Element => {
  const { data, loading, error } = useDashboard();
  const navigate = useNavigate();

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: 24 }}>
      <h1>System Dashboard</h1>

      <Card>
        <p>Dashboard overview placeholder.</p>

        <button
          onClick={() => navigate('/teacher/dashboard')}
          style={{
            padding: '10px 16px',
            marginTop: 12,
            cursor: 'pointer'
          }}
        >
          Open Teacher Dashboard
        </button>

        <button
          onClick={() => navigate('/teacher/group-progress')}
          style={{
            padding: '10px 16px',
            marginTop: 12,
            marginLeft: 8,
            cursor: 'pointer'
          }}
        >
          View Group Progress
        </button>

        {loading && <p>Loading dashboard data...</p>}
        {error && <p>{error}</p>}
        {data && <p>API summary: {data.summary}</p>}
      </Card>
    </main>
  );
};